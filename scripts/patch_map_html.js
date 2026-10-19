const fs = require('fs');
const path = require('path');

const mapFilePath = path.join(__dirname, '..', 'static', 'map.html');
const rootMapPath = path.join(__dirname, '..', 'map.html');

console.log('Reading:', mapFilePath);
let raw = fs.readFileSync(mapFilePath, 'utf8');
// Normalize all line endings to LF for reliable multi-line matching
let html = raw.replace(/\r\n/g, '\n');

// 1. Add News Intel Tab in Nav Bar
const navTarget = `<button class="nav-tab-btn active" data-view="viewMap">🗺️ State Map</button>`;
const navReplacement = `<button class="nav-tab-btn active" data-view="viewMap">🗺️ State Map</button>
        <button class="nav-tab-btn" data-view="viewIncidents">⚡ News Intel (<span id="tabCountIncidents">0</span>)</button>`;

if (html.includes(navTarget) && !html.includes('data-view="viewIncidents"')) {
  html = html.replace(navTarget, navReplacement);
  console.log('✓ Nav tab added');
}

// 2. Add viewIncidents section before viewHospitals
const viewHospitalsTarget = `<!-- ================= TAB 2: HOSPITALS & BEDS (130+ INSTITUTIONS) ================= -->
      <section id="viewHospitals" class="view-panel">`;

const viewIncidentsHtml = `<!-- ================= TAB: NEWS INTELLIGENCE FEED (GDELT & REGIONAL NEWS) ================= -->
      <section id="viewIncidents" class="view-panel">
        <div class="view-container">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Tamil Nadu Real-Time News Intelligence Layer</h2>
              <p>Automated situational awareness harvested from GDELT Project & regional Tamil Nadu publications. Multi-source corroborated incident reporting across 7 disaster categories.</p>
            </div>
            <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
              <select id="incidentCatFilter" class="district-select-box" style="border-color:#38bdf8; color:#38bdf8;" aria-label="Filter incidents by category">
                <option value="all">🌐 All News Categories</option>
                <option value="natural_disaster">🌊 Natural Disasters & Floods</option>
                <option value="infrastructure">🚧 Infrastructure Disruptions</option>
                <option value="protest_civil_disturbance">📢 Protests & Civil Unrest</option>
                <option value="public_safety">🛡️ Public Safety & Security</option>
                <option value="accident_emergency">🚨 Accidents & Emergencies</option>
                <option value="public_health">☣️ Public Health & Outbreaks</option>
                <option value="environmental">🏭 Environmental Incidents</option>
              </select>

              <select id="incidentVerifyFilter" class="district-select-box" aria-label="Filter incidents by verification status">
                <option value="all">🔍 All Verifications</option>
                <option value="corroborated">⚡ Corroborated Multi-Source</option>
                <option value="confirmed">✓ Confirmed</option>
                <option value="unverified">⚠️ Unverified</option>
                <option value="disputed">❓ Disputed</option>
              </select>

              <button class="btn-action-scan" id="btnSyncGdeltFeed" style="border-color:#38bdf8; color:#38bdf8;">
                🔄 Refresh News Intelligence
              </button>
            </div>
          </div>

          <!-- Status & Telemetry Banner -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px;">
            <div class="metric-box" style="text-align:left; padding:12px;">
              <div style="font-size:11px; color:var(--text-muted); font-family:'JetBrains Mono';">MONITORED INCIDENTS</div>
              <div class="metric-val" id="metricTotalIncidents" style="color:#38bdf8;">0</div>
              <div style="font-size:10.5px; color:var(--text-faint);">Across 38 TN Districts</div>
            </div>
            <div class="metric-box" style="text-align:left; padding:12px;">
              <div style="font-size:11px; color:var(--text-muted); font-family:'JetBrains Mono';">CORROBORATED MULTI-SOURCE</div>
              <div class="metric-val" id="metricCorroborated" style="color:var(--green);">0</div>
              <div style="font-size:10.5px; color:var(--text-faint);">Validated by &ge; 2 Publishers</div>
            </div>
            <div class="metric-box" style="text-align:left; padding:12px;">
              <div style="font-size:11px; color:var(--text-muted); font-family:'JetBrains Mono';">INGESTED ARTICLES</div>
              <div class="metric-val" id="metricIngestedArticles" style="color:var(--amber);">0</div>
              <div style="font-size:10.5px; color:var(--text-faint);">GDELT DOC 2.0 Ingestion</div>
            </div>
            <div class="metric-box" style="text-align:left; padding:12px;">
              <div style="font-size:11px; color:var(--text-muted); font-family:'JetBrains Mono';">DATABASE PERSISTENCE</div>
              <div class="metric-val" id="metricDbStatus" style="font-size:13px; color:#fff; padding-top:4px;">Connecting...</div>
              <div style="font-size:10.5px; color:var(--text-faint);" id="metricLastSynced">Last synced: Just now</div>
            </div>
          </div>

          <!-- Incidents Cards Grid -->
          <div class="cards-grid" id="incidentsGrid">
            <!-- Dynamically populated -->
          </div>
        </div>
      </section>

      <!-- ================= TAB 2: HOSPITALS & BEDS (130+ INSTITUTIONS) ================= -->
      <section id="viewHospitals" class="view-panel">`;

