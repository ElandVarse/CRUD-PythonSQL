import sqlite3

def list_users():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row  # Faz o retorno ser um dicionário
    cursor = conn.cursor()

    cursor.execute('SELECT id, name, email, password FROM users')
    users = cursor.fetchall()
    conn.close()

    return [dict(user) for user in users]  # transforma cada linha em dict
