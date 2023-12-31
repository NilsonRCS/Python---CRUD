import sqlite3
from prettytable import PrettyTable

def create_table():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            produto TEXT,
            valor REAL,
            quantidade INTEGER,
            valor_final REAL
        )
    ''')
    connection.commit()
    connection.close()

def insert_record():
    try:
        cliente = input("Nome do cliente: ")
        produto = input("Pedido: ")
        valor = float(input("Valor do produto: "))
        quantidade = int(input("Quantidade: "))
        
        if valor < 0 or quantidade < 0:
            print("Valor e quantidade devem ser números positivos.")
            return

        valor_final = valor * quantidade

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO pedidos (cliente, produto, valor, quantidade, valor_final) VALUES (?, ?, ?, ?, ?)',
                       (cliente, produto, valor, quantidade, valor_final))
        connection.commit()
        connection.close()
        print("Pedido inserido com sucesso.")
    except ValueError:
        print("Erro ao inserir pedido. Certifique-se de fornecer valores válidos.")

def get_all_records():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM pedidos')
    rows = cursor.fetchall()
    connection.close()
    return rows

def display_records(records):
    table = PrettyTable()
    table.field_names = ["ID", "Cliente", "Produto", "Valor", "Quantidade", "Valor Final"]
    for record in records:
        table.add_row(record)
    print(table)

def update_record():
    try:
        records = get_all_records()
        display_records(records)

        id = int(input("\nDigite o ID do pedido que deseja atualizar: "))
        
        # Verifica se o ID existe na tabela
        if not any(record[0] == id for record in records):
            print("Pedido não encontrado.")
            return

        cliente = input("Atualizar dados do cliente: ")
        produto = input("Atualizar dados do produto: ")
        valor = float(input("Atualizar valor do produto: "))
        quantidade = int(input("Atualizar a quantidade: "))
        
        if valor < 0 or quantidade < 0:
            print("Valor e quantidade devem ser números positivos.")
            return

        valor_final = valor * quantidade

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE pedidos 
            SET cliente=?, produto=?, valor=?, quantidade=?, valor_final=?
            WHERE id=?
        ''', (cliente, produto, valor, quantidade, valor_final, id))
        connection.commit()
        connection.close()
        print("Pedido atualizado com sucesso.")
    except ValueError:
        print("Erro ao atualizar pedido. Certifique-se de fornecer valores válidos.")

def delete_record():
    try:
        records = get_all_records()
        display_records(records)

        id = int(input("\Informe o ID do pedido que deseja excluir: "))
        
        # Verifica se o ID existe na tabela
        if not any(record[0] == id for record in records):
            print("Pedido não encontrado.")
            return

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM pedidos WHERE id=?', (id,))
        connection.commit()
        connection.close()
        print("Pedido excluído com sucesso.")
    except ValueError:
        print("Erro ao excluir pedido. Certifique-se de fornecer um ID válido.")

# Criar a tabela (execute apenas uma vez)
create_table()

while True:
    print("\nProjetinho CRUD:")
    print("1 - Inserir um novo pedido")
    print("2 - Visualizar todos os pedidos")
    print("3 - Atualizar um pedido")
    print("4 - Excluir um pedido")
    print("0 - Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        insert_record()
    elif escolha == '2':
        records = get_all_records()
        display_records(records)
    elif escolha == '3':
        update_record()
    elif escolha == '4':
        delete_record()
    elif escolha == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")
