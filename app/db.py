import sqlite3

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL
                    )""")

    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect("users.db")

def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password), )
    conn.commit()
    conn.close()

def get_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users WHERE username=?", (username,), )
    user = cursor.fetchone()
    conn.close()
    return user

def delete_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username=?", (username,), )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()