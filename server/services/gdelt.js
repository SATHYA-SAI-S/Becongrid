/**
 * GDELT DOC 2.0 News Intelligence Client & Incident Extraction Engine
 */
const crypto = require('crypto');
const https = require('https');
const config = require('../config');
const { gdeltCache } = require('./cache');

// Tamil Nadu 38 Districts & Coordinates
const TN_DISTRICT_COORDS = {
  chennai: { name: "Chennai", lat: 13.0827, lon: 80.2707, precision: "city" },
  chengalpattu: { name: "Chengalpattu", lat: 12.6819, lon: 79.9888, precision: "city" },
  kancheepuram: { name: "Kancheepuram", lat: 12.8342, lon: 79.7036, precision: "city" },
  tiruvallur: { name: "Tiruvallur", lat: 13.1432, lon: 79.9079, precision: "city" },
  cuddalore: { name: "Cuddalore", lat: 11.7480, lon: 79.7714, precision: "city" },
  viluppuram: { name: "Viluppuram", lat: 11.9401, lon: 79.4861, precision: "city" },
  kallakurichi: { name: "Kallakurichi", lat: 11.7384, lon: 78.9639, precision: "city" },
  vellore: { name: "Vellore", lat: 12.9165, lon: 79.1325, precision: "city" },
  ranipet: { name: "Ranipet", lat: 12.9272, lon: 79.3330, precision: "city" },
  tirupathur: { name: "Tirupathur", lat: 12.4958, lon: 78.5678, precision: "city" },
  tiruvannamalai: { name: "Tiruvannamalai", lat: 12.2253, lon: 79.0747, precision: "city" },
  salem: { name: "Salem", lat: 11.6643, lon: 78.1460, precision: "city" },
  namakkal: { name: "Namakkal", lat: 11.2189, lon: 78.1674, precision: "city" },
  dharmapuri: { name: "Dharmapuri", lat: 12.1211, lon: 78.1582, precision: "city" },
  krishnagiri: { name: "Krishnagiri", lat: 12.5186, lon: 78.2137, precision: "city" },
  erode: { name: "Erode", lat: 11.3410, lon: 77.7172, precision: "city" },
  tiruppur: { name: "Tiruppur", lat: 11.1085, lon: 77.3411, precision: "city" },
  coimbatore: { name: "Coimbatore", lat: 11.0168, lon: 76.9558, precision: "city" },
  nilgiris: { name: "Nilgiris", lat: 11.4102, lon: 76.6950, precision: "city" },
  madurai: { name: "Madurai", lat: 9.9252, lon: 78.1198, precision: "city" },
  theni: { name: "Theni", lat: 10.0104, lon: 77.4768, precision: "city" },
  dindigul: { name: "Dindigul", lat: 10.3673, lon: 77.9803, precision: "city" },
  ramanathapuram: { name: "Ramanathapuram", lat: 9.3639, lon: 78.8395, precision: "city" },
  virudhunagar: { name: "Virudhunagar", lat: 9.5872, lon: 77.9514, precision: "city" },
  sivaganga: { name: "Sivaganga", lat: 9.8433, lon: 78.4809, precision: "city" },
  trichy: { name: "Tiruchirappalli", lat: 10.7905, lon: 78.7047, precision: "city" },
  karur: { name: "Karur", lat: 10.9601, lon: 78.0766, precision: "city" },
  perambalur: { name: "Perambalur", lat: 11.2342, lon: 78.8820, precision: "city" },
  ariyalur: { name: "Ariyalur", lat: 11.1401, lon: 79.0786, precision: "city" },
  thanjavur: { name: "Thanjavur", lat: 10.7870, lon: 79.1378, precision: "city" },
  nagapattinam: { name: "Nagapattinam", lat: 10.7656, lon: 79.8424, precision: "city" },
  mayiladuthurai: { name: "Mayiladuthurai", lat: 11.1075, lon: 79.6522, precision: "city" },
  tiruvarur: { name: "Tiruvarur", lat: 10.7725, lon: 79.6365, precision: "city" },
  pudukkottai: { name: "Pudukkottai", lat: 10.3797, lon: 78.8208, precision: "city" },
  tirunelveli: { name: "Tirunelveli", lat: 8.7139, lon: 77.7567, precision: "city" },
  tenkasi: { name: "Tenkasi", lat: 8.9594, lon: 77.3152, precision: "city" },
  thoothukudi: { name: "Thoothukudi", lat: 8.7642, lon: 78.1348, precision: "city" },
  kanyakumari: { name: "Kanniyakumari", lat: 8.0883, lon: 77.5385, precision: "city" }
};

