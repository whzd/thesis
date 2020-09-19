import os
import sqlite3
from sqlite3 import Error

class DBQuery:

    # Setting filepath of the DB
    DATABASE = os.path.join(os.path.dirname(__file__), "pythonsqlite.db")

    # Create a DB connection
    def create_connection(self, db_file):

        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    # Select a sign based on a particular word
    def select_sign_by_word(self, word):
        """Gets the sign referent to a word

        Args:
            word (str): The word to search for

        Returns:
            dict: a dictionary containing the row data from the sign
        """

        conn = self.create_connection(self.DATABASE)

        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        sql = "SELECT * FROM wordsPT WHERE word=\"%s\"" % word
        cur.execute(sql)

        res = cur.fetchone()

        return res

if __name__ == '__main__':
    print("(DBQuery) Insert the word to search: ")
    word = input()
    print(select_sign_by_word(word))
