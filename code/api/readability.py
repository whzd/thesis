import sys
import string
import unidecode
from collections import OrderedDict
from db.querydb import DBQuery
from formula.lgp import LGPFormula

class Readability:

    #  Database query instance
    querydb = DBQuery()

    #  Readability formula instance
    formula = LGPFormula()

    #  Returns the readability score of a sentence
    def sentenceReadability(sentence):
        sentenceSum = 0
        wordCont = 0
        for word in sentence.split(' '):
            onlyWord = word.translate(str.maketrans('', '', string.punctuation))
            sentenceSum += Readability.wordReadability(onlyWord)
            wordCont += 1
        return round((sentenceSum / wordCont), 3)

    #  Returns the readability score of a word
    def wordReadability(word):
        queryResult = Readability.querydb.select_sign_by_word(word)
        if queryResult == None:
            charSum = 0
            charList = unidecode.unidecode(word)
            for char in charList:
                char = char.upper()
                charSum += Readability.charReadability(char)
            return charSum
        else:
            return Readability.formula.readability(queryResult['configs'], queryResult['moments'], queryResult['hands'], queryResult['facialExp'])

    #  Returns the readability score of a character
    def charReadability(char):
        queryResult = Readability.querydb.select_sign_by_word(char)
        #  In most cases a number
        if queryResult == None:
            return 1.5
        return Readability.formula.readability(queryResult['configs'], queryResult['moments'], queryResult['hands'], queryResult['facialExp'])

    def pretty(array):
        print("============================================")
        for context in array:
            for key,value in context.items():
                print(key, value)
            print("============================================")

    def dictionarySorting(dic):
        return OrderedDict(sorted(dic.items(), key=lambda x: x[1]))

if __name__ == "__main__":

    testArray = [['Género de banda desenhada de origem japonesa.'], ['Grande quantidade de gente.', 'Pastagem cercada para cavalos e bois.'], ['Fruto da mangueira, de formato oblongo, carnudo, de polpa amarela e fibrosa envolvendo um caroço grande, aromático e de sabor agradável.', 'Árvore grande (Mangifera indica), da família das anacardiáceas, de tronco liso, copa grande e frondosa, folhas perenes oblongas, flores pequenas dispostas em cachos, de origem asiática e muito cultivada em climas tropicais pelo seu fruto, a manga.'], ['Parte do vestuário que cobre o braço ou parte dele.', 'Objecto cuja forma se assemelha a essa parte do vestuário.', 'Filtro em forma de saco.', 'Tubo flexível.', 'Túnel regulável que liga a entrada de um avião a uma porta de embarque do aeroporto.', 'Mecanismo insuflável instalado em algumas saídas dos aviões, destinado à evacuação de passageiros em caso de emergência.', 'Extremidade do eixo em que entra a roda.', 'Dispositivo de forma cónica, que indica a direcção e a intensidade do vento.', 'Redoma; campânula.', 'Chaminé de candeeiro de malha metálica que aumenta a intensidade da luz.', "Tromba-d'água.", 'Chocalho grande.', 'Parte de uma competição, geralmente em provas de automobilismo ou de motociclismo.']]


    score = []
    for context in testArray:
        contextScore = {}
        for sentence in context:
            contextScore[sentence] = Readability.sentenceReadability(sentence)
        sorted_vec = Readability.dictionarySorting(contextScore)
        score.append(sorted_vec)
    Readability.pretty(score)


