import sqlite3

def delete_user(user_id):
    # Conecta ao banco
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Deleta o usuário
    cursor.execute('''
        DELETE FROM users
        WHERE id = ?
    ''', (user_id,))

    # Verifica se algum usuário foi deletado
    if cursor.rowcount == 0:
        print(f"Nenhum usuário encontrado com ID {user_id}.")
    else:
        print(f"Usuário ID {user_id} deletado com sucesso! 🗑️")

    conn.commit()
    conn.close()

# Execução direta
if __name__ == "__main__":
    try:
        user_id = int(input("Digite o ID do usuário que você quer deletar: "))
        delete_user(user_id)
    except ValueError:
        print("ID inválido. Digite um número inteiro.")
