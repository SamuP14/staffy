# 🧩 API Staffy | Easy Staff Solutions

**Staffy API** permite gestionar empleados, roles y tareas de forma eficiente mediante endpoints RESTful, diseñada para pequeñas y medianas empresas que requieren una solución moderna, modular y escalable.

---

## 🔗 Endpoints disponibles

### 👤 Perfiles de Usuario

#### `GET /accounts/profile/`

Devuelve la lista de todos los perfiles.

**Ejemplo de respuesta:**

```json
[
  {
    "id": 1,
    "user": {
      "username": "jdoe",
      "first_name": "John",
      "last_name": "Doe",
      "email": "jdoe@example.com"
    },
    "id_number": "12345678",
    "phone": "+34111222333",
    "profession": "Ingeniero",
    "experience": "",
    "avatar": "http://localhost:8000/media/avatars/jdoe.png",
    "role": ["Admin", "RRHH"]
  }
]
```

#### `POST /accounts/profile/add/`

Crea un nuevo perfil de usuario.

**Campos requeridos:** `username`, `first_name`, `last_name`, `id_number`, `email`, `password`, `phone`, `profession`  
**Opcionales:** `avatar (base64)`, `role (lista de códigos)`

**Ejemplo de respuesta:**

```json
{
  "id": 3
}
```

#### `GET /accounts/profile/<username>/`

Devuelve los datos completos del perfil.

#### `POST /accounts/profile/<username>/edit/`

Edita campos del perfil: `experience`, `profession`, `phone`, `id_number`, `avatar`

#### `POST /accounts/profile/<username>/delete/`

Elimina el usuario y su perfil asociado.

#### `POST /accounts/profile/<username>/role/add/`

Agrega roles al perfil.

**Body esperado:**

```json
{ "role_codes": ["ADM", "HR"] }
```

#### `POST /accounts/profile/<username>/role/<role_code>/delete/`

Elimina un rol específico del perfil.

---

### 🧩 Roles

#### `GET /accounts/role/`

Lista todos los roles disponibles.

```json
[
  {
    "id": "ADM",
    "code": "ADM",
    "name": "Administrador"
  }
]
```

#### `POST /accounts/role/add/`

Agrega un nuevo rol.

**Body requerido:**

```json
{ "code": "DEV", "name": "Desarrollador" }
```

#### `POST /accounts/role/<role_code>/delete/`

Elimina un rol por su código.

---

### 🔐 Autenticación

#### `POST /accounts/login/`

Autentica al usuario.

**Body requerido:**

```json
{ "username": "jdoe", "password": "admin123" }
```

**Respuesta exitosa:**

```json
{
  "success": true,
  "username": "jdoe",
  "user_id": 1,
  "avatar": "http://localhost:8000/media/avatars/jdoe.png"
}
```

#### `POST /accounts/logout/`

Cierra la sesión actual.

```json
{ "success": true }
```

---

### ✅ Tareas

#### `GET /tasks/`

Lista todas las tareas.

```json
[
  {
    "id": 1,
    "title": "Entrevista a candidatos",
    "description": "Revisión y entrevista para vacantes",
    "due_date": "2025-06-10",
    "status": "Pending",
    "priority": "High",
    "employees": [
      {
        "id": 1,
        "user": {
          "username": "jdoe",
          "first_name": "John",
          "last_name": "Doe",
          "email": "jdoe@example.com"
        },
        "id_number": "12345678",
        "phone": "+34111222333",
        "profession": "RRHH",
        "experience": "",
        "avatar": "http://localhost:8000/media/avatars/jdoe.png",
        "role": ["RRHH"]
      }
    ],
    "created_at": "2025-05-21T10:00:00",
    "updated_at": "2025-05-21T10:30:00"
  }
]
```

#### `GET /tasks/<task_id>/`

Detalle de una tarea específica.

#### `POST /tasks/add/`

Agrega una nueva tarea.

**Body esperado:**

```json
{
  "title": "Lanzar campaña",
  "description": "Campaña publicitaria julio",
  "due_date": "2025-07-01",
  "status": "pending",
  "priority": "medium",
  "employees": ["jdoe", "mjane"]
}
```

#### `POST /tasks/<task_id>/edit/`

Edita campos de la tarea.

#### `POST /tasks/<task_id>/delete/`

Elimina una tarea existente.

---

## 🧰 Utilidades

### Validaciones

- `validate_required_fields`: asegura que los campos requeridos estén presentes en el JSON recibido.

### Decoradores

- `@get_required`: fuerza el método GET.
- `@post_required`: fuerza el método POST.

---

## 🧪 Resumen de Respuestas

- Todas las respuestas son en formato JSON.
- Códigos de estado: `200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `405 Method Not Allowed`.

---

## 🧾 Notas

- Las imágenes (avatar) deben enviarse en formato base64.
- Las URLs son relativas al servidor actual (`http://localhost:8000` en desarrollo).

---

© 2025 Staffy | Easy Staff Solutions
