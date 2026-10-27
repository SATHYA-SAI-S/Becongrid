/**
 * BeaconGrid DOCX Generator
 * Compiles Source Code & Playwright Output Screenshots into a Word Document (.docx)
 * 
 * Student Credentials:
 * 24MID0077 - Jai Kishore K
 * 24MID0112 - Sathya Sai S
 * 24MID0135 - Sudharshini Manikandan
 */

const fs = require('fs');
const path = require('path');
const docx = require('docx');
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  Table,
  TableRow,
  TableCell,
  ImageRun,
  PageBreak,
  HeadingLevel,
  AlignmentType,
  WidthType,
  ShadingType,
  BorderStyle
} = docx;

console.log('Generating BeaconGrid Code & Output DOCX Report...');

// Source files
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

// Helper: Create Section Title Bar Table
function createSectionHeader(title, fileBadge) {
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            shading: { fill: '0F172A', type: ShadingType.CLEAR },
            borders: {
              top: { style: BorderStyle.NONE },
              bottom: { style: BorderStyle.NONE },
              left: { style: BorderStyle.NONE },
              right: { style: BorderStyle.NONE }
            },
            margins: { top: 120, bottom: 120, left: 180, right: 180 },
            children: [
              new Paragraph({
                children: [
                  new TextRun({
                    text: title + '  ',
                    bold: true,
                    size: 26, // 13pt
                    color: 'FFFFFF',
                    font: 'Arial'
                  }),
                  new TextRun({
                    text: ` [ ${fileBadge} ]`,
                    bold: true,
                    size: 20, // 10pt
                    color: '38BDF8',
                    font: 'Consolas'
                  })
                ]
              })
            ]
          })
        ]
      })
    ]
  });
}

// Helper: Create Formatted Code Box Table
function createCodeBox(codeString, maxLines = 75) {
  const lines = codeString.split(/\r?\n/).slice(0, maxLines);
  const codeParagraphs = lines.map(line => new Paragraph({
    spacing: { before: 20, after: 20, line: 240 },
    children: [
      new TextRun({
        text: line.length > 0 ? line : ' ',
        font: 'Consolas',
        size: 15, // 7.5pt
        color: '1E293B'
      })
    ]
  }));

  if (codeString.split(/\r?\n/).length > maxLines) {
    codeParagraphs.push(new Paragraph({
      spacing: { before: 40, after: 20 },
      children: [
        new TextRun({
          text: `... [Truncated for readability: ${codeString.split(/\r?\n/).length - maxLines} additional lines in source file] ...`,
          font: 'Consolas',
          italic: true,
          size: 15,
          color: '64748B'
        })
      ]
    }));
  }

  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            shading: { fill: 'F8FAFC', type: ShadingType.CLEAR },
            borders: {
              top: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
              bottom: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
              left: { style: BorderStyle.SINGLE, size: 14, color: '2563EB' }, // Blue accent
              right: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' }
            },
            margins: { top: 100, bottom: 100, left: 160, right: 160 },
            children: codeParagraphs
          })
        ]
      })
    ]
  });
}

// Helper: Create Output Image with Border & Caption
function createOutputCard(imagePath, width, height, viewTitle, captionText) {
  const imgData = fs.readFileSync(imagePath);
  return [
    new Paragraph({
      spacing: { before: 200, after: 60 },
      children: [
        new TextRun({
          text: '🖥️ Browser Output: ',
          bold: true,
          size: 20,
          color: '0F172A',
          font: 'Arial'
        }),
        new TextRun({
          text: viewTitle,
          bold: true,
          size: 20,
          color: '2563EB',
          font: 'Arial'
        })
      ]
    }),
    new Table({
      width: { size: 100, type: WidthType.PERCENTAGE },
      rows: [
        new TableRow({
          children: [
            new TableCell({
              shading: { fill: '0F172A', type: ShadingType.CLEAR },
              borders: {
                top: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
                bottom: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
                left: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
                right: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' }
              },
              margins: { top: 120, bottom: 120, left: 120, right: 120 },
              children: [
                new Paragraph({
                  alignment: AlignmentType.CENTER,
                  children: [
                    new ImageRun({
                      data: imgData,
                      transformation: { width, height }
                    })
                  ]
                })
              ]
            })
          ]
        })
      ]
    }),
    new Paragraph({
      spacing: { before: 60, after: 200 },
      children: [
        new TextRun({
          text: 'Verification Note: ',
          bold: true,
          italic: true,
          size: 18,
          color: '475569',
          font: 'Arial'
        }),
        new TextRun({
          text: captionText,
          italic: true,
          size: 18,
          color: '64748B',
          font: 'Arial'
        })
      ]
    })
  ];
}

