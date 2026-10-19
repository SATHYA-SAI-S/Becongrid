/**
 * MongoDB Connection & Index Management
 */
const { MongoClient } = require('mongodb');
const config = require('../config');

let client = null;
let db = null;
let connected = false;
let connectionAttempted = false;

async function connectToMongo(uri = config.MONGODB_URI, dbName = config.MONGODB_DB_NAME) {
  if (connected && db) return db;
  connectionAttempted = true;

  try {
    client = new MongoClient(uri, {
      serverSelectionTimeoutMS: 2000,
      connectTimeoutMS: 2000
    });

    await client.connect();
    db = client.db(dbName);
    connected = true;
    console.log(`✓ Connected to MongoDB database: ${dbName}`);

    // Create required indexes
    await ensureIndexes(db);
    return db;
  } catch (err) {
    connected = false;
    db = null;
    console.warn(`⚠️ MongoDB connection unavailable (${err.message}). BeaconGrid will run in resilient In-Memory Geo Store mode.`);
    return null;
  }
}

async function ensureIndexes(database) {
  try {
    const articlesCol = database.collection('articles');
    const incidentsCol = database.collection('incidents');

    // Articles indexes
    await articlesCol.createIndex({ articleId: 1 }, { unique: true });
    await articlesCol.createIndex({ url: 1 }, { unique: true });
    await articlesCol.createIndex({ fingerprint: 1 });
    await articlesCol.createIndex({ category: 1, seendate: -1 });

    // Incidents indexes (including 2dsphere for geospatial queries)
    await incidentsCol.createIndex({ location: '2dsphere' });
    await incidentsCol.createIndex({ incidentId: 1 }, { unique: true });
    await incidentsCol.createIndex({ district: 1, category: 1 });
    await incidentsCol.createIndex({ verificationStatus: 1 });
    await incidentsCol.createIndex({ lastReportedAt: -1 });

    console.log('✓ MongoDB 2dsphere and unique indexes verified successfully.');
  } catch (indexErr) {
    console.warn('⚠️ Warning creating MongoDB indexes:', indexErr.message);
  }
}

function getDb() {
  return connected ? db : null;
}

function isConnected() {
  return connected;
}

async function closeConnection() {
  if (client) {
    try {
      await client.close();
    } catch (e) {}
    client = null;
    db = null;
    connected = false;
  }
}

module.exports = {
  connectToMongo,
  getDb,
  isConnected,
  closeConnection
};
