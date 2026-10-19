/**
 * BeaconGrid API Routes: Emergency Resources, Geocoding, Routing, GDELT Incidents & MongoDB
 */
const express = require('express');
const router = express.Router();
const { resourceCache } = require('../services/cache');
const { getResources } = require('../services/overpass');
const { searchLocations } = require('../services/geocoding');
const { getRoute } = require('../services/routing');
const { storage } = require('../db/storage');
const { ingestionPipeline } = require('../services/ingestion');
const { isConnected } = require('../db/mongo');

/**
 * Health Check Endpoint
 */
router.get('/health', async (req, res) => {
  const stats = resourceCache.getStats();
  const storageStats = await storage.getStats();
  const ingestionStatus = ingestionPipeline.getStatus();

  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    cache: {
      resource_hits: stats.hits,
      resource_misses: stats.misses
    },
    database: {
      mongodbConnected: storageStats.connectedToMongo,
      storageEngine: storageStats.storageEngine,
      totalIncidents: storageStats.incidentsCount,
      totalArticles: storageStats.articlesCount
    },
    intelligence: {
      lastIngestionRun: ingestionStatus.lastRunAt,
      lastIngestionSuccess: ingestionStatus.lastSuccessAt,
      isIngesting: ingestionStatus.isIngesting
    }
  });
});

/**
 * Emergency Resources Endpoint (OpenStreetMap / Overpass)
 */
router.get('/resources', async (req, res) => {
  const latStr = req.query.lat;
  const lonStr = req.query.lon;
  const radiusStr = req.query.radius || '5000';
  const categoriesStr = req.query.categories;

  if (latStr === undefined || lonStr === undefined) {
    return res.status(422).json({ detail: 'lat and lon query parameters are required' });
  }

  const lat = parseFloat(latStr);
  const lon = parseFloat(lonStr);
  const radius = parseInt(radiusStr, 10);

  if (isNaN(lat) || lat < -90 || lat > 90) {
    return res.status(422).json({ detail: 'lat must be between -90 and 90' });
  }
  if (isNaN(lon) || lon < -180 || lon > 180) {
    return res.status(422).json({ detail: 'lon must be between -180 and 180' });
  }
  if (isNaN(radius) || radius < 50 || radius > 10000) {
    return res.status(422).json({ detail: 'radius must be between 50 and 10000 meters' });
  }

  const categories = categoriesStr ? categoriesStr.split(',').map(s => s.trim()).filter(Boolean) : [];

  try {
    const result = await getResources({ lat, lon, radius, categories });
    res.json(result);
  } catch (err) {
    console.error('Error fetching resources:', err.message);
    res.status(503).json({
      detail: 'OpenStreetMap upstream service unavailable. Please retry shortly.',
      error: err.message
    });
  }
});

/**
 * Geocode Search Endpoint (Nominatim)
 */
router.get('/geocode', async (req, res) => {
  const query = req.query.q;
  if (!query || !query.trim()) {
    return res.json({ status: 'ok', query: '', results: [] });
  }

  try {
    const results = await searchLocations(query);
    res.json({
      status: 'ok',
      query: query,
      results: results
    });
  } catch (err) {
    res.status(500).json({ status: 'error', detail: err.message });
  }
});

/**
 * Route Calculation Endpoint (OSRM)
 */
router.get('/route', async (req, res) => {
  const startLatStr = req.query.start_lat;
  const startLonStr = req.query.start_lon;
  const endLatStr = req.query.end_lat;
  const endLonStr = req.query.end_lon;

  if (!startLatStr || !startLonStr || !endLatStr || !endLonStr) {
    return res.status(422).json({ detail: 'start_lat, start_lon, end_lat, and end_lon are required' });
  }

  const startLat = parseFloat(startLatStr);
  const startLon = parseFloat(startLonStr);
  const endLat = parseFloat(endLatStr);
  const endLon = parseFloat(endLonStr);

  try {
    const routeData = await getRoute(startLat, startLon, endLat, endLon);
    res.json(routeData);
  } catch (err) {
    res.status(500).json({ detail: 'Routing error', error: err.message });
  }
});

/**
 * GDELT Incident Intelligence Query Endpoint
 * Filters: category, district, verificationStatus, bbox (minLon,minLat,maxLon,maxLat), hours, limit
 */
router.get('/incidents', async (req, res) => {
  const { category, district, verificationStatus, bbox, hours, limit } = req.query;

  try {
    const incidents = await storage.queryIncidents({
      category,
      district,
      verificationStatus,
      bbox,
      hours: hours ? parseInt(hours, 10) : 168,
      limit: limit ? parseInt(limit, 10) : 100
    });

    const statusInfo = ingestionPipeline.getStatus();

    res.json({
      status: 'ok',
      count: incidents.length,
      data: incidents,
      meta: {
        databaseConnected: isConnected(),
        lastUpdated: statusInfo.lastSuccessAt,
        isIngesting: statusInfo.isIngesting,
        disclaimer: "News intelligence reports are derived from regional news publishers via GDELT. Reports are subject to verification and should not replace official disaster advisories."
      }
    });
  } catch (err) {
    res.status(500).json({ status: 'error', detail: err.message });
  }
});

/**
 * Single Incident Detail with Supporting Articles
 */
router.get('/incidents/:id', async (req, res) => {
  const incidentId = req.params.id;

  try {
    const incident = await storage.getIncidentById(incidentId);
    if (!incident) {
      return res.status(404).json({ detail: 'Incident record not found' });
    }

    const articles = await storage.getArticlesForIncident(incidentId);

    res.json({
      status: 'ok',
      incident: incident,
      articles: articles
    });
  } catch (err) {
    res.status(500).json({ status: 'error', detail: err.message });
  }
});

/**
 * Controlled Incident Ingestion Trigger (Refresh Button)
 */
router.post('/incidents/refresh', async (req, res) => {
  try {
    const outcome = await ingestionPipeline.run({ manual: true });
    res.json({
      status: outcome.status,
      message: outcome.message || 'Ingestion cycle processed.',
      cycleStats: outcome.cycleStats,
      stats: outcome.stats
    });
  } catch (err) {
    res.status(500).json({ status: 'error', detail: err.message });
  }
});

/**
 * Ingestion Status & Health Endpoint
 */
router.get('/incidents/status', async (req, res) => {
  const status = ingestionPipeline.getStatus();
  const storageStats = await storage.getStats();

  res.json({
    status: 'ok',
    ingestion: status,
    storage: storageStats
  });
});

/**
 * User Report of Incorrect or Outdated Incident Marker
 */
router.post('/incidents/report-issue', async (req, res) => {
  const { incidentId, issueType, comments, contactEmail } = req.body || {};

  if (!incidentId) {
    return res.status(422).json({ detail: 'incidentId is required' });
  }

  console.log(`[Incident Audit] Community feedback for incident ${incidentId}: Issue: ${issueType}, Comments: ${comments}`);

  // If community disputes an unverified incident, mark as disputed
  const inc = await storage.getIncidentById(incidentId);
  if (inc && inc.verificationStatus === 'unverified') {
    inc.verificationStatus = 'disputed';
    await storage.upsertIncident(inc);
  }

  res.json({
    status: 'ok',
    message: 'Thank you. Incident record flagged for manual review by Tamil Nadu disaster coordination desk.'
  });
});

module.exports = router;
