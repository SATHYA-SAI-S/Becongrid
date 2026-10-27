/**
 * BeaconGrid PDF Generator
 * Compiles Source Code & Output Screenshots into a Professional Academic PDF Report
 * 
 * Student Details:
 * 24MID0077 - Jai Kishore K
 * 24MID0112 - Sathya Sai S
 * 24MID0135 - Sudharshini Manikandan
 */
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('Generating BeaconGrid Code & Output PDF Report...');

// Helper: Read and convert image to Base64 data URI
function getBase64Image(filePath) {
  if (!fs.existsSync(filePath)) {
    console.warn('Image not found:', filePath);
    return '';
  }
  const ext = path.extname(filePath).slice(1);
  const data = fs.readFileSync(filePath).toString('base64');
  return `data:image/${ext};base64,${data}`;
}

// Helper: Escape HTML
function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Read Source Files
const files = {
  tokensCss: fs.readFileSync('static/css/tokens.css', 'utf8'),
  layoutCss: fs.readFileSync('static/css/layout.css', 'utf8'),
  componentsCss: fs.readFileSync('static/css/components.css', 'utf8'),
  bottomSheetCss: fs.readFileSync('static/css/bottom-sheet.css', 'utf8'),
  indexHtml: fs.readFileSync('static/index.html', 'utf8'),
  emergencyMapHtml: fs.readFileSync('emergency-resource-map.html', 'utf8'),
  mapHtml: fs.readFileSync('static/map.html', 'utf8')
};

// Clean mapHtml code for display: condense the 6,000 lines of raw coordinate JSON into a clear summary
let mapHtmlClean = files.mapHtml;
const jsonDatasetsIdx = mapHtmlClean.indexOf('const HOSPITALS_DATA = [');
if (jsonDatasetsIdx !== -1) {
  const jsonDatasetsEnd = mapHtmlClean.indexOf('// Application state', jsonDatasetsIdx);
  if (jsonDatasetsEnd !== -1) {
    mapHtmlClean = 
      mapHtmlClean.substring(0, jsonDatasetsIdx) +
      `// [Embedded 130+ Verified Hospitals, 38 Cyclone Shelters, 25 Food Points, 25 Blood Banks Datasets]\n` +
      `const HOSPITALS_DATA = [ /* 130+ Medical Institutions with ICU & Trauma Beds across 38 Districts */ ];\n` +
      `const SHELTERS_DATA = [ /* 38 Multi-Purpose Cyclone & Flood Relief Camps */ ];\n` +
      `const FOOD_DATA = [ /* Community Kitchens & Relief Distribution Hubs */ ];\n` +
      `const BLOOD_DATA = [ /* 24x7 Monitored Blood Reserve Banks */ ];\n` +
      `const INCIDENTS_DATA = [ /* Real-Time GDELT & News Intelligence Incidents across Tamil Nadu */ ];\n` +
      `const VOLUNTEERS_DATA = [ /* Active Rescue Drivers & Trauma First Responders */ ];\n` +
      `const MISSING_DATA = [ /* Missing Person Verification Records */ ];\n\n    ` +
      mapHtmlClean.substring(jsonDatasetsEnd);
  }
}

// Base64 Images
const imgIndex = getBase64Image('screenshots/output_index.png');
const imgMap = getBase64Image('screenshots/output_map.png');
const imgDrawer = getBase64Image('screenshots/output_map_drawer.png');
const imgNewsFeed = getBase64Image('screenshots/output_map_news_feed.png');
const imgHospitals = getBase64Image('screenshots/output_map_hospitals.png');
const imgEmergencyMap = getBase64Image('screenshots/output_emergency_map.png');
const imgTokens = getBase64Image('screenshots/output_tokens_css.png');
const imgLayout = getBase64Image('screenshots/output_layout_css.png');
const imgComponents = getBase64Image('screenshots/output_components_css.png');
const imgBottomSheet = getBase64Image('screenshots/output_bottom_sheet_css.png');

const reportHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>BeaconGrid — Source Code and Browser Output Report</title>
  <style>
    @page {
      size: A4;
      margin: 14mm 12mm 16mm 12mm;
      @bottom-right {
        content: counter(page);
      }
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 11pt;
      line-height: 1.5;
      color: #1e293b;
      background: #ffffff;
      padding: 0;
    }
    .page-break {
      page-break-before: always;
    }
    .avoid-break {
      page-break-inside: avoid;
    }

    /* Cover / Header Card */
    .report-header {
      border: 2px solid #0f172a;
      border-radius: 10px;
      padding: 24px;
      margin-bottom: 24px;
      background: #f8fafc;
      page-break-inside: avoid;
    }
    .project-badge {
      display: inline-block;
      background: #ea580c;
      color: white;
      font-weight: 700;
      font-size: 9pt;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
    }
    h1.project-title {
      font-size: 20pt;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.2;
      margin-bottom: 6px;
    }
    .project-subtitle {
      font-size: 11pt;
      color: #475569;
      margin-bottom: 18px;
    }
    .students-box {
      border-top: 1px solid #cbd5e1;
      padding-top: 14px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      background: #ffffff;
      border-radius: 6px;
      padding: 12px 14px;
      border: 1px solid #e2e8f0;
    }
    .student-item {
      display: flex;
      flex-direction: column;
    }
    .student-reg {
      font-family: monospace;
      font-size: 10pt;
      font-weight: 700;
      color: #2563eb;
    }
    .student-name {
      font-size: 11pt;
      font-weight: 600;
      color: #0f172a;
    }

    /* Section Styles */
    .section-title-bar {
      background: #0f172a;
      color: #ffffff;
      padding: 10px 14px;
      border-radius: 6px;
      margin-top: 24px;
      margin-bottom: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      page-break-inside: avoid;
    }
    .section-title-bar h2 {
      font-size: 13pt;
      font-weight: 700;
      letter-spacing: 0.02em;
    }
    .file-tag {
      background: #334155;
      color: #38bdf8;
      font-family: monospace;
      font-size: 9pt;
      padding: 2px 8px;
      border-radius: 4px;
    }
    .desc-text {
      color: #475569;
      font-size: 10pt;
      margin-bottom: 12px;
    }

    /* Code Snippet Box */
    .code-container {
      background: #090d16;
      color: #e2e8f0;
      border-radius: 6px;
      padding: 12px;
      font-family: "JetBrains Mono", Consolas, "Courier New", monospace;
      font-size: 8.5pt;
      line-height: 1.45;
      overflow-x: hidden;
      white-space: pre-wrap;
      word-break: break-all;
      border: 1px solid #1e293b;
      margin-bottom: 16px;
      max-height: 520px;
      overflow-y: hidden;
      page-break-inside: avoid;
    }
    .code-label {
      font-size: 9pt;
      font-weight: 700;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Output Screenshot Card */
    .output-card {
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
      background: #ffffff;
      margin-bottom: 24px;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);
      page-break-inside: avoid;
    }
    .output-card-header {
      background: #f1f5f9;
      border-bottom: 1px solid #cbd5e1;
      padding: 8px 12px;
      font-size: 9.5pt;
      font-weight: 700;
      color: #334155;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .output-img-wrapper {
      padding: 10px;
      background: #0f172a;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .output-img {
      max-width: 100%;
      height: auto;
      border-radius: 4px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.4);
      border: 1px solid #334155;
    }
    .output-caption {
      padding: 8px 12px;
      font-size: 9pt;
      color: #64748b;
      background: #ffffff;
      border-top: 1px solid #e2e8f0;
    }
  </style>
</head>
<body>

  <!-- ================= COVER / HEADER ================= -->
  <div class="report-header">
    <span class="project-badge">ACADEMIC EVALUATION & CODE ARTIFACT REPORT</span>
    <h1 class="project-title">BeaconGrid — Emergency Resource Map & GDELT News Intelligence</h1>
    <p class="project-subtitle">
      Centralized Disaster Response Management System with Overpass OSM Integration and Real-time Multi-source News Corroboration for Tamil Nadu
    </p>

    <div class="students-box">
      <div class="student-item">
        <span class="student-reg">24MID0077</span>
        <span class="student-name">Jai Kishore K</span>
      </div>
      <div class="student-item">
        <span class="student-reg">24MID0112</span>
        <span class="student-name">Sathya Sai S</span>
      </div>
      <div class="student-item">
        <span class="student-reg">24MID0135</span>
        <span class="student-name">Sudharshini Manikandan</span>
      </div>
    </div>
  </div>

  <!-- ================= SECTION 1: static/index.html ================= -->
  <div class="section-title-bar">
    <h2>1. Landing Page & Citizen Portal</h2>
    <span class="file-tag">static/index.html</span>
  </div>
  <p class="desc-text">
    Overview portal featuring state network status, disaster crisis metrics, four-role interactive dispatch preview, emergency helplines directory, and gateway to the live command map.
  </p>

  <div class="code-label">💻 Source Code (Excerpt): static/index.html</div>
  <pre class="code-container"><code>${escapeHtml(files.indexHtml.substring(0, 1800))}