if (html.includes(viewHospitalsTarget) && !html.includes('id="viewIncidents"')) {
  html = html.replace(viewHospitalsTarget, viewIncidentsHtml);
  console.log('✓ News view panel added');
}

// 3. Add Dispute Modal before Global Toast
const toastTarget = `  <!-- Global Toast -->
  <div id="globalToast"></div>`;

const disputeModalHtml = `  <!-- Incident Dispute Report Modal -->
  <div class="modal-backdrop" id="disputeModal">
    <div class="modal-box">
      <div class="modal-header">
        <h3>⚠️ Report Disputed / Mislocated Incident</h3>
        <button class="drawer-close" id="closeDisputeModalBtn">&times;</button>
      </div>
      <div class="modal-body">
        <input type="hidden" id="disputeIncidentId">
        <p style="color:var(--text-muted); font-size:12.5px;">
          Flag inaccurate, resolved, or mislocated news intelligence to keep the disaster grid reliable for responders:
        </p>
        <div class="form-group">
          <label>INCIDENT TITLE</label>
          <div id="disputeIncidentTitle" style="color:#fff; font-weight:600; font-size:13px;">-</div>
        </div>
        <div class="form-group">
          <label>REASON FOR DISPUTE</label>
          <select id="disputeReason" class="form-control">
            <option value="mislocated">Incorrect Geographic Location / Wrong District</option>
            <option value="resolved">Incident Has Ended / Situation Cleared</option>
            <option value="duplicate">Duplicate of Another Incident</option>
            <option value="false_report">Misleading / Inaccurate News Report</option>
            <option value="other">Other Issue</option>
          </select>
        </div>
        <div class="form-group">
          <label>ADDITIONAL DETAILS (OPTIONAL)</label>
          <textarea id="disputeComment" class="form-control" rows="3" placeholder="Provide context, ground observations, or official corrections..."></textarea>
        </div>
        <button type="button" class="btn-action-primary" id="submitDisputeBtn" style="justify-content:center; padding:10px;">
          Submit Verification Feedback
        </button>
      </div>
    </div>
  </div>

  <!-- Global Toast -->
  <div id="globalToast"></div>`;

if (html.includes(toastTarget) && !html.includes('id="disputeModal"')) {
  html = html.replace(toastTarget, disputeModalHtml);
  console.log('✓ Dispute modal added');
}

// 4. Add state.incidents
const stateTarget = `    // Application state
    let state = {
      currentRole: 'citizen',`;

