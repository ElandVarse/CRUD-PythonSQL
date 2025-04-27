import sqlite3
import bcrypt

def add_user(name, email, password):
    try:
        # Gera um hash da senha
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Conecta ao banco
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Insere o usuário
        cursor.execute('''
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
        ''', (name, email, hashed_password))

        conn.commit()
        print(f"Usuário '{name}' adicionado com sucesso! 🎉")

    except sqlite3.IntegrityError:
        print("Erro: esse email já está cadastrado!")
    
    finally:
        conn.close()

# Execução direta
if __name__ == "__main__":
    name = input("Digite o nome: ")
    email = input("Digite o email: ")
    password = input("Digite a senha: ")

    add_user(name, email, password)
