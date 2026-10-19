// Main Application Bootstrapper and Coordinator

import { CONFIG } from './config.js';
import { fetchResources, geocodeSearch } from './api.js';
import { 
  initMap, 
  renderResourceMarkers, 
  highlightMarker, 
  setUserLocation, 
  setSearchCenter, 
  panTo, 
  getMapCenter,
  getLeafletMapInstance 
} from './map.js';
import { initCategoryFilters, getActiveCategoryList } from './categories.js';
import { initBottomSheet, initDesktopSidebar } from './sheet.js';
import { 
  initUI, 
  setUserPosition, 
  showLoadingState, 
  renderResults, 
  highlightSelectedCard, 
  openDetailModal, 
  showUpstreamError, 
  showToast 
} from './ui.js';
import { calculateAndDrawRoute } from './routing.js';

let mapInstance = null;
let currentQueryCoords = { lat: CONFIG.DEFAULT_CENTER[0], lon: CONFIG.DEFAULT_CENTER[1] };
let currentQueryRadius = CONFIG.DEFAULT_RADIUS_METERS;
let userCoords = null;
let isFirstLoad = true;

document.addEventListener('DOMContentLoaded', async () => {
  // 1. Initialize Leaflet Map
  mapInstance = initMap('map', {
    onMarkerSelected: (item) => handleSelectItem(item),
    onAreaMoved: (newCenter) => {
      showSearchAreaButton(true);
    }
  });

  // 2. Initialize UI Module
  initUI(mapInstance);

  // 3. Initialize Category Filters
  const categoryFilterBar = document.getElementById('categoryFilterBar');
  initCategoryFilters(categoryFilterBar, () => {
    // Re-query when category selection changes
    executeSearch(currentQueryCoords.lat, currentQueryCoords.lon, currentQueryRadius);
  });

  // 4. Initialize Desktop Sidebar & Mobile Bottom Sheet
  initDesktopSidebar({
    sidebarEl: document.getElementById('desktopSidebar'),
    toggleBtnEl: document.getElementById('sidebarToggleBtn'),
    closeBtnEl: document.getElementById('closeSidebarBtn'),
    appContainerEl: document.getElementById('app')
  });

  initBottomSheet({
    sheetEl: document.getElementById('bottomSheet'),
    handleEl: document.getElementById('sheetHandleArea'),
    backdropEl: document.getElementById('bottomSheetBackdrop')
  });

  // 5. Setup Search Bar & Geocoding
  setupSearchBar();

  // 6. Setup "Search this area" Button
  const searchThisAreaBtn = document.getElementById('searchThisAreaBtn');
  if (searchThisAreaBtn) {
    searchThisAreaBtn.addEventListener('click', () => {
      const center = getMapCenter();
      showSearchAreaButton(false);
      executeSearch(center.lat, center.lon, currentQueryRadius);
    });
  }

  // 7. Setup Explicit Geolocation Button
  const locateMeBtn = document.getElementById('locateMeBtn');
  if (locateMeBtn) {
    locateMeBtn.addEventListener('click', () => handleLocateMe());
  }

  // 8. Render Lucide icons
  if (window.lucide && window.lucide.createIcons) {
    window.lucide.createIcons();
  }

  // 9. Initial Load with Default Coordinates
  await executeSearch(currentQueryCoords.lat, currentQueryCoords.lon, currentQueryRadius);
  isFirstLoad = false;
});

/**
 * Handle explicit user geolocation request
 * Data Integrity: Only triggers on user action, never automatically
 */
function handleLocateMe() {
  if (!navigator.geolocation) {
    showToast('Geolocation is not supported by your browser.', 'warning');
    return;
  }

  showToast('Locating your position...');

  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const lat = pos.coords.latitude;
      const lon = pos.coords.longitude;
      userCoords = { lat, lon };
      setUserPosition(lat, lon);
      setUserLocation(lat, lon);
      panTo(lat, lon, 15);
      showToast('Location identified. Searching nearby emergency resources.');
      executeSearch(lat, lon, currentQueryRadius);
    },
    (err) => {
      console.warn('Geolocation error:', err);
      let errMsg = 'Location access was denied or unavailable.';
      if (err.code === 1) {
        errMsg = 'Location permission denied. You can search by entering an address above or panning the map.';
      } else if (err.code === 2) {
        errMsg = 'Location unavailable. Please check your GPS/network settings.';
      } else if (err.code === 3) {
        errMsg = 'Location request timed out. Please try again.';
      }
      showToast(errMsg, 'warning');
    },
    { enableHighAccuracy: true, timeout: 10000, maximumAge: 30000 }
  );
}

/**
 * Executes backend resource fetch with race condition protection
 */