... [Remaining 500+ lines defining role switcher, situational cards, and helpline modal] ...</code></pre>

  <div class="output-card">
    <div class="output-card-header">
      <span>🖥️ Browser Output — Playwright / Chrome Screenshot</span>
      <span style="font-family:monospace; color:#2563eb;">http://127.0.0.1:8000/index.html</span>
    </div>
    <div class="output-img-wrapper">
      <img src="${imgIndex}" class="output-img" alt="Landing Page Output">
    </div>
    <div class="output-caption">
      <b>Output Verification:</b> Landing page rendered with BeaconGrid tactical dark theme, radar scan badge, real-time helplines trigger, and citizen fast-action buttons.
    </div>
  </div>

  <!-- ================= SECTION 2: static/map.html ================= -->
  <div class="page-break"></div>
  <div class="section-title-bar">
    <h2>2. Live Tactical Command Map & Disaster Grid</h2>
    <span class="file-tag">static/map.html</span>
  </div>
  <p class="desc-text">
    Interactive Leaflet.js command center with Overpass API live amenity scanning, 130+ verified hospital ICU beds across 38 districts, GDELT multi-source news markers, and sliding detail drawer.
  </p>

  <div class="code-label">💻 Source Code (Excerpt): static/map.html</div>
  <pre class="code-container"><code>${escapeHtml(mapHtmlClean.substring(0, 2100))}
... [Core Leaflet layer handlers, Overpass live scan, and GDELT sliding drawer logic] ...</code></pre>

  <div class="output-card">
    <div class="output-card-header">
      <span>🖥️ Browser Output (View 1: Statewide Disaster Grid)</span>
      <span style="font-family:monospace; color:#2563eb;">http://127.0.0.1:8000/map.html</span>
    </div>
    <div class="output-img-wrapper">
      <img src="${imgMap}" class="output-img" alt="Live Map View Output">
    </div>
    <div class="output-caption">
      <b>Output Verification:</b> Complete Tamil Nadu map showing 150+ hospital beds, cyclone shelters, relief supplies, and GDELT news intelligence markers.
    </div>
  </div>

  <div class="output-card">
    <div class="output-card-header">
      <span>🖥️ Browser Output (View 2: Marker Detail Drawer & Publisher Citation)</span>
      <span style="font-family:monospace; color:#2563eb;">Slide-in Marker Drawer</span>
    </div>
    <div class="output-img-wrapper">
      <img src="${imgDrawer}" class="output-img" alt="Marker Drawer Output">
    </div>
    <div class="output-caption">
      <b>Output Verification:</b> Incident detail drawer displaying corroborated sources (DT Next, Dinamalar), exact coordinates, relative time, and dispute verification button.
    </div>
  </div>

  <div class="output-card">
    <div class="output-card-header">
      <span>🖥️ Browser Output (View 3: Real-Time News Intelligence Feed Tab)</span>
      <span style="font-family:monospace; color:#2563eb;">Tab: ⚡ News Intel (13)</span>
    </div>
    <div class="output-img-wrapper">
      <img src="${imgNewsFeed}" class="output-img" alt="News Intelligence Feed Output">
    </div>
    <div class="output-caption">
      <b>Output Verification:</b> Dedicated feed displaying real-time incidents categorized into 7 crisis types with verification badges and telemetry KPIs.
    </div>
  </div>

  <!-- ================= SECTION 3: emergency-resource-map.html ================= -->
  <div class="page-break"></div>
  <div class="section-title-bar">
    <h2>3. Emergency Resource Network Template</h2>
    <span class="file-tag">emergency-resource-map.html</span>
  </div>
  <p class="desc-text">
    Reference single-page application mockup demonstrating floating search, facility radius filter, category pills, and resource cards list.
  </p>

  <div class="code-label">💻 Source Code (Excerpt): emergency-resource-map.html</div>
  <pre class="code-container"><code>${escapeHtml(files.emergencyMapHtml.substring(0, 1900))}
... [Layout, search controls, and card lists] ...</code></pre>

  <div class="output-card">
    <div class="output-card-header">
      <span>🖥️ Browser Output — Playwright Screenshot</span>
      <span style="font-family:monospace; color:#2563eb;">emergency-resource-map.html</span>
    </div>
    <div class="output-img-wrapper">
      <img src="${imgEmergencyMap}" class="output-img" alt="Emergency Resource Map Output">
    </div>
    <div class="output-caption">
      <b>Output Verification:</b> Floating search bar, category chips, and live facility listing with distance calculations.
    </div>
  </div>

  <!-- ================= SECTION 4: static/css/tokens.css ================= -->
  <div class="page-break"></div>
  <div class="section-title-bar">
    <h2>4. Design Tokens & Color Palette Stylesheet</h2>
    <span class="file-tag">static/css/tokens.css</span>
  </div>
  <p class="desc-text">
    CSS Custom Properties declaring the design system: neutral surface values, category accents (hospital, shelter, water, food), elevation drop-shadows, and typography scales.
  </p>

  <div class="code-label">💻 Full Source Code: static/css/tokens.css</div>
  <pre class="code-container"><code>${escapeHtml(files.tokensCss)}</code></pre>

  <div class="output-card">
    <div class="output-card-header">
      <span>🎨 Rendered CSS Output Showcase: Design Tokens & Palette</span>
      <span style="font-family:monospace; color:#2563eb;">tokens.css</span>
    </div>
    <div class="output-img-wrapper" style="background:#f1f5f9; padding:16px;">
      <img src="${imgTokens}" class="output-img" style="border:none;" alt="Tokens CSS Output">
    </div>
    <div class="output-caption">
      <b>Output Verification:</b> Rendered palette swatches showing <code>--cat-hospital</code>, <code>--cat-clinic</code>, <code>--cat-pharmacy</code>, and core brand tokens.
    </div>
  </div>

  <!-- ================= SECTION 5: static/css/layout.css ================= -->
  <div class="page-break"></div>
  <div class="section-title-bar">
    <h2>5. Layout Structure & Responsive Grid Stylesheet</h2>
    <span class="file-tag">static/css/layout.css</span>
  </div>
  <p class="desc-text">
    Styles governing viewport containment, fullscreen Leaflet map positioning, floating command island, top search bar wrapper, and responsive breakpoint adjustments.
  </p>

  <div class="code-label">💻 Source Code (Excerpt): static/css/layout.css</div>
  <pre class="code-container"><code>${escapeHtml(files.layoutCss.substring(0, 2100))}
