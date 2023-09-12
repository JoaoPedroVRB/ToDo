import sqlite3

conexao = sqlite3.connect("EXERCICIO_M2S4.sqlite3")

cursor = conexao.cursor()

def insert():
    tarefas = input("Quantas tarefas deseja adicionar ? ")
    tarefas_1 = int(tarefas)
    for i in range(tarefas_1):
        desc_tarefa = input("Qual a descrição de suas tarefa ? ")
        data_tarefa = input("Qual a data que sua tarefa deve ser executada ? ")
        sql = """SELECT * FROM categoria"""
        categorias = cursor.execute(sql)
        conexao.commit()
        for categoria in categorias:
            print(categoria)
        categoria_id = input("Qual categoria sua tarefa pertence ? ")
        categoria_id = int(categoria_id)
        sql = """
        INSERT INTO tarefa (desc_tarefa, data_tarefa, categoria_id) VALUES (?,?,?)
        """
        valores = [desc_tarefa, data_tarefa, categoria_id,]

        cursor.execute(sql, valores)
        conexao.commit()

def insert_cat():
    quant = input("Quantas categoria deseja cria?\n")
    quant = int(quant)
    for categoria in range(quant):
        descricao = input("Qual a nova categoria que deseja adicionar? \n")
        sqlA ="""INSERT INTO categoria (descricao) VALUES (?)"""
        valor = [descricao]
        cursor.execute(sqlA,valor)
        conexao.commit()

def update():
    pergunta = input("Deseja atualizar qual coluna ?  1) descrição da tarefa. 2) dia de realizar a tarefa. 3) mudar a categoria da trefa ")
    pergunta1 = int(pergunta)
    if pergunta1 == 1:
        coluna = input('Qual a nova descrição de tarefa ? ')
        sql2 = """SELECT * FROM tarefa;"""
        lista = cursor.execute(sql2)
        for tarefa in lista:
            print(tarefa)
        id = input("Qual é o id que deseja atualizar ? ")
        id = int(id)
        sql = """ UPDATE tarefa SET desc_tarefa = ? WHERE id = ? """
        valores = [coluna, id]
        cursor.execute(sql, valores)  
        conexao.commit()
    elif pergunta1 == 2:
        coluna2 = input('Qual o novo dia de realizar a tarefa ? ')
        sql3 = """SELECT * FROM tarefa"""
        lista2 = cursor.execute(sql3)
        for dia in lista2:
            print(dia)
        id2 = input("Qual é o id que deseja atualizar ? ")
        id2 = int(id2)
        sql4 = """UPDATE tarefa SET data_tarefa = ? WHERE id = ?"""
        valores2 = [coluna2, id2]
        cursor.execute(sql4, valores2)
        conexao.commit()
    elif pergunta1 == 3:
        sql5 = """SELECT * FROM categoria"""
        lista3 = cursor.execute(sql5)
        for categoria in lista3:
            print(categoria)
        coluna3 = input("Qual sera o novo id ? ")
        coluna3 = int(coluna3)
        sql6 = """SELECT * FROM tarefa"""
        lista4 = cursor.execute(sql6)
        for categoria2 in lista4:
            print(categoria2)
        id3 = input("Qual é o id que deseja atualizar ? ")
        id3 = int(id3)
        sql7 ="""UPDATE tarefa SET categoria_id = ? WHERE id = ?"""
        valores3 = [coluna3, id3]
        cursor.execute(sql7,valores3)
        conexao.commit()

def up_cat():
    desc = input("Qual o novo nome da categoria ?\n")
    sqlB2 ="""SELECT * FROM categoria"""
    lista = cursor.execute(sqlB2)
    for list in lista:
        print(list)
    id = input("Qual id da categoria deseja atualizar ?\n")
    id = int(id)
    sqlB = """UPDATE categoria SET descricao = ? WHERE id = ?"""
    valores = [desc,id]
    cursor.execute(sqlB,valores)
    conexao.commit()

def delete():
    sql = """ SELECT * FROM tarefa;"""
    tarefas = cursor.execute(sql)
    for tarefa in tarefas:
        print(tarefa)
    id = input("Digite o id que deseja excluir. ")
    id = int(id)
    sql = """ DELETE FROM tarefa WHERE id = ?"""
    valor = [id] 
    cursor.execute(sql,valor) 
    conexao.commit()

def delete_cat():
    sqlc = """SELECT * FROM categoria"""
    categorias = cursor.execute(sqlc)
    for categoria in categorias:
        print(categoria)
    id = input("Digite o id da categoria que deseja apagar.\n")
    id = int(id)
    sqlC= """DELETE FROM categoria WHERE id = ?"""
    valor = [id]
    cursor.execute(sqlC,valor)
    conexao.commit()

def filtro_dia():
    data = input("Qual a data da tarefa que você esta procurando ?")
    sql ="""SELECT * FROM tarefa WHERE data_tarefa = ?"""
    valor = [data]
    listas = cursor.execute(sql,valor)
    for lista in listas:
        print(lista)
    conexao.commit()

def select():
    sql = """ SELECT * FROM categoria"""
    lista = cursor.execute(sql)
    for categoria in lista:
        print(categoria)
    conexao.commit()

def up_status():
    sql ="""SELECT * FROM tarefa"""
    lista = cursor.execute(sql)
    for list in lista:
        print(list)
    id = input("Qual id voçê deseja marcar como concluido ? ")
    id = int(id)
    sql2 = """UPDATE tarefa SET status = 'concluido' WHERE id = ?"""
    valor = [id]
    cursor.execute(sql2,valor)
    conexao.commit()


inicio = input("Digite o numero da tabela que deseja mexer ?\n1)Tabela tarefa\n2)Tabela categoria\n")
inicio = int(inicio)
if inicio == 1:
    while True:
        opcao = input("Digite o numero da opção que deseja escolher.\n1)Deseja criar uma tarefa nova?\n2)Deseja atualizar uma tarefa?\n3)Deseja excluir uma tarefa?\n4)Deseja filtrar as tarefas por dia?\n5)Deseja marcar uma tarefa como concluida?\n6)Deseja sair do sistema?\n")
        opcao = int(opcao)
        if opcao == 1:
            insert()
        elif opcao == 2:
            update()
        elif opcao == 3:
            delete()
        elif opcao == 4:
            filtro_dia()
        elif opcao == 5:
            up_status()
        elif opcao == 6:
            conexao.close()
            break
elif inicio == 2:
    while True:
        opcao = input("Digite o numero da opção que deseja escolher.\n1)Deseja criar uma categoria nova?\n2)Deseja atualizar uma categoria?\n3)Deseja excluir uma categoria?\n4)Deseja ver todas as categorias?\n5)Deseja sair do sistema?\n")
        opcao = int(opcao)
        if opcao == 1:
            insert_cat()
        elif opcao == 2:
            up_cat()
        elif opcao == 3:
            delete_cat()
        elif opcao == 4:
            select()
        elif opcao == 5:
            conexao.close()
            break