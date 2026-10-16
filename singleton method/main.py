from conexao import Conexao
# solicita conexao
conexao = Conexao().get_conexao()
# cria um cursor para executar comandos sql
cursor = conexao.cursor()
#executa o comando para buscar todos os produtos
cursor.execute("SELECT * FROM produtos")
# converter os produtos par uma lista de produtos
produtos = cursor.fetchall() # [produtoA, produtoB]
# exibir os dados
for produto in produtos:
    print(produto)

# liberar os recursos usados pelo cursor
cursor.close()

