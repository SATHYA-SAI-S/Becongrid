/**
 * BeaconGrid Server Configuration
 */
const path = require('path');
require('dotenv').config();

module.exports = {
  PORT: parseInt(process.env.PORT || '8000', 10),
  HOST: process.env.HOST || '127.0.0.1',
  
  // MongoDB Configuration
  MONGODB_URI: process.env.MONGODB_URI || 'mongodb://127.0.0.1:27017/beacongrid',
  MONGODB_DB_NAME: process.env.MONGODB_DB_NAME || 'beacongrid',
  
  // GDELT DOC 2.0 API Configuration
  GDELT: {
    API_URL: 'https://api.gdeltproject.org/api/v2/doc/doc',
    RATE_LIMIT_MS: 6000, // GDELT enforces 1 request per 5 seconds
    TIMEOUT_MS: 12000,
    MAX_RECORDS: 50,
    TIMESPAN: '7d',
    USER_AGENT: 'BeaconGrid/2.0 (Emergency Incident Intelligence; Tamil Nadu Disaster Grid)'
  },
  
  // Upstream OSM / Overpass Servers with Fallback
  OVERPASS_SERVERS: [
    'https://overpass-api.de/api/interpreter',
    'https://overpass.kumi.systems/api/interpreter',
    'https://maps.mail.ru/osm/tools/overpass/api/interpreter'
  ],
  
  // Geocoding and Routing
  NOMINATIM_URL: 'https://nominatim.openstreetmap.org/search',
  OSRM_URL: 'https://router.project-osrm.org/route/v1/driving',
  
  // Cache and Rate Limits
  CACHE_TTL_MS: 10 * 60 * 1000, // 10 minutes
  INGESTION_INTERVAL_MS: 15 * 60 * 1000, // 15 minutes
  
  // Paths
  STATIC_DIR: path.join(__dirname, '..', 'static'),
  INDEX_FILE: path.join(__dirname, '..', 'static', 'index.html'),
  MAP_FILE: path.join(__dirname, '..', 'static', 'map.html')
};
