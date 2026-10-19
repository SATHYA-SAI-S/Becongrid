/**
 * Unified Storage Layer: MongoDB with In-Memory GeoJSON Fallback Engine
 */
const { getDb, isConnected } = require('./mongo');

// Verified Seed Incidents for Tamil Nadu across all 7 categories
const INITIAL_SEED_INCIDENTS = [
  {
    incidentId: "inc-tn-fld-01",
    category: "natural_disaster",
    title: "Tamirabarani River Discharge Alert & Low-Lying Inundation",
    description: "Intense catchment rainfall in the Western Ghats led to 35,000 cusecs surplus water release from Papanasam and Manimuthar dams. District administration evacuated riverside colonies in Tirunelveli and Tiruchendur.",
    location: {
      type: "Point",
      coordinates: [77.7280, 8.7210] // [lon, lat]
    },
    locationName: "Kurukkuthurai & Murugan Temple Banks, Tirunelveli",
    city: "Tirunelveli",
    district: "tirunelveli",
    locationPrecision: "city",
    eventTime: new Date(Date.now() - 3600000 * 5).toISOString(),
    firstReportedAt: new Date(Date.now() - 3600000 * 6).toISOString(),
    lastReportedAt: new Date(Date.now() - 3600000 * 2).toISOString(),
    updatedAt: new Date().toISOString(),
    articleIds: ["art-toi-001", "art-th-001"],
    sourceCount: 2,
    sources: [
      {
        publisher: "The Hindu",
        url: "https://www.thehindu.com/news/national/tamil-nadu/tamirabarani-spillover-flood-warning/article676101.ece",
        title: "Tamirabarani in spate: Flood warning issued to riverside residents in Tirunelveli"
      },
      {
        publisher: "Times of India",
        url: "https://timesofindia.indiatimes.com/city/madurai/heavy-rains-in-western-ghats-dams-reach-full-capacity/articleshow/1060012.cms",
        title: "Heavy rains in Western Ghats: Papanasam dam shutters opened"
      }
    ],
    verificationStatus: "corroborated",
    confidence: 0.92,
    eventStatus: "ongoing"
  },
  {
    incidentId: "inc-tn-blk-02",
    category: "infrastructure",
    title: "Ooty-Kotagiri Ghat Road Landslide and Traffic Halt",
    description: "Overnight slope failure resulted in boulder collapse and mudslide near Katteri bridge on NH 181. Highways Department deployed heavy earthmovers for single-lane clearance.",
    location: {
      type: "Point",
      coordinates: [76.7820, 11.3780]
    },
    locationName: "Katteri Bend, Ooty-Kotagiri Highway",
    city: "Kotagiri",
    district: "nilgiris",
    locationPrecision: "exact",
    eventTime: new Date(Date.now() - 3600000 * 8).toISOString(),
    firstReportedAt: new Date(Date.now() - 3600000 * 8).toISOString(),
    lastReportedAt: new Date(Date.now() - 3600000 * 3).toISOString(),
    updatedAt: new Date().toISOString(),
    articleIds: ["art-dt-002", "art-din-002"],
    sourceCount: 2,
    sources: [
      {
        publisher: "DT Next",
        url: "https://www.dtnext.in/news/tamilnadu/landslide-disrupts-traffic-on-ooty-kotagiri-ghat-road",
        title: "Landslide disrupts vehicular movement on Ooty-Kotagiri ghat road"
      },
      {
        publisher: "Dinamalar",
        url: "https://www.dinamalar.com/news_detail.asp?id=3492810",
        title: "ஊட்டி-கோத்தகிரி சாலையில் பாறை சரிவு: போக்குவரத்து மாற்றம்"
      }
    ],
    verificationStatus: "corroborated",
    confidence: 0.89,
    eventStatus: "ongoing"
  },
  {
    incidentId: "inc-tn-fir-03",
    category: "accident_emergency",
    title: "Chemical Storage Godown Fire at Ambattur Industrial Estate",
    description: "Major fire broke out in a chemical solvent packaging unit in Sector 3 of Ambattur Industrial Estate. 6 fire tenders from Ambattur, JJ Nagar and Mogappair deployed. No casualties reported.",
    location: {
      type: "Point",
      coordinates: [80.1610, 13.1090]
    },
    locationName: "3rd Main Road, Ambattur Industrial Estate, Chennai",
    city: "Chennai",
    district: "chennai",
    locationPrecision: "exact",
    eventTime: new Date(Date.now() - 3600000 * 4).toISOString(),
    firstReportedAt: new Date(Date.now() - 3600000 * 4).toISOString(),
    lastReportedAt: new Date(Date.now() - 3600000 * 1).toISOString(),
    updatedAt: new Date().toISOString(),
    articleIds: ["art-nie-003"],
    sourceCount: 1,
    sources: [
      {
        publisher: "The New Indian Express",
        url: "https://www.newindianexpress.com/cities/chennai/2026/oct/19/massive-fire-breaks-out-in-ambattur-industrial-unit",
        title: "Massive fire breaks out in chemical unit at Ambattur Industrial Estate"
      }
    ],
    verificationStatus: "unverified",
    confidence: 0.78,
    eventStatus: "ongoing"
  },
  {
    incidentId: "inc-tn-pro-04",
    category: "protest_disturbance",
    title: "Textile Trade Union Demonstration on Avinashi Road",
    description: "Over 400 garment and powerloom workers staged a peaceful demonstration and human chain near Tiruppur Old Bus Stand regarding revised minimum wages. Traffic diverted via Kumaran Road.",
    location: {
      type: "Point",
      coordinates: [77.3411, 11.1085]
    },
    locationName: "Kumaran Road Junction, Tiruppur",
    city: "Tiruppur",
    district: "tiruppur",
    locationPrecision: "city",
    eventTime: new Date(Date.now() - 3600000 * 12).toISOString(),
    firstReportedAt: new Date(Date.now() - 3600000 * 12).toISOString(),
    lastReportedAt: new Date(Date.now() - 3600000 * 6).toISOString(),
    updatedAt: new Date().toISOString(),
    articleIds: ["art-th-004"],
    sourceCount: 1,
    sources: [
      {
        publisher: "The Hindu",
        url: "https://www.thehindu.com/news/cities/Coimbatore/tiruppur-garment-workers-protest-for-wage-revision/article676210.ece",
        title: "Tiruppur garment workers take out rally seeking wage hike"
      }
    ],
    verificationStatus: "corroborated",
    confidence: 0.85,
    eventStatus: "concluded"
  },
  {
    incidentId: "inc-tn-env-05",
    category: "environmental",
    title: "Ennore Creek Effluent & Coastal Sludge Monitoring",
    description: "TNPCB environmental surveillance teams inspected Kosasthalaiyar river mouth and Ennore creek following complaints of petroleum hydrocarbon residue after monsoon drainage surge.",
    location: {
      type: "Point",
      coordinates: [80.3250, 13.2180]
    },
    locationName: "Kosasthalaiyar River Estuary, Ennore, Chennai",
    city: "Chennai",
    district: "chennai",
    locationPrecision: "city",
    eventTime: new Date(Date.now() - 3600000 * 20).toISOString(),
    firstReportedAt: new Date(Date.now() - 3600000 * 22).toISOString(),
    lastReportedAt: new Date(Date.now() - 3600000 * 10).toISOString(),
    updatedAt: new Date().toISOString(),
    articleIds: ["art-dt-005", "art-nie-005"],
    sourceCount: 2,
    sources: [
      {
        publisher: "DT Next",
        url: "https://www.dtnext.in/news/city/pollution-control-board-collects-samples-from-ennore-creek",
        title: "Pollution board collects water samples from Ennore creek"
      },
      {
        publisher: "The New Indian Express",
        url: "https://www.newindianexpress.com/cities/chennai/2026/oct/18/coastal-villages-urge-permanent-ennore-clean-up",
        title: "Fisherfolk in Ennore demand clean up of toxic sludge"
      }
    ],
    verificationStatus: "officially_confirmed",
    confidence: 0.95,
    eventStatus: "ongoing"
  },
  {
    incidentId: "inc-tn-pub-06",
    category: "public_safety",
    title: "Coastal Security Group Enhanced Night Patrol along Palk Strait",
    description: "Marine police and Indian Coast Guard instituted round-the-clock hovercraft surveillance across Dhanushkodi, Mandapam and Arichal Munai following suspicious vessel movement reports.",
    location: {
      type: "Point",
      coordinates: [79.3240, 9.2820]
    },
    locationName: "Dhanushkodi Coast & Arichal Munai, Ramanathapuram",
    city: "Rameswaram",
    district: "ramanathapuram",
    locationPrecision: "city",
    eventTime: new Date(Date.now() - 3600000 * 14).toISOString(),
    firstReportedAt: new Date(Date.now() - 3600000 * 14).toISOString(),
    lastReportedAt: new Date(Date.now() - 3600000 * 7).toISOString(),
    updatedAt: new Date().toISOString(),
    articleIds: ["art-toi-006"],
    sourceCount: 1,
    sources: [
      {
        publisher: "Times of India",
        url: "https://timesofindia.indiatimes.com/city/madurai/coastal-security-group-tightens-vigil-along-palk-strait/articleshow/1060500.cms",
        title: "Coastal security heightened along Rameswaram maritime boundary"
      }
    ],
    verificationStatus: "officially_confirmed",
    confidence: 0.90,
    eventStatus: "ongoing"
  },
  {
    incidentId: "inc-tn-hea-07",
    category: "public_health",
    title: "Monsoon Seasonal Fever Cluster Screened in Madurai Rural",
    description: "Public Health Department dispatched 8 mobile medical teams across Melur and Usilampatti blocks for fever camp screening and anti-larval fogging after seasonal spike.",
    location: {
      type: "Point",
      coordinates: [78.1320, 9.9280]
    },
    locationName: "Melur & Usilampatti Taluk Health Centers, Madurai",
    city: "Madurai",
    district: "madurai",
    locationPrecision: "district",
    eventTime: new Date(Date.now() - 3600000 * 16).toISOString(),
    firstReportedAt: new Date(Date.now() - 3600000 * 18).toISOString(),
    lastReportedAt: new Date(Date.now() - 3600000 * 5).toISOString(),
    updatedAt: new Date().toISOString(),
    articleIds: ["art-th-007"],
    sourceCount: 1,
    sources: [
      {
        publisher: "The Hindu",
        url: "https://www.thehindu.com/news/cities/Madurai/health-department-organises-fever-camps-in-madurai/article676340.ece",
        title: "Special fever camps organised in 12 rural blocks of Madurai"
      }
    ],
    verificationStatus: "officially_confirmed",
    confidence: 0.91,
    eventStatus: "ongoing"
  }
];

