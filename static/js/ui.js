// UI Rendering and View Synchronization Module

import { getCategoryById } from './config.js';
import { getSvgIcon } from './icons.js';
import { formatDistance, formatDuration, getNavigationFallbacks, calculateAndDrawRoute, clearRoute } from './routing.js';

let activeSelectedId = null;
let currentResources = [];
let userCurrentPos = null;

// DOM Element cache
let elements = {};

export function initUI(mapInstance) {
  elements = {
    resultsList: document.getElementById('resultsList'),
    mobileResultsList: document.getElementById('mobileResultsList'),
    resultsCount: document.getElementById('resultsCount'),
    cacheStatusBadge: document.getElementById('cacheStatusBadge'),
    cacheStatusText: document.getElementById('cacheStatusText'),
    retrievalTimeText: document.getElementById('retrievalTimeText'),
    mobileSummaryText: document.getElementById('mobileSummaryText'),
    upstreamErrorBanner: document.getElementById('upstreamErrorBanner'),
    upstreamErrorMessage: document.getElementById('upstreamErrorMessage'),
    retryUpstreamBtn: document.getElementById('retryUpstreamBtn'),
    toastContainer: document.getElementById('toastContainer'),
    
    // Detail Modal elements
    detailModalOverlay: document.getElementById('detailModalOverlay'),
    closeDetailModalBtn: document.getElementById('closeDetailModalBtn'),
    modalCategoryIcon: document.getElementById('modalCategoryIcon'),
    modalCategoryBadge: document.getElementById('modalCategoryBadge'),
    modalPlaceTitle: document.getElementById('modalPlaceTitle'),
    modalDistanceBadge: document.getElementById('modalDistanceBadge'),
    modalEmergencyBadge: document.getElementById('modalEmergencyBadge'),
    modalHoursPill: document.getElementById('modalHoursPill'),
    modalCallBtn: document.getElementById('modalCallBtn'),
    modalRouteBtn: document.getElementById('modalRouteBtn'),
    routeInfoBox: document.getElementById('routeInfoBox'),
    routeSummaryBadge: document.getElementById('routeSummaryBadge'),
    openGoogleMapsBtn: document.getElementById('openGoogleMapsBtn'),
    openOsmDirectionsBtn: document.getElementById('openOsmDirectionsBtn'),
    openGeoUriBtn: document.getElementById('openGeoUriBtn'),
    modalAddress: document.getElementById('modalAddress'),
    modalPhone: document.getElementById('modalPhone'),
    modalHours: document.getElementById('modalHours'),
    modalWheelchair: document.getElementById('modalWheelchair'),
    modalOperator: document.getElementById('modalOperator'),
    modalOsmLink: document.getElementById('modalOsmLink'),
    modalRawTagsTable: document.getElementById('modalRawTagsTable'),

    // Emergency numbers modal
    emergencyNumbersBtn: document.getElementById('emergencyNumbersBtn'),
    emergencyNumbersModalOverlay: document.getElementById('emergencyNumbersModalOverlay'),
    closeEmergencyModalBtn: document.getElementById('closeEmergencyModalBtn'),

    // Disclaimer banner
    disclaimerBanner: document.getElementById('disclaimerBanner'),
    dismissBannerBtn: document.getElementById('dismissBannerBtn')
  };

  // Close detail modal events
  if (elements.closeDetailModalBtn) {
    elements.closeDetailModalBtn.addEventListener('click', closeDetailModal);
  }
  if (elements.detailModalOverlay) {
    elements.detailModalOverlay.addEventListener('click', (e) => {
      if (e.target === elements.detailModalOverlay) closeDetailModal();
    });
  }

  // Emergency modal events
  if (elements.emergencyNumbersBtn && elements.emergencyNumbersModalOverlay) {
    elements.emergencyNumbersBtn.addEventListener('click', () => {
      elements.emergencyNumbersModalOverlay.classList.add('active');
    });
    elements.closeEmergencyModalBtn.addEventListener('click', () => {
      elements.emergencyNumbersModalOverlay.classList.remove('active');
    });
    elements.emergencyNumbersModalOverlay.addEventListener('click', (e) => {
      if (e.target === elements.emergencyNumbersModalOverlay) {
        elements.emergencyNumbersModalOverlay.classList.remove('active');
      }
    });
  }

  // Disclaimer dismissal
  if (elements.dismissBannerBtn && elements.disclaimerBanner) {
    elements.dismissBannerBtn.addEventListener('click', () => {
      elements.disclaimerBanner.style.display = 'none';
    });
  }

  // Escape key closes modals
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeDetailModal();
      if (elements.emergencyNumbersModalOverlay) {
        elements.emergencyNumbersModalOverlay.classList.remove('active');
      }
    }
  });

  return elements;
}

