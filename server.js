/**
 * BeaconGrid Server: Node.js + Express Application
 * Emergency Resource Map & GDELT News Intelligence System for Tamil Nadu
 */
const express = require('express');
const cors = require('cors');
const path = require('path');
const config = require('./server/config');
const apiRoutes = require('./server/routes/api');
const { connectToMongo, closeConnection } = require('./server/db/mongo');
const { ingestionPipeline } = require('./server/services/ingestion');

const app = express();

// Middlewares
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Static file hosting
app.use(express.static(config.STATIC_DIR));

// Page Routes
app.get('/', (req, res) => {
  res.sendFile(config.INDEX_FILE);
});

app.get('/index.html', (req, res) => {
  res.sendFile(config.INDEX_FILE);
});

app.get('/map', (req, res) => {
  res.sendFile(config.MAP_FILE);
});

app.get('/map.html', (req, res) => {
  res.sendFile(config.MAP_FILE);
});

// API Routes
app.use('/api', apiRoutes);

// Fallback 404 handler for API routes
app.use('/api/*', (req, res) => {
  res.status(404).json({ detail: 'API route not found' });
});

// Global error handler
app.use((err, req, res, next) => {
  console.error('Unhandled server error:', err);
  res.status(500).json({ detail: 'Internal server error', error: err.message });
});

// Start Server and Database Connection
let server = null;
let ingestionTimer = null;

async function startServer() {
  // Try connecting to MongoDB (falls back to resilient In-Memory store if not reachable)
  await connectToMongo().catch(err => {
    console.warn('MongoDB startup check completed with fallback mode.');
  });

  server = app.listen(config.PORT, config.HOST, () => {
    console.log(`=======================================================`);
    console.log(`⚡ BeaconGrid Node.js Server running at: http://${config.HOST}:${config.PORT}/`);
    console.log(`🗺️ Live Map Dashboard available at: http://${config.HOST}:${config.PORT}/map.html`);
    console.log(`📰 GDELT News Intelligence Layer initialized`);
    console.log(`=======================================================`);
  });

  // Scheduled background ingestion (every 15 minutes)
  ingestionTimer = setInterval(() => {
    ingestionPipeline.run({ manual: false }).catch(err => {
      console.warn('Background ingestion cycle notice:', err.message);
    });
  }, config.INGESTION_INTERVAL_MS);

  return server;
}

// Graceful termination
async function shutdown() {
  console.log('\nGracefully shutting down BeaconGrid server...');
  if (ingestionTimer) clearInterval(ingestionTimer);
  if (server) {
    server.close(() => {
      console.log('HTTP server closed.');
    });
  }
  await closeConnection();
  process.exit(0);
}

process.on('SIGINT', shutdown);
process.on('SIGTERM', shutdown);

// Auto-start when executed directly
if (require.main === module) {
  startServer().catch(err => {
    console.error('Fatal server startup error:', err);
    process.exit(1);
  });
}

module.exports = { app, startServer, shutdown };