// Prominent Towns Mapping to District
const TN_TOWNS_MAP = {
  hosur: { district: "krishnagiri", name: "Hosur", lat: 12.7410, lon: 77.8340 },
  ooty: { district: "nilgiris", name: "Udhagamandalam (Ooty)", lat: 11.4080, lon: 76.7020 },
  coonoor: { district: "nilgiris", name: "Coonoor", lat: 11.3530, lon: 76.7950 },
  kumbakonam: { district: "thanjavur", name: "Kumbakonam", lat: 10.9610, lon: 79.3850 },
  pollachi: { district: "coimbatore", name: "Pollachi", lat: 10.6620, lon: 77.0120 },
  sivakasi: { district: "virudhunagar", name: "Sivakasi", lat: 9.4530, lon: 77.7980 },
  karaikudi: { district: "sivaganga", name: "Karaikudi", lat: 10.0680, lon: 78.7840 },
  kovilpatti: { district: "thoothukudi", name: "Kovilpatti", lat: 9.1740, lon: 77.8680 },
  ambur: { district: "tirupathur", name: "Ambur", lat: 12.7885, lon: 78.7150 },
  velachery: { district: "chennai", name: "Velachery, Chennai", lat: 12.9780, lon: 80.2190 },
  tambaram: { district: "chengalpattu", name: "Tambaram", lat: 12.9250, lon: 80.1170 },
  ennore: { district: "chennai", name: "Ennore, Chennai", lat: 13.2180, lon: 80.3250 },
  rameswaram: { district: "ramanathapuram", name: "Rameswaram", lat: 9.2880, lon: 79.3130 },
  courtallam: { district: "tenkasi", name: "Courtallam", lat: 8.9320, lon: 77.2720 },
  kodaikanal: { district: "dindigul", name: "Kodaikanal", lat: 10.2340, lon: 77.4890 },
  yercaud: { district: "salem", name: "Yercaud", lat: 11.7750, lon: 78.2090 }
};

// Keyword sets for category classification
const CATEGORY_RULES = {
  natural_disaster: {
    weight: 1.2,
    keywords: ['flood', 'flooding', 'cyclone', 'inundation', 'rain', 'heavy rain', 'downpour', 'landslide', 'mudslide', 'storm surge', 'dam discharge', 'reservoir spill', 'வெள்ளம்', 'மழை', 'புயல்', 'நிலச்சரிவு']
  },
  accident_emergency: {
    weight: 1.1,
    keywords: ['fire', 'blaze', 'explosion', 'blast', 'collision', 'accident', 'building collapse', 'derailed', 'injured', 'casualty', 'தீ விபத்து', 'விபத்து', 'வெடிவிபத்து']
  },
  protest_disturbance: {
    weight: 1.0,
    keywords: ['protest', 'demonstration', 'strike', 'rally', 'road block', 'road roko', 'bandh', 'dharna', 'unrest', 'slogan', 'போராட்டம்', 'மறியல்', 'வேலைநிறுத்தம்']
  },
  infrastructure: {
    weight: 1.0,
    keywords: ['power cut', 'blackout', 'substation', 'road closed', 'highway blocked', 'traffic halt', 'bridge collapse', 'pipeline burst', 'water disruption', 'flight canceled', 'train diverted', 'மின் தடை', 'போக்குவரத்து நிறுத்தம்']
  },
  public_health: {
    weight: 1.0,
    keywords: ['dengue', 'malaria', 'fever camp', 'outbreak', 'epidemic', 'food poisoning', 'contamination', 'hospital bed shortage', 'infection cluster', 'காய்ச்சல்', 'தொற்றுநோய்']
  },
  environmental: {
    weight: 1.0,
    keywords: ['oil spill', 'toxic waste', 'chemical leak', 'sludge', 'gas leak', 'air pollution', 'effluent discharge', 'marine hazard', 'நச்சுக்கழிவு', 'எண்ணெய் கசிவு']
  },
  public_safety: {
    weight: 0.9,
    keywords: ['security threat', 'police alert', 'curfew', 'patrol', 'clash', 'violence', 'detained', 'suspicious boat', 'கடலோர பாதுகாப்பு', 'காவல்துறை']
  }
};

