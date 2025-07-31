import mysql.connector

conexao = mysql.connector.connect (
    host='localhost',
    user='root',
    password = '',
    database = 'db_registros',
)

cursor = conexao.cursor()

var_choice = str(input('Deseja inserir, mostrar, editar ou deletar os valores? [I/M/E/D]: '))

if var_choice.upper() == 'I':

    while True: 
        nome_produto = str(input('Digite o nome do produto: '))
        valor_produto = int(input('Digite o valor do produto: '))

        comando = f'INSERT INTO vendas(nome_produto, valor_produto) VALUES ("{nome_produto}", {valor_produto})'
        cursor.execute(comando)
        conexao.commit() #edita o banco de dados

        var_choice = str(input('Deseja continuar? [S/N]: '))

        if var_choice.upper() == 'N': 
            break
elif var_choice.upper() == 'M': 
        comando_sel = 'SELECT * FROM vendas'
        cursor.execute(comando_sel)
        resultado_sel = cursor.fetchall()

        print(resultado_sel)
elif var_choice.upper() == 'E': 
    var_produto = str(input('Digite o nome do produto que você deseja editar: '))
    var_new_produto = str(input('Digite o novo nome do produto: '))
    var_new_valor = int(input('Digite o novo valor do produto: '))
    comando = f'UPDATE vendas SET valor_produto = {var_new_valor}, nome_produto = "{var_new_produto}" WHERE nome_produto = "{var_produto}"'
    cursor.execute(comando)
    conexao.commit()
elif var_choice.upper() == 'D': 
    var_nome_produto = str(input('Digite o nome do produto que você deseja deletar: '))
    comando = f'DELETE FROM vendas WHERE nome_produto = "{var_nome_produto}"'
    cursor.execute(comando)
    conexao.commit()

cursor.close()
conexao.close()
