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
def create_table(conn, tableName, tableRowConfig):

    sql = """ CREATE TABLE IF NOT EXISTS %s (
    id integer PRIMARY KEY,
    """ % tableName

    keysLength = len(tableRowConfig.keys())
    for cfg in tableRowConfig.keys():
        if(keysLength == len(tableRowConfig.keys())):
            sql += "%s %s NOT NULL UNIQUE,\n" % (cfg, tableRowConfig[cfg])
            keysLength -= 1
        elif(keysLength != 1):
            sql += "%s %s NOT NULL,\n" % (cfg, tableRowConfig[cfg])
            keysLength -= 1
        else:
            sql += "%s %s NOT NULL\n" % (cfg, tableRowConfig[cfg])

    sql += ");"

    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

# Insert Rows into a Table in a given DB
def insert_row(conn, tableName, tableRow):

    sql = """ INSERT INTO %s( """ % tableName
    sql += (',').join(tableRow.keys())
    sql += ") VALUES ("

    valuesLength = len(tableRow.values())
    for val in tableRow.values():
        if(isinstance(val, str)):
            sql += "\"%s\"" % val
        else:
            sql += "%d" % val
        if(valuesLength != 1):
            sql += ","
            valuesLength -= 1

    sql += ")"

    try:
        c = conn.cursor()
        c.execute(sql)
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
    return jsonFileData[2]

# Filter table row data
def filterTableRow(rowData):

    word = rowData['word']
    moments = eval(rowData['config'])
    nrMoments = len(moments)

    nrFacialExp = 0
    configRight = set()
    configLeft = set()

    for mnt in moments:

        nrFacialExp += int(mnt['FE'])

        if(mnt['CONFR'] != "nenhumaR"):
            configRight.add(mnt['CONFR'])
        if(mnt['CONFL'] != "nenhumaL"):
            configLeft.add(mnt['CONFL'])

    if(len(configRight) > 0 and len(configLeft) > 0):
        nrHands = 2
    else:
        nrHands = 1

    nrConfigs = len(configRight)+len(configLeft)

    return {'word': word, 'moments': nrMoments, 'configs': nrConfigs, 'facialExp': nrFacialExp, 'hands': nrHands}


def main():

    # Import file
    fileData = importFromJSONFile("./wordsPT.JSON")
    table = removeFileHeader(fileData)

    # Create DB connection
    database = "./pythonsqlite.db"
    conn = create_connection(database)

    # Create table
    tableName = table['name']
    tableRowConfig = {'word': 'integer', 'moments': 'integer', 'configs': 'integer',
            'configs': 'integer', 'facialExp': 'integer', 'hands': 'integer'}
    create_table(conn, tableName, tableRowConfig)

    # Inset data into the created table
    for tableData in table['data']:
        tableRow = filterTableRow(tableData)
        insert_row(conn, tableName, tableRow)

if __name__ == '__main__':
    main()
