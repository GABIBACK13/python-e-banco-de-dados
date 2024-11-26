import sqlite3

conexao = sqlite3.connect('escolaf.db')
cursor = conexao.cursor()

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
#FOREIGN KEY associa aluno_id na tabela notas com o id da tabela alunos. Garante que não existira notas para alunos inexistentes.

def inserir_aluno(nome, turma, notas):
    cursor.execute('INSERT INTO alunos (nome, turma) VALUES (?, ?)', (nome, turma))
    aluno_id = cursor.lastrowid
    # Inserir cada nota na tabela de notas
    for n in notas:
        cursor.execute('INSERT INTO notas (aluno_id, nota) VALUES (?, ?)', (aluno_id, n))

def retornar_log():
    cursor.execute('''
        SELECT alunos.id, alunos.nome, alunos.turma, notas.nota
        FROM alunos
        LEFT JOIN notas ON alunos.id = notas.aluno_id
    ''')
    resultados = cursor.fetchall()
    
    # Organizar as notas por aluno
    alunos_dict = {}
    for aluno_id, nome, turma, nota in resultados:
        if aluno_id not in alunos_dict:
            alunos_dict[aluno_id] = {"nome": nome, "turma": turma, "notas": []}
        alunos_dict[aluno_id]["notas"].append(nota)
    
    # Exibir os dados
    for aluno_id, dados in alunos_dict.items():
        print(f"\nID: {aluno_id},\n Nome: {dados['nome']},\n Turma: {dados['turma']},\n Notas: {dados['notas']}\n")

def calcular_media(lista):
    return round(sum(lista) / len(lista), 2)

def selecionar_notas(id):
    select_notas = "SELECT nota, aluno_id, * FROM notas WHERE aluno_id LIKE ?"
    cursor.execute(select_notas,(id,))
    list1 = cursor.fetchall()
    notas = [tupla[0] for tupla in list1]
    return  calcular_media(notas)

def retornar_log_turma(turma):
    t = f"{turma}"
    select = "SELECT alunos.id, * FROM alunos WHERE turma LIKE ?"
    cursor.execute(select,(t,))
    resultado = cursor.fetchall()
    id_list = [tupla[0] for tupla in resultado]
    name_list = [tupla[2] for tupla in resultado]
    turma_list = [tupla[3] for tupla in resultado]
    alunos_dict2 = {}
    idf = 0
    for id in id_list:
        if id not in alunos_dict2:
            alunos_dict2[id] = {"ID":id, "nome":name_list[idf], "turma":turma_list[idf], "media":selecionar_notas(id)}
        idf = idf + 1
    # Exibir os dados
    for chave, valor in alunos_dict2.items():
        print(f"{chave}: {valor}")

#CHAMADA DE FUNÇÃO
inserir_aluno("Ricardo Back", "B", 10)
conexao.commit()
conexao.close()