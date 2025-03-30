from flask import Flask, request, jsonify
from flask_cors import CORS
import pymssql

app = Flask(__name__)
CORS(app)

# ===== Database configuration =====
server = "localhost"
port = 1433
database = "master"
username = "sa"
password = "YourPassword123!"

# ===== Database connection function =====
def get_connection():
    return pymssql.connect(server=server, port=port, user=username, password=password, database=database)

# ===== Tabla usuario =====
@app.route('/Usuario', methods=['GET'])
def get_usuario():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Usuario')
    data = cursor.fetchall()
    conn.close(), 
    return jsonify(data)

@app.route('/Usuario', methods=['POST'])
def create_usuario():
    data = request.json
    email = data['email']
    NombreUsuario = data['NombreUsuario']
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO Usuario (email, NombreUsuario) VALUES (%s, %s)', (email, NombreUsuario))
        conn.commit()
        return jsonify({'mensaje': 'Usuario creado'}), 201
    except pymssql.IntegrityError:
        return jsonify({'mensaje': 'El email ya existe'}), 400
    finally:
        conn.close()

@app.route('/Usuario/<string:email>', methods=['PUT'])
def update_usuario(email):
    data = request.json
    nuevo_nombre = data['NombreUsuario']
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE Usuario SET NombreUsuario = %s WHERE email = %s', (nuevo_nombre, email))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'mensaje': 'Usuario no encontrado'}), 404
        return jsonify({'mensaje': 'Usuario actualizado'})
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()

