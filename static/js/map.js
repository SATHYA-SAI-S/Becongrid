// Leaflet Map Controller with Marker Clustering and Custom Pins

import { CONFIG, getCategoryById } from './config.js';
import { createPinIconHtml } from './icons.js';

let mapInstance = null;
let clusterGroup = null;
let markerMap = new Map(); // id -> L.Marker
let userLocationMarker = null;
let searchRadiusCircle = null;
let lastQueriedCenter = null;

let onMarkerSelectedCallback = null;
let onAreaMovedCallback = null;

export function initMap(elementId, { onMarkerSelected, onAreaMoved }) {
  onMarkerSelectedCallback = onMarkerSelected;
  onAreaMovedCallback = onAreaMoved;

  // Initialize Leaflet map
  mapInstance = L.map(elementId, {
    center: CONFIG.DEFAULT_CENTER,
    zoom: CONFIG.DEFAULT_ZOOM,
    zoomControl: false // We will place zoom control cleanly
  });

  // Clean zoom control on bottom right
  L.control.zoom({ position: 'bottomright' }).addTo(mapInstance);

  // Add OSM tile layer with proper attribution
  L.tileLayer(CONFIG.TILE_URL, {
    attribution: CONFIG.TILE_ATTRIBUTION,
    maxZoom: 19,
    minZoom: 3
  }).addTo(mapInstance);

  // Initialize MarkerClusterGroup
  clusterGroup = L.markerClusterGroup({
    showCoverageOnHover: false,
    maxClusterRadius: 45,
    iconCreateFunction: function (cluster) {
      const count = cluster.getChildCount();
      return L.divIcon({
        html: `<div class="marker-cluster-emergency"><div>${count}</div></div>`,
        className: 'custom-cluster-icon',
        iconSize: L.point(40, 40)
      });
    }
  });
  mapInstance.addLayer(clusterGroup);

  // Listen to map moveend to trigger "Search this area"
  mapInstance.on('moveend', () => {
    if (!lastQueriedCenter) return;
    const currentCenter = mapInstance.getCenter();
    const distMoved = currentCenter.distanceTo(lastQueriedCenter);

    // If moved more than 600m from last query center, suggest searching this area
    if (distMoved > 600 && onAreaMovedCallback) {
      onAreaMovedCallback(currentCenter);
    }
  });

  return mapInstance;
}

export function getLeafletMapInstance() {
  return mapInstance;
}

export function getMapCenter() {
  if (!mapInstance) return { lat: CONFIG.DEFAULT_CENTER[0], lon: CONFIG.DEFAULT_CENTER[1] };
  const center = mapInstance.getCenter();
  return { lat: center.lat, lon: center.lng };
}

/**
 * Render resource pins into the cluster group
 */
export function renderResourceMarkers(resources = [], selectedId = null) {
  if (!clusterGroup) return;

  clusterGroup.clearLayers();
  markerMap.clear();

  resources.forEach(item => {
    const cat = getCategoryById(item.category);
    const isSelected = item.id === selectedId;

    const icon = L.divIcon({
      html: createPinIconHtml(cat, isSelected),
      className: '',
      iconSize: [32, 38],
      iconAnchor: [16, 38],
      popupAnchor: [0, -36]
    });

    const marker = L.marker([item.lat, item.lon], { icon, title: item.name });

    marker.on('click', () => {
      if (onMarkerSelectedCallback) {
        onMarkerSelectedCallback(item);
      }
    });

    clusterGroup.addLayer(marker);
    markerMap.set(item.id, { marker, item, category: cat });
  });
}

/**
 * Visually highlight the selected pin marker
 */
export function highlightMarker(id) {
  markerMap.forEach((entry, itemId) => {
    const isTarget = itemId === id;
    const newIcon = L.divIcon({
      html: createPinIconHtml(entry.category, isTarget),
      className: '',
      iconSize: [32, 38],
      iconAnchor: [16, 38]
    });
    entry.marker.setIcon(newIcon);

    if (isTarget) {
      // If marker is inside a cluster, zoom to it or open cluster
      clusterGroup.zoomToShowLayer(entry.marker, () => {
        mapInstance.panTo([entry.item.lat, entry.item.lon], { animate: true });
      });
    }
  });
}

/**
 * Set user location radar marker
 */
export function setUserLocation(lat, lon) {
  if (!mapInstance) return;

  if (userLocationMarker) {
    userLocationMarker.setLatLng([lat, lon]);
  } else {
    const userRadarIcon = L.divIcon({
      html: '<div class="user-radar-pin"></div>',
      className: '',
      iconSize: [20, 20],
      iconAnchor: [10, 10]
    });
    userLocationMarker = L.marker([lat, lon], {
      icon: userRadarIcon,
      zIndexOffset: 1000,
      title: 'Your Location'
    }).addTo(mapInstance);
  }
}

/**
 * Set the center and radius boundary circle for the current search
 */
export function setSearchCenter(lat, lon, radiusMeters) {
  if (!mapInstance) return;
  lastQueriedCenter = L.latLng(lat, lon);

  if (searchRadiusCircle) {
    searchRadiusCircle.setLatLng([lat, lon]);
    searchRadiusCircle.setRadius(radiusMeters);
  } else {
    searchRadiusCircle = L.circle([lat, lon], {
      radius: radiusMeters,
      color: '#2563eb',
      weight: 1.5,
      dashArray: '6, 6',
      fillColor: '#3b82f6',
      fillOpacity: 0.05,
      interactive: false
    }).addTo(mapInstance);
  }
}

export function panTo(lat, lon, zoom = 15) {
  if (!mapInstance) return;
  mapInstance.setView([lat, lon], zoom, { animate: true });
}