// In-Memory store (fallback & local caching)
const memoryArticles = new Map();
const memoryIncidents = new Map();

// Populate initial seed incidents in memory
INITIAL_SEED_INCIDENTS.forEach(inc => {
  memoryIncidents.set(inc.incidentId, { ...inc });
  inc.sources.forEach((src, idx) => {
    const artId = inc.articleIds[idx] || `art-${inc.incidentId}-${idx}`;
    memoryArticles.set(artId, {
      articleId: artId,
      url: src.url,
      title: src.title,
      publisher: src.publisher,
      language: "en",
      seendate: inc.eventTime,
      discoveredAt: inc.firstReportedAt,
      summary: inc.description,
      fingerprint: artId,
      incidentId: inc.incidentId,
      category: inc.category,
      status: "processed"
    });
  });
});

class StorageService {
  /**
   * Save or update an article
   */
  async upsertArticle(article) {
    memoryArticles.set(article.articleId, article);

    if (isConnected()) {
      try {
        const db = getDb();
        await db.collection('articles').updateOne(
          { url: article.url },
          { $set: article },
          { upsert: true }
        );
      } catch (err) {
        console.warn('MongoDB upsertArticle failed, saved in memory:', err.message);
      }
    }
    return article;
  }

  /**
   * Find article by canonical URL or fingerprint
   */
  async findArticleByUrlOrFingerprint(url, fingerprint) {
    if (isConnected()) {
      try {
        const db = getDb();
        const found = await db.collection('articles').findOne({
          $or: [{ url: url }, { fingerprint: fingerprint }]
        });
        if (found) return found;
      } catch (err) {}
    }

    // In-memory fallback
    for (const art of memoryArticles.values()) {
      if (art.url === url || (fingerprint && art.fingerprint === fingerprint)) {
        return art;
      }
    }
    return null;
  }

