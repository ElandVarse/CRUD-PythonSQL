import sqlite3

def list_users():
    # Conecta ao banco de dados
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Pega todos os usuários
    cursor.execute('SELECT id, name, email, password FROM users')
    users = cursor.fetchall()

    if users:
        print("\nUsuários cadastrados:")
        print("----------------------")
        for user in users:
            print(f"ID: {user[0]} | Nome: {user[1]} | Email: {user[2]} | Senha: {user[3]}")
    else:
        print("Nenhum usuário encontrado.")

    # Fecha a conexão
    conn.close()

# Execução direta
if __name__ == "__main__":
    list_users()
