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
    cliente = input("Digite o nome do cliente: ")
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    
    valor_final = valor * quantidade

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO pedidos (cliente, produto, valor, quantidade, valor_final) VALUES (?, ?, ?, ?, ?)',
                   (cliente, produto, valor, quantidade, valor_final))
    connection.commit()
    connection.close()

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
    records = get_all_records()
    display_records(records)

    id = int(input("\nDigite o ID do pedido que deseja atualizar: "))
    cliente = input("Digite o novo nome do cliente: ")
    produto = input("Digite o novo nome do produto: ")
    valor = float(input("Digite o novo valor do produto: "))
    quantidade = int(input("Digite a nova quantidade: "))
    
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

def delete_record():
    records = get_all_records()
    display_records(records)

    id = int(input("\nDigite o ID do pedido que deseja excluir: "))
    
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM pedidos WHERE id=?', (id,))
    connection.commit()
    connection.close()

# Criar a tabela (execute apenas uma vez)
create_table()

while True:
    print("\nEscolha uma opção:")
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
