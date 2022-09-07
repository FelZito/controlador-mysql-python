from db_factory import *

print("GESTOR DE BANCO DE DADOS")

# Inserir valores no BD
nome = input("Informe o nome: ")
descricao = input("Informe a descrição: ")

inserir_DB(nome, descricao)

# Listar dados
listar_db()

# Fechar conexão
fecha_db()
