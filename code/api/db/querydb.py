import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def check_pt_number_of_words(conn, sentence):

    cur = conn.cursor()

    firstWord = True
    sql = "SELECT COUNT(*) FROM signs_pt WHERE word IN ("
    for w in sentence.split():
        if not firstWord:
            sql = sql + ", "
        sql = sql + "'" + w + "'"
        firstWord = False
    sql = sql + ")"

    cur.execute(sql)

    res=cur.fetchone()

    return res[0]

def check_pt_word(conn, word):

    cur = conn.cursor()
    cur.execute("SELECT COUNT(1) FROM signs_pt WHERE word = ?", (word,))

    res = cur.fetchone()

    return res[0]

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

        print("Does word 'coisa' exists in the database?")

        if(check_pt_word(conn, 'coisa') == 1):
            print('yes')
        else:
            print('no')

        sentence1 = "há um tempo um bom moço foi ter a minha casa"
        print("SENTENCE1: " + sentence1)
        print("How many words from SENTENCE1 are there in the database?")
        print(check_pt_number_of_words(conn, sentence1))

if __name__ == '__main__':
    main()
