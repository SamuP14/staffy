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
git clone https://github.com/tu_usuario/staffy.git
cd staffy
```

### 2. Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
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

```
Usuario: admin@example.com
Contraseña: admin123
```

> Puedes cambiarlas desde el panel de Django Admin.

---

## 🧪 Tests

### Django

```bash
python manage.py test
```

### Vue (si se usan pruebas)

```bash
npm run test
```

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

Este proyecto está bajo la licencia MIT. Puedes usarlo, adaptarlo y redistribuirlo libremente.

---

## 🤝 Contribuciones

¿Quieres colaborar? Toda ayuda es bienvenida. Puedes abrir issues o pull requests con mejoras, correcciones o nuevas ideas.

---

## 📈 Plan de Marketing

### 1. Análisis de Situación

**Producto:**  
Staffy es una solución SaaS ligera, intuitiva y flexible que permite a empresas centralizar la gestión de empleados, roles y tareas en un solo lugar.

**Público objetivo:**  
- Empresas de 5 a 250 empleados.  
- Sectores: retail, servicios, logística, salud, tecnología, educación.  
- Roles objetivo: Directores de RRHH, gerentes de operaciones, dueños de pymes.

**Competencia:**  
- Factorial, Holded, Kenjo, Zoho People.  
- Diferenciador: Staffy es más adaptable, económica y rápida de implementar.

**Análisis DAFO**
![Gráfico Análisis DAFO circulo texto Creativo Multicolor](https://github.com/user-attachments/assets/05b6c963-4339-4204-8a15-801d8576ba33)


---

### 2. Objetivos de Marketing

- Alcanzar **1.000 usuarios registrados** en el primer año.
- Captar **100 empresas activas** en los primeros 6 meses.
- Lograr **3 alianzas estratégicas** con agencias o distribuidores TI.

---

### 3. Estrategias y Tácticas

#### 💡 Branding y Propuesta de Valor

- Slogan: *"Making staff management simple, fast, and efficient."*  
- Enfocado en facilidad, personalización y eficiencia operativa.

#### 📣 Difusión y Adquisición

- Sitio web optimizado para SEO orientado a "software gestión empleados pymes".
- Inbound marketing: artículos, ebooks, casos de uso.
- Campañas pagadas en Google Ads y LinkedIn.

#### 📱 Presencia en Redes Sociales

- **LinkedIn:** publicaciones de valor y contenido profesional.
- **Instagram y TikTok:** contenido visual, behind-the-scenes, tips de gestión.
- **YouTube:** tutoriales breves, demos y explicaciones.

#### 🤝 Ventas y Distribución

- Plan freemium con escalado por funciones.
- Distribución por partners: desarrolladores y agencias locales.

---

### 4. Indicadores Clave (KPIs)

- CAC (Costo de adquisición por cliente).
- Tasa de conversión demo > suscripción.
- Tasa de cancelación mensual.
- Tráfico web y leads generados.
- Tiempo de implementación promedio.

---

## 🚀 Roadmap de Producto (Ideas a Futuro)

- ✅ **Revisión de tareas por admin** al marcar como completadas.
- 📆 **Calendario de tareas** global por equipo o usuario.
- ⏱️ **Sistema de Punch In / Punch Out** para control horario.
  
> Estos módulos serán integrables como características opcionales y escalarán el valor del producto según necesidades del cliente.

---

## 🌱 Plan de Sostenibilidad

### 1. Compromiso

Integrar prácticas responsables a nivel ambiental, social y económico, tanto en el desarrollo del software como en su uso final por parte de empresas.

---

### 2. Objetivos

- Minimizar el impacto ambiental digital.
- Promover la inclusión, accesibilidad y bienestar laboral.
- Proveer herramientas que fomenten buenas prácticas laborales.

---

### 3. Ejes de Acción

#### 🌍 Ambiental
- Hosting ecológico (energía renovable, servidores eficientes).
- Optimización de código y rendimiento para menor consumo de datos.
- UI/UX ecoeficiente: carga ligera, mínima dependencia externa.

#### 👥 Social
- Interfaz accesible (cumple con WCAG 2.1).
- Lenguaje y diseño inclusivo.
- Diversidad e inclusión en el equipo de desarrollo y soporte.

#### 💼 Económico
- Precios transparentes y justos.
- Modelo escalable y ético.
- Reinversión en soporte comunitario y mejoras sostenibles.

---

### 4. Medición y Evaluación

- Análisis de consumo energético y eficiencia trimestral.
- Encuestas semestrales de bienestar del equipo.
- Feedback anual de usuarios sobre ética, impacto y mejora continua.

---