@app.route('/Usuario/<string:email>', methods=['DELETE'])
def delete_usuario(email):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT 1 FROM Usuario WHERE email = %s', (email,))
        if not cursor.fetchone():
            return jsonify({'mensaje': 'Usuario no encontrado'}), 404
        
        cursor.execute('DELETE FROM Usuario WHERE email = %s', (email,))
        conn.commit()
        
        return jsonify({'mensaje': 'Usuario eliminado'})
    except pymssql.IntegrityError:
        return jsonify({'mensaje': 'No se puede eliminar el usuario porque tiene registros relacionados'}), 400
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()
#=========Tabla Pregunta ===========
@app.route('/Pregunta', methods=['GET'])
def get_pregunta():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Pregunta')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/Pregunta', methods=['POST'])
def create_pregunta():
    data = request.json
    pregunta = data['pregunta']
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO Pregunta (pregunta) VALUES (%s)', (pregunta))
        conn.commit()
        return jsonify({'mensaje': 'Pregunta creada'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
    finally:
        conn.close()

@app.route('/Pregunta/<int:idPregunta>', methods=['PUT'])
def update_pregunta(idPregunta):
    data = request.json
    nueva_pregunta = data['pregunta']
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE Pregunta SET pregunta = %s WHERE idPregunta = %s', (nueva_pregunta, idPregunta))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'mensaje': 'Pregunta no encontrada'}), 404
        return jsonify({'mensaje': 'Pregunta actualizada'})
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()

@app.route('/Pregunta/<int:idPregunta>', methods=['DELETE'])
def delete_pregunta(idPregunta):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT 1 FROM Pregunta WHERE idPregunta = %s', (idPregunta,))
        if not cursor.fetchone():
            return jsonify({'mensaje': 'Pregunta no encontrada'}), 404
        
        cursor.execute('DELETE FROM Pregunta WHERE idPregunta = %s', (idPregunta,))
        conn.commit()
        
        return jsonify({'mensaje': 'Pregunta eliminada'})
    except pymssql.IntegrityError:
        return jsonify({'mensaje': 'No se puede eliminar la pregunta porque tiene registros relacionados'}), 400
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()
#=========Tabla Imagen ===========
@app.route('/Imagen', methods=['GET'])
def get_imagen():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Imagen;') #No regresa la respuesta porque sería peligroso que los usuarios pudieran acceder a ella
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/Imagen', methods=['POST'])
def create_imagen():
    data = request.json
    activo = data['Activo']
    respuesta = data['Respuesta']
    fecha_inicio = data['fechaInicio']
    fecha_finalizacion = data['fechaFinalizacion']
    imagen_url = data['ImagenURL']
    email_usuario = data.get('email_Usuario')
    
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO Imagen (Activo, Respuesta, fechaInicio, fechaFinalizacion, ImagenURL, email_Usuario) 
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (activo, respuesta, fecha_inicio, fecha_finalizacion, imagen_url, email_usuario))
        conn.commit()
        return jsonify({'mensaje': 'Imagen creada'}), 201
    except pymssql.IntegrityError as e:
        return jsonify({'mensaje': 'Error de integridad: ' + str(e)}), 400
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
    finally:
        conn.close()

@app.route('/Imagen/<int:ImagenID>', methods=['PUT'])
def update_imagen(ImagenID):
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE Imagen SET 
                Activo = %s,
                Respuesta = %s,
                fechaInicio = %s,
                fechaFinalizacion = %s,
                ImagenURL = %s,
                email_Usuario = %s
            WHERE ImagenID = %s
        ''', (
            data.get('Activo'),
            data.get('Respuesta'),
            data.get('fechaInicio'),
            data.get('fechaFinalizacion'),
            data.get('ImagenURL'),
            data.get('email_Usuario'),
            ImagenID
        ))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'mensaje': 'Imagen no encontrada'}), 404
        return jsonify({'mensaje': 'Imagen actualizada'})
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()

@app.route('/Imagen/<int:ImagenID>', methods=['DELETE'])
def delete_imagen(ImagenID):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT 1 FROM Imagen WHERE ImagenID = %s', (ImagenID,))
        if not cursor.fetchone():
            return jsonify({'mensaje': 'Imagen no encontrada'}), 404
        
        cursor.execute('DELETE FROM Imagen WHERE ImagenID = %s', (ImagenID,))
        conn.commit()
        
        return jsonify({'mensaje': 'Imagen eliminada'})
    except pymssql.IntegrityError:
        return jsonify({'mensaje': 'No se puede eliminar la imagen porque tiene registros relacionados'}), 400
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()

#========= Respuesta Pregunta ===========
@app.route('/Respuesta', methods=['GET'])
def get_respuesta():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT RespuestaID, Respuesta FROM Respuesta;') #No regresa si la respuesta es correcta o no por la misma razóm
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/Respuesta', methods=['POST'])
def create_respuesta():
    data = request.json
    respuesta = data['Respuesta']
    correcta = data['Correcta']
    id_pregunta = data['idPregunta']
    
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO Respuesta (Respuesta, Correcta, idPregunta) 
            VALUES (%s, %s, %s)
        ''', (respuesta, correcta, id_pregunta))
        conn.commit()
        return jsonify({'mensaje': 'Respuesta creada'}), 201
    except pymssql.IntegrityError:
        return jsonify({'mensaje': 'La pregunta referenciada no existe'}), 400
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
    finally:
        conn.close()

@app.route('/Respuesta/<int:RespuestaID>', methods=['PUT'])
def update_respuesta(RespuestaID):
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE Respuesta SET 
                Respuesta = %s,
                Correcta = %s,
                idPregunta = %s
            WHERE RespuestaID = %s
        ''', (
            data.get('Respuesta'),
            data.get('Correcta'),
            data.get('idPregunta'),
            RespuestaID
        ))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'mensaje': 'Respuesta no encontrada'}), 404
        return jsonify({'mensaje': 'Respuesta actualizada'})
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()

@app.route('/Respuesta/<int:RespuestaID>', methods=['DELETE'])
def delete_respuesta(RespuestaID):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT 1 FROM Respuesta WHERE RespuestaID = %s', (RespuestaID,))
        if not cursor.fetchone():
            return jsonify({'mensaje': 'Respuesta no encontrada'}), 404
        
        cursor.execute('DELETE FROM Respuesta WHERE RespuestaID = %s', (RespuestaID,))
        conn.commit()
        
        return jsonify({'mensaje': 'Respuesta eliminada'})
    except pymssql.IntegrityError:
        return jsonify({'mensaje': 'No se puede eliminar la respuesta porque tiene registros relacionados'}), 400
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()

#========= Tabla Grixel ===========
@app.route('/Grixel', methods=['GET'])
def get_grixel():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Grixel')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/Grixel', methods=['POST'])
def create_grixel():
    data = request.json
    imagen_id = data['ImagenID']
    coor_x = data['CoorX']
    coor_y = data['CoorY']
    email_usuario = data.get('email_Usuario')
    id_pregunta = data['idPregunta_Pregunta']
    
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO Grixel (ImagenID, CoorX, CoorY, email_Usuario, idPregunta_Pregunta) 
            VALUES (%s, %s, %s, %s, %s)
        ''', (imagen_id, coor_x, coor_y, email_usuario, id_pregunta))
        conn.commit()
        return jsonify({'mensaje': 'Grixel creado'}), 201
    except pymssql.IntegrityError as e:
        return jsonify({'mensaje': 'Error de integridad: ' + str(e)}), 400
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
    finally:
        conn.close()