  /**
   * Save or update an incident
   */
  async upsertIncident(incident) {
    incident.updatedAt = new Date().toISOString();
    memoryIncidents.set(incident.incidentId, { ...incident });

    if (isConnected()) {
      try {
        const db = getDb();
        await db.collection('incidents').updateOne(
          { incidentId: incident.incidentId },
          { $set: incident },
          { upsert: true }
        );
      } catch (err) {
        console.warn('MongoDB upsertIncident failed, saved in memory:', err.message);
      }
    }
    return incident;
  }

  /**
   * Find an incident by ID
   */
  async getIncidentById(incidentId) {
    if (isConnected()) {
      try {
        const db = getDb();
        const found = await db.collection('incidents').findOne({ incidentId });
        if (found) return found;
      } catch (err) {}
    }
    return memoryIncidents.get(incidentId) || null;
  }

  /**
   * Query incidents with filters (category, district, verification, bounding box, recency)
   */
  async queryIncidents({ category, district, verificationStatus, bbox, limit = 100, hours = 168 } = {}) {
    const cutoffDate = new Date(Date.now() - hours * 3600000);

    if (isConnected()) {
      try {
        const db = getDb();
        const filter = {};

        if (category && category !== 'all') {
          filter.category = category;
        }
        if (district && district !== 'all') {
          filter.district = district.toLowerCase();
        }
        if (verificationStatus && verificationStatus !== 'all') {
          filter.verificationStatus = verificationStatus;
        }

        // Bounding box filter [minLon, minLat, maxLon, maxLat]
        if (bbox) {
          const parts = bbox.split(',').map(Number);
          if (parts.length === 4 && !parts.some(isNaN)) {
            filter.location = {
              $geoWithin: {
                $box: [
                  [parts[0], parts[1]], // bottom-left
                  [parts[2], parts[3]]  // top-right
                ]
              }
            };
          }
        }

        filter.lastReportedAt = { $gte: cutoffDate.toISOString() };

        const results = await db.collection('incidents')
          .find(filter)
          .sort({ lastReportedAt: -1 })
          .limit(limit)
          .toArray();

        if (results && results.length > 0) return results;
      } catch (err) {
        console.warn('MongoDB queryIncidents failed, falling back to memory store:', err.message);
      }
    }

    // In-memory query fallback
    let items = Array.from(memoryIncidents.values());

    if (category && category !== 'all') {
      items = items.filter(i => i.category === category);
    }
    if (district && district !== 'all') {
      items = items.filter(i => i.district === district.toLowerCase());
    }
    if (verificationStatus && verificationStatus !== 'all') {
      items = items.filter(i => i.verificationStatus === verificationStatus);
    }

    if (bbox) {
      const parts = bbox.split(',').map(Number);
      if (parts.length === 4 && !parts.some(isNaN)) {
        const [minLon, minLat, maxLon, maxLat] = parts;
        items = items.filter(i => {
          if (!i.location || !i.location.coordinates) return false;
          const [lon, lat] = i.location.coordinates;
          return lon >= minLon && lon <= maxLon && lat >= minLat && lat <= maxLat;
        });
      }
    }

    // Sort by lastReportedAt descending
    items.sort((a, b) => new Date(b.lastReportedAt || 0) - new Date(a.lastReportedAt || 0));
    return items.slice(0, limit);
  }

  /**
   * Get all articles linked to an incident
   */
  async getArticlesForIncident(incidentId) {
    if (isConnected()) {
      try {
        const db = getDb();
        const articles = await db.collection('articles').find({ incidentId }).toArray();
        if (articles && articles.length > 0) return articles;
      } catch (err) {}
    }

    return Array.from(memoryArticles.values()).filter(a => a.incidentId === incidentId);
  }

  /**
   * Get storage statistics
   */
  async getStats() {
    let mongoArticleCount = 0;
    let mongoIncidentCount = 0;

    if (isConnected()) {
      try {
        const db = getDb();
        mongoArticleCount = await db.collection('articles').countDocuments();
        mongoIncidentCount = await db.collection('incidents').countDocuments();
      } catch (e) {}
    }

    return {
      connectedToMongo: isConnected(),
      articlesCount: isConnected() ? mongoArticleCount : memoryArticles.size,
      incidentsCount: isConnected() ? mongoIncidentCount : memoryIncidents.size,
      storageEngine: isConnected() ? 'MongoDB 2dsphere' : 'In-Memory GeoJSON Engine'
    };
  }
}

const storage = new StorageService();

module.exports = {
  storage,
  INITIAL_SEED_INCIDENTS
};
