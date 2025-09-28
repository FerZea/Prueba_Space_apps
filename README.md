# 🛰️ Meteor Impact App

Visualizador de impactos de meteoritos usando **FastAPI (backend)** + **React + Vite + TypeScript + Cesium (frontend)**, con datos de **NASA NEO** y **USGS**.

---

## 📦 Estructura del repositorio

```
meteor-app/
├─ backend/                              # API y lógica de simulación
│  ├─ app/
│  │  ├─ api/                            # Endpoints FastAPI
│  │  ├─ clients/                        # Integraciones externas (NASA, USGS)
│  │  ├─ domain/                         # Modelos y cálculos físicos (NumPy)
│  │  ├─ services/                       # Orquestación de lógica
│  │  └─ __init__.py
│  ├─ main.py                            # Punto de entrada FastAPI
│  ├─ requirements.txt                   # Dependencias Python
│  ├─ .env                               # ⚠️ Variables reales (NO subir, está en .gitignore)
│  └─ .env.example                       # ✅ Plantilla para el repo (sí subir)
│
├─ frontend/                             # UI en React + Vite + Cesium
│  ├─ public/
│  │  └─ cesium/                         # Assets copiados desde node_modules/cesium/Build/Cesium
│  ├─ src/
│  │  ├─ api/                            # Cliente HTTP al backend
│  │  ├─ components/                     # Componentes React (Globo, Controles)
│  │  ├─ App.tsx                         # Layout principal (sidebar + globo)
│  │  ├─ main.tsx                        # Punto de entrada Vite
│  │  └─ styles.css                      # Estilos globales
│  ├─ .env.development                   # ⚠️ Local (no subir)
│  ├─ .env.example                       # ✅ Plantilla (sí subir)
│  ├─ package.json
│  ├─ vite.config.ts
│  └─ index.html
│
├─ .gitignore                            # Ignora venv, node_modules, .env*
└─ README.md                             # Documentación principal
```

> 📌 **Regla**: `.env` y `.env.development` son privados → **no suben**.  
> En cambio `.env.example` sí se sube como **plantilla** para guiar al resto del equipo.

---

## 🔑 Variables de entorno

### Backend (`backend/.env`)

Debes crear un archivo `.env` dentro de la carpeta `backend/` con la configuración siguiente:

```env
# NASA API Key (obligatoria, consíguela en https://api.nasa.gov)
NASA_API_KEY=tu_api_key_aqui

# USGS (opcional, solo si necesitas endpoints privados)
USGS_USERNAME=
USGS_PASSWORD=
```

⚠️ **No subas tu `.env` real a GitHub.** El archivo `.env` ya está en `.gitignore`.

También debes crear un archivo de plantilla `backend/.env.example` con el contenido:

```env
NASA_API_KEY=your_api_key_here
USGS_USERNAME=
USGS_PASSWORD=
```

### Frontend (`frontend/.env.development`)

Ejemplo de configuración para desarrollo:

```env
VITE_CESIUM_ION_TOKEN=TU_TOKEN_CESIUM_ION
VITE_API_BASE=http://localhost:8000/api
```

El archivo de plantilla `frontend/.env.example` debe contener:

```env
VITE_CESIUM_ION_TOKEN=your_cesium_token_here
VITE_API_BASE=http://localhost:8000/api
```

---

## 🌐 Fuentes de APIs y librerías externas

- **NASA NEO API** → [https://api.nasa.gov/](https://api.nasa.gov/)  
- **Cesium Ion (globo 3D)** → [https://cesium.com/platform/cesium-ion/](https://cesium.com/platform/cesium-ion/)  
- **USGS ScienceBase (Python client)** → [https://github.com/DOI-USGS/sciencebasepy](https://github.com/DOI-USGS/sciencebasepy)  

---

## ⬇️ Clonar el repositorio

```bash
# Clonar
git clone https://github.com/FerZea/Prueba_Space_apps.git
cd meteor-app

# Ver ramas disponibles
git branch -a

# Cambiar a main
git checkout main
```
---

## 🛠️ Instalación

### Backend (FastAPI)

#### Linux / macOS
1. Crear entorno virtual e instalar dependencias:
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
2. Probar:  
- Health: http://localhost:8000/api/health  
- Docs: http://localhost:8000/docs  

#### Windows

**PowerShell**
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
Copy-Item .env.example .env
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```

**CMD**
```bat
cd backend
python -m venv .venv
.\.venv\Scriptsctivate.bat
copy .env.example .env
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```

**Git Bash**
```bash
cd backend
python -m venv .venv
source .venv/Scripts/activate
cp .env.example .env
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```

---

### Frontend (React + Vite + Cesium)

#### Linux / macOS
```bash
cd frontend
cp .env.example .env.development
npm install
npm run dev
# abre http://localhost:5173
```

#### Windows (PowerShell / CMD / Git Bash)

**PowerShell**
```powershell
cd frontend
Copy-Item .env.example .env.development
npm install
npm run dev
```

**CMD**
```bat
cd frontend
copy .env.example .env.development
npm install
npm run dev
```

**Git Bash**
```bash
cd frontend
cp .env.example .env.development
npm install
npm run dev
```

> En `src/main.tsx` debe existir:  
> `import 'cesium/Build/Cesium/Widgets/widgets.css';`

---

## 🧪 Flujo de trabajo con Git

```bash
# crear rama
git checkout main
git pull origin main
git checkout -b feat/<nombre>

# commit y push
git add .
git commit -m "feat: descripción clara"
git push -u origin feat/<nombre>

# abrir Pull Request en GitHub (base: main, compare: tu rama)
```

Si el remoto tiene cambios: `git pull --rebase origin main` y resuelve conflictos.

---

## 📚 Dependencias principales

**Backend**
- fastapi, uvicorn, httpx (NASA)
- sciencebasepy (USGS)
- numpy, pandas, shapely, pyproj
- python-dotenv / pydantic-settings
- pytest (dev)

**Frontend**
- react, vite, typescript
- cesium (globo 3D)
- shx (copiado cross‑platform de assets Cesium)

---

## 🐛 Problemas comunes

- **`uvicorn: command not found`** → activa venv o usa `python -m uvicorn`.  
- **Globo de Cesium pequeño/negro** → falta `widgets.css` o `public/cesium`.  
- **CORS** → el proxy de Vite apunta a `http://localhost:8000` (cambia `VITE_API_BASE` si es necesario).  
- **Windows - error de scripts al activar venv** → ejecutar:  
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ```

---

## 🧭 Diseño de capas (resumen)

- `api/` → recibe requests y valida (Pydantic).  
- `services/` → orquesta: llama a `clients/` y `domain/`.  
- `domain/physics/` → cálculos con NumPy.  
- `clients/` → acceso a APIs externas (NASA/USGS).

---