const stateReplacement = `    // Application state
    let state = {
      currentRole: 'citizen',
      incidents: [],`;

if (html.includes(stateTarget) && !html.includes('incidents: [],')) {
  html = html.replace(stateTarget, stateReplacement);
  console.log('✓ state.incidents added');
}

// 5. Update renderMapMarkers to render news incidents and counters
const renderMarkersTarget = `      // Update counters in UI
      document.getElementById('countAll').textContent = Object.values(counts).reduce((a, b) => a + b, 0);`;

const renderMarkersReplacement = `      // 6. Real-Time News Incidents (GDELT & Corroborated Reports)
      state.incidents.forEach(item => {
        counts.news = (counts.news || 0) + 1;
        if (currentCategoryFilter === 'all' || currentCategoryFilter === 'news' || currentCategoryFilter === item.category) {
          const lat = item.location ? item.location.coordinates[1] : 0;
          const lon = item.location ? item.location.coordinates[0] : 0;
          const sym = getIncidentIconSymbol(item.category);
          const marker = L.marker([lat, lon], {
            icon: createMarkerIcon(\`news-intel \${item.category} \${item.verificationStatus}\`, sym)
          });
          marker.customData = { type: 'incident', id: item.incidentId };
          marker.on('click', () => openIncidentDrawer(item));
          markersLayer.addLayer(marker);
        }
      });

      const countIncEl = document.getElementById('countIncidents');
      if (countIncEl) countIncEl.textContent = counts.news || 0;

      // Update counters in UI
      document.getElementById('countAll').textContent = Object.values(counts).reduce((a, b) => a + b, 0);`;

if (html.includes(renderMarkersTarget) && !html.includes('counts.news = (counts.news || 0) + 1;')) {
  html = html.replace(renderMarkersTarget, renderMarkersReplacement);
  console.log('✓ renderMapMarkers updated for news incidents');
}

// 6. Update filterMapMarkers
const filterMarkersTarget = `      state.bloodBanks.forEach(bb => {
        if (match(bb.name) || match(bb.address) || match(bb.district)) {
          const marker = L.marker([bb.lat, bb.lon], { icon: createMarkerIcon('blood', '🩸') });
          marker.customData = { type: 'blood', id: bb.id };
          marker.on('click', () => openBloodDrawer(bb));
          markersLayer.addLayer(marker);
        }
      });`;

const filterMarkersReplacement = `      state.bloodBanks.forEach(bb => {
        if (match(bb.name) || match(bb.address) || match(bb.district)) {
          const marker = L.marker([bb.lat, bb.lon], { icon: createMarkerIcon('blood', '🩸') });
          marker.customData = { type: 'blood', id: bb.id };
          marker.on('click', () => openBloodDrawer(bb));
          markersLayer.addLayer(marker);
        }
      });

      state.incidents.forEach(item => {
        if (match(item.title) || match(item.description) || match(item.district) || match(item.city) || match(item.locationName)) {
          const lat = item.location ? item.location.coordinates[1] : 0;
          const lon = item.location ? item.location.coordinates[0] : 0;
          const sym = getIncidentIconSymbol(item.category);
          const marker = L.marker([lat, lon], {
            icon: createMarkerIcon(\`news-intel \${item.category} \${item.verificationStatus}\`, sym)
          });
          marker.customData = { type: 'incident', id: item.incidentId };
          marker.on('click', () => openIncidentDrawer(item));
          markersLayer.addLayer(marker);
        }
      });`;

if (html.includes(filterMarkersTarget) && !html.includes('state.incidents.forEach(item => {')) {
  html = html.replace(filterMarkersTarget, filterMarkersReplacement);
  console.log('✓ filterMapMarkers updated for news incidents');
}

// 7. Add JavaScript functions for News Intelligence
const setupViewsTarget = `    function setupViews() {
      renderHospitalsView();
      renderSheltersView();
      renderFoodView();
      renderVolunteersView();
      renderMissingView();
    }`;

