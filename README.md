# 🧩 Staffy | Easy Staff Solutions

**Staffy** es una plataforma web de gestión de empleados, tareas y perfiles diseñada para pequeñas y medianas empresas. Permite centralizar operaciones de RRHH y coordinación interna en una interfaz moderna, rápida y adaptable.

---

## 🚀 Características principales

- Gestión de empleados, tareas y contactos
- Asignación de tareas por rol o persona
- Roles personalizados y perfiles de usuario
- Interfaz responsive y accesible

---

## 🛠️ Tecnologías utilizadas

### 🐍 Backend (Django)

- [**Django 5.2**](https://docs.djangoproject.com/en/5.2/) – Framework principal del backend
- [**django-cors-headers**](https://pypi.org/project/django-cors-headers/) – Manejo de CORS entre backend y frontend
- [**django-colorfield**](https://pypi.org/project/django-colorfield/) – Campos de color en modelos/admin
- [**Faker**](https://faker.readthedocs.io/) – Generación de datos falsos (útil para pruebas)
- [**pytest**](https://docs.pytest.org/) + [**pytest-django**](https://pytest-django.readthedocs.io/) – Testing automatizado del backend
- [**model-bakery**](https://model-bakery.readthedocs.io/) – Factory para crear instancias en pruebas
- Base de datos: **PostgreSQL** en producción / **SQLite** en desarrollo

### 🌐 Frontend (Vue 3 + Vite)

- [**Vue 3.5**](https://vuejs.org/) + Composition API
- [**Vue Router 4.5**](https://router.vuejs.org/) – Ruteo dinámico
- [**Pinia 3.0**](https://pinia.vuejs.org/) – Manejo de estado
- [**Axios 1.9**](https://axios-http.com/) – Cliente HTTP
- [**Bootstrap 5.3**](https://getbootstrap.com/) + [**Bootstrap Icons**](https://icons.getbootstrap.com/)
- [**Vite 6.1**](https://vitejs.dev/) – Bundler ultrarrápido
- [**Vitest**](https://vitest.dev/) – Testing del frontend
- [**Prettier**](https://prettier.io/) + [**ESLint**](https://eslint.org/) – Formato y calidad de código
- [**Vue Test Utils**](https://test-utils.vuejs.org/) – Testing de componentes
- Soporte para **TypeScript**

---

## 📁 Estructura del proyecto

```bash
staffy/
├── backend/                # Proyecto Django
│   ├── accounts/           # App para perfiles y roles
│   ├── main/               # Configuración general
│   ├── media/              # Archivos cargados desde la aplicación
│   ├── shared/             # Funcionalidad compartida entre apps
│   ├── tasks/              # Apps para tareas
│   └── manage.py
├── frontend/              # Proyecto Vue 3
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── router/
│   │   └── main.js
│   └── vite.config.js
├── docs/                  # Documentación técnica adicional
└── README.md              # Este archivo
```

---

## 🧑‍💻 Instalación local

### Requisitos previos

- Python 3.9+
- Node.js 18+ y npm
- PostgreSQL o SQLite

### 1. Clonar el repositorio

```bash
git clone https://github.com/SamuP14/staffy.git
cd staffy
```

### 2. Backend (Django)

```bash
cd backend
python -m venv .venv --prompt staffy
.venv/bin/activate
pip install -r requirements.txt
python manage.py migrate (o) just m
python manage.py createsuperuser
python manage.py runserver (o) just
```

### 3. Frontend (Vue 3)

```bash
cd ../frontend
npm install
npm run dev
```

Accede a: `http://localhost:5173`

---

## 🔐 Credenciales de ejemplo

```bash
Usuario: admin@example.com
Contraseña: admin123
```

> Puedes cambiarlas desde el panel de Django Admin.

---

## 🧾 Documentación adicional

- [`docs/api.md`](docs/api.md) – Endpoints disponibles
- [`docs/deploy.md`](docs/deploy.md) – Despliegue en producción
- [`docs/frontend.md`](docs/frontend.md) – Estructura de la app Vue
- [`docs/backend.md`](docs/backend.md) – Modelos y lógica del backend

---

## 📦 Despliegue

Staffy puede desplegarse fácilmente en servicios como DigitalOcean, Heroku o cualquier VPS con soporte Docker (si aplicable).

Consulta la guía [`docs/deploy.md`](docs/deploy.md).

---

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

---

## 🤝 Contribuciones

¿Quieres colaborar? Toda ayuda es bienvenida. Puedes abrir issues o pull requests con mejoras, correcciones o nuevas ideas.
