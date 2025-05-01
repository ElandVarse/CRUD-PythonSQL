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
        return {"message": f"Usuário '{name}' adicionado com sucesso! 🎉"}

    except sqlite3.IntegrityError:
        return {"error": "Email já cadastrado. Tente outro."}
    except Exception as e:
        return {"error": f"Erro ao adicionar usuário: {str(e)}"}
    finally:
        # Fecha a conexão
        if conn:
            conn.close()