const setupViewsReplacement = `    function setupViews() {
      renderHospitalsView();
      renderSheltersView();
      renderFoodView();
      renderVolunteersView();
      renderMissingView();
      renderIncidentsFeed();
    }

    // ================= NEWS INTELLIGENCE FUNCTIONS =================
    function getIncidentIconSymbol(cat) {
      if (cat === 'natural_disaster') return '🌊';
      if (cat === 'infrastructure') return '🚧';
      if (cat === 'protest_civil_disturbance') return '📢';
      if (cat === 'public_safety') return '🛡️';
      if (cat === 'accident_emergency') return '🚨';
      if (cat === 'public_health') return '☣️';
      if (cat === 'environmental') return '🏭';
      return '⚡';
    }

    function formatTimeAgo(isoString) {
      if (!isoString) return 'Recent';
      const diff = Math.floor((Date.now() - new Date(isoString).getTime()) / 1000);
      if (diff < 60) return 'Just now';
      if (diff < 3600) return \`\${Math.floor(diff / 60)}m ago\`;
      if (diff < 86400) return \`\${Math.floor(diff / 3600)}h ago\`;
      return \`\${Math.floor(diff / 86400)}d ago\`;
    }

    function getVerificationBadgeHtml(status, sourceCount = 1) {
      if (status === 'confirmed') {
        return '<span class="badge badge-success">✓ CONFIRMED</span>';
      } else if (status === 'corroborated') {
        return \`<span class="badge badge-info">⚡ CORROBORATED (\${sourceCount} SOURCES)</span>\`;
      } else if (status === 'disputed') {
        return '<span class="badge badge-danger">❓ DISPUTED</span>';
      } else {
        return '<span class="badge badge-amber">⚠️ UNVERIFIED REPORT</span>';
      }
    }

    function getCategoryBadgeHtml(cat) {
      const map = {
        'natural_disaster': { label: 'NATURAL DISASTER', icon: '🌊', color: '#ea580c' },
        'infrastructure': { label: 'INFRASTRUCTURE', icon: '🚧', color: '#ca8a04' },
        'protest_civil_disturbance': { label: 'CIVIL DISTURBANCE', icon: '📢', color: '#9333ea' },
        'public_safety': { label: 'PUBLIC SAFETY', icon: '🛡️', color: '#dc2626' },
        'accident_emergency': { label: 'ACCIDENT / EMERGENCY', icon: '🚨', color: '#e11d48' },
        'public_health': { label: 'PUBLIC HEALTH', icon: '☣️', color: '#059669' },
        'environmental': { label: 'ENVIRONMENTAL', icon: '🏭', color: '#16a34a' }
      };
      const c = map[cat] || { label: (cat || 'NEWS').toUpperCase(), icon: '⚡', color: '#38bdf8' };
      return \`<span class="badge" style="background:\${c.color}22; color:\${c.color}; border:1px solid \${c.color}55;">\${c.icon} \${c.label}</span>\`;
    }

    function openIncidentDrawer(inc) {
      const drawer = document.getElementById('mapDetailDrawer');
      document.getElementById('drawerTitle').innerHTML = '⚡ News Intelligence Report';

      const sourcesHtml = (inc.sources || []).map(s => \`
        <a href="\${s.url}" target="_blank" rel="noopener noreferrer" style="display:flex; justify-content:space-between; align-items:center; background:rgba(10,15,28,0.7); border:1px solid var(--grid-line); padding:8px 10px; border-radius:6px; color:#edf1f5; font-size:12px; text-decoration:none; transition:border-color 0.15s;">
          <span style="font-weight:600; color:#38bdf8;">📰 \${s.publisher || 'Regional Media'}</span>
          <span style="color:var(--text-muted); font-size:11px;">Open Source ↗</span>
        </a>
      \`).join('');

      const lat = inc.location ? inc.location.coordinates[1] : 0;
      const lon = inc.location ? inc.location.coordinates[0] : 0;

      document.getElementById('drawerBody').innerHTML = \`
        <div style="display:flex; justify-content:space-between; align-items:start; gap:8px;">
          <div>
            <h4 style="font-size:16px; color:#fff; font-weight:700;">\${inc.title}</h4>
            <p style="font-size:12px; color:var(--text-muted); margin-top:2px;">
              📍 \${inc.locationName || inc.city || inc.district} · District: <b style="color:#fff;">\${(inc.district || '').toUpperCase()}</b>
            </p>
          </div>
        </div>

        <div style="display:flex; flex-wrap:wrap; gap:6px;">
          \${getCategoryBadgeHtml(inc.category)}
          \${getVerificationBadgeHtml(inc.verificationStatus, inc.sourceCount)}
          <span class="badge" style="background:rgba(255,255,255,0.08);">\${(inc.locationPrecision || 'approx').toUpperCase()} PRECISION</span>
        </div>

        <p style="font-size:13px; color:#edf1f5; line-height:1.5; background:rgba(0,0,0,0.3); padding:10px; border-radius:6px; border:1px solid var(--grid-line);">
          \${inc.description}
        </p>

        <div class="metric-row">
          <div class="metric-box">
            <div class="metric-val" style="color:var(--blue); font-size:14px;">\${formatTimeAgo(inc.eventTime || inc.firstReportedAt)}</div>
            <div class="metric-lbl">Event Occurred</div>
          </div>
          <div class="metric-box">
            <div class="metric-val" style="color:var(--green); font-size:14px;">\${inc.sourceCount || 1} Publisher(s)</div>
            <div class="metric-lbl">Corroborating Sources</div>
          </div>
        </div>

        <div>
          <label style="font-size:11px; color:var(--text-muted); font-family:'JetBrains Mono'; font-weight:600;">INDEPENDENT SOURCE ARTICLES</label>
          <div style="display:flex; flex-direction:column; gap:6px; margin-top:6px;">
            \${sourcesHtml || '<div style="font-size:11.5px; color:var(--text-faint);">GDELT DOC 2.0 Ingested Article</div>'}
          </div>
        </div>

        <div style="display:flex; gap:8px;">
          <a href="https://www.google.com/maps/dir/?api=1&destination=\${lat},\${lon}" target="_blank" rel="noopener noreferrer" class="card-btn card-btn-primary" style="display:flex; align-items:center; justify-content:center; gap:6px;">
            🧭 Route to Vicinity
          </a>
          <button class="card-btn card-btn-outline" onclick="openDisputeModal('\${inc.incidentId}', '\${encodeURIComponent(inc.title)}')">
            ⚠️ Flag / Dispute Marker
          </button>
        </div>

        <div style="font-size:10.5px; color:var(--text-faint); border-top:1px solid rgba(255,255,255,0.06); padding-top:8px; line-height:1.4;">
          ℹ️ Automated news intelligence from regional Tamil Nadu media via GDELT. May describe developing situations; not an official government evacuation order.
        </div>
      \`;
      drawer.classList.add('open');
    }

    function renderIncidentsFeed() {
      const grid = document.getElementById('incidentsGrid');
      if (!grid) return;
      grid.innerHTML = '';

      const catFilter = document.getElementById('incidentCatFilter') ? document.getElementById('incidentCatFilter').value : 'all';
      const verFilter = document.getElementById('incidentVerifyFilter') ? document.getElementById('incidentVerifyFilter').value : 'all';

      const filtered = state.incidents.filter(inc => {
        if (catFilter !== 'all' && inc.category !== catFilter) return false;
        if (verFilter !== 'all' && inc.verificationStatus !== verFilter) return false;
        return true;
      });

      if (filtered.length === 0) {
        grid.innerHTML = \`
          <div style="grid-column: 1 / -1; padding: 40px; text-align: center; color: var(--text-muted); background: var(--bg-panel); border: 1px dashed var(--grid-line); border-radius: var(--radius);">
            <p style="font-size: 15px; font-weight: 600; color: #fff;">No News Incidents Match Current Filters</p>
            <p style="font-size: 12px; margin-top: 6px;">Try changing the category or verification filter, or click Refresh News Intelligence.</p>
          </div>
        \`;
        return;
      }

      filtered.forEach(inc => {
        const card = document.createElement('div');
        card.className = 'card';
        const lat = inc.location ? inc.location.coordinates[1] : 0;
        const lon = inc.location ? inc.location.coordinates[0] : 0;

        const sourceLinks = (inc.sources || []).slice(0, 2).map(s => \`
          <a href="\${s.url}" target="_blank" rel="noopener noreferrer" style="color: #38bdf8; font-size: 11px; text-decoration: underline; margin-right: 8px;">
            \${s.publisher || 'Source'} ↗
          </a>
        \`).join('');

        card.innerHTML = \`
          <div class="card-header">
            <div>
              <div style="display: flex; gap: 6px; margin-bottom: 6px; flex-wrap: wrap;">
                \${getCategoryBadgeHtml(inc.category)}
                \${getVerificationBadgeHtml(inc.verificationStatus, inc.sourceCount)}
              </div>
              <div class="card-title">\${inc.title}</div>
              <div style="font-size: 11.5px; color: var(--text-muted); margin-top: 2px;">
                📍 \${inc.locationName || inc.city || inc.district} · \${(inc.district || '').toUpperCase()} (\${inc.locationPrecision || 'approx'})
              </div>
            </div>
          </div>

          <p style="font-size: 12.5px; color: #edf1f5; line-height: 1.45;">
            \${inc.description}
          </p>

          <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: var(--text-muted); font-family: 'JetBrains Mono';">
            <span>⏱️ \${formatTimeAgo(inc.eventTime || inc.firstReportedAt)}</span>
            <span>Sources: \${sourceLinks || inc.sourceCount || 1}</span>
          </div>

          <div class="card-actions">
            <button class="card-btn card-btn-primary" onclick="locateIncidentOnMap(\${lat}, \${lon}, '\${inc.incidentId}')">
              🗺️ View on Map
            </button>
            <button class="card-btn card-btn-outline" onclick="openDisputeModal('\${inc.incidentId}', '\${encodeURIComponent(inc.title)}')">
              ⚠️ Flag Issue
            </button>
          </div>
        \`;
        grid.appendChild(card);
      });
    }

    function locateIncidentOnMap(lat, lon, incidentId) {
      const mapTabBtn = document.querySelector('.nav-tab-btn[data-view="viewMap"]');
      if (mapTabBtn) mapTabBtn.click();

      setTimeout(() => {
        map.flyTo([lat, lon], 13, { duration: 1.2 });
        const inc = state.incidents.find(i => i.incidentId === incidentId);
        if (inc) openIncidentDrawer(inc);
      }, 250);
    }

    function openDisputeModal(incidentId, encodedTitle) {
      document.getElementById('disputeIncidentId').value = incidentId;
      document.getElementById('disputeIncidentTitle').textContent = decodeURIComponent(encodedTitle);
      document.getElementById('disputeComment').value = '';
      document.getElementById('disputeModal').classList.add('open');
    }

    async function submitDispute() {
      const incidentId = document.getElementById('disputeIncidentId').value;
      const reason = document.getElementById('disputeReason').value;
      const comment = document.getElementById('disputeComment').value;
      const btn = document.getElementById('submitDisputeBtn');

      btn.textContent = 'Submitting...';
      btn.disabled = true;

      try {
        const res = await fetch('/api/incidents/report-issue', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ incidentId, reason, comment })
        });
        const data = await res.json();
        document.getElementById('disputeModal').classList.remove('open');
        showNotification(data.message || 'Verification dispute reported. Thank you!', 'success');

        const target = state.incidents.find(i => i.incidentId === incidentId);
        if (target) {
          target.verificationStatus = 'disputed';
          renderMapMarkers();
          renderIncidentsFeed();
        }
      } catch (err) {
        showNotification('Unable to submit dispute at this moment.', 'warning');
      } finally {
        btn.textContent = 'Submit Verification Feedback';
        btn.disabled = false;
      }
    }

    async function refreshGdeltNews(triggerBtn = null) {
      if (triggerBtn) {
        triggerBtn.textContent = '⏳ Refreshing...';
        triggerBtn.disabled = true;
      }
      showNotification('Fetching latest news intelligence from GDELT across Tamil Nadu...', 'info');

      try {
        const res = await fetch('/api/incidents/refresh', { method: 'POST' });
        const data = await res.json();

        await loadIncidents();

        if (data.cycleStats) {
          showNotification(\`✓ News Sync Complete: \${data.cycleStats.newArticles || 0} articles ingested, \${data.cycleStats.updatedIncidents || 0} incidents updated.\`, 'success');
        } else {
          showNotification(data.message || 'News intelligence up to date.', 'success');
        }
      } catch (err) {
        showNotification('GDELT news sync throttled or busy. Showing persistent cached incidents.', 'warning');
      } finally {
        if (triggerBtn) {
          triggerBtn.textContent = '🔄 Refresh News';
          triggerBtn.disabled = false;
        }
      }
    }

    async function loadIncidents() {
      try {
        const res = await fetch('/api/incidents?hours=168&limit=100');
        if (!res.ok) return;
        const data = await res.json();
        if (data.data) {
          state.incidents = data.data;

          const countEl = document.getElementById('countIncidents');
          if (countEl) countEl.textContent = state.incidents.length;

          const tabCountEl = document.getElementById('tabCountIncidents');
          if (tabCountEl) tabCountEl.textContent = state.incidents.length;

          const metricTotal = document.getElementById('metricTotalIncidents');
          if (metricTotal) metricTotal.textContent = state.incidents.length;

          const metricCorrob = document.getElementById('metricCorroborated');
          if (metricCorrob) {
            const corrobCount = state.incidents.filter(i => i.verificationStatus === 'corroborated' || i.verificationStatus === 'confirmed').length;
            metricCorrob.textContent = corrobCount;
          }

          const metricArticles = document.getElementById('metricIngestedArticles');
          if (metricArticles) {
            const totalArts = state.incidents.reduce((acc, i) => acc + (i.sourceCount || 1), 0);
            metricArticles.textContent = totalArts;
          }

          const dbStatusEl = document.getElementById('metricDbStatus');
          if (dbStatusEl) {
            dbStatusEl.textContent = data.meta && data.meta.databaseConnected ? 'MongoDB (2dsphere)' : 'GeoJSON Engine';
            dbStatusEl.style.color = data.meta && data.meta.databaseConnected ? 'var(--green)' : 'var(--amber)';
          }

          renderMapMarkers();
          renderIncidentsFeed();
        }
      } catch (err) {
        console.error('Error loading incidents:', err);
      }
    }`;

