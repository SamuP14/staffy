# 🌐 Documentación del Frontend – Staffy | Easy Staff Solutions

Este documento describe la estructura, componentes, dependencias y lógica principal del **frontend de Staffy**, desarrollado en Vue 3 con TypeScript y Vite.

---

## 🧰 Tecnologías principales

- **Vue 3 + Composition API**
- **TypeScript**
- **Vite** como bundler
- **Pinia** para el manejo del estado global
- **Axios** para peticiones HTTP
- **Vue Router** para navegación SPA
- **Bootstrap 5.3 + Bootstrap Icons**
- **Accesibilidad con ARIA y WCAG 2.1**

---

## 📁 Estructura del proyecto

```bash
frontend/
├── src/
│   ├── assets/              # Archivos estáticos (CSS, logos)
│   ├── components/          # Todos los componentes funcionales
│   ├── router/              # Rutas de navegación (Vue Router)
│   ├── stores/              # Estado global (Pinia)
│   ├── App.vue              # Raíz de la aplicación
│   └── main.ts              # Punto de entrada principal
└── vite.config.ts           # Configuración de Vite
```

---

## 🚦 Navegación y rutas (router)

Las rutas están protegidas con `meta.requiresAuth`. Las vistas principales incluyen:

- `/employees` – Lista de empleados
- `/employees/:username` – Detalle de perfil
- `/employees/add`, `/edit` – Crear o editar empleados
- `/tasks`, `/tasks/:id` – Listado y detalle de tareas
- `/roles`, `/roles/add` – Listado y creación de roles
- `/contact` – Formulario de contacto
- `/login` – Página de autenticación

---

## 🔐 Manejo de autenticación

Usamos **Pinia** para mantener el estado del usuario:

- `auth.login()` – realiza login y guarda en `localStorage`
- `auth.logout()` – limpia la sesión
- `auth.init()` – carga estado guardado al refrescar

Los datos guardados incluyen: `username`, `userId`, `avatar`, `isLoggedIn`.

---

## 📦 Componentes principales

### 👥 Empleados

- `AddEmployeeForm.vue` – Formulario para añadir empleado
- `EditEmployeeForm.vue` – Editar campos básicos y experiencia
- `WorkerList.vue` – Tabla con todos los empleados
- `ProfileDetail.vue` – Vista extendida con avatar, roles y más

### 🧩 Roles

- `RoleList.vue` – Lista de roles (asignables y eliminables)
- `AddRoleForm.vue` – Crear un nuevo rol

### ✅ Tareas

- `TaskList.vue` – Tabla de tareas
- `TaskDetails.vue` – Detalle de una tarea específica
- `AddTaskForm.vue`, `EditTaskForm.vue` – Formularios para tareas

### 📬 Contacto

- `ContactForm.vue` – Formulario genérico sin backend conectado aún

### 🧭 Navegación

- `NavBar.vue` – Barra principal
- `AppFooter.vue` – Footer con redes y mensaje institucional

---

## 🧠 Lógica interna destacada

- **Avatar**: permite subir imagen como base64 y editar avatar con previsualización.
- **Formularios**: todos usan `v-model`, validación nativa y `@submit.prevent`.
- **Accesibilidad**: se usa `role`, `aria-label`, y etiquetas semánticas en formularios.
- **Multiselección**: asignación de roles y empleados usa `<select multiple>`.
- **Control de errores**: feedback básico vía `console.error` y `alert()`.

---

## 🌍 Internacionalización

La app está escrita principalmente en inglés, pero con mensajes visibles en español en fechas, botones y formularios. Se contempla la futura integración de i18n para múltiples idiomas.

---

## 📐 Diseño y estilos

- Diseño **responsive** gracias a Bootstrap Grid
- Colores personalizados (`#0D7BA6`) para botones y navegación
- Iconos de acciones (ver, editar, eliminar) con `Bootstrap Icons`
- Avatar y componentes visuales tienen diseño accesible y minimalista

---

## 🧪 Testing y mantenimiento

Actualmente no se implementan pruebas automáticas, pero se planea utilizar:

- **Vitest** + **Vue Test Utils**
- **Cypress** para pruebas end-to-end
- **Prettier** y **ESLint** para formato y calidad

---

## 📦 Build de producción

```bash
npm install
npm run build
```

El contenido generado en `dist/` puede ser:

- Servido por un servidor como Nginx
- Integrado en un backend monolítico (Django static files)
- Subido a servicios como Vercel o Netlify

---

## ✅ Checklist de buenas prácticas

- [x] Interfaz responsive
- [x] Formularios con accesibilidad básica (WCAG 2.1)
- [x] Separación de componentes por funcionalidad
- [x] Gestión de errores básicos
- [x] Código limpio y legible

---

## 🔮 Mejoras futuras

- Gestión de notificaciones visuales
- Soporte multiidioma
- Componentes reutilizables globales
- Carga progresiva de datos
- Modo oscuro
