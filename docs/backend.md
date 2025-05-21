# 📦 Staffy Backend API – Documentación Técnica

**Versión:** `v1.0`  
**Framework:** Django 5.1.6  
**Base de datos:** SQLite (desarrollo) / PostgreSQL (producción)  
**Autenticación:** Sesiones de Django (`/login/`, `/logout/`)

---

## 🌐 API REST – Endpoints Disponibles

### 🔐 Autenticación

| Método | Endpoint          | Descripción                     |
|--------|-------------------|---------------------------------|
| POST   | `/api/accounts/login/`   | Iniciar sesión con `username` y `password` |
| POST   | `/api/accounts/logout/`  | Cerrar sesión actual            |

#### Ejemplo de respuesta (login exitoso)

```json
{
  "success": true,
  "username": "juan",
  "user_id": 3,
  "avatar": "http://localhost:8000/media/avatars/juan.png"
}
```

---

### 👤 Perfiles de Usuario

| Método | Endpoint                             | Descripción                           |
|--------|--------------------------------------|---------------------------------------|
| GET    | `/api/accounts/profile/`             | Obtener todos los perfiles            |
| GET    | `/api/accounts/profile/<username>/`  | Obtener detalle de perfil             |
| POST   | `/api/accounts/profile/add/`         | Crear un nuevo perfil de usuario      |
| POST   | `/api/accounts/profile/<username>/edit/` | Editar un perfil existente       |
| POST   | `/api/accounts/profile/<username>/delete/` | Eliminar un perfil             |
| POST   | `/api/accounts/profile/<username>/role/add/` | Asignar roles al perfil        |
| POST   | `/api/accounts/profile/<username>/role/<role_code>/delete/` | Quitar rol del perfil |

#### Campos requeridos para creación (`POST /profile/add/`)

```json
{
  "username": "ana",
  "first_name": "Ana",
  "last_name": "Martínez",
  "id_number": "12345678",
  "email": "ana@example.com",
  "password": "1234",
  "phone": "555-1234",
  "profession": "Administrativa",
  "avatar": "data:image/png;base64,...",
  "role": ["ADM"]
}
```

---

### 🎭 Roles

| Método | Endpoint                        | Descripción                 |
|--------|---------------------------------|-----------------------------|
| GET    | `/api/accounts/role/`           | Listar todos los roles      |
| POST   | `/api/accounts/role/add/`       | Crear un nuevo rol          |
| POST   | `/api/accounts/role/<code>/delete/` | Eliminar un rol existente |

#### Ejemplo creación de rol

```json
{
  "code": "ADM",
  "name": "Administrador"
}
```

---

### ✅ Tareas

| Método | Endpoint               | Descripción                      |
|--------|------------------------|----------------------------------|
| GET    | `/api/tasks/`          | Listar todas las tareas          |
| GET    | `/api/tasks/<id>/`     | Ver detalle de una tarea         |
| POST   | `/api/tasks/add/`      | Crear nueva tarea                |
| POST   | `/api/tasks/<id>/edit/`| Editar tarea existente           |
| POST   | `/api/tasks/<id>/delete/`| Eliminar una tarea              |

#### Ejemplo de creación de tarea

```json
{
  "title": "Enviar informe mensual",
  "description": "Debe enviarse antes del 15",
  "due_date": "2025-06-15",
  "status": "pending",
  "priority": "high",
  "employees": ["ana", "juan"]
}
```

---

## 🗂️ Modelos de Datos

### `Profile`

```python
class Profile(models.Model):
    user = OneToOneField(User)
    id_number = CharField(unique=True)
    phone = CharField()
    profession = CharField()
    experience = TextField()
    avatar = ImageField()
    role = ManyToManyField(Role)
```

### `Role`

```python
class Role(models.Model):
    code = CharField(primary_key=True)
    name = CharField()
```

### `Task`

```python
class Task(models.Model):
    title = CharField()
    description = TextField()
    due_date = DateField()
    status = CharField(choices=["pending", "in_progress", "completed"])
    priority = CharField(choices=["low", "medium", "high"])
    employees = ManyToManyField(Profile)
```

---

## ⚙️ Utilidades y Decoradores

- `@get_required` – Solo permite métodos GET.
- `@post_required` – Solo permite métodos POST.
- `utils.validate_required_fields()` – Verifica presencia de campos obligatorios en el body.

---

## 🧪 Testing y Seguridad

- Las respuestas HTTP tienen códigos de estado claros (`201`, `400`, `404`, `200`, `401`).
- No se permite acceso por otros métodos (`405`).
- Protección CSRF deshabilitada para facilitar testing (usar con cuidado en producción).

---

## 📌 Notas Finales

- Las URLs están configuradas bajo `/api/accounts/` y `/api/tasks/`.
- Las imágenes se almacenan en `media/avatars/`.
- Se recomienda implementar autenticación por token o JWT en producción.