if (html.includes(setupViewsTarget) && !html.includes('renderIncidentsFeed();')) {
  html = html.replace(setupViewsTarget, setupViewsReplacement);
  console.log('✓ News functions added');
}

// 8. Update DOMContentLoaded to loadIncidents
const domLoadedTarget = `    // App Initialization
    document.addEventListener('DOMContentLoaded', () => {
      initMap();
      setupTabs();
      setupRoleSwitcher();
      setupDistrictSelector();
      setupModals();
      setupViews();
      renderAnalytics();`;

const domLoadedReplacement = `    // App Initialization
    document.addEventListener('DOMContentLoaded', () => {
      initMap();
      setupTabs();
      setupRoleSwitcher();
      setupDistrictSelector();
      setupModals();
      setupViews();
      renderAnalytics();
      loadIncidents();`;

if (html.includes(domLoadedTarget) && !html.includes('loadIncidents();')) {
  html = html.replace(domLoadedTarget, domLoadedReplacement);
  console.log('✓ DOMContentLoaded updated with loadIncidents');
}

// 9. Update setupModals to bind dispute modal listeners
const setupModalsTarget = `      // SOS Modal
      const sosModal = document.getElementById('sosModal');`;

const setupModalsReplacement = `      // Dispute Modal
      const closeDisputeBtn = document.getElementById('closeDisputeModalBtn');
      if (closeDisputeBtn) {
        closeDisputeBtn.addEventListener('click', () => {
          document.getElementById('disputeModal').classList.remove('open');
        });
      }
      const submitDisputeBtn = document.getElementById('submitDisputeBtn');
      if (submitDisputeBtn) {
        submitDisputeBtn.addEventListener('click', submitDispute);
      }

      // SOS Modal
      const sosModal = document.getElementById('sosModal');`;

