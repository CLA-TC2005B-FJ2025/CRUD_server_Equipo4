
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
[{"email": "usuario1@email.com", "NombreUsuario": "Usuario1"}]
```

#### Crear un nuevo usuario
```
POST /Usuario
```
**Body:**
```json
{"email": "nuevo@email.com", "NombreUsuario": "NuevoUsuario"}
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
{"NombreUsuario": "UsuarioActualizado"}
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
[{"idPregunta": 1, "pregunta": "¿Cuál es la capital de Francia?"}]
```

#### Crear una nueva pregunta
```
POST /Pregunta
```
**Body:**
```json
{"pregunta": "¿Qué es Flask?"}
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
{"pregunta": "Pregunta actualizada"}
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
[{"ImagenID": 1, "ImagenURL": "http://example.com/imagen1.jpg"}]
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

#### Actualizar una imagen
```
PUT /Imagen/{ImagenID}
```
**Body:**
```json
{
  "Activo": false,
  "Respuesta": "ImagenActualizada",
  "fechaInicio": "2025-04-01",
  "fechaFinalizacion": "2025-04-10",
  "ImagenURL": "http://example.com/imagen2.jpg",
  "email_Usuario": "usuario2@email.com"
}
```
**Respuesta:**
```json
{"mensaje": "Imagen actualizada"}
```

#### Eliminar una imagen
```
DELETE /Imagen/{ImagenID}
```
**Respuesta:**
```json
{"mensaje": "Imagen eliminada"}
```

---

### 4. Respuesta

#### Obtener todas las respuestas
```
GET /Respuesta
```
**Respuesta:**
```json
[{"RespuestaID": 1, "Respuesta": "París"}]
```

#### Crear una nueva respuesta
```
POST /Respuesta
```
**Body:**
```json
{
  "Respuesta": "Python",
  "Correcta": true,
  "idPregunta": 1
}
```
**Respuesta:**
```json
{"mensaje": "Respuesta creada"}
```

#### Actualizar una respuesta
```
PUT /Respuesta/{RespuestaID}
```
**Body:**
```json
{
  "Respuesta": "Django",
  "Correcta": false,
  "idPregunta": 2
}
```
**Respuesta:**
```json
{"mensaje": "Respuesta actualizada"}
```

#### Eliminar una respuesta
```
DELETE /Respuesta/{RespuestaID}
```
**Respuesta:**
```json
{"mensaje": "Respuesta eliminada"}
```

---

### 5. Grixel

#### Obtener todos los Grixel
```
GET /Grixel
```
**Respuesta:**
```json
[{"IDgrixel": 1, "ImagenID": 1, "CoorX": 10, "CoorY": 15}]
```

#### Crear un nuevo Grixel
```
POST /Grixel
```
**Body:**
```json
{
  "ImagenID": 1,
  "CoorX": 10,
  "CoorY": 15,
  "email_Usuario": "usuario1@email.com",
  "idPregunta_Pregunta": 2
}
```
**Respuesta:**
```json
{"mensaje": "Grixel creado"}
```

#### Actualizar un Grixel
```
PUT /Grixel/{IDgrixel}/{ImagenID}
```
**Body:**
```json
{
  "CoorX": 12,
  "CoorY": 18,
  "email_Usuario": "usuario2@email.com",
  "idPregunta_Pregunta": 3
}
```
**Respuesta:**
```json
{"mensaje": "Grixel actualizado"}
```

#### Eliminar un Grixel
```
DELETE /Grixel/{IDgrixel}/{ImagenID}
```
**Respuesta:**
```json
{"mensaje": "Grixel eliminado"}
```

---

### 6. Responde (Registro de respuestas)

#### Obtener todos los registros de respuesta
```
GET /Responde
```
**Respuesta:**
```json
[{"IDregistro": 1, "Fecha": "2025-03-29", "Hora": "10:30"}]
```

#### Crear un nuevo registro de respuesta
```
POST /Responde
```
**Body:**
```json
{
  "Fecha": "2025-03-29",
  "Hora": "10:30",
  "email_Usuario": "usuario1@email.com",
  "RespuestaID": 1
}
```
**Respuesta:**
```json
{"mensaje": "Registro de respuesta creado"}
```

#### Actualizar un registro de respuesta
```
PUT /Responde/{IDregistro}
```
**Body:**
```json
{
  "Fecha": "2025-03-30",
  "Hora": "11:00",
  "email_Usuario": "usuario2@email.com",
  "RespuestaID": 2
}
```
**Respuesta:**
```json
{"mensaje": "Registro de respuesta actualizado"}
```

#### Eliminar un registro de respuesta
```
DELETE /Responde/{IDregistro}
```
**Respuesta:**
```json
{"mensaje": "Registro de respuesta eliminado"}
```
