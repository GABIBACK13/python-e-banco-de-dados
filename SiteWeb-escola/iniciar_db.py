import sqlite3 

conn = sqlite3.connect('SiteWeb-escola/escola.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        turma TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER,
        nota REAL NOT NULL,
        FOREIGN KEY (aluno_id) REFERENCES alunos (id)
    )
''')

conn.commit()
conn.close()
print("Banco de dados criado com sucesso!")