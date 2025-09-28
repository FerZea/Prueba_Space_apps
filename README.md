# 🚀 Meteor Impact App

Proyecto web para visualizar impactos de meteoritos usando **FastAPI (backend)** + **React + Vite + TypeScript + Cesium (frontend)**.  
Consume datos de **NASA NEO** y **USGS**.

---

## 📂 Estructura
```
meteor-app/
│── backend/                         # API en FastAPI (Python)
│   ├── app/
│   │   ├── api/                     # Endpoints REST
│   │   │   ├── __init__.py
│   │   │   └── routes_simulation.py # Ruta POST /simulate/impact
│   │   ├── clients/                 # Clientes a APIs externas
│   │   │   ├── __init__.py
│   │   │   ├── nasa_neo.py          # Cliente NASA NEO (httpx)
│   │   │   └── usgs_client.py       # Cliente USGS (sciencebasepy)
│   │   ├── domain/                  # Modelos y lógica de negocio
│   │   │   ├── __init__.py
│   │   │   ├── schemas.py           # Pydantic: entradas/salidas
│   │   │   └── physics/
│   │   │       ├── __init__.py
│   │   │       └── impact.py        # Cálculos físicos (NumPy)
│   │   ├── services/                # Orquestación de lógica
│   │   │   ├── __init__.py
│   │   │   └── simulation_service.py# Llama a domain + clients
│   │   └── __init__.py
│   ├── main.py                      # Punto de entrada FastAPI
│   ├── requirements.txt             # Dependencias Python
│   └── .venv/                       # Entorno virtual local
│
│── frontend/                        # UI en React + Vite + Cesium
│   ├── public/
│   │   └── cesium/                  # Assets de Cesium (copiados de node_modules)
│   ├── src/
│   │   ├── api/
│   │   │   └── client.ts            # Cliente HTTP al backend
│   │   ├── components/
│   │   │   ├── CesiumGlobe.tsx      # Renderiza el globo y carga GeoJSON
│   │   │   └── Controls.tsx         # Formulario de simulación
│   │   ├── App.tsx                  # Layout principal (sidebar + globo)
│   │   ├── main.tsx                 # Punto de entrada Vite
│   │   └── styles.css               # Estilos globales
│   ├── .env.example                 # Variables de entorno (plantilla)
│   ├── package.json                 # Scripts npm (dev/build)
│   ├── vite.config.ts               # Configuración Vite (proxy, Cesium)
│   └── index.html                   # HTML base
│
│── README.md                        # Documentación principal
│── .gitignore                       # Ignorar venv, node_modules, envs, etc.

```

---

## 🛠️ Requisitos
- Git
- Python 3.10+
- Node.js 18+
- npm

---

## 🔑 Variables de entorno

En `frontend/.env.development`(crealo en la otra seccion o edita .env.example para poner el token):

El token se consigue en: https://cesium.com/platform/cesium-ion/

```
VITE_CESIUM_ION_TOKEN=TU_TOKEN_CESIUM_ION
VITE_API_BASE=http://localhost:8000/api
```

⚠️ **Nunca subas tu token real a GitHub.**  
El archivo `.env` ya está en `.gitignore`.

---

## 🐍 Backend (FastAPI)

### Linux / Mac
```bash
cd backend
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Windows (PowerShell)
```powershell
cd backend
python -m venv .venv

# Activar venv
.\.venv\Scripts\Activate.ps1
# Si ves error de ejecución de scripts:
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
python -m uvicorn app.main:app --reload --port 8000
```

Prueba:  
👉 [http://localhost:8000/api/health](http://localhost:8000/api/health) → `{ "ok": true }`  
👉 [http://localhost:8000/docs](http://localhost:8000/docs) → Swagger UI

---

## 💻 Frontend (React + TS + Cesium)

### Linux / Mac
```bash
cd frontend
cp .env.example .env.development
npm install
npm run dev
```

### Windows (PowerShell / CMD / Git Bash)
```powershell
cd frontend
# PowerShell
Copy-Item .env.example .env.development
# CMD clásico: copy .env.example .env.development
# Git Bash: cp .env.example .env.development

# Instalar dependencias (usa shx para copiar assets de Cesium en Windows)
npm install
npm run dev
```

> ⚠️ Asegúrate de que en `src/main.tsx` exista:
> ```ts
> import 'cesium/Build/Cesium/Widgets/widgets.css';
> ```

Abrir 👉 [http://localhost:5173](http://localhost:5173)

---

## 🌳 Flujo de trabajo con Git

1. Clonar el repo:
   ```bash
   git clone https://github.com/TU_USUARIO/meteor-app.git
   cd meteor-app
   ```

2. Crear una rama de trabajo:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feat/<nombre-feature>
   ```

3. Hacer cambios, luego:
   ```bash
   git add .
   git commit -m "feat: descripción corta"
   git push -u origin feat/<nombre-feature>
   ```

4. Abrir un Pull Request en GitHub (base: `main`, compare: tu rama).

5. Al aprobarse, sincronizar:
   ```bash
   git checkout main
   git pull origin main
   ```

---

## 👥 Roles sugeridos
- **Backend**
  - API NASA/USGS
  - Servicios y lógica de simulación
  - Integración con frontend
- **Frontend**
  - Interfaz React + Cesium
  - Panel de controles (formulario lat/lon/velocidad/diámetro)
  - Visualización GeoJSON en el globo

---

## ⚠️ Problemas comunes
- **`uvicorn: command not found`**  
  - Activa venv e instala requirements.
  - En Windows usa `python -m uvicorn` en vez de `uvicorn` directo.

- **Globo de Cesium se ve pequeño**  
  - Falta importar los estilos base:
    ```ts
    import 'cesium/Build/Cesium/Widgets/widgets.css';
    ```

- **No carga el token**  
  - Confirmar que está en `.env.development` y empieza con `VITE_`.

---