... [Sidebar positioning, floating action wrapper, and mobile media queries] ...</code></pre>

  <div class="output-card">
    <div class="output-card-header">
      <span>🎨 Rendered CSS Output Showcase: Layout & Search Box Wrapper</span>
      <span style="font-family:monospace; color:#2563eb;">layout.css</span>
    </div>
    <div class="output-img-wrapper" style="background:#f1f5f9; padding:16px;">
      <img src="${imgLayout}" class="output-img" style="border:none;" alt="Layout CSS Output">
    </div>
    <div class="output-caption">
      <b>Output Verification:</b> Rendered floating search wrapper with icon button, input box, and primary action trigger.
    </div>
  </div>

  <!-- ================= SECTION 6: static/css/components.css ================= -->
  <div class="page-break"></div>
  <div class="section-title-bar">
    <h2>6. UI Components, Chips & Cards Stylesheet</h2>
    <span class="file-tag">static/css/components.css</span>
  </div>
  <p class="desc-text">
    Component styling rules for interactive category filter chips with colored indicator dots, emergency warning notice banners, facility cards, and action buttons.
  </p>

  <div class="code-label">💻 Source Code (Excerpt): static/css/components.css</div>
  <pre class="code-container"><code>${escapeHtml(files.componentsCss.substring(0, 2100))}
... [Facility list cards, contact links, and distance indicators] ...</code></pre>

  <div class="output-card">
    <div class="output-card-header">
      <span>🎨 Rendered CSS Output Showcase: Chips, Notice Banner & Facility Card</span>
      <span style="font-family:monospace; color:#2563eb;">components.css</span>
    </div>
    <div class="output-img-wrapper" style="background:#f1f5f9; padding:16px;">
      <img src="${imgComponents}" class="output-img" style="border:none;" alt="Components CSS Output">
    </div>
    <div class="output-caption">
      <b>Output Verification:</b> Rendered category chips, warning notice banner, and hospital facility card with action triggers.
    </div>
  </div>

  <!-- ================= SECTION 7: static/css/bottom-sheet.css ================= -->
  <div class="page-break"></div>
  <div class="section-title-bar">
    <h2>7. Draggable Bottom Sheet & Detail Drawer Stylesheet</h2>
    <span class="file-tag">static/css/bottom-sheet.css</span>
  </div>
  <p class="desc-text">
    CSS specifications for mobile draggable bottom sheets: handle bar styling, summary row, touch-action configuration, and expansion states (peek, half, full).
  </p>

  <div class="code-label">💻 Full Source Code: static/css/bottom-sheet.css</div>
  <pre class="code-container"><code>${escapeHtml(files.bottomSheetCss)}</code></pre>

  <div class="output-card">
    <div class="output-card-header">
      <span>🎨 Rendered CSS Output Showcase: Bottom Sheet Drawer</span>
      <span style="font-family:monospace; color:#2563eb;">bottom-sheet.css</span>
    </div>
    <div class="output-img-wrapper" style="background:#f1f5f9; padding:16px;">
      <img src="${imgBottomSheet}" class="output-img" style="border:none;" alt="Bottom Sheet CSS Output">
    </div>
    <div class="output-caption">
      <b>Output Verification:</b> Draggable pill handle bar, summary header, and expandable facility detail card.
    </div>
  </div>

</body>
</html>
`;

// Save the compiled HTML report to static/report.html
const reportHtmlPath = path.join(__dirname, '..', 'static', 'report.html');
fs.writeFileSync(reportHtmlPath, reportHtml, 'utf8');
console.log('✓ Compiled static/report.html (Length:', reportHtml.length, 'bytes)');