async function buildDocx() {
  const doc = new Document({
    creator: 'BeaconGrid Dev Team',
    title: 'BeaconGrid — Source Code & Browser Output Report',
    description: 'Academic evaluation artifact documenting HTML & CSS source code paired with Playwright browser output screenshots',
    styles: {
      default: {
        document: {
          run: {
            font: 'Arial',
            size: 22, // 11pt
            color: '1E293B'
          }
        }
      }
    },
    sections: [
      {
        properties: {
          page: {
            margin: {
              top: 1000,
              bottom: 1000,
              left: 1000,
              right: 1000
            }
          }
        },
        children: [
          // ================= TITLE & COVER =================
          new Paragraph({
            spacing: { before: 0, after: 80 },
            children: [
              new TextRun({
                text: 'ACADEMIC EVALUATION & CODE ARTIFACT REPORT',
                bold: true,
                size: 18,
                color: 'EA580C',
                font: 'Arial'
              })
            ]
          }),
          new Paragraph({
            spacing: { before: 0, after: 120 },
            children: [
              new TextRun({
                text: 'BeaconGrid — Emergency Resource Map & GDELT News Intelligence',
                bold: true,
                size: 34, // 17pt
                color: '0F172A',
                font: 'Arial'
              })
            ]
          }),
          new Paragraph({
            spacing: { before: 0, after: 240 },
            children: [
              new TextRun({
                text: 'Centralized Disaster Response Management System with Overpass OSM Integration and Real-time Multi-source News Corroboration for Tamil Nadu',
                size: 22,
                color: '475569',
                font: 'Arial'
              })
            ]
          }),

          // Students Box Table
          new Table({
            width: { size: 100, type: WidthType.PERCENTAGE },
            rows: [
              new TableRow({
                children: [
                  new TableCell({
                    width: { size: 33, type: WidthType.PERCENTAGE },
                    shading: { fill: 'F1F5F9', type: ShadingType.CLEAR },
                    borders: {
                      top: { style: BorderStyle.SINGLE, size: 6, color: '2563EB' },
                      bottom: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
                      left: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
                      right: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' }
                    },
                    margins: { top: 120, bottom: 120, left: 140, right: 140 },
                    children: [
                      new Paragraph({
                        children: [
                          new TextRun({ text: '24MID0077', bold: true, size: 22, color: '2563EB', font: 'Consolas' })
                        ]
                      }),
                      new Paragraph({
                        children: [
                          new TextRun({ text: 'Jai Kishore K', bold: true, size: 22, color: '0F172A' })
                        ]
                      })
                    ]
                  }),
                  new TableCell({
                    width: { size: 33, type: WidthType.PERCENTAGE },
                    shading: { fill: 'F1F5F9', type: ShadingType.CLEAR },
                    borders: {
                      top: { style: BorderStyle.SINGLE, size: 6, color: '2563EB' },
                      bottom: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
                      left: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
                      right: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' }
                    },
                    margins: { top: 120, bottom: 120, left: 140, right: 140 },
                    children: [
                      new Paragraph({
                        children: [
                          new TextRun({ text: '24MID0112', bold: true, size: 22, color: '2563EB', font: 'Consolas' })
                        ]
                      }),
                      new Paragraph({
                        children: [
                          new TextRun({ text: 'Sathya Sai S', bold: true, size: 22, color: '0F172A' })
                        ]
                      })
                    ]
                  }),
                  new TableCell({
                    width: { size: 34, type: WidthType.PERCENTAGE },
                    shading: { fill: 'F1F5F9', type: ShadingType.CLEAR },
                    borders: {
                      top: { style: BorderStyle.SINGLE, size: 6, color: '2563EB' },
                      bottom: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
                      left: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' },
                      right: { style: BorderStyle.SINGLE, size: 4, color: 'CBD5E1' }
                    },
                    margins: { top: 120, bottom: 120, left: 140, right: 140 },
                    children: [
                      new Paragraph({
                        children: [
                          new TextRun({ text: '24MID0135', bold: true, size: 22, color: '2563EB', font: 'Consolas' })
                        ]
                      }),
                      new Paragraph({
                        children: [
                          new TextRun({ text: 'Sudharshini Manikandan', bold: true, size: 22, color: '0F172A' })
                        ]
                      })
                    ]
                  })
                ]
              })
            ]
          }),

          // Metadata Info
          new Paragraph({
            spacing: { before: 180, after: 240 },
            children: [
              new TextRun({ text: 'Course / Domain: ', bold: true, size: 20, color: '475569' }),
              new TextRun({ text: 'Advanced Web Technology (AWT) | Emergency Geospatial Information Systems\n', size: 20 }),
              new TextRun({ text: 'Execution Runtime: ', bold: true, size: 20, color: '475569' }),
              new TextRun({ text: 'Node.js Express Server (Port 8000) & Playwright Chromium Automation Engine\n', size: 20 }),
              new TextRun({ text: 'Report Scope: ', bold: true, size: 20, color: '475569' }),
              new TextRun({ text: '3 HTML Documents + 4 CSS Stylesheets, paired with Rendered Browser Outputs', size: 20 })
            ]
          }),

          // ================= SECTION 1: static/index.html =================
          new Paragraph({ children: [new PageBreak()] }),
          createSectionHeader('1. Landing Page & Citizen Portal', 'static/index.html'),
          new Paragraph({
            spacing: { before: 140, after: 100 },
            children: [
              new TextRun({
                text: 'Functional Overview: Overview portal featuring state network status, disaster crisis metrics, four-role interactive dispatch preview, emergency helplines directory, and gateway to the live command map.',
                size: 20,
                color: '475569'
              })
            ]
          }),
          new Paragraph({
            spacing: { before: 80, after: 60 },
            children: [
              new TextRun({ text: '💻 Source Code (Excerpt): static/index.html', bold: true, size: 19, color: '334155' })
            ]
          }),
          createCodeBox(files.indexHtml, 65),
          ...createOutputCard(
            'screenshots/output_index.png',
            560,
            350,
            'Landing Page & Citizen Portal (static/index.html)',
            'Landing page rendered in Playwright browser with BeaconGrid tactical dark theme, radar scan badge, real-time helplines trigger, and citizen fast-action buttons.'
          ),

          // ================= SECTION 2: static/map.html =================
          new Paragraph({ children: [new PageBreak()] }),
          createSectionHeader('2. Live Tactical Command Map & Disaster Grid', 'static/map.html'),
          new Paragraph({
            spacing: { before: 140, after: 100 },
            children: [
              new TextRun({
                text: 'Functional Overview: Interactive Leaflet.js command center with Overpass API live amenity scanning, 130+ verified hospital ICU beds across 38 districts, GDELT multi-source news markers, and sliding detail drawer.',
                size: 20,
                color: '475569'
              })
            ]
          }),
          new Paragraph({
            spacing: { before: 80, after: 60 },
            children: [
              new TextRun({ text: '💻 Source Code (Excerpt): static/map.html', bold: true, size: 19, color: '334155' })
            ]
          }),
          createCodeBox(mapHtmlClean, 70),
          ...createOutputCard(
            'screenshots/output_map.png',
            560,
            350,
            'Statewide Disaster Grid View (static/map.html)',
            'Complete Tamil Nadu map showing 130+ hospital ICU beds, cyclone shelters, relief supplies, and GDELT news intelligence markers.'
          ),
          ...createOutputCard(
            'screenshots/output_map_drawer.png',
            560,
            350,
            'Slide-in Marker Drawer & Multi-Source Corroboration',
            'Incident detail drawer displaying corroborated sources (DT Next, Dinamalar), exact coordinates, relative time, and dispute verification button.'
          ),
          ...createOutputCard(
            'screenshots/output_map_news_feed.png',
            560,
            350,
            'Real-Time News Intelligence Feed Tab',
            'Dedicated feed displaying real-time incidents categorized into 7 crisis types with verification badges and telemetry KPIs.'
          ),

          // ================= SECTION 3: emergency-resource-map.html =================
          new Paragraph({ children: [new PageBreak()] }),
          createSectionHeader('3. Emergency Resource Network Template', 'emergency-resource-map.html'),
          new Paragraph({
            spacing: { before: 140, after: 100 },
            children: [
              new TextRun({
                text: 'Functional Overview: Reference single-page application mockup demonstrating floating search, facility radius filter, category pills, and resource cards list.',
                size: 20,
                color: '475569'
              })
            ]
          }),
          new Paragraph({
            spacing: { before: 80, after: 60 },
            children: [
              new TextRun({ text: '💻 Source Code (Excerpt): emergency-resource-map.html', bold: true, size: 19, color: '334155' })
            ]
          }),
          createCodeBox(files.emergencyMapHtml, 65),
          ...createOutputCard(
            'screenshots/output_emergency_map.png',
            560,
            350,
            'Emergency Resource Network Mockup (emergency-resource-map.html)',
            'Floating search bar, category chips, and live facility listing with distance calculations.'
          ),

          // ================= SECTION 4: static/css/tokens.css =================
          new Paragraph({ children: [new PageBreak()] }),
          createSectionHeader('4. Design Tokens & Color Palette Stylesheet', 'static/css/tokens.css'),
          new Paragraph({
            spacing: { before: 140, after: 100 },
            children: [
              new TextRun({
                text: 'Functional Overview: CSS Custom Properties declaring the design system: neutral surface values, category accents (hospital, shelter, water, food), elevation drop-shadows, and typography scales.',
                size: 20,
                color: '475569'
              })
            ]
          }),
          new Paragraph({
            spacing: { before: 80, after: 60 },
            children: [
              new TextRun({ text: '💻 Full Source Code: static/css/tokens.css', bold: true, size: 19, color: '334155' })
            ]
          }),
          createCodeBox(files.tokensCss, 80),
          ...createOutputCard(
            'screenshots/output_tokens_css.png',
            560,
            132,
            'Rendered CSS Showcase: Design Tokens & Palette',
            'Rendered palette swatches showing --cat-hospital, --cat-clinic, --cat-pharmacy, and core brand tokens.'
          ),

          // ================= SECTION 5: static/css/layout.css =================
          new Paragraph({ children: [new PageBreak()] }),
          createSectionHeader('5. Layout Structure & Responsive Grid Stylesheet', 'static/css/layout.css'),
          new Paragraph({
            spacing: { before: 140, after: 100 },
            children: [
              new TextRun({
                text: 'Functional Overview: Styles governing viewport containment, fullscreen Leaflet map positioning, floating command island, top search bar wrapper, and responsive breakpoint adjustments.',
                size: 20,
                color: '475569'
              })
            ]
          }),
          new Paragraph({
            spacing: { before: 80, after: 60 },
            children: [
              new TextRun({ text: '💻 Source Code (Excerpt): static/css/layout.css', bold: true, size: 19, color: '334155' })
            ]
          }),
          createCodeBox(files.layoutCss, 65),
          ...createOutputCard(
            'screenshots/output_layout_css.png',
            560,
            123,
            'Rendered CSS Showcase: Layout & Search Box Wrapper',
            'Rendered floating search wrapper with icon button, input box, and primary action trigger.'
          ),

          // ================= SECTION 6: static/css/components.css =================
          new Paragraph({ children: [new PageBreak()] }),
          createSectionHeader('6. UI Components, Chips & Cards Stylesheet', 'static/css/components.css'),
          new Paragraph({
            spacing: { before: 140, after: 100 },
            children: [
              new TextRun({
                text: 'Functional Overview: Component styling rules for interactive category filter chips with colored indicator dots, emergency warning notice banners, facility cards, and action buttons.',
                size: 20,
                color: '475569'
              })
            ]
          }),
          new Paragraph({
            spacing: { before: 80, after: 60 },
            children: [
              new TextRun({ text: '💻 Source Code (Excerpt): static/css/components.css', bold: true, size: 19, color: '334155' })
            ]
          }),
          createCodeBox(files.componentsCss, 65),
          ...createOutputCard(
            'screenshots/output_components_css.png',
            560,
            213,
            'Rendered CSS Showcase: Chips, Notice Banner & Facility Card',
            'Rendered category chips, warning notice banner, and hospital facility card with action triggers.'
          ),

          // ================= SECTION 7: static/css/bottom-sheet.css =================
          new Paragraph({ children: [new PageBreak()] }),
          createSectionHeader('7. Draggable Bottom Sheet & Detail Drawer Stylesheet', 'static/css/bottom-sheet.css'),
          new Paragraph({
            spacing: { before: 140, after: 100 },
            children: [
              new TextRun({
                text: 'Functional Overview: CSS specifications for mobile draggable bottom sheets: handle bar styling, summary row, touch-action configuration, and expansion states (peek, half, full).',
                size: 20,
                color: '475569'
              })
            ]
          }),
          new Paragraph({
            spacing: { before: 80, after: 60 },
            children: [
              new TextRun({ text: '💻 Full Source Code: static/css/bottom-sheet.css', bold: true, size: 19, color: '334155' })
            ]
          }),
          createCodeBox(files.bottomSheetCss, 80),
          ...createOutputCard(
            'screenshots/output_bottom_sheet_css.png',
            560,
            143,
            'Rendered CSS Showcase: Bottom Sheet Drawer',
            'Draggable pill handle bar, summary header, and expandable facility detail card.'
          )
        ]
      }
    ]
  });

  const buffer = await Packer.toBuffer(doc);
  const outPath = path.join(__dirname, '..', 'BeaconGrid_Code_and_Outputs_Report.docx');
  fs.writeFileSync(outPath, buffer);
  console.log(`✓ BeaconGrid DOCX Report successfully generated at: ${outPath} (${buffer.length} bytes)`);
}

buildDocx().catch(err => {
  console.error('Failed to generate DOCX:', err);
  process.exit(1);
});