export function setUserPosition(lat, lon) {
  userCurrentPos = { lat, lon };
}

/**
 * Render loading skeletons in results lists
 */
export function showLoadingState() {
  hideUpstreamError();
  const skeletonHtml = Array(4).fill(0).map(() => `
    <div class="skeleton-card">
      <div style="display: flex; gap: 8px; align-items: center;">
        <div class="skeleton-line" style="width: 32px; height: 32px; border-radius: 8px;"></div>
        <div style="flex: 1; display: flex; flex-direction: column; gap: 6px;">
          <div class="skeleton-line" style="width: 70%;"></div>
          <div class="skeleton-line" style="width: 40%; height: 10px;"></div>
        </div>
      </div>
      <div class="skeleton-line" style="width: 90%;"></div>
    </div>
  `).join('');

  if (elements.resultsList) elements.resultsList.innerHTML = skeletonHtml;
  if (elements.mobileResultsList) elements.mobileResultsList.innerHTML = skeletonHtml;
  if (elements.resultsCount) elements.resultsCount.textContent = 'Searching...';
  if (elements.mobileSummaryText) elements.mobileSummaryText.textContent = 'Searching nearby resources...';
}

/**
 * Render results cards in both desktop and mobile lists
 */
export function renderResults(resources = [], meta = {}, onSelectCard, onRouteClick) {
  currentResources = resources;
  hideUpstreamError();

  const count = resources.length;
  if (elements.resultsCount) {
    elements.resultsCount.textContent = `${count} ${count === 1 ? 'resource' : 'resources'} found`;
  }
  if (elements.mobileSummaryText) {
    elements.mobileSummaryText.textContent = `${count} emergency ${count === 1 ? 'place' : 'places'} nearby`;
  }

  // Update Meta Cache status
  if (meta && elements.cacheStatusBadge && elements.cacheStatusText) {
    const isCached = meta.cached;
    elements.cacheStatusBadge.className = `meta-status-badge ${isCached ? 'cached' : 'live'}`;
    const age = meta.cache_age_seconds !== undefined ? `${Math.round(meta.cache_age_seconds)}s ago` : '';
    elements.cacheStatusText.textContent = isCached ? `Cached (${age})` : 'Live OSM';
    
    if (elements.retrievalTimeText && meta.retrieved_at) {
      try {
        const d = new Date(meta.retrieved_at);
        elements.retrievalTimeText.textContent = d.toLocaleTimeString();
      } catch (_) {}
    }
  }

  if (count === 0) {
    const emptyHtml = `
      <div style="text-align: center; padding: 32px 16px; color: var(--text-muted);">
        <div style="margin-bottom: 8px; color: var(--text-secondary);">${getSvgIcon('map-pin', 32)}</div>
        <strong style="display: block; font-size: 14px; margin-bottom: 4px; color: var(--text-primary);">No resources found</strong>
        <p style="font-size: 12px; margin: 0;">Try expanding your category filters, increasing search radius, or moving the map to another area.</p>
      </div>
    `;
    if (elements.resultsList) elements.resultsList.innerHTML = emptyHtml;
    if (elements.mobileResultsList) elements.mobileResultsList.innerHTML = emptyHtml;
    return;
  }

  // Build cards HTML
  const cardsHtml = resources.map(item => createCardHtml(item)).join('');

  if (elements.resultsList) elements.resultsList.innerHTML = cardsHtml;
  if (elements.mobileResultsList) elements.mobileResultsList.innerHTML = cardsHtml;

  // Attach card click handlers
  attachCardListeners(elements.resultsList, onSelectCard, onRouteClick);
  attachCardListeners(elements.mobileResultsList, onSelectCard, onRouteClick);

  // Re-highlight if active selection exists
  if (activeSelectedId) {
    highlightSelectedCard(activeSelectedId);
  }
}