@app.route('/Grixel/<int:IDgrixel>/<int:ImagenID>', methods=['PUT'])
def update_grixel(IDgrixel, ImagenID):
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE Grixel SET 
                CoorX = %s,
                CoorY = %s,
                email_Usuario = %s,
                idPregunta_Pregunta = %s
            WHERE IDgrixel = %s AND ImagenID = %s
        ''', (
            data.get('CoorX'),
            data.get('CoorY'),
            data.get('email_Usuario'),
            data.get('idPregunta_Pregunta'),
            IDgrixel,
            ImagenID
        ))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'mensaje': 'Grixel no encontrado'}), 404
        return jsonify({'mensaje': 'Grixel actualizado'})
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()

@app.route('/Grixel/<int:IDgrixel>/<int:ImagenID>', methods=['DELETE'])
def delete_grixel(IDgrixel, ImagenID):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT 1 FROM Grixel WHERE IDgrixel = %s AND ImagenID = %s', (IDgrixel, ImagenID))
        if not cursor.fetchone():
            return jsonify({'mensaje': 'Grixel no encontrado'}), 404
        
        cursor.execute('DELETE FROM Grixel WHERE IDgrixel = %s AND ImagenID = %s', (IDgrixel, ImagenID))
        conn.commit()
        
        return jsonify({'mensaje': 'Grixel eliminado'})
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()

#=========Tabla Responde (log respuestas) ===========
@app.route('/Responde', methods=['GET'])
def get_responde():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Responde')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/Responde', methods=['POST'])
def create_responde():
    data = request.json
    fecha = data['Fecha']
    hora = data['Hora']
    email_usuario = data['email_Usuario']
    respuesta_id = data['RespuestaID']
    
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO Responde (Fecha, Hora, email_Usuario, RespuestaID) 
            VALUES (%s, %s, %s, %s)
        ''', (fecha, hora, email_usuario, respuesta_id))
        conn.commit()
        return jsonify({'mensaje': 'Registro de respuesta creado'}), 201
    except pymssql.IntegrityError as e:
        return jsonify({'mensaje': 'Error de integridad: ' + str(e)}), 400
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
    finally:
        conn.close()

@app.route('/Responde/<int:IDregistro>', methods=['PUT'])
def update_responde(IDregistro):
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE Responde SET 
                Fecha = %s,
                Hora = %s,
                email_Usuario = %s,
                RespuestaID = %s
            WHERE IDregistro = %s
        ''', (
            data.get('Fecha'),
            data.get('Hora'),
            data.get('email_Usuario'),
            data.get('RespuestaID'),
            IDregistro
        ))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'mensaje': 'Registro de respuesta no encontrado'}), 404
        return jsonify({'mensaje': 'Registro de respuesta actualizado'})
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()

@app.route('/Responde/<int:IDregistro>', methods=['DELETE'])
def delete_responde(IDregistro):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT 1 FROM Responde WHERE IDregistro = %s', (IDregistro,))
        if not cursor.fetchone():
            return jsonify({'mensaje': 'Registro de respuesta no encontrado'}), 404
        
        cursor.execute('DELETE FROM Responde WHERE IDregistro = %s', (IDregistro,))
        conn.commit()
        
        return jsonify({'mensaje': 'Registro de respuesta eliminado'})
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=2025)
