// Configuration and taxonomy constants

export const CONFIG = {
  // Default coordinates: Central location fallback (London Trafalgar Sq or NYC Central Park)
  // Used before explicit user geolocation or search
  DEFAULT_CENTER: [51.5074, -0.1278],
  DEFAULT_ZOOM: 14,
  DEFAULT_RADIUS_METERS: 3500,
  MAX_RADIUS_METERS: 10000,
  MIN_RADIUS_METERS: 500,

  // Map Tile Provider: OpenStreetMap Standard with proper attribution
  TILE_URL: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
  TILE_ATTRIBUTION: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap contributors</a>',

  // API Endpoints
  API_RESOURCES: '/api/resources',
  API_GEOCODE: '/api/geocode',
  API_ROUTE: '/api/route',
  API_HEALTH: '/api/health',

  // Categories definition
  CATEGORIES: [
    {
      id: 'hospital',
      label: 'Hospitals & ER',
      icon: 'cross',
      color: '#e11d48',
      bgColor: '#ffe4e6',
      description: 'Hospitals, emergency departments, and trauma centers'
    },
    {
      id: 'clinic',
      label: 'Clinics & Urgent Care',
      icon: 'stethoscope',
      color: '#0d9488',
      bgColor: '#ccfbf1',
      description: 'Walk-in clinics, outpatient centers, general practitioners'
    },
    {
      id: 'pharmacy',
      label: 'Pharmacies',
      icon: 'pill',
      color: '#059669',
      bgColor: '#d1fae5',
      description: 'Pharmacies, chemists, and dispensaries'
    },
    {
      id: 'police',
      label: 'Police Stations',
      icon: 'shield',
      color: '#2563eb',
      bgColor: '#dbeafe',
      description: 'Police stations and law enforcement posts'
    },
    {
      id: 'fire_station',
      label: 'Fire Stations',
      icon: 'flame',
      color: '#ea580c',
      bgColor: '#ffedd5',
      description: 'Fire and rescue stations'
    },
    {
      id: 'shelter',
      label: 'Shelters',
      icon: 'home',
      color: '#d97706',
      bgColor: '#fef3c7',
      description: 'Emergency shelters, severe weather shelters, homeless shelters'
    },
    {
      id: 'drinking_water',
      label: 'Drinking Water',
      icon: 'droplet',
      color: '#0284c7',
      bgColor: '#e0f2fe',
      description: 'Public drinking water fountains and refill points'
    },
    {
      id: 'food_bank',
      label: 'Food Banks',
      icon: 'utensils',
      color: '#7c3aed',
      bgColor: '#ede9fe',
      description: 'Food banks, pantries, and soup kitchens'
    },
    {
      id: 'toilets',
      label: 'Public Toilets',
      icon: 'bath',
      color: '#6366f1',
      bgColor: '#e0e7ff',
      description: 'Public restrooms and sanitary facilities'
    }
  ]
};

export function getCategoryById(id) {
  return CONFIG.CATEGORIES.find(c => c.id === id) || {
    id: id || 'other',
    label: id || 'Emergency Resource',
    icon: 'map-pin',
    color: '#475569',
    bgColor: '#f1f5f9'
  };
}
