import sqlite3


def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")
    conn.commit()
    conn.close()

def save_username(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
    conn.commit()
    conn.close()

def get_username():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()  # Fetch the most recent username (it returns one row)
    conn.close()
    if row:
        return row[0]
    return None

#Checking if each functions are working as per expectation.
# if __name__ == "__main__":
#     init_db()

#     username = input("Enter your username: ")
#     save_username(username)

#     print("Stored username:", get_username())