if (html.includes(setupModalsTarget) && !html.includes('closeDisputeModalBtn')) {
  html = html.replace(setupModalsTarget, setupModalsReplacement);
  console.log('✓ setupModals updated for dispute modal');
}

// 10. Update initMap to listen for btnRefreshGdelt and category pills
const initMapTarget = `      // Scan OSM button
      document.getElementById('btnScanOverpass').addEventListener('click', () => {
        scanOverpassForCurrentView();
      });`;

const initMapReplacement = `      // Scan OSM button
      document.getElementById('btnScanOverpass').addEventListener('click', () => {
        scanOverpassForCurrentView();
      });

      const btnRefreshGdelt = document.getElementById('btnRefreshGdelt');
      if (btnRefreshGdelt) {
        btnRefreshGdelt.addEventListener('click', () => refreshGdeltNews(btnRefreshGdelt));
      }

      const btnSyncGdeltFeed = document.getElementById('btnSyncGdeltFeed');
      if (btnSyncGdeltFeed) {
        btnSyncGdeltFeed.addEventListener('click', () => refreshGdeltNews(btnSyncGdeltFeed));
      }

      const incidentCatFilter = document.getElementById('incidentCatFilter');
      if (incidentCatFilter) {
        incidentCatFilter.addEventListener('change', renderIncidentsFeed);
      }
      const incidentVerifyFilter = document.getElementById('incidentVerifyFilter');
      if (incidentVerifyFilter) {
        incidentVerifyFilter.addEventListener('change', renderIncidentsFeed);
      }`;

if (html.includes(initMapTarget) && !html.includes('btnRefreshGdelt.addEventListener')) {
  html = html.replace(initMapTarget, initMapReplacement);
  console.log('✓ initMap updated with refresh listeners');
}

// 11. Update updateZoomAmenityVisibility to keep news incidents visible
const zoomVisibilityTarget = `if (itemType === 'fire' || itemType === 'flood' || itemType === 'blocked') {
            layer.setOpacity(1.0);`;
const zoomVisibilityReplacement = `if (itemType === 'fire' || itemType === 'flood' || itemType === 'blocked' || itemType === 'incident') {
            layer.setOpacity(1.0);`;

if (html.includes(zoomVisibilityTarget) && !html.includes("itemType === 'incident'")) {
  html = html.replace(zoomVisibilityTarget, zoomVisibilityReplacement);
  console.log('✓ updateZoomAmenityVisibility updated');
}

// Save to static/map.html and root map.html
fs.writeFileSync(mapFilePath, html, 'utf8');
fs.writeFileSync(rootMapPath, html, 'utf8');
console.log('ALL PATCHES APPLIED TO static/map.html AND map.html');
