from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('SiteWeb-escola/escola.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods= ['GET', 'POST'])
def index():
    conn = get_db_connection()
    
    if request.method == 'POST':
        name = request.form['name']
        turma = request.form['turma']
        try:
            conn.execute('INSERT INTO alunos (name, turma) VALUES (?, ?)', (name, turma))
            conn.commit()
        except sqlite3.IntegrityError:
            return 'aluno já existe'
        
    alunos = conn.execute('SELECT * FROM alunos').fetchall()
    conn.close()
    return render_template('index.html', alunos = alunos)

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)