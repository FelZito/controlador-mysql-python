import mysql.connector
db_connect = mysql.connector.connect(host="localhost", user="root", password="root1402@123", database="loja_virtual")
cursor = db_connect.cursor()

def inserir_DB(nome, descricao):
    values = (nome, descricao)
    sql_insert = "INSERT INTO PRODUTO (nome, descricao) VALUES (%s, %s)"
    cursor.execute(sql_insert, values)
    db_connect.commit()

def listar_db():
    sql_list = ("SELECT * FROM PRODUTO")
    cursor.execute(sql_list)
    print("ID || NOME || DESCRIÇÃO")
    for (id, nome, descricao) in cursor:
        print(id, nome, descricao)
    db_connect.commit()

def fecha_db():
    db_connect.close()