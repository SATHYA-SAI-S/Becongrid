# BeaconGrid 2.0 — Tamil Nadu Emergency Resource Map & Real-Time News Intelligence 🛡️⚡

BeaconGrid is a centralized emergency resource locator, disaster management dashboard, and real-time news intelligence platform engineered for Tamil Nadu.

Powered by a high-performance **Node.js Express backend**, **MongoDB geospatial persistence**, and the **GDELT Project (DOC 2.0 API)**, BeaconGrid delivers comprehensive situational awareness across all 38 districts of Tamil Nadu.

---

## 🚀 Key Features

### 1. Two-Page Responsive Architecture
- **Page 1 (`/index.html`)**: Clean Overview & Landing Portal introducing the disaster network, statistics, and quick-action access.
- **Page 2 (`/map.html`)**: Tactical Command Center featuring dark high-contrast crisis tiles, floating control island, and live resource layers.

### 2. Verified Physical Emergency Resources (Statewide Across All 38 Districts)
- **🟢 130+ Hospitals & Trauma Centers**: Monitored trauma beds, ICU readiness, emergency doctors on duty, ambulances ready, and live blood inventory.
- **🔵 38 Multi-Purpose Cyclone & Flood Shelters**: Real-time occupancy tracking, female safety zones, pet accommodations, and medical assistance indicators.
- **🟣 Food & Clean Drinking Water Relief**: Community kitchens, Amma Canteens, and TNCSC distribution centers.
- **🟡 24x7 Blood Banks**: Monitored units by blood group across regional medical colleges.
- **⚫ Hazard Zones & Blocked Highways**: Flood inundation, fire outbreaks, and ghat road landslide diversions.
- **🌐 OpenStreetMap Integration**: On-demand Overpass API scanner (`⚡ Scan OSM`) for clinics, pharmacies, and police stations within the active viewport.

### 3. GDELT Real-Time News Intelligence Layer ⚡
- **GDELT DOC 2.0 Integration**: Automated ingestion pipeline scanning regional English and Tamil press.
- **7 Monitored Emergency Categories**:
  1. *Natural Disasters*: Floods, cyclones, storm surge, landslides, heatwaves.
  2. *Infrastructure Disruptions*: Road closures, bridge collapses, power outages, water cuts.
  3. *Protests & Civil Disturbances*: Rallies, highway blockades, trade union strikes.
  4. *Public Safety*: Security alerts, coastal vigilance, emergency cordon operations.
  5. *Accidents & Emergencies*: Industrial fires, godown incidents, transit collisions.
  6. *Public Health*: Epidemic surveillance, seasonal fever camps, contamination reports.
  7. *Environmental Emergencies*: Chemical spills, toxic runoff, coastal sludge incidents.
- **Multi-Publisher Corroboration**: Automatically cross-references independent reports (e.g. *The Hindu*, *Times of India*, *Dinamalar*, *DT Next*) and elevates verified status.
- **Verification Indicators**: Explicitly badges items as `✓ Officially Confirmed`, `⚡ Corroborated (X Sources)`, `⚠️ Unverified News Report`, or `❓ Disputed Marker`.
- **Sliding Marker Detail Drawer**: Full summary, event occurrence time, exact source publisher links, and navigation routing.
- **Crowdsourced Dispute Mechanism**: Users and responders can flag mislocated, duplicate, or resolved incidents directly into the audit stream via `POST /api/incidents/report-issue`.
- **Manual Refresh Control**: `[ 🔄 Refresh News ]` button with rate-limit protection and polite backoff.

### 4. Dual-Mode Storage Architecture
- **Production MongoDB**: Native `2dsphere` geospatial indexing on `location`, unique deduplication indexes on `articles` (URL and SHA-256 fingerprint), and compound indexing for rapid bounding-box and category queries.
- **Resilient Fallback Mode**: If MongoDB is not running locally, the system automatically runs an in-memory GeoJSON engine with 100% API parity, guaranteeing zero downtime.

---

## 💻 Tech Stack

- **Runtime**: Node.js (v20+)
- **Server Framework**: Express.js
- **Database**: MongoDB (with in-memory GeoJSON fallback)
- **Geospatial & Mapping**: Leaflet.js, OpenStreetMap, OSRM (Routing), Nominatim (Geocoding), Overpass API
- **External Data**: GDELT Project DOC 2.0 API
- **Visual Analytics**: Chart.js
- **Testing**: Node.js native test runner (`node --test`), Supertest

---

## 🛠️ Installation & Quickstart

### Prerequisites
- Node.js (v20+ installed)
- (Optional) MongoDB running on `mongodb://127.0.0.1:27017`

### 1. Install Dependencies
```bash
npm install
```

### 2. Start Server
```bash
npm start
```
The server will start at:
- **Landing Page**: `http://127.0.0.1:8000/`
- **Live Command Map**: `http://127.0.0.1:8000/map.html`

### 3. Run Automated Tests
```bash
npm test
```
Executes all 14 unit and integration tests verifying API endpoints, rate limiting, GDELT classification, and deduplication.

---

## 📡 REST API Reference

| Endpoint | Method | Description |
|---|---|---|
| `/api/health` | `GET` | Health status, storage engine mode, and ingestion telemetry. |
| `/api/resources` | `GET` | Overpass OSM emergency amenities by `lat`, `lon`, and `radius`. |
| `/api/geocode` | `GET` | Nominatim place search across Tamil Nadu. |
| `/api/route` | `GET` | Turn-by-turn driving route coordinates via OSRM with fallbacks. |
| `/api/incidents` | `GET` | Filter news incidents by `category`, `district`, `verificationStatus`, `hours`, or `bbox`. |
| `/api/incidents/:id` | `GET` | Detailed incident record and list of supporting source articles. |
| `/api/incidents/refresh` | `POST` | Triggers controlled manual GDELT ingestion cycle. |
| `/api/incidents/report-issue` | `POST` | Submits dispute/verification correction for a specific incident. |
| `/api/incidents/status` | `GET` | Live ingestion state, rate limiter timing, and article count. |

---

## 📜 License
MIT License. Open-source disaster management project for public safety in Tamil Nadu.