async function executeSearch(lat, lon, radius) {
  currentQueryCoords = { lat, lon };
  currentQueryRadius = radius;
  setSearchCenter(lat, lon, radius);
  showSearchAreaButton(false);

  showLoadingState();

  const categories = getActiveCategoryList();

  try {
    const response = await fetchResources({ lat, lon, radius, categories });
    const resources = response.data || [];
    const meta = response.meta || {};

    // Render Markers on Map
    renderResourceMarkers(resources);

    // Render Result Cards in Desktop Sidebar & Mobile Sheet
    renderResults(
      resources, 
      meta,
      (item) => handleSelectItem(item),
      (item) => handleRouteItem(item)
    );

    // Re-render Lucide icons for newly inserted DOM cards
    if (window.lucide && window.lucide.createIcons) {
      window.lucide.createIcons();
    }
  } catch (err) {
    if (err.name === 'AbortError') {
      // Obsolete request cancelled, ignore
      return;
    }
    console.error('Failed to load resources:', err);
    showUpstreamError(
      err.message || 'Upstream OpenStreetMap service failed. Please check network connection.',
      () => executeSearch(lat, lon, radius)
    );
  }
}

/**
 * Agreement between Map pin, results list, and detail modal
 */
function handleSelectItem(item) {
  highlightMarker(item.id);
  highlightSelectedCard(item.id);
  openDetailModal(item, mapInstance);

  if (window.lucide && window.lucide.createIcons) {
    window.lucide.createIcons();
  }
}

/**
 * Direct route calculation from card or modal
 */
async function handleRouteItem(item) {
  handleSelectItem(item);

  try {
    const startLat = userCoords ? userCoords.lat : item.lat + 0.01;
    const startLon = userCoords ? userCoords.lon : item.lon + 0.01;
    await calculateAndDrawRoute(mapInstance, startLat, startLon, item.lat, item.lon);
  } catch (err) {
    showToast('Routing failed. Use fallback navigation links in place details.', 'warning');
  }
}

/**
 * Floating "Search this area" button visibility toggle
 */
function showSearchAreaButton(visible) {
  const btn = document.getElementById('floatingAreaSearch');
  if (btn) {
    btn.classList.toggle('visible', visible);
  }
}

/**
 * Search Bar Autocomplete and Geocoding setup
 */
function setupSearchBar() {
  const input = document.getElementById('searchInput');
  const suggestionsBox = document.getElementById('searchSuggestions');
  const clearBtn = document.getElementById('clearSearchBtn');
  const submitBtn = document.getElementById('searchSubmitBtn');

  if (!input || !suggestionsBox) return;

  let debounceTimer = null;

  input.addEventListener('input', () => {
    const query = input.value.trim();
    if (clearBtn) clearBtn.style.display = query.length > 0 ? 'flex' : 'none';

    clearTimeout(debounceTimer);
    if (query.length < 2) {
      suggestionsBox.classList.remove('active');
      suggestionsBox.innerHTML = '';
      return;
    }

    debounceTimer = setTimeout(async () => {
      const results = await geocodeSearch(query, currentQueryCoords);
      renderSuggestions(results, suggestionsBox, input);
    }, 350);
  });

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      input.value = '';
      clearBtn.style.display = 'none';
      suggestionsBox.classList.remove('active');
      suggestionsBox.innerHTML = '';
      input.focus();
    });
  }

  if (submitBtn) {
    submitBtn.addEventListener('click', async () => {
      const query = input.value.trim();
      if (!query) return;
      const results = await geocodeSearch(query, currentQueryCoords);
      if (results.length > 0) {
        selectSuggestion(results[0], suggestionsBox, input);
      }
    });
  }

  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      const firstItem = suggestionsBox.querySelector('.suggestion-item');
      if (firstItem) {
        firstItem.click();
      } else if (input.value.trim()) {
        if (submitBtn) submitBtn.click();
      }
    }
  });

  // Close suggestions on outside click
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.search-box-wrapper') && !e.target.closest('.search-suggestions')) {
      suggestionsBox.classList.remove('active');
    }
  });
}

function renderSuggestions(results, container, input) {
  container.innerHTML = '';
  if (!results || results.length === 0) {
    container.classList.remove('active');
    return;
  }

  results.forEach(res => {
    const item = document.createElement('div');
    item.className = 'suggestion-item';
    item.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
      <div style="flex: 1; min-width: 0;">
        <div style="font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${escapeHtml(res.name || res.display_name.split(',')[0])}</div>
        <div style="font-size: 11px; color: var(--text-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${escapeHtml(res.display_name)}</div>
      </div>
    `;

    item.addEventListener('click', () => {
      selectSuggestion(res, container, input);
    });

    container.appendChild(item);
  });

  container.classList.add('active');
}

function selectSuggestion(res, container, input) {
  container.classList.remove('active');
  input.value = res.name || res.display_name.split(',')[0];

  const lat = parseFloat(res.lat);
  const lon = parseFloat(res.lon);

  panTo(lat, lon, 14);
  executeSearch(lat, lon, currentQueryRadius);
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
