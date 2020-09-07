import json


CONST1 = 0.7
CONST2 = 0.3
CONST3 = 1
CONST4 = 0.5


# Calculates the readability score
def readability(configs, moments, hands, expressions):
    res = (CONST1 * configs + CONST2 * moments + CONST4 * expressions) * (CONST3 * hands)
    return res


#Imports JSON file
def importFromJSONFile(filePath):
    try:
        file = open(filePath,)
        return json.load(file)
    except FileNotFoundError:
        print("The file " + file + " was not found.")


# Removes the JSON file header leaving only the table data
def removeFileHeader(jsonFileData):
    return jsonFileData[2]['data']


# Extracts the important data from a JSON line
def extractSignData(jsonLine):
    word = jsonLine['word']
    moments = eval(jsonLine['config'])
    nrMoments = len(moments)
    configRight = set()
    configLeft = set()
    for mmt in moments:
        configRight.add(mmt['CONFR'])
        if(mmt['CONFL'] != "nenhumaL"):
            configLeft.add(mmt['CONFL'])
    return {'word': word, 'moments': nrMoments, 'configRight': len(configRight), 'configLeft': len(configLeft)}

# Finds the lowest and highst readability score from the table data
def findHighAndLowScore(tableData):
    highest = []
    lowest = []
    # Skip the 26 letters
    for sign in tableData[26:29]:
        signData = extractSignData(sign)
        print()
        print(signData)
        print()
        if(signData['configLeft'] > 0):
            score = readability((signData['configRight'] + signData['configLeft']), signData['moments'], 2, 1)
        else:
            score = readability(signData['configRight'], signData['moments'], 1, 1)
        print(score)

        #TODO find high and low signs bases on score


# Formats the formula print
def prettyPrint(configs, moments, hands, expressions):
    print("LGP Readability Formula")
    print()
    formula = "({} * Configs + {} * Moments + {} * Expressions) * ({} * Hands)".format(CONST1, CONST2, CONST4, CONST3)
    print(formula)


def manualRun():
    print()
    configs = int(input("Enter the number of hand configurations: "))
    moments = int(input("Enter the number of moments: "))
    hands = int(input("Enter the number of hands: "))
    expressions = int(input("Enter the number of facial expressions: "))
    print()
    prettyPrint(configs, moments, hands, expressions)
    print()
    res = readability(configs, moments, hands, expressions)
    print("Readability: " + str(res))


def fileRun():
    print()
    data = importFromJSONFile("wordsPT.JSON")
    tableData = removeFileHeader(data)
    findHighAndLowScore(tableData)


def main():
    print()
    print("LGP Expression Readability Calculator")
    print()
    print("1: Run with manual values.")
    print("2: Run from file.")
    print()
    option = int(input("Option: "))
    if(option == 1):
        manualRun()
    elif(option == 2):
        fileRun()


if __name__ == "__main__":
    main()
