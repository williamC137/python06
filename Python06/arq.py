import sqlite3
from modelos import Pessoa, Marca, Veiculo

#arquivo de como vai se chamar o banco
banco = sqlite3.connect('database.db')
#Ativar o uso da chave estrangeira para quando for chamada
banco.execute ("PRAGMA foreign_keys=on")
#para escrever em sql, para inserir os dados, deletar, as manipulações no banco
cursor = banco.cursor()


# cursor.execute("CREATE TABLE Pessoa(cpf text, nome text, nascimento text)")


# cursor.execute("CREATE TABLE Marca(nome text, sigla text)")


# cursor.execute("CREATE TABLE Veiculo (placa text, ano integer, cor text)")

# pessoa1 = Pessoa('4324454355','William','2004')
# pessoa1.cpf = 4324454355
# pessoa1.nome = 'William'
# pessoa1.nascimento = 2004
pessoas = [
    Pessoa('54654656', 'William', '2004'),
    Pessoa('54767666', 'Pedro', '1999')
]
#criando uma variável de inserção de dados
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento) VALUES (?, ?, ?);'''
cursor.executemany(comando,[(i.cpf, i.nome, i.nascimento) for i in pessoas])
# Salvar as alterações feitas nas tabela
banco.commit()
# VALUES(:cpf, :nome, :nascimento)
# cursor.execute(comando, vars(pessoas))
# print(vars(pessoas))




