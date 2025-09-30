// frontend/src/api/client.ts

import type {
  FeatureCollection,
  Geometry,
  GeoJsonProperties,
} from 'geojson'

const API_BASE = import.meta.env.VITE_API_BASE || '/api'

// Deben coincidir con los schemas del backend
export interface SimInput {
  lat: number
  lon: number
  diameter_m: number
  velocity_kms: number
}

export interface SimResult {
  geojson: GeoJSON.FeatureCollection
  energy_mt: number
  damage_radii_km: {
    severe: number
    moderate: number
    light: number
  }
}

export async function simulateImpact(params: SimInput): Promise<SimResult> {
  const r = await fetch(`${API_BASE}/simulate/impact`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(params),
  })

  if (!r.ok) {
    throw new Error(`API error ${r.status}`)
  }

  return r.json()
}
