import sqlite3

# Conectar ao banco e criar tabela
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Criar a tabela "users"
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# Salvar alterações e fechar
connection.commit()
connection.close()

print("Banco de dados criado com sucesso!")