let lastGdeltCallTimestamp = 0;

class GdeltService {
  /**
   * Fetch articles from GDELT DOC 2.0 API with rate limiting
   */
  async fetchArticles({ query = 'Tamil Nadu (flood OR rain OR fire OR accident OR protest OR strike OR road OR hospital)', maxRecords = config.GDELT.MAX_RECORDS } = {}) {
    // Check in-memory cache
    const cacheKey = `gdelt_${query}_${maxRecords}`;
    const cached = gdeltCache.get(cacheKey);
    if (cached) {
      return { data: cached.value, fromCache: true };
    }

    // Enforce 6s spacing between calls to respect GDELT rate limits
    const now = Date.now();
    const elapsed = now - lastGdeltCallTimestamp;
    if (elapsed < config.GDELT.RATE_LIMIT_MS) {
      const waitTime = config.GDELT.RATE_LIMIT_MS - elapsed;
      await new Promise(res => setTimeout(res, waitTime));
    }
    lastGdeltCallTimestamp = Date.now();

    const encodedQuery = encodeURIComponent(query);
    const url = `${config.GDELT.API_URL}?query=${encodedQuery}&mode=artlist&maxrecords=${maxRecords}&format=json`;

    return new Promise((resolve) => {
      const req = https.get(url, {
        headers: {
          'User-Agent': config.GDELT.USER_AGENT
        },
        timeout: config.GDELT.TIMEOUT_MS
      }, (res) => {
        let rawData = '';
        res.on('data', chunk => rawData += chunk);
        res.on('end', () => {
          if (res.statusCode === 429) {
            console.warn('⚠️ GDELT DOC API: Rate limited (429). Using persisted and local incident intelligence.');
            return resolve({ data: [], error: 'Rate limited (429) by GDELT DOC API. Backing off.' });
          }

          if (res.statusCode !== 200) {
            return resolve({ data: [], error: `GDELT DOC API responded with HTTP ${res.statusCode}` });
          }

          try {
            const parsed = JSON.parse(rawData);
            const articles = parsed.articles || [];
            gdeltCache.set(cacheKey, articles);
            resolve({ data: articles, fromCache: false });
          } catch (jsonErr) {
            resolve({ data: [], error: 'Non-JSON response received from GDELT' });
          }
        });
      });

      req.on('error', (err) => {
        console.warn('⚠️ GDELT DOC API network error:', err.message);
        resolve({ data: [], error: err.message });
      });

      req.on('timeout', () => {
        req.destroy();
        resolve({ data: [], error: 'GDELT DOC API request timed out' });
      });
    });
  }

  /**
   * Generate SHA-256 fingerprint from title + publisher + date
   */
  generateFingerprint(title, publisher, dateStr) {
    const norm = `${(title || '').toLowerCase().trim()}|${(publisher || '').toLowerCase().trim()}|${dateStr || ''}`;
    return crypto.createHash('sha256').update(norm).digest('hex');
  }

