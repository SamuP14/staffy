# 🚀 Plan de Despliegue en Producción – Staffy | Easy Staff Solutions

Este documento es una **propuesta estructurada** para preparar el despliegue de Staffy en un entorno de producción en el futuro. Está orientado a entornos **Windows** (desarrollo) y un servidor Linux (producción), utilizando tecnologías estándar como Django, Vue, Nginx y PostgreSQL.

---

## 🌐 Objetivo del despliegue

Poner en línea la plataforma Staffy para que pueda ser accedida por empresas, clientes o equipos desde cualquier lugar de forma segura, rápida y estable.

---

## 🧾 Arquitectura propuesta

- **Backend**: Django + Gunicorn
- **Frontend**: Vue 3 (build de producción con Vite)
- **Base de datos**: PostgreSQL
- **Servidor web**: Nginx
- **Sistema operativo en servidor**: Ubuntu (DigitalOcean, AWS, etc.)
- **HTTPS**: Let's Encrypt con Certbot

---

## 🧱 Fases del despliegue

### 1. Configuración del servidor remoto

> En el futuro contaremos con un servidor virtual (VPS) con Linux instalado, probablemente Ubuntu. Desde nuestro entorno Windows, accederemos por SSH usando herramientas como [PuTTY](https://www.putty.org/) o [Windows Terminal].

**Tareas previstas:**

- Crear un usuario para la app
- Configurar firewall (abrir puertos 80 y 443)
- Instalar Python, PostgreSQL, Git, Nginx

### 2. Preparación del backend (Django)

> Se activará un entorno virtual de Python en el servidor, se instalarán dependencias y se configurará la base de datos.

**Tareas previstas:**

- Copiar el proyecto al servidor (vía Git o SCP)
- Instalar dependencias con `pip`
- Configurar variables de entorno (`DEBUG=False`, `ALLOWED_HOSTS`, claves)
- Ejecutar migraciones de base de datos
- Crear superusuario para el admin
- Preparar archivos estáticos (`collectstatic`)

### 3. Preparación del frontend (Vue)

> En nuestra máquina Windows generaremos la build del frontend y la subiremos al servidor para que sea servida por Nginx o un sistema separado.

**Tareas previstas:**

- Ejecutar `npm run build` en local
- Subir carpeta `dist/` al servidor
- Configurar Nginx para servir archivos estáticos

### 4. Configuración del servidor web

> Nginx actuará como intermediario entre el navegador y el backend, sirviendo archivos del frontend y redirigiendo llamadas API a Django.

**Tareas previstas:**

- Crear archivo de configuración de Nginx
- Asegurar acceso a `/static/`, `/media/` y `/api/`
- Habilitar HTTPS con Certbot

### 5. Automatización y seguridad

> El sistema se mantendrá estable con servicios de sistema (como `systemd`) y se reforzará la seguridad del servidor.

**Tareas previstas:**

- Configurar servicio para ejecutar Gunicorn automáticamente
- Habilitar backups regulares (base de datos y archivos)
- Asegurar acceso SSH con claves
- Configurar monitoreo (en futuro)

---

## 💻 Herramientas que usaremos (o evaluaremos)

| Propósito           | Herramienta sugerida       |
|---------------------|----------------------------|
| Servidor remoto     | DigitalOcean / Linode      |
| Acceso remoto       | SSH / PuTTY / VS Code SSH  |
| Control de versiones| Git / GitHub               |
| Base de datos       | PostgreSQL                 |
| Servidor web        | Nginx                      |
| HTTPS               | Certbot / Let's Encrypt    |
| Logs y monitoreo    | UptimeRobot / Netdata      |

---

## 📋 Checklist previa al despliegue

- [ ] Código validado y probado en local (Windows)
- [ ] Base de datos configurada con datos reales o semilla
- [ ] Archivos `.env` o de configuración definidos
- [ ] Build del frontend generada (`npm run build`)
- [ ] Dominio reservado y accesible
- [ ] Decisión tomada sobre el proveedor de hosting

---

## 🧠 Consideraciones futuras

- Hacer el despliegue con Docker puede simplificar la gestión
- Configurar integración continua (CI/CD) para cada push en GitHub
- Añadir tests automáticos antes del despliegue
- Evaluar si frontend se desplegará por separado (ej. Netlify, Vercel)

---

🎯 Este plan está diseñado para facilitar un despliegue ordenado, sin sobresaltos, y adaptable a futuras mejoras.
