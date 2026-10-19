"""
Generates the Live Emergency Resource Map & Disaster Management Dashboard (map.html)
with exact BeaconGrid theme, decluttered top bar, 130+ hospitals across Tamil Nadu,
reliable category filters (Shelters, Blood, Food, Blocked Road, Hospitals),
and Overpass API integration.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.tn_data_expanded import (
    HOSPITALS_TN_EXPANDED,
    SHELTERS_TN_EXPANDED,
    FOOD_CENTERS_TN_EXPANDED,
    BLOOD_BANKS_TN_EXPANDED,
    EMERGENCIES_TN_EXPANDED,
    VOLUNTEERS_TN_EXPANDED,
    MISSING_PERSONS_TN_EXPANDED
)
from tools.generate_tn_data import TN_DISTRICTS

js_districts = json.dumps(TN_DISTRICTS, indent=2)
js_hospitals = json.dumps(HOSPITALS_TN_EXPANDED, indent=2)
js_shelters = json.dumps(SHELTERS_TN_EXPANDED, indent=2)
js_food = json.dumps(FOOD_CENTERS_TN_EXPANDED, indent=2)
js_blood = json.dumps(BLOOD_BANKS_TN_EXPANDED, indent=2)
js_emergencies = json.dumps(EMERGENCIES_TN_EXPANDED, indent=2)
js_volunteers = json.dumps(VOLUNTEERS_TN_EXPANDED, indent=2)
js_missing = json.dumps(MISSING_PERSONS_TN_EXPANDED, indent=2)

MAP_HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>BeaconGrid Live Map — Emergency Resource Map & Disaster Management</title>
  <meta name="description" content="Centralized real-time emergency resource map, 130+ hospital beds, cyclone shelters, relief supplies, and volunteer coordination across Tamil Nadu.">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23ff6a3d'><circle cx='12' cy='12' r='10'/><path d='M12 6v6l4 2' stroke='%230a0f1c' stroke-width='2'/></svg>">

  <!-- Google Fonts: Oswald, Inter, JetBrains Mono (Identical to BeaconGrid) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

  <!-- Leaflet CSS & JS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

  <!-- Chart.js for Analytics -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

  <style>
    :root {{
      --bg: #0a0f1c;
      --bg-panel: #10182b;
      --bg-panel-2: #141f38;
      --grid-line: #1e2a42;
      --text: #edf1f5;
      --text-muted: #8b96aa;
      --text-faint: #56617a;
      --orange: #ff6a3d;
      --orange-dim: #7a3c26;
      --green: #34d399;
      --green-dim: #1c5a45;
      --amber: #fbbf24;
      --amber-dim: #6b551c;
      --blue: #38bdf8;
      --red: #ef4444;
      --radius: 10px;
      --radius-sm: 6px;
      --radius-full: 9999px;
      --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
    }}

    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    html, body {{
      width: 100%; height: 100%; overflow: hidden;
      background: var(--bg); color: var(--text);
      font-family: 'Inter', sans-serif; font-size: 13.5px; line-height: 1.5;
      background-image:
        linear-gradient(var(--grid-line) 1px, transparent 1px),
        linear-gradient(90deg, var(--grid-line) 1px, transparent 1px);
      background-size: 48px 48px;
      background-attachment: fixed;
    }}

    .mono {{ font-family: 'JetBrains Mono', monospace; }}
    h1, h2, h3, .display, .logo {{
      font-family: 'Oswald', sans-serif;
      text-transform: uppercase;
      letter-spacing: 0.02em;
      font-weight: 600;
    }}
    a {{ color: inherit; text-decoration: none; }}
    button, input, select, textarea {{ font-family: inherit; font-size: inherit; }}

    /* Layout structure */
    .app-wrapper {{ display: flex; flex-direction: column; width: 100vw; height: 100vh; overflow: hidden; }}

    /* Clean, Sleek Top Command Header (Single Slim Bar) */
    .top-header {{
      background: rgba(10, 15, 28, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--grid-line);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 18px;
      height: 52px;
      gap: 12px;
      z-index: 1000;
      flex-shrink: 0;
    }}

    .brand-section {{ display: flex; align-items: center; gap: 12px; }}
    .logo {{
      display: flex; align-items: center; gap: 9px;
      font-size: 17px; font-weight: 700; color: #fff;
    }}
    .logo-mark {{
      width: 22px; height: 22px;
      border: 2px solid var(--orange);
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      position: relative;
    }}
    .logo-mark::after {{
      content: "";
      width: 6px; height: 6px;
      background: var(--orange);
      border-radius: 50%;
    }}

    .btn-back-overview {{
      background: transparent;
      color: var(--text-muted);
      border: 1px solid var(--grid-line);
      padding: 5px 11px;
      border-radius: 5px;
      font-size: 11.5px;
      font-weight: 600;
      transition: all 0.15s ease;
      display: flex; align-items: center; gap: 5px;
    }}
    .btn-back-overview:hover {{
      color: #fff; border-color: var(--text-faint); background: rgba(255,255,255,0.04);
    }}

    /* Radar Pulse Dot */
    .dot {{
      width: 7px; height: 7px; border-radius: 50%;
      background: var(--green);
      box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.6);
      animation: pulse-dot 2s infinite;
      flex-shrink: 0;
    }}
    @keyframes pulse-dot {{
      0% {{ box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.55); }}
      70% {{ box-shadow: 0 0 0 7px rgba(52, 211, 153, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(52, 211, 153, 0); }}
    }}

    .status-chip {{
      display: flex; align-items: center; gap: 7px;
      font-size: 11px; color: var(--text-muted);
      letter-spacing: 0.06em; font-family: 'JetBrains Mono', monospace;
    }}

    /* Nav Tabs */
    .nav-tabs {{ display: flex; gap: 4px; overflow-x: auto; scrollbar-width: none; }}
    .nav-tab-btn {{
      background: none; border: 1px solid transparent; color: var(--text-muted);
      padding: 6px 11px; border-radius: 6px; font-size: 12px; font-weight: 600;
      cursor: pointer; display: flex; align-items: center; gap: 5px; white-space: nowrap; transition: all 0.15s;
    }}
    .nav-tab-btn:hover {{ background: var(--bg-panel); color: #fff; border-color: var(--grid-line); }}
    .nav-tab-btn.active {{
      background: var(--bg-panel-2); color: var(--orange); border-color: var(--orange);
    }}

    /* Role Switcher Pill */
    .role-switcher-container {{
      display: flex; align-items: center; gap: 2px; background: var(--bg-panel);
      padding: 2px 4px; border-radius: var(--radius-full); border: 1px solid var(--grid-line);
    }}
    .role-switcher-label {{ font-size: 10px; color: var(--text-faint); font-family: 'JetBrains Mono', monospace; font-weight: 600; padding: 0 4px; }}
    .role-btn {{
      background: none; border: none; color: var(--text-muted); padding: 4px 8px; border-radius: var(--radius-full); font-size: 11.5px; font-weight: 600; cursor: pointer; transition: all 0.2s;
    }}
    .role-btn:hover {{ color: #fff; }}
    .role-btn.active {{ background: var(--orange); color: #10182b; font-weight: 700; box-shadow: 0 2px 6px rgba(255, 106, 61, 0.4); }}

    /* Quick Helplines Modal Trigger */
    .btn-helpline-trigger {{
      background: transparent;
      color: var(--amber);
      border: 1px solid var(--amber-dim);
      padding: 6px 11px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex; align-items: center; gap: 5px;
      white-space: nowrap;
      transition: all 0.15s ease;
    }}
    .btn-helpline-trigger:hover {{
      background: rgba(251, 191, 36, 0.1); border-color: var(--amber); color: #fff;
    }}

    /* Beacon SOS Button */
    .btn-sos {{
      background: var(--orange);
      color: #10182b;
      border: none;
      padding: 7px 14px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 12.5px;
      cursor: pointer;
      display: flex; align-items: center; gap: 6px;
      letter-spacing: 0.02em;
      box-shadow: 0 0 14px rgba(255, 106, 61, 0.45);
      animation: sosPulse 2s infinite;
      white-space: nowrap;
      transition: filter .15s ease;
    }}
    .btn-sos:hover {{ filter: brightness(1.12); }}
    @keyframes sosPulse {{
      0% {{ box-shadow: 0 0 0 0 rgba(255, 106, 61, 0.7); }}
      70% {{ box-shadow: 0 0 0 8px rgba(255, 106, 61, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(255, 106, 61, 0); }}
    }}

    /* Main View Area */
    .main-content-area {{ flex: 1; position: relative; overflow: hidden; display: flex; }}
    .view-panel {{ width: 100%; height: 100%; display: none; overflow-y: auto; position: relative; }}
    .view-panel.active {{ display: flex; flex-direction: column; }}

    /* Tab 1: Map View Layout */
    #viewMap {{ display: none; position: relative; width: 100%; height: 100%; }}
    #viewMap.active {{ display: block; }}
    #leafletMap {{ width: 100%; height: 100%; z-index: 1; background: var(--bg); }}

    /* Tactical Dark Tile Filter (Seamless integration with #0a0f1c with ZERO watermarks) */
    .tactical-dark-tiles .leaflet-tile {{
      filter: brightness(0.65) invert(1) contrast(3) hue-rotate(200deg) saturate(0.35) brightness(0.7);
    }}

    /* SINGLE UNIFIED FLOATING CONTROL ISLAND OVER THE MAP */
    .map-floating-island-wrapper {{
      position: absolute; top: 12px; left: 50%; transform: translateX(-50%);
      z-index: 500; pointer-events: none; width: calc(100% - 32px); max-width: 980px;
    }}
    .map-floating-island {{
      pointer-events: auto;
      background: rgba(10, 15, 28, 0.92);
      backdrop-filter: blur(12px);
      border: 1px solid var(--grid-line);
      border-radius: var(--radius);
      padding: 10px 14px;
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.65);
      display: flex; flex-direction: column; gap: 8px;
    }}

    .island-row-top {{ display: flex; gap: 8px; align-items: center; }}
    .search-input-box {{
      flex: 1; background: rgba(16, 24, 43, 0.85); border: 1px solid var(--grid-line);
      border-radius: 6px; padding: 8px 12px; color: white; outline: none; font-size: 13px;
      transition: border-color 0.15s;
    }}
    .search-input-box:focus {{ border-color: var(--orange); }}

    .district-select-box {{
      background: rgba(16, 24, 43, 0.85); border: 1px solid var(--orange-dim);
      border-radius: 6px; padding: 7px 10px; color: var(--orange); font-weight: 700;
      outline: none; cursor: pointer; font-size: 12.5px;
    }}
    .district-select-box optgroup {{ background: #0a0f1c; color: var(--orange); font-weight: 800; }}
    .district-select-box option {{ background: #10182b; color: var(--text); font-weight: 500; }}

    .btn-action-primary {{
      background: var(--orange); color: #10182b; border: none; padding: 8px 14px; border-radius: 6px;
      font-weight: 700; font-size: 12.5px; cursor: pointer; display: flex; align-items: center; gap: 5px;
      white-space: nowrap; transition: filter .15s;
    }}
    .btn-action-primary:hover {{ filter: brightness(1.1); }}

    .btn-action-scan {{
      background: var(--bg-panel-2); color: var(--green); border: 1px solid var(--green-dim);
      padding: 8px 12px; border-radius: 6px; font-weight: 700; cursor: pointer; display: flex;
      align-items: center; gap: 5px; white-space: nowrap; font-family: 'JetBrains Mono', monospace; font-size: 11.5px;
    }}
    .btn-action-scan:hover {{ background: rgba(52, 211, 153, 0.15); }}

    .btn-action-danger {{
      background: #b91c1c; color: white; border: none; padding: 8px 12px; border-radius: 6px;
      font-weight: 700; font-size: 12px; cursor: pointer; display: flex; align-items: center; gap: 5px;
      white-space: nowrap;
    }}
    .btn-action-danger:hover {{ background: #dc2626; }}

    /* Category Filter Chips Bar on Map */
    .map-category-pills {{
      display: flex; gap: 6px; overflow-x: auto; padding: 2px 0; scrollbar-width: none;
    }}
    .cat-pill {{
      background: rgba(16, 24, 43, 0.85); border: 1px solid var(--grid-line);
      color: var(--text-muted); padding: 5px 11px; border-radius: var(--radius-full);
      font-size: 11px; font-weight: 600; cursor: pointer; white-space: nowrap;
      display: flex; align-items: center; gap: 5px; font-family: 'JetBrains Mono', monospace;
      transition: all 0.15s;
    }}
    .cat-pill:hover {{ border-color: var(--text-faint); color: #fff; }}
    .cat-pill.active {{ background: var(--bg-panel-2); color: var(--orange); border-color: var(--orange); }}
    .cat-pill .dot-badge {{ width: 6px; height: 6px; border-radius: 50%; }}

    /* Map Legend Box */
    .map-legend-card {{
      position: absolute; bottom: 20px; left: 16px; z-index: 400;
      background: rgba(16, 24, 43, 0.94); backdrop-filter: blur(8px);
      border: 1px solid var(--grid-line); border-radius: var(--radius);
      padding: 10px 14px; box-shadow: var(--shadow); max-width: 250px; font-size: 11px;
    }}
    .legend-title {{
      font-family: 'Oswald', sans-serif; font-size: 11px; font-weight: 600;
      letter-spacing: 0.05em; color: var(--orange); margin-bottom: 6px; text-transform: uppercase;
    }}
    .legend-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 4px 8px; }}
    .legend-item {{ display: flex; align-items: center; gap: 5px; color: var(--text-muted); font-size: 10.5px; }}

    /* Sliding Marker Detail Drawer */
    .map-detail-drawer {{
      position: absolute; top: 12px; right: 16px; bottom: 24px; width: 380px; max-width: calc(100vw - 32px);
      z-index: 600; background: var(--bg-panel); border: 1px solid var(--grid-line);
      border-radius: var(--radius); box-shadow: var(--shadow); display: none;
      flex-direction: column; overflow: hidden; animation: slideInRight 0.25s ease-out;
    }}
    .map-detail-drawer.open {{ display: flex; }}
    @keyframes slideInRight {{ from {{ transform: translateX(100%); opacity: 0; }} to {{ transform: translateX(0); opacity: 1; }} }}

    .drawer-header {{
      padding: 14px 18px; border-bottom: 1px solid var(--grid-line);
      display: flex; align-items: center; justify-content: space-between; background: rgba(10, 15, 28, 0.7);
    }}
    .drawer-body {{ padding: 18px; overflow-y: auto; flex: 1; display: flex; flex-direction: column; gap: 14px; }}
    .drawer-close {{ background: none; border: none; color: var(--text-muted); cursor: pointer; font-size: 20px; font-weight: 800; }}
    .drawer-close:hover {{ color: #fff; }}

    /* Custom Pin Markers */
    .custom-marker-pin {{
      display: flex; align-items: center; justify-content: center; width: 34px; height: 34px;
      border-radius: 50%; color: white; font-weight: 800; font-size: 15px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.6); border: 2px solid #ffffff; cursor: pointer;
      transition: transform 0.2s, opacity 0.3s ease;
    }}
    .custom-marker-pin:hover {{ transform: scale(1.18); }}
    .custom-marker-pin.fire {{ background: var(--red); border-color: #fca5a5; }}
    .custom-marker-pin.flood {{ background: #f97316; border-color: #fdba74; }}
    .custom-marker-pin.hospital {{ background: var(--green); border-color: #a7f3d0; }}
    .custom-marker-pin.shelter {{ background: var(--blue); border-color: #bae6fd; }}
    .custom-marker-pin.food {{ background: #a855f7; border-color: #e9d5ff; }}
    .custom-marker-pin.blood {{ background: var(--amber); color: #10182b; border-color: #fde68a; }}
    .custom-marker-pin.blocked {{ background: #1e293b; border-color: var(--red); }}
    .custom-marker-pin.osm {{ background: #0284c7; border-color: #38bdf8; font-size: 12px; }}

    /* Cards Grid */
    .view-container {{ padding: 20px 28px; max-width: 1400px; margin: 0 auto; width: 100%; display: flex; flex-direction: column; gap: 18px; }}
    .view-header {{ display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; }}
    .view-title-group h2 {{ font-size: 22px; color: #fff; }}
    .view-title-group p {{ font-size: 13px; color: var(--text-muted); }}

    .cards-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px; }}
    .card {{
      background: var(--bg-panel); border: 1px solid var(--grid-line); border-radius: var(--radius);
      padding: 18px; display: flex; flex-direction: column; gap: 11px;
      transition: border-color 0.18s, transform 0.18s;
    }}
    .card:hover {{ border-color: var(--text-faint); transform: translateY(-2px); }}
    .card-header {{ display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; }}
    .card-title {{ font-size: 15px; font-weight: 700; color: #fff; }}

    .badge {{
      padding: 3px 8px; border-radius: 4px; font-size: 10.5px; font-weight: 700;
      letter-spacing: 0.04em; font-family: 'JetBrains Mono', monospace; text-transform: uppercase;
    }}
    .badge-success {{ background: rgba(52, 211, 153, 0.12); color: var(--green); border: 1px solid var(--green-dim); }}
    .badge-danger {{ background: rgba(239, 68, 68, 0.15); color: #fca5a5; border: 1px solid #b91c1c; }}
    .badge-info {{ background: rgba(56, 189, 248, 0.12); color: var(--blue); border: 1px solid rgba(56, 189, 248, 0.3); }}
    .badge-amber {{ background: rgba(251, 191, 36, 0.15); color: var(--amber); border: 1px solid var(--amber-dim); }}

    .metric-row {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; }}
    .metric-box {{
      background: rgba(10, 15, 28, 0.6); border: 1px solid var(--grid-line); border-radius: 6px;
      padding: 8px; text-align: center;
    }}
    .metric-val {{ font-size: 17px; font-weight: 700; font-family: 'JetBrains Mono', monospace; color: #fff; }}
    .metric-lbl {{ font-size: 10.5px; color: var(--text-muted); }}

    .card-actions {{ display: flex; gap: 8px; margin-top: auto; padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.06); }}
    .card-btn {{
      flex: 1; padding: 7px 10px; border-radius: 5px; font-size: 11.5px; font-weight: 600;
      cursor: pointer; text-align: center; transition: all 0.15s;
    }}
    .card-btn-primary {{ background: var(--orange); color: #10182b; border: none; font-weight: 700; }}
    .card-btn-primary:hover {{ filter: brightness(1.1); }}
    .card-btn-outline {{ background: transparent; color: var(--text-muted); border: 1px solid var(--grid-line); }}
    .card-btn-outline:hover {{ color: #fff; border-color: var(--text-faint); background: rgba(255,255,255,0.04); }}

    /* Modals */
    .modal-backdrop {{
      position: fixed; inset: 0; background: rgba(10, 15, 28, 0.85); backdrop-filter: blur(6px);
      z-index: 2000; display: none; align-items: center; justify-content: center; padding: 16px;
    }}
    .modal-backdrop.open {{ display: flex; }}
    .modal-box {{
      background: var(--bg-panel); border: 1px solid var(--grid-line); border-radius: var(--radius);
      width: 100%; max-width: 540px; box-shadow: var(--shadow); display: flex; flex-direction: column; overflow: hidden;
      animation: modalFadeIn 0.2s ease-out;
    }}
    @keyframes modalFadeIn {{ from {{ opacity: 0; transform: scale(0.96); }} to {{ opacity: 1; transform: scale(1); }} }}
    .modal-header {{
      padding: 16px 20px; border-bottom: 1px solid var(--grid-line);
      display: flex; align-items: center; justify-content: space-between;
    }}
    .modal-header h3 {{ font-size: 17px; color: #fff; }}
    .modal-body {{ padding: 20px; display: flex; flex-direction: column; gap: 14px; overflow-y: auto; max-height: 80vh; }}
    .form-group {{ display: flex; flex-direction: column; gap: 6px; }}
    .form-group label {{ font-size: 11.5px; font-weight: 600; color: var(--text-muted); font-family: 'JetBrains Mono', monospace; }}
    .form-control {{
      background: rgba(10, 15, 28, 0.8); border: 1px solid var(--grid-line); border-radius: 6px;
      padding: 9px 12px; color: #fff; outline: none; font-size: 13px;
    }}
    .form-control:focus {{ border-color: var(--orange); }}

    /* Notification Toast */
    #globalToast {{
      position: fixed; bottom: 24px; right: 24px; z-index: 9999;
      background: var(--bg-panel-2); border: 1px solid var(--orange);
      color: #fff; padding: 12px 18px; border-radius: 6px; box-shadow: var(--shadow);
      display: none; align-items: center; gap: 10px; font-weight: 500; font-size: 13px;
      animation: toastSlideUp 0.25s ease-out; max-width: 420px;
    }}
    @keyframes toastSlideUp {{ from {{ transform: translateY(20px); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }}

    /* Responsive */
    @media (max-width: 860px) {{
      .top-header {{ padding: 0 10px; }}
      .nav-tabs {{ display: none; }}
      .map-floating-island-wrapper {{ width: calc(100% - 16px); top: 8px; }}
      .island-row-top {{ flex-wrap: wrap; }}
      .search-input-box {{ min-width: 180px; }}
      .map-legend-card {{ display: none; }}
      .map-detail-drawer {{
        left: 0; right: 0; bottom: 0; top: auto; width: 100%; max-width: 100%; height: 60vh;
        border-radius: var(--radius) var(--radius) 0 0;
      }}
    }}
  </style>
</head>
<body>
  <div class="app-wrapper">
    <!-- Clean, Slim Top Command Header -->
    <header class="top-header">
      <div class="brand-section">
        <a href="index.html" class="logo" title="Return to Landing Page">
          <span class="logo-mark"></span>BeaconGrid
        </a>
        <a href="index.html" class="btn-back-overview">← Overview</a>
        <div class="status-chip"><span class="dot"></span> TN GRID</div>
      </div>

      <!-- Navigation Tabs -->
      <nav class="nav-tabs" role="tablist">
        <button class="nav-tab-btn active" data-view="viewMap">🗺️ State Map</button>
        <button class="nav-tab-btn" data-view="viewHospitals">🟢 Hospitals (130+)</button>
        <button class="nav-tab-btn" data-view="viewShelters">🔵 Shelters (38)</button>
        <button class="nav-tab-btn" data-view="viewFood">🟣 Food & Relief</button>
        <button class="nav-tab-btn" data-view="viewVolunteers">🤝 Volunteers</button>
        <button class="nav-tab-btn" data-view="viewMissing">🔍 Missing Board</button>
        <button class="nav-tab-btn" data-view="viewAnalytics">📊 Analytics</button>
      </nav>

      <!-- Right Controls: Role, Helplines Button, SOS -->
      <div style="display: flex; align-items: center; gap: 8px;">
        <div class="role-switcher-container">
          <span class="role-switcher-label">ROLE:</span>
          <button class="role-btn active" data-role="citizen">👤 Citizen</button>
          <button class="role-btn" data-role="volunteer">🤝 Vol</button>
          <button class="role-btn" data-role="ngo">🏢 NGO</button>
          <button class="role-btn" data-role="admin">🛡️ Admin</button>
        </div>

        <button class="btn-helpline-trigger" id="openHelplinesModalBtn" title="Official Tamil Nadu Emergency Helpline Numbers">
          📞 Helplines
        </button>

        <button class="btn-sos" id="globalSosBtn" title="Instant Life-Threatening SOS Dispatch">
          🚨 ONE-CLICK SOS
        </button>
      </div>
    </header>

    <!-- Main Content Area -->
    <main class="main-content-area">

      <!-- ================= TAB 1: LIVE TAMIL NADU MAP ================= -->
      <section id="viewMap" class="view-panel active">
        <div id="leafletMap"></div>

        <!-- Single Floating Island over Map -->
        <div class="map-floating-island-wrapper">
          <div class="map-floating-island">
            <!-- Row 1: District Select, Search, Scan OSM, Report -->
            <div class="island-row-top">
              <select id="districtSelector" class="district-select-box" aria-label="Select Tamil Nadu District">
                <option value="all">📍 All Tamil Nadu (38 Districts Overview)</option>
                <optgroup label="── Chennai Metropolitan Area ──">
                  <option value="chennai" selected>🏙️ Chennai (State Capital)</option>
                  <option value="chengalpattu">🏙️ Chengalpattu</option>
                  <option value="kancheepuram">🏛️ Kancheepuram (Silk & Temples)</option>
                  <option value="tiruvallur">🏭 Tiruvallur (Industrial Hub)</option>
                </optgroup>
                <optgroup label="── Northern Region ──">
                  <option value="cuddalore">🌊 Cuddalore (Coastal Surge Zone)</option>
                  <option value="viluppuram">🌾 Viluppuram</option>
                  <option value="kallakurichi">🌾 Kallakurichi</option>
                  <option value="vellore">🏙️ Vellore (CMC & Fort)</option>
                  <option value="ranipet">🏭 Ranipet</option>
                  <option value="tirupathur">🌄 Tirupathur</option>
                  <option value="tiruvannamalai">⛰️ Tiruvannamalai (Annamalai)</option>
                </optgroup>
                <optgroup label="── Western (Kongu) Region ──">
                  <option value="coimbatore">🏙️ Coimbatore (Kongu Capital)</option>
                  <option value="tiruppur">👕 Tiruppur (Knitwear Hub)</option>
                  <option value="erode">🏭 Erode (Turmeric & River Basin)</option>
                  <option value="salem">⛰️ Salem (Steel & Mango City)</option>
                  <option value="namakkal">🥚 Namakkal (Poultry & Transport)</option>
                  <option value="dharmapuri">🥭 Dharmapuri</option>
                  <option value="krishnagiri">🏭 Krishnagiri / Hosur Tech Corridor</option>
                  <option value="nilgiris">🏔️ Nilgiris / Ooty (Western Ghats)</option>
                </optgroup>
                <optgroup label="── Central & Cauvery Delta Region ──">
                  <option value="trichy">🏙️ Tiruchirappalli (Trichy Central)</option>
                  <option value="thanjavur">🌾 Thanjavur (Cauvery Delta Granary)</option>
                  <option value="nagapattinam">🌊 Nagapattinam (Delta Coast)</option>
                  <option value="mayiladuthurai">🌊 Mayiladuthurai</option>
                  <option value="tiruvarur">🌾 Tiruvarur</option>
                  <option value="karur">🏭 Karur (Textile & Amaravathi)</option>
                  <option value="perambalur">🌾 Perambalur</option>
                  <option value="ariyalur">🏭 Ariyalur (Cement Hub)</option>
                  <option value="pudukkottai">🏛️ Pudukkottai</option>
                </optgroup>
                <optgroup label="── Southern Region ──">
                  <option value="madurai">🏙️ Madurai (Cultural Capital)</option>
                  <option value="dindigul">⛰️ Dindigul (Lock City)</option>
                  <option value="theni">🌄 Theni (Cardamom Hills)</option>
                  <option value="virudhunagar">🏭 Virudhunagar / Sivakasi</option>
                  <option value="sivaganga">🏛️ Sivaganga / Karaikudi</option>
                  <option value="ramanathapuram">🌊 Ramanathapuram / Rameswaram</option>
                  <option value="thoothukudi">⚓ Thoothukudi (VOC Port City)</option>
                  <option value="tirunelveli">🏙️ Tirunelveli (Halwa & River City)</option>
                  <option value="tenkasi">🌊 Tenkasi / Courtallam Falls</option>
                  <option value="kanyakumari">🌊 Kanniyakumari (Cape Comorin)</option>
                </optgroup>
              </select>

              <input type="text" id="mapSearchInput" class="search-input-box" placeholder="Search 130+ hospitals, shelters, towns, highways...">
              <button class="btn-action-primary" id="btnGeocodeSearch" title="Search place">🔍 Search</button>
              <button class="btn-action-scan" id="btnScanOverpass" title="Query Overpass API for live OSM amenities in current view">⚡ Scan OSM</button>
              <button class="btn-action-danger" id="reportEmergencyMapBtn">➕ Report</button>
            </div>

            <!-- Row 2: Category Filter Pills -->
            <div class="map-category-pills" id="mapCategoryPills">
              <button class="cat-pill active" data-cat="all">All (<span id="countAll">0</span>)</button>
              <button class="cat-pill" data-cat="hospital"><span class="dot-badge" style="background:var(--green);"></span>🟢 Hospitals (<span id="countHospital">0</span>)</button>
              <button class="cat-pill" data-cat="shelter"><span class="dot-badge" style="background:var(--blue);"></span>🔵 Shelters (<span id="countShelter">0</span>)</button>
              <button class="cat-pill" data-cat="food"><span class="dot-badge" style="background:#a855f7;"></span>🟣 Food (<span id="countFood">0</span>)</button>
              <button class="cat-pill" data-cat="blood"><span class="dot-badge" style="background:var(--amber);"></span>🟡 Blood Banks (<span id="countBlood">0</span>)</button>
              <button class="cat-pill" data-cat="fire"><span class="dot-badge" style="background:var(--red);"></span>🔴 Fire (<span id="countFire">0</span>)</button>
              <button class="cat-pill" data-cat="flood"><span class="dot-badge" style="background:#f97316;"></span>🟠 Flood (<span id="countFlood">0</span>)</button>
              <button class="cat-pill" data-cat="blocked"><span class="dot-badge" style="background:var(--text-faint);"></span>⚫ Blocked Road (<span id="countBlocked">0</span>)</button>
            </div>
          </div>
        </div>

        <!-- Map Marker Legend -->
        <div class="map-legend-card">
          <div class="legend-title">Disaster Grid Legend</div>
          <div class="legend-grid">
            <div class="legend-item"><span>🟢</span> Hospital / ICU</div>
            <div class="legend-item"><span>🔵</span> Shelter Camp</div>
            <div class="legend-item"><span>🟣</span> Food Supply</div>
            <div class="legend-item"><span>🟡</span> Blood Bank</div>
            <div class="legend-item"><span>🔴</span> Active Fire</div>
            <div class="legend-item"><span>🟠</span> Flood Zone</div>
            <div class="legend-item"><span>⚫</span> Blocked Road</div>
            <div class="legend-item"><span>🌐</span> Live OSM</div>
          </div>
        </div>

        <!-- Sliding Marker Detail Drawer -->
        <div class="map-detail-drawer" id="mapDetailDrawer">
          <div class="drawer-header">
            <h3 id="drawerTitle">Resource Details</h3>
            <button class="drawer-close" id="closeDrawerBtn">&times;</button>
          </div>
          <div class="drawer-body" id="drawerBody">
            <!-- Dynamic Details Loaded Here -->
          </div>
        </div>
      </section>

      <!-- ================= TAB 2: HOSPITALS & BEDS (130+ INSTITUTIONS) ================= -->
      <section id="viewHospitals" class="view-panel">
        <div class="view-container">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Tamil Nadu Hospital & Trauma Network</h2>
              <p>Real-time bed availability, ICU readiness, emergency doctors on duty, and ambulance dispatch across all 38 districts.</p>
            </div>
            <div style="display:flex; gap:10px;">
              <input type="text" id="hospitalSearchInput" class="search-input-box" placeholder="Filter hospitals by district or name..." style="width: 280px;">
            </div>
          </div>
          <div class="cards-grid" id="hospitalsGrid"></div>
        </div>
      </section>

      <!-- ================= TAB 3: SHELTER FINDER ================= -->
      <section id="viewShelters" class="view-panel">
        <div class="view-container">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Emergency Cyclone & Flood Shelters</h2>
              <p>Government multi-purpose cyclone shelters, school relief camps, and community centers with occupancy tracking.</p>
            </div>
            <button class="btn-action-primary" id="openAddShelterModalBtn" style="display:none;">➕ Register New Shelter</button>
          </div>
          <div class="cards-grid" id="sheltersGrid"></div>
        </div>
      </section>

      <!-- ================= TAB 4: FOOD & RELIEF DISTRIBUTION ================= -->
      <section id="viewFood" class="view-panel">
        <div class="view-container">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Food, Drinking Water & Relief Supplies</h2>
              <p>Community kitchens, Amma Canteens, and TNCSC relief supply points. Reserve or coordinate emergency rations.</p>
            </div>
            <button class="btn-action-primary" id="openAddSupplyModalBtn" style="display:none;">➕ Dispatch New Supplies</button>
          </div>
          <div class="cards-grid" id="foodGrid"></div>
        </div>
      </section>

      <!-- ================= TAB 5: VOLUNTEER COORDINATION ================= -->
      <section id="viewVolunteers" class="view-panel">
        <div class="view-container">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Volunteer Coordination & Rapid Dispatch</h2>
              <p>Disaster response teams, boat operators, trauma nurses, and amateur ham radio operators active in the field.</p>
            </div>
            <button class="btn-action-primary" id="registerVolunteerBtn">🙋 Register as Volunteer</button>
          </div>
          <div class="cards-grid" id="volunteersGrid"></div>
        </div>
      </section>

      <!-- ================= TAB 6: MISSING PERSONS BULLETIN ================= -->
      <section id="viewMissing" class="view-panel">
        <div class="view-container">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Missing Persons Emergency Bulletin</h2>
              <p>Help families reunite during natural disasters. Submit or identify missing citizens safely.</p>
            </div>
            <button class="btn-action-danger" id="reportMissingPersonBtn">➕ Report Missing Person</button>
          </div>
          <div class="cards-grid" id="missingGrid"></div>
        </div>
      </section>

      <!-- ================= TAB 7: ANALYTICS DASHBOARD ================= -->
      <section id="viewAnalytics" class="view-panel">
        <div class="view-container">
          <div class="view-header">
            <div class="view-title-group">
              <h2>Disaster Management Incident Analytics</h2>
              <p>Statewide situational telemetry, hospital resource utilization, and volunteer mobilization metrics.</p>
            </div>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
            <div class="card" style="text-align: center;">
              <div class="metric-val" id="kpiEmergencies" style="color:var(--red);">0</div>
              <div class="metric-lbl">Active Emergencies</div>
            </div>
            <div class="card" style="text-align: center;">
              <div class="metric-val" id="kpiHospitalsTotal" style="color:var(--green);">130+</div>
              <div class="metric-lbl">Monitored Hospitals</div>
            </div>
            <div class="card" style="text-align: center;">
              <div class="metric-val" id="kpiEvacuees" style="color:var(--blue);">0</div>
              <div class="metric-lbl">Sheltered Evacuees</div>
            </div>
            <div class="card" style="text-align: center;">
              <div class="metric-val" id="kpiIcu" style="color:var(--amber);">0</div>
              <div class="metric-lbl">Available ICU Units</div>
            </div>
            <div class="card" style="text-align: center;">
              <div class="metric-val" id="kpiVolunteers" style="color:#a855f7;">0</div>
              <div class="metric-lbl">Deployed Volunteers</div>
            </div>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 18px;">
            <div class="card">
              <div class="card-title">Emergencies by Category</div>
              <canvas id="chartEmergencies" style="max-height: 250px;"></canvas>
            </div>
            <div class="card">
              <div class="card-title">Available Beds in Major Districts</div>
              <canvas id="chartBeds" style="max-height: 250px;"></canvas>
            </div>
          </div>
        </div>
      </section>

    </main>
  </div>

  <!-- Quick Helplines Modal -->
  <div class="modal-backdrop" id="helplinesModal">
    <div class="modal-box">
      <div class="modal-header">
        <h3>Official Tamil Nadu Emergency Helplines</h3>
        <button class="drawer-close" id="closeHelplinesModalBtn">&times;</button>
      </div>
      <div class="modal-body">
        <p style="color:var(--text-muted); font-size:12.5px;">Click any number to initiate an immediate emergency telephone call:</p>
        <div style="display:flex; flex-direction:column; gap:8px;">
          <a href="tel:1070" style="background:rgba(255,106,61,0.12); border:1px solid var(--orange); padding:10px 14px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
            <span>State Disaster Control (TNSDMA)</span>
            <b style="color:var(--orange); font-size:16px; font-family:'JetBrains Mono';">1070</b>
          </a>
          <a href="tel:1077" style="background:var(--bg-panel-2); border:1px solid var(--grid-line); padding:10px 14px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
            <span>District Collector Emergency Cell</span>
            <b style="color:var(--amber); font-size:16px; font-family:'JetBrains Mono';">1077</b>
          </a>
          <a href="tel:108" style="background:var(--bg-panel-2); border:1px solid var(--grid-line); padding:10px 14px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
            <span>Emergency Ambulance & Trauma Care</span>
            <b style="color:var(--green); font-size:16px; font-family:'JetBrains Mono';">108</b>
          </a>
          <a href="tel:112" style="background:var(--bg-panel-2); border:1px solid var(--grid-line); padding:10px 14px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
            <span>Police / Unified All Emergency</span>
            <b style="color:#fff; font-size:16px; font-family:'JetBrains Mono';">112</b>
          </a>
          <a href="tel:101" style="background:var(--bg-panel-2); border:1px solid var(--grid-line); padding:10px 14px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
            <span>Fire & Rescue Services (TNFRS)</span>
            <b style="color:var(--red); font-size:16px; font-family:'JetBrains Mono';">101</b>
          </a>
          <a href="tel:1093" style="background:var(--bg-panel-2); border:1px solid var(--grid-line); padding:10px 14px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
            <span>Coastal Marine & Cyclone Security</span>
            <b style="color:var(--blue); font-size:16px; font-family:'JetBrains Mono';">1093</b>
          </a>
          <a href="tel:104" style="background:var(--bg-panel-2); border:1px solid var(--grid-line); padding:10px 14px; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
            <span>Medical Advice & Hospital Bed Info</span>
            <b style="color:var(--amber); font-size:16px; font-family:'JetBrains Mono';">104</b>
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- Report Emergency Modal -->
  <div class="modal-backdrop" id="reportEmergencyModal">
    <div class="modal-box">
      <div class="modal-header">
        <h3>Report Hazard / Disaster Incident</h3>
        <button class="drawer-close" id="closeReportEmergencyBtn">&times;</button>
      </div>
      <form id="emergencyReportForm" class="modal-body">
        <div class="form-group">
          <label>INCIDENT TITLE</label>
          <input type="text" id="reportTitle" class="form-control" placeholder="e.g. Mudichur Low-lying Water Inundation" required>
        </div>
        <div class="form-group">
          <label>CATEGORY</label>
          <select id="reportCategory" class="form-control" required>
            <option value="flood">🌊 Flood / Waterlogging</option>
            <option value="fire">🔴 Fire Incident</option>
            <option value="blocked">⚫ Blocked Highway / Landslide</option>
          </select>
        </div>
        <div class="form-group">
          <label>TAMIL NADU DISTRICT</label>
          <select id="reportDistrict" class="form-control" required>
            <option value="chennai">Chennai</option>
            <option value="chengalpattu">Chengalpattu</option>
            <option value="kancheepuram">Kancheepuram</option>
            <option value="tiruvallur">Tiruvallur</option>
            <option value="cuddalore">Cuddalore</option>
            <option value="coimbatore">Coimbatore</option>
            <option value="nilgiris">Nilgiris</option>
            <option value="madurai">Madurai</option>
            <option value="trichy">Tiruchirappalli</option>
            <option value="thanjavur">Thanjavur</option>
            <option value="tirunelveli">Tirunelveli</option>
            <option value="kanyakumari">Kanniyakumari</option>
          </select>
        </div>
        <div class="form-group">
          <label>DESCRIPTION & SPECIFIC LOCATION</label>
          <textarea id="reportDescription" class="form-control" rows="3" placeholder="Provide landmarks, water depth, number of stranded people..." required></textarea>
        </div>
        <div style="display: flex; gap: 10px; margin-top: 8px;">
          <button type="button" class="card-btn card-btn-outline" id="btnCaptureLocation">📍 Use My GPS</button>
          <button type="submit" class="card-btn card-btn-primary" style="flex:2;">SUBMIT REPORT</button>
        </div>
      </form>
    </div>
  </div>

  <!-- One-Click SOS Modal -->
  <div class="modal-backdrop" id="sosModal">
    <div class="modal-box" style="border-color: var(--orange);">
      <div class="modal-header" style="background: rgba(255, 106, 61, 0.15);">
        <h3 style="color: var(--orange);">🚨 LIFE-THREATENING EMERGENCY SOS</h3>
        <button class="drawer-close" id="closeSosBtn">&times;</button>
      </div>
      <div class="modal-body">
        <p style="color: #fff; font-weight: 600;">Your SOS broadcast will immediately dispatch your GPS location to the nearest Disaster Response Team and Volunteer Wing.</p>
        <div class="form-group">
          <label>YOUR CONTACT PHONE NUMBER</label>
          <input type="tel" id="sosPhone" class="form-control" placeholder="+91 98400 00000" required>
        </div>
        <div class="form-group">
          <label>EMERGENCY TYPE</label>
          <select id="sosType" class="form-control">
            <option value="Medical Emergency">🩺 Severe Medical / Trauma Emergency</option>
            <option value="Trapped in Flood">🌊 Trapped in Rising Floodwater</option>
            <option value="Fire Outbreak">🔥 Trapped in Fire / Smoke</option>
            <option value="Elderly / Infant Rescue">👶 Elderly / Infant Rescue</option>
          </select>
        </div>
        <div class="form-group">
          <label>CURRENT LOCATION STATUS</label>
          <div id="sosGpsStatus" class="mono" style="font-size: 11.5px; color: var(--green); background: rgba(0,0,0,0.4); padding: 8px; border-radius: 4px;">
            Detecting device high-precision coordinates...
          </div>
        </div>
        <button type="button" class="btn-sos" id="confirmSosDispatchBtn" style="width: 100%; justify-content: center; padding: 12px; font-size: 14px;">
          BROADCAST IMMEDIATE RESCUE DISPATCH
        </button>
      </div>
    </div>
  </div>

  <!-- Global Toast -->
  <div id="globalToast"></div>

  <!-- Core JavaScript Data & App Logic -->
  <script>
    // Embedded authentic datasets
    const TN_DISTRICTS = {js_districts};
    const HOSPITALS_DATA = {js_hospitals};
    const SHELTERS_DATA = {js_shelters};
    const FOOD_DATA = {js_food};
    const BLOOD_DATA = {js_blood};
    const EMERGENCIES_DATA = {js_emergencies};
    const VOLUNTEERS_DATA = {js_volunteers};
    const MISSING_DATA = {js_missing};

    // Application state
    let state = {{
      currentRole: 'citizen',
      hospitals: [...HOSPITALS_DATA],
      shelters: [...SHELTERS_DATA],
      foodCenters: [...FOOD_DATA],
      bloodBanks: [...BLOOD_DATA],
      emergencies: [...EMERGENCIES_DATA],
      volunteers: [...VOLUNTEERS_DATA],
      missingPersons: [...MISSING_DATA]
    }};

    let map = null;
    let markersLayer = null;
    let osmLayer = null;
    let currentCategoryFilter = 'all';
    let currentDistrict = 'all';
    let currentActiveTab = 'viewMap';

    // Toast helper
    function showNotification(msg, type = 'info') {{
      const toast = document.getElementById('globalToast');
      toast.textContent = msg;
      toast.style.display = 'flex';
      toast.style.borderColor = type === 'success' ? 'var(--green)' : type === 'warning' ? 'var(--amber)' : 'var(--orange)';
      setTimeout(() => {{
        toast.style.display = 'none';
      }}, 3600);
    }}

    // App Initialization
    document.addEventListener('DOMContentLoaded', () => {{
      initMap();
      setupTabs();
      setupRoleSwitcher();
      setupDistrictSelector();
      setupModals();
      setupViews();
      renderAnalytics();

      // Check URL parameters
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.get('action') === 'report') {{
        document.getElementById('reportEmergencyModal').classList.add('open');
      }}
    }});

    // Tab Navigation
    function setupTabs() {{
      const tabButtons = document.querySelectorAll('.nav-tab-btn');
      tabButtons.forEach(btn => {{
        btn.addEventListener('click', () => {{
          const targetView = btn.dataset.view;
          currentActiveTab = targetView;

          tabButtons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');

          document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));
          const panel = document.getElementById(targetView);
          if (panel) panel.classList.add('active');

          if (targetView === 'viewMap') {{
            setTimeout(() => {{
              if (map) map.invalidateSize();
            }}, 100);
          }}

          // If switching to viewHospitals, filter to hospitals mode
          if (targetView === 'viewHospitals') {{
            renderHospitalsView();
          }}
          updateZoomAmenityVisibility();
        }});
      }});
    }}

    // Role Switcher
    function setupRoleSwitcher() {{
      const roleBtns = document.querySelectorAll('.role-btn');
      roleBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
          roleBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          state.currentRole = btn.dataset.role;

          // Toggle visibility of role-specific buttons
          const isNGO = state.currentRole === 'ngo' || state.currentRole === 'admin';
          const addShelterBtn = document.getElementById('openAddShelterModalBtn');
          const addSupplyBtn = document.getElementById('openAddSupplyModalBtn');
          if (addShelterBtn) addShelterBtn.style.display = isNGO ? 'block' : 'none';
          if (addSupplyBtn) addSupplyBtn.style.display = isNGO ? 'block' : 'none';

          showNotification(`Switched role to ${{state.currentRole.toUpperCase()}}`, 'info');
        }});
      }});
    }}

    // ================= MAP INITIALIZATION & RENDERING =================
    function initMap() {{
      // Center on Tamil Nadu overview: [10.8505, 78.6856], zoom 7.4
      map = L.map('leafletMap', {{
        center: [10.8505, 78.6856],
        zoom: 7.4,
        minZoom: 6.5,
        maxZoom: 18,
        zoomControl: true,
        attributionControl: false
      }});

      // High-performance OpenStreetMap Carto tiles
      L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
        maxZoom: 19,
        subdomains: ['a', 'b', 'c']
      }}).addTo(map);

      // Apply tactical dark filter to tile container
      map.getContainer().classList.add('tactical-dark-tiles');

      markersLayer = L.layerGroup().addTo(map);
      osmLayer = L.layerGroup().addTo(map);

      renderMapMarkers();

      // Zoom event listener for dynamic amenity fading in 'all' mode
      map.on('zoomend moveend', () => {{
        updateZoomAmenityVisibility();
      }});

      // Search bar input
      const mapSearchInput = document.getElementById('mapSearchInput');
      mapSearchInput.addEventListener('input', (e) => {{
        const q = e.target.value.toLowerCase().trim();
        filterMapMarkers(q);
      }});

      // Category pills on map
      document.querySelectorAll('#mapCategoryPills .cat-pill').forEach(btn => {{
        btn.addEventListener('click', () => {{
          document.querySelectorAll('#mapCategoryPills .cat-pill').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          currentCategoryFilter = btn.dataset.cat;

          renderMapMarkers();

          // Auto-fit bounds if we have matching markers so all facilities are immediately visible!
          if (currentCategoryFilter !== 'all') {{
            try {{
              const bounds = markersLayer.getBounds();
              if (bounds.isValid()) {{
                map.fitBounds(bounds.pad(0.06), {{ maxZoom: 14, duration: 0.8 }});
              }}
            }} catch (err) {{}}
          }}

          const catNames = {{
            'all': 'All Resources',
            'hospital': '130+ Hospitals & Trauma Centers',
            'shelter': 'Emergency Cyclone & Flood Shelters',
            'food': 'Food & Water Relief Supplies',
            'blood': '24x7 Blood Banks',
            'fire': 'Fire Incidents',
            'flood': 'Flood & Inundation Zones',
            'blocked': 'Blocked Roads & Landslides'
          }};
          showNotification(`Filter: ${{catNames[currentCategoryFilter] || currentCategoryFilter}}`, 'info');
        }});
      }});

      // Drawer close
      document.getElementById('closeDrawerBtn').addEventListener('click', () => {{
        document.getElementById('mapDetailDrawer').classList.remove('open');
      }});

      // Scan OSM button
      document.getElementById('btnScanOverpass').addEventListener('click', () => {{
        scanOverpassForCurrentView();
      }});

      // Search geocode button
      document.getElementById('btnGeocodeSearch').addEventListener('click', () => {{
        const query = mapSearchInput.value.trim();
        if (query) geocodeAndFly(query);
      }});
    }}

    // ================= ZOOM & CATEGORY VISIBILITY (BUG FIX) =================
    function updateZoomAmenityVisibility() {{
      const zoom = map.getZoom();

      // CRITICAL FIX: If ANY specific category filter is chosen, all items of that category
      // MUST have opacity = 1.0, NEVER faded or hidden!
      const hasSpecificCategory = (currentCategoryFilter && currentCategoryFilter !== 'all');

      markersLayer.eachLayer(layer => {{
        if (!layer.customData) return;
        const itemType = layer.customData.type;

        if (hasSpecificCategory) {{
          // Selected category: 100% visible!
          layer.setOpacity(1.0);
        }} else {{
          // "All" mode:
          // Active disaster hazards (fire, flood, road blocked) always visible
          if (itemType === 'fire' || itemType === 'flood' || itemType === 'blocked') {{
            layer.setOpacity(1.0);
          }} else if (itemType === 'hospital') {{
            // Hospitals visible statewide at high opacity
            layer.setOpacity(zoom >= 10 ? 1.0 : 0.85);
          }} else {{
            // Shelters, food, blood: fully visible at zoom >= 11, subtle at state zoom
            layer.setOpacity(zoom >= 11 ? 1.0 : 0.65);
          }}
        }}
      }});
    }}

    // ================= OVERPASS API LIVE AMENITIES SCAN =================
    async function scanOverpassForCurrentView() {{
      const center = map.getCenter();
      const zoom = map.getZoom();
      const radius = zoom >= 14 ? 3500 : 6000;
      const btn = document.getElementById('btnScanOverpass');
      btn.textContent = '⏳ Scanning...';
      btn.disabled = true;

      try {{
        const url = `/api/resources?lat=${{center.lat.toFixed(4)}}&lon=${{center.lng.toFixed(4)}}&radius=${{radius}}`;
        const resp = await fetch(url);
        if (!resp.ok) throw new Error('Overpass temporarily busy');
        const data = await resp.json();

        if (data.data && data.data.length > 0) {{
          osmLayer.clearLayers();
          data.data.forEach(item => {{
            const marker = L.marker([item.lat, item.lon], {{
              icon: createMarkerIcon('osm', item.category === 'pharmacy' ? '💊' : item.category === 'clinic' ? '🩺' : item.category === 'fire_station' ? '🚒' : item.category === 'police' ? '👮' : '🌐')
            }});
            marker.bindPopup(`
              <div style="font-family:'Inter',sans-serif; color:#0f172a; padding:4px;">
                <strong style="color:#0284c7; font-size:13px;">${{item.name || 'OSM Emergency Node'}}</strong><br>
                <small style="color:#64748b;">${{item.address || item.category}}</small><br>
                <small>Distance: ${{item.distance_meters}}m</small>
              </div>
            `);
            osmLayer.addLayer(marker);
          }});
          showNotification(`⚡ Loaded ${{data.data.length}} live OpenStreetMap facilities in this sector`, 'success');
        }} else {{
          showNotification('No extra OSM emergency points found in this radius.', 'info');
        }}
      }} catch (e) {{
        showNotification('OSM live query throttled. Showing verified Tamil Nadu grid resources.', 'warning');
      }} finally {{
        btn.textContent = '⚡ Scan OSM';
        btn.disabled = false;
      }}
    }}

    async function geocodeAndFly(query) {{
      try {{
        const resp = await fetch(`/api/geocode?q=${{encodeURIComponent(query + ', Tamil Nadu')}}`);
        const data = await resp.json();
        if (data.results && data.results.length > 0) {{
          const first = data.results[0];
          map.flyTo([first.lat, first.lon], 13, {{ duration: 1.2 }});
          showNotification(`📍 Located: ${{first.name}}`, 'info');
        }} else {{
          filterMapMarkers(query.toLowerCase());
        }}
      }} catch (err) {{
        filterMapMarkers(query.toLowerCase());
      }}
    }}

    function setupDistrictSelector() {{
      const select = document.getElementById('districtSelector');
      select.addEventListener('change', (e) => {{
        const distKey = e.target.value;
        const distInfo = TN_DISTRICTS[distKey];
        if (distInfo) {{
          currentDistrict = distKey;
          map.flyTo([distInfo.lat, distInfo.lon], distInfo.zoom, {{ duration: 1.2 }});
          showNotification(`📍 Centered on ${{distInfo.name}}`, 'info');
        }}
      }});
    }}

    // Custom Pin Icons generator
    function createMarkerIcon(type, iconSymbol) {{
      return L.divIcon({{
        className: 'custom-leaflet-icon-wrapper',
        html: `<div class="custom-marker-pin ${{type}}">${{iconSymbol}}</div>`,
        iconSize: [34, 34],
        iconAnchor: [17, 17],
        popupAnchor: [0, -18]
      }});
    }}

    function renderMapMarkers() {{
      if (!markersLayer) return;
      markersLayer.clearLayers();

      let counts = {{ fire: 0, flood: 0, hospital: 0, shelter: 0, food: 0, blood: 0, blocked: 0 }};

      // 1. Emergencies (Fire, Flood, Blocked Road)
      state.emergencies.forEach(item => {{
        if (item.type === 'fire') counts.fire++;
        if (item.type === 'flood') counts.flood++;
        if (item.type === 'blocked') counts.blocked++;

        if (currentCategoryFilter === 'all' || currentCategoryFilter === item.type) {{
          const sym = item.type === 'fire' ? '🔥' : item.type === 'flood' ? '🌊' : '⛔';
          const marker = L.marker([item.lat, item.lon], {{ icon: createMarkerIcon(item.type, sym) }});
          marker.customData = {{ type: item.type, id: item.id }};
          marker.on('click', () => openEmergencyDrawer(item));
          markersLayer.addLayer(marker);
        }}
      }});

      // 2. Hospitals (130+ across all 38 districts)
      state.hospitals.forEach(hosp => {{
        counts.hospital++;
        if (currentCategoryFilter === 'all' || currentCategoryFilter === 'hospital') {{
          const marker = L.marker([hosp.lat, hosp.lon], {{ icon: createMarkerIcon('hospital', '🏥') }});
          marker.customData = {{ type: 'hospital', id: hosp.id }};
          marker.on('click', () => openHospitalDrawer(hosp));
          markersLayer.addLayer(marker);
        }}
      }});

      // 3. Shelters (38 Multi-purpose cyclone & flood camps)
      state.shelters.forEach(sh => {{
        counts.shelter++;
        if (currentCategoryFilter === 'all' || currentCategoryFilter === 'shelter') {{
          const marker = L.marker([sh.lat, sh.lon], {{ icon: createMarkerIcon('shelter', '⛺') }});
          marker.customData = {{ type: 'shelter', id: sh.id }};
          marker.on('click', () => openShelterDrawer(sh));
          markersLayer.addLayer(marker);
        }}
      }});

      // 4. Food Centers
      state.foodCenters.forEach(fc => {{
        counts.food++;
        if (currentCategoryFilter === 'all' || currentCategoryFilter === 'food') {{
          const marker = L.marker([fc.lat, fc.lon], {{ icon: createMarkerIcon('food', '📦') }});
          marker.customData = {{ type: 'food', id: fc.id }};
          marker.on('click', () => openFoodDrawer(fc));
          markersLayer.addLayer(marker);
        }}
      }});

      // 5. Blood Banks
      state.bloodBanks.forEach(bb => {{
        counts.blood++;
        if (currentCategoryFilter === 'all' || currentCategoryFilter === 'blood') {{
          const marker = L.marker([bb.lat, bb.lon], {{ icon: createMarkerIcon('blood', '🩸') }});
          marker.customData = {{ type: 'blood', id: bb.id }};
          marker.on('click', () => openBloodDrawer(bb));
          markersLayer.addLayer(marker);
        }}
      }});

      // Update counters in UI
      document.getElementById('countAll').textContent = Object.values(counts).reduce((a, b) => a + b, 0);
      document.getElementById('countFire').textContent = counts.fire;
      document.getElementById('countFlood').textContent = counts.flood;
      document.getElementById('countHospital').textContent = counts.hospital;
      document.getElementById('countShelter').textContent = counts.shelter;
      document.getElementById('countFood').textContent = counts.food;
      document.getElementById('countBlood').textContent = counts.blood;
      document.getElementById('countBlocked').textContent = counts.blocked;

      updateZoomAmenityVisibility();
    }}

    function filterMapMarkers(searchQuery) {{
      if (!searchQuery) {{
        renderMapMarkers();
        return;
      }}
      markersLayer.clearLayers();
      const match = (text) => text && text.toLowerCase().includes(searchQuery);

      state.emergencies.forEach(item => {{
        if (match(item.title) || match(item.description) || match(item.district)) {{
          const sym = item.type === 'fire' ? '🔥' : item.type === 'flood' ? '🌊' : '⛔';
          const marker = L.marker([item.lat, item.lon], {{ icon: createMarkerIcon(item.type, sym) }});
          marker.customData = {{ type: item.type, id: item.id }};
          marker.on('click', () => openEmergencyDrawer(item));
          markersLayer.addLayer(marker);
        }}
      }});

      state.hospitals.forEach(hosp => {{
        if (match(hosp.name) || match(hosp.address) || match(hosp.district)) {{
          const marker = L.marker([hosp.lat, hosp.lon], {{ icon: createMarkerIcon('hospital', '🏥') }});
          marker.customData = {{ type: 'hospital', id: hosp.id }};
          marker.on('click', () => openHospitalDrawer(hosp));
          markersLayer.addLayer(marker);
        }}
      }});

      state.shelters.forEach(sh => {{
        if (match(sh.name) || match(sh.address) || match(sh.district)) {{
          const marker = L.marker([sh.lat, sh.lon], {{ icon: createMarkerIcon('shelter', '⛺') }});
          marker.customData = {{ type: 'shelter', id: sh.id }};
          marker.on('click', () => openShelterDrawer(sh));
          markersLayer.addLayer(marker);
        }}
      }});

      state.foodCenters.forEach(fc => {{
        if (match(fc.name) || match(fc.address) || match(fc.district)) {{
          const marker = L.marker([fc.lat, fc.lon], {{ icon: createMarkerIcon('food', '📦') }});
          marker.customData = {{ type: 'food', id: fc.id }};
          marker.on('click', () => openFoodDrawer(fc));
          markersLayer.addLayer(marker);
        }}
      }});

      state.bloodBanks.forEach(bb => {{
        if (match(bb.name) || match(bb.address) || match(bb.district)) {{
          const marker = L.marker([bb.lat, bb.lon], {{ icon: createMarkerIcon('blood', '🩸') }});
          marker.customData = {{ type: 'blood', id: bb.id }};
          marker.on('click', () => openBloodDrawer(bb));
          markersLayer.addLayer(marker);
        }}
      }});

      updateZoomAmenityVisibility();
    }}

    // ================= DRAWERS FOR DETAILED VIEW =================
    function openHospitalDrawer(hosp) {{
      const drawer = document.getElementById('mapDetailDrawer');
      document.getElementById('drawerTitle').innerHTML = `🏥 Hospital Facility`;
      const bloodList = Object.entries(hosp.bloodStock || {{}}).map(([type, qty]) => `
        <span style="background:var(--bg-panel-2); border:1px solid var(--amber-dim); padding:2px 7px; border-radius:4px; font-size:11px; font-family:'JetBrains Mono'; color:var(--amber);">
          ${{type}}: <b>${{qty}}u</b>
        </span>
      `).join(' ');

      document.getElementById('drawerBody').innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:start;">
          <div>
            <h4 style="font-size:16px; color:#fff; font-weight:700;">${{hosp.name}}</h4>
            <p style="font-size:12px; color:var(--text-muted); margin-top:2px;">📍 ${{hosp.address}}</p>
          </div>
          <span class="badge badge-success">24x7 EMERGENCY</span>
        </div>

        <div class="metric-row">
          <div class="metric-box">
            <div class="metric-val" style="color:var(--green);">${{hosp.bedsAvailable}} / ${{hosp.bedsTotal}}</div>
            <div class="metric-lbl">Available Beds</div>
          </div>
          <div class="metric-box">
            <div class="metric-val" style="color:var(--amber);">${{hosp.icuAvailable}} Units</div>
            <div class="metric-lbl">ICU Status (${{hosp.icuStatus}})</div>
          </div>
          <div class="metric-box">
            <div class="metric-val">${{hosp.doctorsOnDuty}}</div>
            <div class="metric-lbl">Emergency Doctors</div>
          </div>
          <div class="metric-box">
            <div class="metric-val" style="color:var(--blue);">${{hosp.ambulancesReady}}</div>
            <div class="metric-lbl">Ambulances Ready</div>
          </div>
        </div>

        <div>
          <label style="font-size:11px; color:var(--text-muted); font-family:'JetBrains Mono'; font-weight:600;">BLOOD INVENTORY</label>
          <div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:5px;">
            ${{bloodList}}
          </div>
        </div>

        <div style="background:rgba(10,15,28,0.7); border:1px solid var(--grid-line); border-radius:6px; padding:10px;">
          <div style="font-size:11px; color:var(--text-muted);">EMERGENCY CONTACT</div>
          <div style="font-size:13px; font-weight:700; color:#fff; margin-top:2px;">${{hosp.emergencyContact}}</div>
          <div style="font-size:14px; font-weight:700; color:var(--orange); font-family:'JetBrains Mono'; margin-top:3px;">
            <a href="tel:${{hosp.phone}}">📞 ${{hosp.phone}}</a>
          </div>
        </div>

        <div style="display:flex; gap:8px;">
          <a href="tel:${{hosp.phone}}" class="card-btn card-btn-primary" style="display:flex; align-items:center; justify-content:center; gap:6px;">
            📞 Call Hospital
          </a>
          <a href="https://www.google.com/maps/dir/?api=1&destination=${{hosp.lat}},${{hosp.lon}}" target="_blank" rel="noopener noreferrer" class="card-btn card-btn-outline" style="display:flex; align-items:center; justify-content:center; gap:6px;">
            🧭 Get Directions
          </a>
        </div>
      `;
      drawer.classList.add('open');
    }}

    function openShelterDrawer(sh) {{
      const drawer = document.getElementById('mapDetailDrawer');
      document.getElementById('drawerTitle').innerHTML = `⛺ Emergency Shelter`;
      const occPct = Math.round((sh.occupied / sh.capacity) * 100);

      document.getElementById('drawerBody').innerHTML = `
        <div>
          <h4 style="font-size:16px; color:#fff; font-weight:700;">${{sh.name}}</h4>
          <p style="font-size:12px; color:var(--text-muted); margin-top:2px;">📍 ${{sh.address}}</p>
        </div>

        <div class="metric-row">
          <div class="metric-box">
            <div class="metric-val" style="color:var(--blue);">${{sh.occupied}} / ${{sh.capacity}}</div>
            <div class="metric-lbl">Occupancy (${{occPct}}%)</div>
          </div>
          <div class="metric-box">
            <div class="metric-val" style="color:var(--green);">${{sh.capacity - sh.occupied}}</div>
            <div class="metric-lbl">Remaining Capacity</div>
          </div>
        </div>

        <div style="display:flex; flex-wrap:wrap; gap:6px;">
          ${{sh.womenShelter ? '<span class="badge badge-success">✓ Women Safe Zone</span>' : ''}}
          ${{sh.petFriendly ? '<span class="badge badge-info">✓ Pet Friendly</span>' : ''}}
          ${{sh.medicalSupport ? '<span class="badge badge-amber">✓ Medical Staff Onsite</span>' : ''}}
          ${{sh.wheelchair ? '<span class="badge badge-success">✓ Wheelchair Access</span>' : ''}}
        </div>

        <div style="background:rgba(10,15,28,0.7); border:1px solid var(--grid-line); border-radius:6px; padding:10px;">
          <div style="font-size:11px; color:var(--text-muted);">SHELTER IN-CHARGE HELPLINE</div>
          <div style="font-size:14px; font-weight:700; color:var(--orange); font-family:'JetBrains Mono'; margin-top:3px;">
            <a href="tel:${{sh.phone}}">📞 ${{sh.phone}}</a>
          </div>
        </div>

        <div style="display:flex; gap:8px;">
          <a href="tel:${{sh.phone}}" class="card-btn card-btn-primary" style="display:flex; align-items:center; justify-content:center; gap:6px;">
            📞 Contact Shelter
          </a>
          <a href="https://www.google.com/maps/dir/?api=1&destination=${{sh.lat}},${{sh.lon}}" target="_blank" rel="noopener noreferrer" class="card-btn card-btn-outline" style="display:flex; align-items:center; justify-content:center; gap:6px;">
            🧭 Route to Shelter
          </a>
        </div>
      `;
      drawer.classList.add('open');
    }}

    function openFoodDrawer(fc) {{
      const drawer = document.getElementById('mapDetailDrawer');
      document.getElementById('drawerTitle').innerHTML = `📦 Relief Supplies Center`;
      document.getElementById('drawerBody').innerHTML = `
        <div>
          <h4 style="font-size:16px; color:#fff; font-weight:700;">${{fc.name}}</h4>
          <p style="font-size:12px; color:var(--text-muted); margin-top:2px;">📍 ${{fc.address}}</p>
        </div>

        <div class="metric-row">
          <div class="metric-box">
            <div class="metric-val" style="color:#a855f7;">${{fc.mealsReady}}</div>
            <div class="metric-lbl">Meals Ready</div>
          </div>
          <div class="metric-box">
            <div class="metric-val" style="color:var(--blue);">${{fc.waterLitres}} L</div>
            <div class="metric-lbl">Clean Drinking Water</div>
          </div>
          <div class="metric-box">
            <div class="metric-val">${{fc.blankets}}</div>
            <div class="metric-lbl">Blankets Stocked</div>
          </div>
          <div class="metric-box">
            <div class="metric-val" style="color:var(--amber);">${{fc.packetsRice}} pkts</div>
            <div class="metric-lbl">Dry Rations</div>
          </div>
        </div>

        <div style="background:rgba(10,15,28,0.7); border:1px solid var(--grid-line); border-radius:6px; padding:10px;">
          <div style="font-size:11px; color:var(--text-muted);">COORDINATION OFFICER</div>
          <div style="font-size:13px; font-weight:700; color:#fff; margin-top:2px;">${{fc.contact}}</div>
        </div>

        <div style="display:flex; gap:8px;">
          <button class="card-btn card-btn-primary" onclick="reserveSupply('${{fc.id}}')">Reserve Rations</button>
          <a href="https://www.google.com/maps/dir/?api=1&destination=${{fc.lat}},${{fc.lon}}" target="_blank" rel="noopener noreferrer" class="card-btn card-btn-outline" style="display:flex; align-items:center; justify-content:center; gap:6px;">
            🧭 Navigate
          </a>
        </div>
      `;
      drawer.classList.add('open');
    }}

    function openBloodDrawer(bb) {{
      const drawer = document.getElementById('mapDetailDrawer');
      document.getElementById('drawerTitle').innerHTML = `🩸 Blood Bank`;
      const bloodList = Object.entries(bb.stock || {{}}).map(([type, qty]) => `
        <span style="background:var(--bg-panel-2); border:1px solid var(--amber-dim); padding:3px 8px; border-radius:4px; font-size:12px; font-family:'JetBrains Mono'; color:var(--amber);">
          ${{type}}: <b>${{qty}} units</b>
        </span>
      `).join(' ');

      document.getElementById('drawerBody').innerHTML = `
        <div>
          <h4 style="font-size:16px; color:#fff; font-weight:700;">${{bb.name}}</h4>
          <p style="font-size:12px; color:var(--text-muted); margin-top:2px;">📍 ${{bb.address}}</p>
        </div>

        <div>
          <label style="font-size:11px; color:var(--text-muted); font-family:'JetBrains Mono'; font-weight:600;">TESTED BLOOD STOCK READY</label>
          <div style="display:flex; flex-wrap:wrap; gap:8px; margin-top:6px;">
            ${{bloodList}}
          </div>
        </div>

        <div style="background:rgba(10,15,28,0.7); border:1px solid var(--grid-line); border-radius:6px; padding:10px;">
          <div style="font-size:11px; color:var(--text-muted);">BLOOD TRANSFUSION HELPLINE</div>
          <div style="font-size:14px; font-weight:700; color:var(--orange); font-family:'JetBrains Mono'; margin-top:3px;">
            <a href="tel:${{bb.phone}}">📞 ${{bb.phone}}</a>
          </div>
        </div>

        <div style="display:flex; gap:8px;">
          <a href="tel:${{bb.phone}}" class="card-btn card-btn-primary" style="display:flex; align-items:center; justify-content:center; gap:6px;">
            📞 Call Blood Bank
          </a>
          <a href="https://www.google.com/maps/dir/?api=1&destination=${{bb.lat}},${{bb.lon}}" target="_blank" rel="noopener noreferrer" class="card-btn card-btn-outline" style="display:flex; align-items:center; justify-content:center; gap:6px;">
            🧭 Route
          </a>
        </div>
      `;
      drawer.classList.add('open');
    }}

    function openEmergencyDrawer(item) {{
      const drawer = document.getElementById('mapDetailDrawer');
      const sym = item.type === 'fire' ? '🔴 Fire Incident' : item.type === 'flood' ? '🟠 Flood / Waterlogging' : '⚫ Blocked Highway';
      document.getElementById('drawerTitle').innerHTML = sym;

      document.getElementById('drawerBody').innerHTML = `
        <div>
          <h4 style="font-size:16px; color:#fff; font-weight:700;">${{item.title}}</h4>
          <p style="font-size:12px; color:var(--text-muted); margin-top:2px;">Sector: ${{item.district.toUpperCase()}} · Reported ${{item.time}}</p>
        </div>

        <p style="font-size:13px; color:#edf1f5; line-height:1.5; background:rgba(0,0,0,0.3); padding:10px; border-radius:6px; border:1px solid var(--grid-line);">
          ${{item.description}}
        </p>

        ${{item.photo ? `<img src="${{item.photo}}" alt="Incident Photo" style="width:100%; height:180px; object-fit:cover; border-radius:6px; border:1px solid var(--grid-line);">` : ''}}

        <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px; color:var(--text-muted); font-family:'JetBrains Mono';">
          <span>REPORTED BY: <b>${{item.reporter}}</b></span>
          <span class="badge badge-danger">${{item.severity}}</span>
        </div>

        <div style="display:flex; gap:8px;">
          <button class="card-btn card-btn-primary" onclick="acceptVolunteerTask('${{item.id}}')">Accept Dispatch Mission</button>
          <a href="https://www.google.com/maps/dir/?api=1&destination=${{item.lat}},${{item.lon}}" target="_blank" rel="noopener noreferrer" class="card-btn card-btn-outline" style="display:flex; align-items:center; justify-content:center; gap:6px;">
            🧭 View Hazard Zone
          </a>
        </div>
      `;
      drawer.classList.add('open');
    }}

    // ================= DEDICATED VIEW CARDS POPULATION =================
    function setupViews() {{
      renderHospitalsView();
      renderSheltersView();
      renderFoodView();
      renderVolunteersView();
      renderMissingView();
    }}

    function renderHospitalsView() {{
      const grid = document.getElementById('hospitalsGrid');
      if (!grid) return;
      grid.innerHTML = '';

      state.hospitals.forEach(hosp => {{
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
          <div class="card-header">
            <div>
              <div class="card-title">${{hosp.name}}</div>
              <div style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">📍 ${{hosp.district.toUpperCase()}} · ${{hosp.address}}</div>
            </div>
            <span class="badge badge-success">ICU READY</span>
          </div>

          <div class="metric-row">
            <div class="metric-box">
              <div class="metric-val" style="color:var(--green);">${{hosp.bedsAvailable}} / ${{hosp.bedsTotal}}</div>
              <div class="metric-lbl">Free Beds</div>
            </div>
            <div class="metric-box">
              <div class="metric-val" style="color:var(--amber);">${{hosp.icuAvailable}} Units</div>
              <div class="metric-lbl">ICU Available</div>
            </div>
          </div>

          <div style="font-size:11.5px; color:var(--text-muted); display:flex; justify-content:space-between;">
            <span>Doctors on Duty: <b>${{hosp.doctorsOnDuty}}</b></span>
            <span>Ambulances: <b>${{hosp.ambulancesReady}}</b></span>
          </div>

          <div class="card-actions">
            <button class="card-btn card-btn-primary" onclick="locateOnMap(${{hosp.lat}}, ${{hosp.lon}}, 'hospital', '${{hosp.id}}')">📍 Locate on Map</button>
            <a href="tel:${{hosp.phone}}" class="card-btn card-btn-outline">📞 Call ${{hosp.phone}}</a>
          </div>
        `;
        grid.appendChild(card);
      }});

      // Hospital search filter
      const searchBox = document.getElementById('hospitalSearchInput');
      if (searchBox) {{
        searchBox.addEventListener('input', (e) => {{
          const term = e.target.value.toLowerCase().trim();
          document.querySelectorAll('#hospitalsGrid .card').forEach(c => {{
            const txt = c.textContent.toLowerCase();
            c.style.display = txt.includes(term) ? 'flex' : 'none';
          }});
        }});
      }}
    }}

    function renderSheltersView() {{
      const grid = document.getElementById('sheltersGrid');
      if (!grid) return;
      grid.innerHTML = '';

      state.shelters.forEach(sh => {{
        const card = document.createElement('div');
        card.className = 'card';
        const occPct = Math.round((sh.occupied / sh.capacity) * 100);

        card.innerHTML = `
          <div class="card-header">
            <div>
              <div class="card-title">${{sh.name}}</div>
              <div style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">📍 ${{sh.district.toUpperCase()}} · ${{sh.address}}</div>
            </div>
            <span class="badge badge-info">${{occPct}}% FULL</span>
          </div>

          <div class="metric-row">
            <div class="metric-box">
              <div class="metric-val" style="color:var(--blue);">${{sh.occupied}} / ${{sh.capacity}}</div>
              <div class="metric-lbl">Occupancy</div>
            </div>
            <div class="metric-box">
              <div class="metric-val" style="color:var(--green);">${{sh.capacity - sh.occupied}}</div>
              <div class="metric-lbl">Remaining Space</div>
            </div>
          </div>

          <div style="display:flex; flex-wrap:wrap; gap:5px;">
            ${{sh.womenShelter ? '<span class="badge badge-success">✓ Women Safe</span>' : ''}}
            ${{sh.petFriendly ? '<span class="badge badge-info">✓ Pet Friendly</span>' : ''}}
            ${{sh.medicalSupport ? '<span class="badge badge-amber">✓ Medical Aid</span>' : ''}}
          </div>

          <div class="card-actions">
            <button class="card-btn card-btn-primary" onclick="locateOnMap(${{sh.lat}}, ${{sh.lon}}, 'shelter', '${{sh.id}}')">📍 Locate on Map</button>
            <a href="tel:${{sh.phone}}" class="card-btn card-btn-outline">📞 Call Shelter</a>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    function renderFoodView() {{
      const grid = document.getElementById('foodGrid');
      if (!grid) return;
      grid.innerHTML = '';

      state.foodCenters.forEach(fc => {{
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
          <div class="card-header">
            <div>
              <div class="card-title">${{fc.name}}</div>
              <div style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">📍 ${{fc.district.toUpperCase()}} · ${{fc.address}}</div>
            </div>
            <span class="badge badge-success">${{fc.status}}</span>
          </div>

          <div class="metric-row">
            <div class="metric-box">
              <div class="metric-val" style="color:#a855f7;">${{fc.mealsReady}}</div>
              <div class="metric-lbl">Meals Ready</div>
            </div>
            <div class="metric-box">
              <div class="metric-val" style="color:var(--blue);">${{fc.waterLitres}} L</div>
              <div class="metric-lbl">Drinking Water</div>
            </div>
          </div>

          <div class="card-actions">
            <button class="card-btn card-btn-primary" onclick="locateOnMap(${{fc.lat}}, ${{fc.lon}}, 'food', '${{fc.id}}')">📍 Locate</button>
            <button class="card-btn card-btn-outline" onclick="reserveSupply('${{fc.id}}')">📦 Reserve Supplies</button>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    function renderVolunteersView() {{
      const grid = document.getElementById('volunteersGrid');
      if (!grid) return;
      grid.innerHTML = '';

      state.volunteers.forEach(vol => {{
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
          <div class="card-header">
            <div>
              <div class="card-title">${{vol.name}}</div>
              <div style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">📍 ${{vol.district.toUpperCase()}} · ${{vol.currentLocation}}</div>
            </div>
            <span class="badge badge-info">${{vol.status}}</span>
          </div>

          <div style="font-size:12px; color:#fff;">
            <b>Skills:</b> ${{vol.skills}}
          </div>
          <div style="font-size:12px; color:var(--amber);">
            <b>Active Task:</b> ${{vol.activeTask}}
          </div>

          <div class="card-actions">
            <a href="tel:${{vol.phone}}" class="card-btn card-btn-primary">📞 Call ${{vol.phone}}</a>
            <button class="card-btn card-btn-outline" onclick="locateOnMap(${{vol.lat}}, ${{vol.lon}})">📍 Live Location</button>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    function renderMissingView() {{
      const grid = document.getElementById('missingGrid');
      if (!grid) return;
      grid.innerHTML = '';

      state.missingPersons.forEach(mp => {{
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
          <div class="card-header">
            <div>
              <div class="card-title">${{mp.name}} (${{mp.age}} yrs)</div>
              <div style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">Last Seen: ${{mp.lastSeen}}</div>
            </div>
            <span class="badge ${{mp.status === 'Found' ? 'badge-success' : 'badge-danger'}}">${{mp.status}}</span>
          </div>

          ${{mp.photo ? `<img src="${{mp.photo}}" alt="Missing Person Photo" style="width:100%; height:140px; object-fit:cover; border-radius:6px; border:1px solid var(--grid-line);">` : ''}}

          <p style="font-size:12px; color:#edf1f5; line-height:1.4;">${{mp.description}}</p>

          <div class="card-actions">
            <a href="tel:${{mp.contactPhone}}" class="card-btn card-btn-primary">📞 Contact Family</a>
            <button class="card-btn card-btn-outline" onclick="alert('Thank you for assisting. Police Control Room notified.')">Report Sighting</button>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    function locateOnMap(lat, lon, type = null, id = null) {{
      // Switch tab to viewMap
      const mapTabBtn = document.querySelector('.nav-tab-btn[data-view="viewMap"]');
      if (mapTabBtn) mapTabBtn.click();

      setTimeout(() => {{
        map.flyTo([lat, lon], 14, {{ duration: 1.2 }});
        if (type === 'hospital') {{
          const item = state.hospitals.find(h => h.id === id);
          if (item) openHospitalDrawer(item);
        }} else if (type === 'shelter') {{
          const item = state.shelters.find(s => s.id === id);
          if (item) openShelterDrawer(item);
        }} else if (type === 'food') {{
          const item = state.foodCenters.find(f => f.id === id);
          if (item) openFoodDrawer(item);
        }}
      }}, 250);
    }}

    function reserveSupply(id) {{
      showNotification('✓ Emergency ration reservation confirmed. Dispatch token generated.', 'success');
    }}

    function acceptVolunteerTask(id) {{
      showNotification('✓ Dispatch mission accepted. Coordinates pinned to volunteer route.', 'success');
    }}

    // ================= MODAL SETUP & SOS =================
    function setupModals() {{
      // Helplines modal
      const helplinesModal = document.getElementById('helplinesModal');
      document.getElementById('openHelplinesModalBtn').addEventListener('click', () => {{
        helplinesModal.classList.add('open');
      }});
      document.getElementById('closeHelplinesModalBtn').addEventListener('click', () => {{
        helplinesModal.classList.remove('open');
      }});

      // Report Emergency Modal
      const reportModal = document.getElementById('reportEmergencyModal');
      document.getElementById('reportEmergencyMapBtn').addEventListener('click', () => {{
        reportModal.classList.add('open');
      }});
      document.getElementById('closeReportEmergencyBtn').addEventListener('click', () => {{
        reportModal.classList.remove('open');
      }});

      // SOS Modal
      const sosModal = document.getElementById('sosModal');
      document.getElementById('globalSosBtn').addEventListener('click', () => {{
        sosModal.classList.add('open');
        if (navigator.geolocation) {{
          navigator.geolocation.getCurrentPosition(
            (pos) => {{
              document.getElementById('sosGpsStatus').textContent = `✓ GPS Locked: ${{pos.coords.latitude.toFixed(5)}}° N, ${{pos.coords.longitude.toFixed(5)}}° E (Accurate to ${{Math.round(pos.coords.accuracy)}}m)`;
            }},
            (err) => {{
              document.getElementById('sosGpsStatus').textContent = '⚠️ GPS permission denied. Centering on active sector.';
            }}
          );
        }}
      }});
      document.getElementById('closeSosBtn').addEventListener('click', () => {{
        sosModal.classList.remove('open');
      }});

      document.getElementById('confirmSosDispatchBtn').addEventListener('click', () => {{
        const phone = document.getElementById('sosPhone').value;
        if (!phone) {{
          alert('Please enter your contact phone number.');
          return;
        }}
        sosModal.classList.remove('open');
        showNotification('🚨 SOS DISPATCH TRANSMITTED! SDRF & Volunteers dispatched to your GPS coordinates.', 'warning');
      }});

      // Form submission
      document.getElementById('emergencyReportForm').addEventListener('submit', (e) => {{
        e.preventDefault();
        const title = document.getElementById('reportTitle').value;
        const category = document.getElementById('reportCategory').value;
        const district = document.getElementById('reportDistrict').value;
        const desc = document.getElementById('reportDescription').value;

        const center = map.getCenter();
        const newEmerg = {{
          id: 'emg-user-' + Date.now(),
          district: district,
          type: category,
          title: title,
          description: desc,
          lat: center.lat + (Math.random() - 0.5) * 0.02,
          lon: center.lng + (Math.random() - 0.5) * 0.02,
          severity: 'High',
          status: 'Active',
          time: 'Just now',
          reporter: 'Citizen Report (Self)'
        }};

        state.emergencies.unshift(newEmerg);
        renderMapMarkers();
        reportModal.classList.remove('open');
        showNotification('✓ Emergency report broadcast to live disaster grid.', 'success');
      }});
    }}

    // ================= ANALYTICS =================
    function renderAnalytics() {{
      const ctx1 = document.getElementById('chartEmergencies');
      const ctx2 = document.getElementById('chartBeds');
      if (!ctx1 || !ctx2) return;

      new Chart(ctx1, {{
        type: 'doughnut',
        data: {{
          labels: ['Flood / Waterlogging', 'Fire Incidents', 'Blocked Roads'],
          datasets: [{{
            data: [10, 4, 6],
            backgroundColor: ['#f97316', '#ef4444', '#56617a'],
            borderColor: '#10182b',
            borderWidth: 2
          }}]
        }},
        options: {{
          responsive: true,
          plugins: {{ legend: {{ labels: {{ color: '#8b96aa', font: {{ family: 'JetBrains Mono' }} }} }} }}
        }}
      }});

      new Chart(ctx2, {{
        type: 'bar',
        data: {{
          labels: ['Chennai', 'Coimbatore', 'Madurai', 'Trichy', 'Vellore', 'Salem'],
          datasets: [{{
            label: 'Free Emergency Beds',
            data: [320, 185, 160, 130, 140, 115],
            backgroundColor: '#34d399',
            borderRadius: 4
          }}]
        }},
        options: {{
          responsive: true,
          scales: {{
            x: {{ ticks: {{ color: '#8b96aa' }}, grid: {{ color: '#1e2a42' }} }},
            y: {{ ticks: {{ color: '#8b96aa' }}, grid: {{ color: '#1e2a42' }} }}
          }},
          plugins: {{ legend: {{ labels: {{ color: '#8b96aa', font: {{ family: 'JetBrains Mono' }} }} }} }}
        }}
      }});

      // KPIs
      document.getElementById('kpiEmergencies').textContent = state.emergencies.length;
      document.getElementById('kpiEvacuees').textContent = state.shelters.reduce((acc, s) => acc + s.occupied, 0).toLocaleString();
      document.getElementById('kpiIcu').textContent = state.hospitals.reduce((acc, h) => acc + h.icuAvailable, 0);
      document.getElementById('kpiVolunteers').textContent = state.volunteers.length;
    }}
  </script>
</body>
</html>
"""

# Write to static/map.html and root map.html
with open("static/map.html", "w", encoding="utf-8") as f:
    f.write(MAP_HTML_CONTENT)

with open("map.html", "w", encoding="utf-8") as f:
    f.write(MAP_HTML_CONTENT)

print(f"BeaconGrid Map application created successfully (Length: {len(MAP_HTML_CONTENT)} bytes)")
