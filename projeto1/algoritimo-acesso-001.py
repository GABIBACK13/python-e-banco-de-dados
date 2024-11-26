#tá nessa pasta pq esqueci de jogar pra outra e to com preguiça
import sqlite3
conn = sqlite3.connect('projeto1/exemplo.db')
cursor = conn.cursor()
create_table = """

CREATE TABLE IF NOT EXISTS comidas (

    id INTEGER PRIMARY KEY,

    nome TEXT NOT NULL,

    acessoA INTEGER,

    acessoB INTEGER,

    acessoC INTEGER

);

"""
cursor.execute(create_table)
#VARIAVEIS
insert_product = "INSERT INTO comidas (nome, acessoA, acessoB, acessoC) VALUES(?, ?, ?, ?)"
pull_off = "SELECT * FROM comidas"
salaA = "acessoA"
salaB = "acessoB"
salaC = "acessoC"
#FUNÇÕES
def ListAdd():
    nome = str(input("qual é o nome do funcionário:"))
    print("\n defina as permições:")
    acssA = int(input("o funcionário tem permissão para acessas a sala A?"))
    acssB = int(input("o funcionário tem permissão para acessas a sala B?"))
    acssC = int(input("o funcionário tem permissão para acessas a sala C?"))
    novoFuncionario = (nome,acssA,acssB,acssC)
    cursor.execute(insert_product,novoFuncionario)
    # atribui as permissões necessáirias e as adiciona no banco de dados. (bínario (0;1))
def chamarLista():
    cursor.execute(pull_off)
    funcionarios = cursor.fetchall()
    for f in funcionarios:
        print(f'\n{f}')
def acessRoom(sala,funcionario):
    x ="%"+f"{funcionario}"+"%"
    select = f"SELECT {sala}, * FROM comidas WHERE nome LIKE ?"
    cursor.execute(select,(x,))
    result = cursor.fetchall()
    ac= result[0]
    acesso = ac[0]
    if acesso == 0:
        return(f'\nAcesso Negado para o funcionário {funcionario}.\n\n')
    else:
        return(f'\nAcesso concedido para o funcionário {funcionario}.\n\n')
#CHAMADA DE FUNÇÃO

chamarLista()
#print(acessRoom(salaB,'Gabriel Back'))
#ListAdd()

#CLOSE
conn.commit()
conn.close()