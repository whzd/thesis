import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_pt_sign_by_word(conn, word):

    cur = conn.cursor()
    cur.execute("SELECT * FROM signs_pt WHERE word=?", (word,))

    res = cur.fetchone()

    return res

def main():

    database = "db/pythonsqlite.db"

    conn = create_connection(database)

    if conn is not None:

        print("Sign with word 'coisa'.")

        print(select_pt_sign_by_word(conn, 'coisa'))

if __name__ == '__main__':
    main()
