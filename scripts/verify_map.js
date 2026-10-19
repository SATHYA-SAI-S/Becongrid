const fs = require('fs');
const html = fs.readFileSync('static/map.html', 'utf8');

const checks = {
  'viewIncidents tab': html.includes('data-view="viewIncidents"'),
  'viewIncidents section': html.includes('id="viewIncidents"'),
  'btnRefreshGdelt button': html.includes('btnRefreshGdelt'),
  'countIncidents element': html.includes('countIncidents'),
  'disputeModal': html.includes('id="disputeModal"'),
  'openIncidentDrawer function': html.includes('function openIncidentDrawer'),
  'loadIncidents function': html.includes('function loadIncidents'),
  'renderIncidentsFeed function': html.includes('function renderIncidentsFeed')
};

console.log('Verification Results:');
for (const [k, v] of Object.entries(checks)) {
  console.log(`${v ? '✅' : '❌'} ${k}: ${v}`);
}
