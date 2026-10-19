# ResQCommand - Centralized Disaster & Emergency Response Platform 🛡️🚨

A real-time, interactive disaster management dashboard, volunteer coordination portal, and emergency resource locator. 

Engineered as a **complete, self-contained single-page command dashboard** that can run **standalone** (just double-click `index.html` in any browser) or served via a local web server (FastAPI/Node.js/Python).

---

## 🌟 The Problem Solved

During floods, earthquakes, cyclones, fires, or medical crises, crucial life-saving information is scattered across news feeds, social media, and emergency dispatch. **ResQCommand** brings everything into one unified, real-time command dashboard:

- **Where is the nearest shelter?** Check live capacity, occupancy percentages, and filter for women-only, pet-friendly, wheelchair-accessible, or medical facilities.
- **Which hospitals have available beds?** View live ICU beds, trauma beds, on-duty emergency doctors, and ready ambulances.
- **Which blood banks are open?** Check live inventories by blood group (A+, A-, B+, B-, O+, O-, AB+, AB-).
- **Where can I get food or clean drinking water?** Locate relief depots, view current kg of rice/water/blankets/medical kits, and reserve emergency rations.
- **Which roads are impassable?** See blocked roads and detours plotted on the map.
- **Where are volunteers currently dispatched?** View live volunteer assignments, accept rescue tasks, and track missions in progress.
- **Find missing family members?** Dedicated Missing Persons Notice Board with photos, last seen details, and direct reporter contacts.
- **Immediate Life Threat?** One-Click pulsing **SOS button** with instant GPS location broadcast.

---

## 👥 4 User Roles & Real-Time Permissions

You can switch roles on the fly using the **ROLE SWITCHER** in the top header:

| Role | Capabilities & Actions |
|---|---|
| **👤 Citizen** | Report emergencies with photos & GPS coordinates, request food/supplies reservations, view shelters & hospital beds, report missing persons, and trigger **One-Click SOS**. |
| **🤝 Volunteer** | Access the **Volunteer Dispatch Queue**, view pending distress incidents, click **"Accept Dispatch"**, update mission status (`Assigned` ➔ `Completed`), and view active volunteers on duty. |
| **🏢 Organization / NGO** | Register new evacuation relief shelters, manage shelter capacity & amenities, and update inventory counts for rice, water, blankets, and medical kits. |
| **🛡️ Government / Admin** | Broadcast emergency disaster alerts (cyclone warnings, flood evacuation orders) to the live ticker, verify citizen reports, resolve/close incidents, mark missing persons as found, and monitor real-time command analytics. |

---

## 🗺️ Disaster Map & Markers Taxonomy

The interactive Leaflet map renders 7 distinct, color-coded emergency pins:

- **🔴 Fire Outbreak**: Active fires, toxic plumes, and chemical hazard zones.
- **🟠 Flood Water**: Inundated roads, river surge levels, and stranded citizen locations.
- **🟢 Hospital**: Available beds, ICU status, emergency doctors, ready ambulances, and blood bank stock.
- **🔵 Evacuation Shelter**: Capacity vs. occupancy progress bar, pet-friendly, women-safe, and medical assistance indicators.
- **🟣 Food & Relief**: Rice (kg), drinking water (L), blankets, and medical supply depots with pickup reservation.
- **🟡 Blood Bank**: Live inventory breakdowns by blood group.
- **⚫ Blocked Road**: Road closures, debris, fallen trees, and detour directions.

---

## 📊 Live Features Breakdown

1. **Live Resource Map**: Interactive map with high-contrast crisis tiles, search bar, category filter pills (`All Layers`, `🔴 Fire`, `🟠 Flood`, `🟢 Hospital`, `🔵 Shelter`, `🟣 Food`, `🟡 Blood Bank`, `⚫ Blocked Road`), map legend, and click-to-open sliding detail drawer with turn-by-turn navigation links.
2. **Emergency Incident Reporting**: Modal form to report title, category, description, upload image evidence with instant image preview, capture GPS coordinates, and drop pins immediately on the live map.
3. **Shelter Finder & Check-In**: Instant filter chips for `Women Shelters`, `Pet Friendly`, `Medical Support`, and `Wheelchair Access`. Interactive progress bars dynamically switch from blue to red when occupancy exceeds 85%.
4. **Hospital & Blood Directory**: Grid of emergency hospitals showing free trauma beds, free ICU slots, on-duty doctors, ambulances ready, and blood reserve units.
5. **Volunteer Dispatch Portal**: Live task feed with priority rankings (`Critical`, `High`, `Medium`). Volunteers can claim dispatches with a single click.
6. **Relief & Ration Distribution**: NGO inventory tracking for staples. Citizens can enter family size and receive an instant pickup code (`RESQ-XXXXXX`).
7. **Missing Person Board**: Photo cards, age, last-seen location, medical needs, and direct contact buttons.
8. **Emergency Alerts Broadcast**: Admin-controlled ticker banner with severity tags (`EXTREME ALERT`, `SEVERE ALERT`, `ADVISORY`).
9. **One-Click SOS**: High-priority red pulsing button. Captures GPS position and creates an immediate distress beacon dispatched to all active volunteers.
10. **Command Center Analytics**: Live KPI counters (Emergencies, Beds Free, Shelter Occupancy %, Volunteers) and 3 responsive Chart.js graphics:
    - *Active Incidents by Category* (Donut Chart)
    - *Hospital Bed Availability & ICU Capacity* (Bar Chart)
    - *Volunteer Response Times Over Last 12 Hours* (Line Chart)

---

## ⚡ Zero-Setup Execution

### Option 1: Direct Browser Launch (Standalone Single File)
Double-click `index.html` in your file manager or open it in any browser:
```
file:///e:/AWT/index.html
```
- **Zero server needed**, zero Node.js or Python required.
- Everything runs client-side using `localStorage` for complete persistence!

### Option 2: Run via Python Server
```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```
Open **`http://127.0.0.1:8000`** in your browser.
