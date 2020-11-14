import os
from collections import OrderedDict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Similarity:

    #  Folder containing the created summaries
    SOURCE = './summaries/'

    #  Global similarity array
    SIMILARITY_ARRAY = {}

    #  Minimum number of character a sentence must have in order to be accepted
    MIN_CHAR = 40

    #  Maximum number of similar sentences
    MAX_SENT_NUMBER = 5

    # Minimum cosine similarity accepted
    MIN_COSINE = 0.125

    def similarity(originalStr):
        Similarity.SIMILARITY_ARRAY = {}
        for filename in os.listdir(Similarity.SOURCE):
            file_path = os.path.join(Similarity.SOURCE, filename)
            f = open(file_path, 'r')
            #  Skip first line
            next(f)

            content = f.read()
            splited = content.split("\n")
            Similarity.fileSentenceSimilarity(originalStr,splited)

        res = Similarity.formatResult()
        return res

    #  Adds each sentence of
    def fileSentenceSimilarity(originalStr, sentences):
        for sentence in sentences:
            if len(sentence) > Similarity.MIN_CHAR:
                if "." in sentence:
                    vecSentence = sentence.split(".")
                    for newSent in vecSentence:
                        newSent = newSent.strip()
                        if len(newSent) > Similarity.MIN_CHAR:
                            Similarity.SIMILARITY_ARRAY[newSent] = Similarity.calculateSimilarity(originalStr, newSent)
                else:
                    Similarity.SIMILARITY_ARRAY[sentence] = Similarity.calculateSimilarity(originalStr, sentence)

    #  Formats result as an array of strings
    def formatResult():
        result = []
        sorted_vec = OrderedDict(sorted(Similarity.SIMILARITY_ARRAY.items(), key=lambda x: x[1], reverse=True))
        filtered_vec = list(sorted_vec.items())[:Similarity.MAX_SENT_NUMBER]
        for ele in filtered_vec:
            if ele[1] >= Similarity.MIN_COSINE:
                result.append(ele[0])
        return result

    # The higher the cosine value, the more simmilar two senteces are
    def calculateSimilarity(originalStr, newStr):
        original_tokens = word_tokenize(originalStr, language='portuguese')
        newStr_tokens = word_tokenize(newStr, language='portuguese')

        stop_words = stopwords.words('portuguese')

        original_set = { word for word in original_tokens if not word in stop_words}
        newStr_set = { word for word in newStr_tokens if not word in stop_words}

        original_list = []
        newStr_list = []

        keywords = original_set.union(newStr_set)
        for word in keywords:
            if word in original_set:
                original_list.append(1)
            else:
                original_list.append(0)
            if word in newStr_set:
                newStr_list.append(1)
            else:
                newStr_list.append(0)

        calcSum=0
        for i in range(len(keywords)):
            calcSum += original_list[i]*newStr_list[i]
        cosine = calcSum / float((sum(original_list)*sum(newStr_list))**0.5)

        return cosine

if __name__ == "__main__":
    orgSTR = "Fruto comestível da laranjeira, de forma esférica, casca dura e polpa dividida em secções, rodeadas por uma película fina."
    res = Similarity.similarity(orgSTR)
    print(res)
