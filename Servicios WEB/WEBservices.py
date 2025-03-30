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
    
    """cursor.execute('INSERT INTO Test (id, name, email) VALUES (%s,%s, %s)', (email, NombreUsuario))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Registro creado'}), 201""" 
    # Comente lo de arriba pq quiero intentar lo de abajo avr que onda, es para validar si ya existe el usuario

    try:
        cursor.execute('INSERT INTO Usuario (email, NombreUsuario) VALUES (%s, %s)', (email, nombreUsuario))
        conn.commit()
        return jsonify({'mensaje': 'Usuario creado'}), 201
    except pymssql.IntegrityError:
        return jsonify({'mensaje': 'El email ya existe'}), 400
    finally:
        conn.close()

@app.route('/Usuario/<string:email>', methods=['GET'])
def get_usuario_by_email(email):
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Usuario WHERE email = %s', (email,))
    data = cursor.fetchone()
    conn.close()
    if data is None:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404
    return jsonify(data)

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

# ===== Tabla preguntas =====
@app.route('/Pregunta', methods=['GET'])
def get_preguntas():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Pregunta;') #No regresa la respuesta porque sería peligroso que los usuarios pudieran acceder a ella
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

    @app.route('/preguntas/<int:id>', methods=['GET'])
def get_pregunta(id):
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Pregunta WHERE idPregunta = %s', (id,))
    data = cursor.fetchone()
    conn.close()
    if data:
        return jsonify(data)
    else:
        return jsonify({'mensaje': 'Pregunta no encontrada'}), 404

# ===== Tabla imagen =====
@app.route('/Imagen', methods=['GET'])
def get_imagen():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT ImagenID, Activo, fechaInicio, fechaFinalizacion FROM Imagen;') #No regresa la respuesta porque sería peligroso que los usuarios pudieran acceder a ella
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/Imagen', methods=['POST'])
def post_imagen():
    data = request.json
    email = data['email']
    NombreUsuario = data['NombreUsuario']
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO Usuario (email, NombreUsuario) VALUES (%s, %s)', (email, nombreUsuario))
        conn.commit()
        return jsonify({'mensaje': 'Usuario creado'}), 201




@app.route('/Respuesta', methods=['GET}'])
def get_Imagen():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT RespuestaID, Respuesta FROM Respuesta;') #No regresa si la respuesta es correcta o no por la misma razóm

    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/Responde', methods=['GET'])
def get_Imagen():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Responde;')

    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/Grixel', methods=['GET'])
def get_Imagen():
    conn = get_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Grixel;')

    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/test/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    name = data['name']
    email = data['email']
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Test SET name = %s, email = %s WHERE id = %s', (name, email, id))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Registro actualizado'})

@app.route('/test/<int:id>', methods=['DELETE'])
def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Test WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Registro borrado'})

if __name__ == '__main__':
    app.run(debug=True, port=2025)
