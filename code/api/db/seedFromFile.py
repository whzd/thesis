import json
import sqlite3
from sqlite3 import Error

# Create a DB connection to a file
def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e :
        print(e)

    return conn

# Create a Table in a given DB
def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# Insert Value to a Table in a given DB
def insert_sign(conn, table, value):

    sql = ''' INSERT INTO %s(value) VALUES (?) ''' % table

    try:
        c = conn.cursor()
        c.execute(sql, [sign])
        conn.commit()
    except Error as e:
        print(e)


# Import JSON file
def importFromJSONFile(filePath):
    try:
        file = open(filePath,)
        return json.load(file)
    except FileNotFoundError:
        print("The file " + file + " was not found.")

# Removes the JSON file header leaving only the table data
def removeFileHeader(jsonFileData):
    return jsonFileData[2]['data']

def main():

    table = "test"
    sql = ''' INSERT INTO %s(value) VALUES (?) ''' % table
    print(sql, [table])

if __name__ == '__main__':
    main()
