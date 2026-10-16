import mysql.connector

class Conexao:
    instancia = None
    def __new__(cls):
        if cls.instancia is None:
            print("Criando conexão com o banco...")
            cls.instancia = super().__new__(cls)
            cls.instancia.conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='loja_singleton'
            )
            return cls.instancia
    def get_conexao(self):
        return self.conexao