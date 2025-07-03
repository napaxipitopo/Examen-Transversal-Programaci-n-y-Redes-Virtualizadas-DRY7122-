#IGNACIO CATALAN
import sqlite3
import hashlib
from flask import Flask, request

app = Flask(__name__)
db_name = 'test.db'

# Crear tabla si no existe al inicio del servidor
def create_table():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS USERS (USERNAME TEXT PRIMARY KEY NOT NULL, HASH TEXT NOT NULL);')
    conn.commit()
    conn.close()

create_table()  # Llamar al inicio

@app.route('/')
def index():
    return 'Servidor de gestión de usuarios con contraseñas hasheadas corriendo en puerto 5800'

@app.route('/signup', methods=['POST'])
def signup():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    try:
        username = request.form['username']
        password = request.form['password']
        hash_value = hashlib.sha256(password.encode()).hexdigest()
        c.execute("INSERT INTO USERS (USERNAME, HASH) VALUES (?, ?);", (username, hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        return "El usuario ya está registrado"
    finally:
        conn.close()
    return "Registro exitoso"

def verify_user(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT HASH FROM USERS WHERE USERNAME = ?"
    c.execute(query, (username,))
    record = c.fetchone()
    conn.close()
    if not record:
        return False
    return record[0] == hashlib.sha256(password.encode()).hexdigest()

@app.route('/login', methods=['POST'])
def login():
    if verify_user(request.form['username'], request.form['password']):
        return "Inicio de sesión exitoso"
    else:
        return "Usuario o contraseña inválidos"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800)
#IGNACIO CATALAN