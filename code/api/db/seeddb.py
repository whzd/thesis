import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn = None
    try:
        conn= sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_sign_PT(conn, sign):

    sql = ''' INSERT INTO signs_pt(word)
              VALUES (?) '''
    cur = conn.cursor()
    cur.execute(sql, [sign])
    conn.commit()

    return cur.lastrowid

def create_sign_EN(conn, sign):

    sql = ''' INSERT INTO signs_en(word)
              VALUES (?) '''
    cur = conn.cursor()
    cur.execute(sql, [sign])
    conn.commit()

    return cur.lastrowid

def tables(conn):


    sql_create_signs_pt_table = """ CREATE TABLE IF NOT EXISTS signs_pt (
                                            id integer PRIMARY KEY,
                                            word text NOT NULL
                                    ); """

    sql_create_signs_en_table = """ CREATE TABLE IF NOT EXISTS signs_en (
                                            id integer PRIMARY KEY,
                                            word text NOT NULL
                                    ); """

    if conn is not None:

        create_table(conn, sql_create_signs_pt_table)

        create_table(conn, sql_create_signs_en_table)

    else:

        print("Error! cannot create the database connection for tables.")

def rows(conn):

    wordsPT = ['coisa', 'casa', 'tempo', 'ano', 'dia', 'vez', 'homem',
                'senhor', 'senhora', 'moço', 'moça', 'bom', 'grande', 'melhor',
                'pior', 'certo', 'último', 'próprio', 'ser', 'ir', 'estar',
                'ter', 'haver', 'fazer', 'dar', 'ficar', 'poder', 'ver', 'não',
                'mais', 'muito', 'já', 'quando', 'mesmo', 'depois', 'ainda',
                'um', 'dois', 'primeiro', 'cem', 'mil']

    wordsEN = ['be', 'have', 'not', 'do', 'say', 'will', 'one', 'all',
                'would', 'up', 'out', 'about', 'get', 'go', 'make', 'can',
                'like', 'time', 'no', 'know', 'take', 'people', 'year', 'good'
                'some', 'could', 'see', 'other', 'look', 'come', 'think']

    if conn is not None:

        for wPT in wordsPT:
            sign_id = create_sign_PT(conn, wPT)

        for wEN in wordsEN:
            sign_id = create_sign_EN(conn, wEN)

    else:

        print("Error! cannot create the database connection for rows.")


def main():

    database = r"pythonsqlite.db"

    conn = create_connection(database)

    tables(conn)
    rows(conn)

if __name__ == '__main__':
    main()
