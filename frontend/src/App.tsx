import { useState } from 'react'
import CesiumGlobe from './components/CesiumGlobe'
import Controls from './components/Controls'
import { simulateImpact } from './api/client'

export default function App() {
  const [geojson, setGeojson] = useState<any | null>(null)
  const [busy, setBusy] = useState(false)

  const run = async (p: { lat: number; lon: number; diameter_m: number; velocity_kms: number }) => {
    setBusy(true)
    try {
      const data = await simulateImpact(p)
      setGeojson(data)
    } finally {
      setBusy(false)
    }
  }

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '320px 1fr', height: '100vh' }}>
      <Controls onRun={run} busy={busy} />
      <CesiumGlobe geojson={geojson} />
    </div>
  )
}
