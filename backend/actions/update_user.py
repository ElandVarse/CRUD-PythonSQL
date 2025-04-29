import sqlite3

def update_email(user_id, new_email):
    try:
        # Conecta ao banco
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Atualiza o email do usuário pelo ID
        cursor.execute('''
            UPDATE users
            SET email = ?
            WHERE id = ?
        ''', (new_email, user_id))

        # Verifica se algum registro foi alterado
        if cursor.rowcount == 0:
            print(f"Nenhum usuário encontrado com ID {user_id}.")
        else:
            print(f"Email do usuário ID {user_id} atualizado com sucesso! 🎯")

        conn.commit()

    except sqlite3.IntegrityError:
        print("Erro: esse email já está cadastrado para outro usuário.")
    
    finally:
        conn.close()

# Execução direta
if __name__ == "__main__":
    try:
        user_id = int(input("Digite o ID do usuário que você quer atualizar: "))
        new_email = input("Digite o novo email: ")
        update_email(user_id, new_email)
    except ValueError:
        print("ID inválido. Digite um número inteiro.")