function createCardHtml(item) {
  const cat = getCategoryById(item.category);
  const distStr = formatDistance(item.distance_meters);
  const isSelected = item.id === activeSelectedId;

  // Honest Status Logic:
  // Never fabricate hours or claim open unless explicitly tagged
  let statusBadgeHtml = '';
  if (item.emergency === 'yes') {
    statusBadgeHtml = `<span class="status-pill emergency-yes">Emergency 24/7</span>`;
  } else if (item.opening_hours) {
    statusBadgeHtml = `<span class="status-pill hours" title="Reported in OSM">Hours: ${escapeHtml(item.opening_hours)}</span>`;
  } else {
    statusBadgeHtml = `<span class="status-pill unreported">Hours not reported</span>`;
  }

  // Phone button only if phone exists
  let phoneBtnHtml = '';
  if (item.phone) {
    phoneBtnHtml = `
      <a href="tel:${escapeHtml(item.phone)}" class="card-action-btn call-btn" onclick="event.stopPropagation();" title="Call ${escapeHtml(item.phone)}">
        ${getSvgIcon('phone', 12)}
        <span>Call</span>
      </a>
    `;
  }

  return `
    <article class="result-card ${isSelected ? 'selected' : ''}" data-id="${item.id}" role="article" tabindex="0">
      <div class="card-top">
        <div class="card-title-group">
          <div class="card-icon" style="background-color: ${cat.color};">
            ${getSvgIcon(cat.icon, 16, '#ffffff')}
          </div>
          <div style="min-width: 0;">
            <h3 class="card-title" title="${escapeHtml(item.name)}">${escapeHtml(item.name)}</h3>
            <span class="card-category-badge" style="color: ${cat.color};">${cat.label}</span>
          </div>
        </div>
        <span class="card-distance">${distStr}</span>
      </div>

      <div class="card-info-row">
        ${statusBadgeHtml}
        ${item.wheelchair ? `<span class="info-item" title="Wheelchair accessible: ${item.wheelchair}">${getSvgIcon('bath', 12)} ${item.wheelchair}</span>` : ''}
      </div>

      ${item.address ? `<div style="font-size: 11.5px; color: var(--text-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${escapeHtml(item.address)}</div>` : ''}

      <div class="card-actions">
        ${phoneBtnHtml}
        <button type="button" class="card-action-btn route-btn" data-action="route" data-id="${item.id}" onclick="event.stopPropagation();">
          ${getSvgIcon('navigation', 12)}
          <span>Directions</span>
        </button>
      </div>
    </article>
  `;
}

function attachCardListeners(container, onSelectCard, onRouteClick) {
  if (!container) return;
  
  container.querySelectorAll('.result-card').forEach(card => {
    const id = card.dataset.id;
    const item = currentResources.find(r => r.id === id);

    card.addEventListener('click', () => {
      if (item && onSelectCard) onSelectCard(item);
    });

    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        if (item && onSelectCard) onSelectCard(item);
      }
    });

    const routeBtn = card.querySelector('[data-action="route"]');
    if (routeBtn) {
      routeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (item && onRouteClick) onRouteClick(item);
      });
    }
  });
}

/**
 * Highlights a card in both desktop and mobile lists
 */
export function highlightSelectedCard(id) {
  activeSelectedId = id;

  document.querySelectorAll('.result-card').forEach(card => {
    const isTarget = card.dataset.id === id;
    card.classList.toggle('selected', isTarget);
    if (isTarget) {
      card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  });
}

/**
 * Open Detail View Modal with verified place info
 */
export function openDetailModal(item, mapInstance) {
  activeSelectedId = item.id;
  highlightSelectedCard(item.id);

  const cat = getCategoryById(item.category);

  // Header & Title
  elements.modalPlaceTitle.textContent = item.name;
  elements.modalCategoryBadge.textContent = cat.label;
  elements.modalCategoryBadge.style.color = cat.color;
  elements.modalCategoryIcon.style.backgroundColor = cat.color;
  elements.modalCategoryIcon.innerHTML = getSvgIcon(cat.icon, 20, '#ffffff');

  // Distance & Pills
  elements.modalDistanceBadge.textContent = `${formatDistance(item.distance_meters)} away`;
  
  if (item.emergency === 'yes') {
    elements.modalEmergencyBadge.style.display = 'inline-flex';
    elements.modalEmergencyBadge.textContent = 'Verified Emergency Department';
  } else {
    elements.modalEmergencyBadge.style.display = 'none';
  }

  if (item.opening_hours) {
    elements.modalHoursPill.className = 'status-pill hours';
    elements.modalHoursPill.textContent = `Reported: ${item.opening_hours}`;
    elements.modalHours.textContent = item.opening_hours;
    elements.modalHours.classList.remove('unreported');
  } else {
    elements.modalHoursPill.className = 'status-pill unreported';
    elements.modalHoursPill.textContent = 'Hours: Not reported in OSM';
    elements.modalHours.textContent = 'Not reported in OpenStreetMap';
    elements.modalHours.classList.add('unreported');
  }

  // Address
  if (item.address) {
    elements.modalAddress.textContent = item.address;
    elements.modalAddress.classList.remove('unreported');
  } else {
    elements.modalAddress.textContent = 'No street address listed in OpenStreetMap';
    elements.modalAddress.classList.add('unreported');
  }

  // Phone Call Action
  if (item.phone) {
    elements.modalPhone.textContent = item.phone;
    elements.modalPhone.classList.remove('unreported');
    elements.modalCallBtn.href = `tel:${item.phone}`;
    elements.modalCallBtn.style.display = 'inline-flex';
    elements.modalCallBtn.querySelector('span').textContent = `Call ${item.phone}`;
  } else {
    elements.modalPhone.textContent = 'No phone number listed in OpenStreetMap';
    elements.modalPhone.classList.add('unreported');
    elements.modalCallBtn.style.display = 'none';
  }

  // Wheelchair & Operator
  elements.modalWheelchair.textContent = item.wheelchair || 'Not reported';
  elements.modalOperator.textContent = item.operator || 'Not reported';

  // Navigation Fallbacks setup
  const originLat = userCurrentPos ? userCurrentPos.lat : null;
  const originLon = userCurrentPos ? userCurrentPos.lon : null;
  const fallbacks = getNavigationFallbacks(item.lat, item.lon, item.name, originLat, originLon);

  elements.openGoogleMapsBtn.href = fallbacks.googleMapsUrl;
  elements.openOsmDirectionsBtn.href = fallbacks.osmUrl;
  elements.openGeoUriBtn.href = fallbacks.geoUri;

  // Reset route box
  elements.routeInfoBox.style.display = 'none';

  // Modal Route button handler
  elements.modalRouteBtn.onclick = async () => {
    elements.modalRouteBtn.disabled = true;
    elements.modalRouteBtn.querySelector('span').textContent = 'Calculating route...';
    try {
      const startLat = userCurrentPos ? userCurrentPos.lat : item.lat + 0.01;
      const startLon = userCurrentPos ? userCurrentPos.lon : item.lon + 0.01;
      const routeData = await calculateAndDrawRoute(mapInstance, startLat, startLon, item.lat, item.lon);
      
      elements.routeInfoBox.style.display = 'block';
      const distStr = formatDistance(routeData.distance_meters);
      const durStr = formatDuration(routeData.duration_seconds);
      elements.routeSummaryBadge.textContent = `${distStr} (~${durStr})`;
      showToast(`Route plotted: ${distStr} (${durStr})`);
    } catch (err) {
      showToast('Routing failed. Use Google Maps / OSM links below.', 'warning');
      elements.routeInfoBox.style.display = 'block';
      elements.routeSummaryBadge.textContent = 'Direct fallback navigation';
    } finally {
      elements.modalRouteBtn.disabled = false;
      elements.modalRouteBtn.querySelector('span').textContent = 'Get Route';
    }
  };

  // OSM Link & Raw Tags Table
  const osmType = item.osm_type || 'node';
  const osmId = item.osm_id || '';
  elements.modalOsmLink.href = `https://www.openstreetmap.org/${osmType}/${osmId}`;
  elements.modalOsmLink.textContent = `OSM ${osmType}/${osmId}`;

  const tbody = elements.modalRawTagsTable.querySelector('tbody');
  tbody.innerHTML = '';
  if (item.tags_raw) {
    Object.entries(item.tags_raw).forEach(([k, v]) => {
      const row = document.createElement('tr');
      row.innerHTML = `<td>${escapeHtml(k)}</td><td>${escapeHtml(String(v))}</td>`;
      tbody.appendChild(row);
    });
  }

  // Display modal
  elements.detailModalOverlay.classList.add('active');
}

export function closeDetailModal() {
  if (elements.detailModalOverlay) {
    elements.detailModalOverlay.classList.remove('active');
  }
}

/**
 * Show upstream error message with retry button
 */
export function showUpstreamError(message, retryCallback) {
  if (!elements.upstreamErrorBanner) return;
  elements.upstreamErrorMessage.textContent = message || 'Upstream OpenStreetMap service failed.';
  elements.upstreamErrorBanner.style.display = 'flex';

  if (retryCallback && elements.retryUpstreamBtn) {
    elements.retryUpstreamBtn.onclick = () => {
      hideUpstreamError();
      retryCallback();
    };
  }
}

export function hideUpstreamError() {
  if (elements.upstreamErrorBanner) {
    elements.upstreamErrorBanner.style.display = 'none';
  }
}

/**
 * Toast notifications
 */
export function showToast(message, type = 'info') {
  if (!elements.toastContainer) return;

  const toast = document.createElement('div');
  toast.className = 'toast';
  const icon = type === 'warning' ? 'alert-triangle' : 'info';
  toast.innerHTML = `${getSvgIcon(icon, 16)} <span>${escapeHtml(message)}</span>`;

  elements.toastContainer.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transition = 'opacity 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
