/**
 * Ingestion Pipeline: GDELT -> Normalization -> Classification -> Deduplication -> MongoDB
 */
const crypto = require('crypto');
const { gdeltService } = require('./gdelt');
const { storage } = require('../db/storage');

let isIngesting = false;
let ingestionStats = {
  lastRunAt: new Date().toISOString(),
  lastSuccessAt: new Date().toISOString(),
  lastStatus: "idle",
  totalRuns: 0,
  discovered: 0,
  accepted: 0,
  rejected: 0,
  updated: 0,
  lastError: null
};

class IngestionPipeline {
  /**
   * Run the full ingestion cycle
   */
  async run({ manual = false } = {}) {
    if (isIngesting) {
      return {
        status: "already_running",
        message: "An incident intelligence ingestion cycle is already in progress.",
        stats: ingestionStats
      };
    }

    isIngesting = true;
    ingestionStats.lastRunAt = new Date().toISOString();
    ingestionStats.lastStatus = "running";
    ingestionStats.totalRuns++;
    ingestionStats.lastError = null;

    let discoveredCount = 0;
    let acceptedCount = 0;
    let rejectedCount = 0;
    let updatedCount = 0;

    try {
      console.log(`[Ingestion] Starting ${manual ? 'manual' : 'scheduled'} GDELT intelligence cycle for Tamil Nadu...`);
      
      const { data: rawArticles, error: fetchError } = await gdeltService.fetchArticles();
      
      if (fetchError) {
        ingestionStats.lastError = fetchError;
        ingestionStats.lastStatus = "completed_with_upstream_notice";
        console.warn(`[Ingestion] Upstream note: ${fetchError}`);
        // Return existing storage state gracefully
        return {
          status: "completed_with_upstream_notice",
          notice: fetchError,
          stats: ingestionStats
        };
      }

      discoveredCount = rawArticles.length;

      for (const raw of rawArticles) {
        if (!raw.url) {
          rejectedCount++;
          continue;
        }

        const normalized = gdeltService.normalizeGdeltArticle(raw);

        // Check if article is geographically relevant to Tamil Nadu
        if (!normalized.locationInfo) {
          rejectedCount++;
          continue;
        }

        // Check deduplication in database
        const existingArticle = await storage.findArticleByUrlOrFingerprint(normalized.url, normalized.fingerprint);
        if (existingArticle) {
          // Already ingested
          continue;
        }

        acceptedCount++;

        // Find or create matching incident (corroboration)
        const incident = await this.corroborateOrCreateIncident(normalized);
        normalized.incidentId = incident.incidentId;

        // Persist article
        await storage.upsertArticle(normalized);
        updatedCount++;
      }

      ingestionStats.lastSuccessAt = new Date().toISOString();
      ingestionStats.lastStatus = "success";
      ingestionStats.discovered += discoveredCount;
      ingestionStats.accepted += acceptedCount;
      ingestionStats.rejected += rejectedCount;
      ingestionStats.updated += updatedCount;

      console.log(`[Ingestion] Cycle complete. Discovered: ${discoveredCount}, Accepted: ${acceptedCount}, Rejected: ${rejectedCount}, Updated: ${updatedCount}`);

      return {
        status: "success",
        cycleStats: {
          discovered: discoveredCount,
          accepted: acceptedCount,
          rejected: rejectedCount,
          updated: updatedCount
        },
        stats: ingestionStats
      };
    } catch (err) {
      ingestionStats.lastStatus = "failed";
      ingestionStats.lastError = err.message;
      console.error('[Ingestion] Ingestion cycle error:', err);
      return {
        status: "error",
        error: err.message,
        stats: ingestionStats
      };
    } finally {
      isIngesting = false;
    }
  }

  /**
   * Corroborate an article into an existing incident or create a new one
   */
  async corroborateOrCreateIncident(article) {
    const loc = article.locationInfo;
    const category = article.category;
    const recentIncidents = await storage.queryIncidents({
      category: category,
      district: loc.district,
      hours: 48,
      limit: 20
    });

    // Check if an existing incident matches location & category
    let matched = null;
    for (const inc of recentIncidents) {
      // Distance check or district + category match
      if (inc.district === loc.district && inc.category === category) {
        matched = inc;
        break;
      }
    }

    if (matched) {
      // Corroborate existing incident
      const alreadyHasSource = matched.sources.some(s => s.url === article.url);
      if (!alreadyHasSource) {
        matched.sources.push({
          publisher: article.publisher,
          url: article.url,
          title: article.title
        });
        matched.articleIds.push(article.articleId);
        matched.sourceCount = matched.sources.length;
        matched.lastReportedAt = article.seendate;

        // Elevate status if multiple independent sources report it
        const uniquePublishers = new Set(matched.sources.map(s => s.publisher.toLowerCase()));
        if (uniquePublishers.size >= 2 && matched.verificationStatus === 'unverified') {
          matched.verificationStatus = 'corroborated';
          matched.confidence = Math.min(0.85 + uniquePublishers.size * 0.05, 0.98);
        }

        await storage.upsertIncident(matched);
      }
      return matched;
    } else {
      // Create new incident
      const incidentId = `inc-${loc.district.substring(0, 3)}-${crypto.randomBytes(4).toString('hex')}`;
      const newIncident = {
        incidentId,
        category: category,
        title: article.title,
        description: article.summary,
        location: {
          type: "Point",
          coordinates: [loc.lon, loc.lat] // [longitude, latitude]
        },
        locationName: loc.locationName,
        city: loc.city,
        district: loc.district,
        locationPrecision: loc.precision,
        eventTime: article.seendate,
        firstReportedAt: article.seendate,
        lastReportedAt: article.seendate,
        updatedAt: new Date().toISOString(),
        articleIds: [article.articleId],
        sourceCount: 1,
        sources: [
          {
            publisher: article.publisher,
            url: article.url,
            title: article.title
          }
        ],
        verificationStatus: "unverified", // Starts unverified per safety rules
        confidence: article.classificationConfidence || 0.70,
        eventStatus: "ongoing"
      };

      await storage.upsertIncident(newIncident);
      return newIncident;
    }
  }

  getStatus() {
    return {
      isIngesting,
      ...ingestionStats
    };
  }
}

const ingestionPipeline = new IngestionPipeline();

module.exports = {
  ingestionPipeline
};
