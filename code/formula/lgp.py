CONST1 = 0.7
CONST2 = 0.3
CONST3 = 1
CONST4 = 0.5

def readability(configs, moments, hands, expressions):
    res = (CONST1 * configs + CONST2 * moments + CONST4 * expressions) * (CONST3 * hands)
    return res

def prettyPrint(configs, moments, hands, expressions):
    print("LGP Readability Formula")
    print()
    formula = "({} * Configs + {} * Moments + {} * Expressions) * ({} * Hands)".format(CONST1, CONST2, CONST4, CONST3)
    print(formula)

def main():
    print()
    print("LGP Expression Readability Calculator")
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

if __name__ == "__main__":
    main()
