from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página principal: lista de usuários e formulário
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    
    if request.method == 'POST':
        # Adicionar novo usuário
        name = request.form['name']
        email = request.form['email']
        try:
            conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Email já existe!", 400
    
    # Consultar todos os usuários
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
