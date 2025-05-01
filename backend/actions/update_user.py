import sqlite3

def update_email(user_id, new_email):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Tenta atualizar
        cursor.execute('''
            UPDATE users
            SET email = ?
            WHERE id = ?
        ''', (new_email, user_id))

        conn.commit()

        if cursor.rowcount == 0:
            return {"error": f"Nenhum usuário encontrado com ID {user_id}."}
        else:
            return {"message": f"Email do usuário ID {user_id} atualizado com sucesso! 🎯"}

    except sqlite3.IntegrityError:
        return {"error": "Esse email já está cadastrado para outro usuário."}

    except Exception as e:
        return {"error": f"Ocorreu um erro ao atualizar o email: {str(e)}"}

    finally:
        conn.close()
