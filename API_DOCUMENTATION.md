
# Documentación de la API RESTful

## Introducción
Esta API RESTful gestiona las siguientes entidades:
- **Usuario**
- **Pregunta**
- **Imagen**
- **Respuesta**
- **Grixel**
- **Responde**

### Base URL
```
http://localhost:2025
```

## Endpoints

### 1. Usuario

#### Obtener todos los usuarios
```
GET /Usuario
```
**Respuesta:**
```json
[
  {"email": "usuario1@email.com", "NombreUsuario": "Usuario1"},
  {"email": "usuario2@email.com", "NombreUsuario": "Usuario2"}
]
```

#### Crear un nuevo usuario
```
POST /Usuario
```
**Body:**
```json
{
  "email": "nuevo@email.com",
  "NombreUsuario": "NuevoUsuario"
}
```
**Respuesta:**
```json
{"mensaje": "Usuario creado"}
```

#### Actualizar un usuario
```
PUT /Usuario/{email}
```
**Body:**
```json
{
  "NombreUsuario": "UsuarioActualizado"
}
```
**Respuesta:**
```json
{"mensaje": "Usuario actualizado"}
```

#### Eliminar un usuario
```
DELETE /Usuario/{email}
```
**Respuesta:**
```json
{"mensaje": "Usuario eliminado"}
```

---

### 2. Pregunta

#### Obtener todas las preguntas
```
GET /Pregunta
```
**Respuesta:**
```json
[
  {"idPregunta": 1, "pregunta": "¿Cuál es la capital de Francia?"}
]
```

#### Crear una nueva pregunta
```
POST /Pregunta
```
**Body:**
```json
{
  "pregunta": "¿Qué es Flask?"
}
```
**Respuesta:**
```json
{"mensaje": "Pregunta creada"}
```

#### Actualizar una pregunta
```
PUT /Pregunta/{idPregunta}
```
**Body:**
```json
{
  "pregunta": "Pregunta actualizada"
}
```
**Respuesta:**
```json
{"mensaje": "Pregunta actualizada"}
```

#### Eliminar una pregunta
```
DELETE /Pregunta/{idPregunta}
```
**Respuesta:**
```json
{"mensaje": "Pregunta eliminada"}
```

---

### 3. Imagen

#### Obtener todas las imágenes
```
GET /Imagen
```
**Respuesta:**
```json
[
  {"ImagenID": 1, "ImagenURL": "http://example.com/imagen1.jpg"}
]
```

#### Crear una nueva imagen
```
POST /Imagen
```
**Body:**
```json
{
  "Activo": true,
  "Respuesta": "Imagen1",
  "fechaInicio": "2025-03-29",
  "fechaFinalizacion": "2025-04-05",
  "ImagenURL": "http://example.com/imagen1.jpg",
  "email_Usuario": "usuario1@email.com"
}
```
**Respuesta:**
```json
{"mensaje": "Imagen creada"}
```