import sqlite3

def delete_user(user_id):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return {"error": f"Nenhum usuário encontrado com ID {user_id}."}
        else:
            return {"message": f"Usuário ID {user_id} deletado com sucesso! 🗑️"}

    except Exception as e:
        return {"error": f"Erro ao deletar usuário: {str(e)}"}

    finally:
        conn.close()
