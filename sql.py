from flask import Flask, request, redirect, url_for, render_template_string
import sqlite3
import hashlib

app = Flask(_name_)

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
            conn.commit()
        except sqlite3.IntegrityError:
            return 'El usuario ya existe'
        finally:
            conn.close()
        return redirect(url_for('login'))
    return render_template_string('''
        <form method="post">
            Usuario: <input type="text" name="username"><br>
            Contraseña: <input type="password" name="password"><br>
            <input type="submit" value="Registrar">
        </form>
    ''')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password_hash = ?', (username, password_hash))
        user = cursor.fetchone()
        conn.close()
        if user:
            return f'Bienvenido {username}!'
        else:
            return 'Usuario o contraseña incorrecta'
    return render_template_string('''
        <form method="post">
            Usuario: <input type="text" name="username"><br>
            Contraseña: <input type="password" name="password"><br>
            <input type="submit" value="Iniciar sesión">
        </form>
    ''')

if _name_ == '_main_':
    app.run(port=5800)