  /**
   * Classify an article into one of the 7 incident categories
   */
  classifyArticle(title = '', snippet = '') {
    const text = `${title} ${snippet}`.toLowerCase();
    let bestCat = 'public_safety';
    let bestScore = 0;

    for (const [cat, rule] of Object.entries(CATEGORY_RULES)) {
      let matches = 0;
      for (const kw of rule.keywords) {
        if (text.includes(kw.toLowerCase())) {
          matches++;
        }
      }
      const score = matches * rule.weight;
      if (score > bestScore) {
        bestScore = score;
        bestCat = cat;
      }
    }

    return {
      category: bestCat,
      confidence: bestScore > 0 ? Math.min(0.65 + bestScore * 0.1, 0.95) : 0.5
    };
  }

  /**
   * Extract Tamil Nadu location from article text
   */
  extractLocation(title = '', snippet = '') {
    const text = `${title} ${snippet}`.toLowerCase();

    // Check specific towns first (higher precision)
    for (const [townKey, townData] of Object.entries(TN_TOWNS_MAP)) {
      if (text.includes(townKey)) {
        return {
          locationName: townData.name,
          city: townData.name,
          district: townData.district,
          lat: townData.lat,
          lon: townData.lon,
          precision: "exact"
        };
      }
    }

    // Check 38 district names
    for (const [distKey, distData] of Object.entries(TN_DISTRICT_COORDS)) {
      if (text.includes(distKey) || text.includes(distData.name.toLowerCase())) {
        return {
          locationName: `${distData.name} District`,
          city: distData.name,
          district: distKey,
          lat: distData.lat,
          lon: distData.lon,
          precision: "city"
        };
      }
    }

    // If only "tamil nadu" is mentioned without specific district
    if (text.includes('tamil nadu') || text.includes('tamilnadu')) {
      return {
        locationName: "Tamil Nadu State Overview",
        city: "Statewide",
        district: "all",
        lat: 10.8505,
        lon: 78.6856,
        precision: "state"
      };
    }

    return null;
  }

  /**
   * Normalize a raw GDELT article into BeaconGrid format
   */
  normalizeGdeltArticle(raw) {
    const url = raw.url;
    const title = raw.title || 'Untitled Incident Report';
    const publisher = raw.domain || raw.source || 'News Wire';
    const seendate = raw.seendate ? this.parseGdeltDate(raw.seendate) : new Date().toISOString();
    const fingerprint = this.generateFingerprint(title, publisher, seendate);
    const articleId = `art-${crypto.createHash('md5').update(url).digest('hex').substring(0, 12)}`;

    const { category, confidence } = this.classifyArticle(title, raw.summary || '');
    const locationInfo = this.extractLocation(title, raw.summary || '');

    return {
      articleId,
      url,
      title,
      publisher,
      language: raw.language || 'en',
      seendate,
      discoveredAt: new Date().toISOString(),
      summary: raw.summary || title,
      fingerprint,
      category,
      classificationConfidence: confidence,
      locationInfo,
      status: 'extracted'
    };
  }

  /**
   * Parse GDELT compact date format (YYYYMMDDTHHMMSSZ or YYYYMMDDHHMMSS)
   */
  parseGdeltDate(gdeltDateStr) {
    try {
      if (!gdeltDateStr) return new Date().toISOString();
      const cleaned = gdeltDateStr.replace(/[^0-9]/g, '');
      if (cleaned.length >= 14) {
        const year = cleaned.substring(0, 4);
        const month = cleaned.substring(4, 6);
        const day = cleaned.substring(6, 8);
        const hour = cleaned.substring(8, 10);
        const min = cleaned.substring(10, 12);
        const sec = cleaned.substring(12, 14);
        return new Date(`${year}-${month}-${day}T${hour}:${min}:${sec}Z`).toISOString();
      }
      return new Date().toISOString();
    } catch (e) {
      return new Date().toISOString();
    }
  }
}

const gdeltService = new GdeltService();

module.exports = {
  gdeltService,
  TN_DISTRICT_COORDS,
  TN_TOWNS_MAP,
  CATEGORY_RULES
};
