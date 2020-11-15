from bs4 import BeautifulSoup
import requests
import sys

class Priberam:

    URL = "https://dicionario.priberam.org/"
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def scrap(string):
        path = (Priberam.URL+string)
        source = requests.get(path, headers=Priberam.HEADERS).content
        soup = BeautifulSoup(source, "lxml")
        results = []
        sublteTest = soup.find('div', {'id': 'resultados'})
        notFoundSubtle = sublteTest.find_next('b').text.strip()
        if(notFoundSubtle == "Palavra não encontrada"):
            notFound = notFoundSubtle
        else:
            notFound = soup.find('div', {'class': 'alert alert-info'})
        if(notFound==None):
            multipleContexts = soup.find('sup')
            if ' ' in string :
                results.append(["Funcionalidade ainda não implementada."])
                #expression = soup.find_all('span', text=string , attr={'class':'def'})
                #expreDef = expression.find_next_sibling('span', attr={'class':'def'})
            elif multipleContexts != None :
                targetBlock = soup.find('div', {'style': 'padding:10px;border:2px solid #d0d2d7;-webkit-border-radius: 2px;-moz-border-radius: 2px;border-radius: 2px;'})
                typoMsg = soup.find('div', {'style': 'margin-top:10px;'})
                if typoMsg != None :
                    targetBlock = typoMsg
                skipBlock = targetBlock.find_next_sibling('div')
                res = skipBlock.find_next_sibling('div')
                allDivs = res.find_all('div')
                for t in allDivs:
                    options = []
                    numberOne = False
                    isContext = t.find_next('sup')
                    if(isContext!=None):
                        sections = t.find_all('p', attrs={'style':'padding-left:12px;margin:0;'})
                        for x in sections:
                            number = x.find_next('span', attrs={'style': 'font-size:0.9em; color:#999;'})
                            if number != None :
                                number = number.text.strip()
                                definition = x.find_next('span', {'class':'def'}).text
                                if number=="1." and not numberOne :
                                    options.append(definition)
                                    numberOne = True
                                if number!="1." and numberOne:
                                    options.append(definition)
                        if options :
                            results.append(options)
            else:
                res = soup.find('div', {'id': 'resultados'})
                options = []
                isComplex = res.find('span', attrs={'style': 'font-size:0.9em; color:#999;'})
                if isComplex != None :
                    sections = res.find_all('p', attrs={'style':'padding-left:12px;margin:0;'})
                    for x in sections:
                        number = x.find_next('span', attrs={'style': 'font-size:0.9em; color:#999;'})
                        if(number!=None):
                            definition = x.find_next('span', {'class':'def'}).text
                            options.append(definition)
                else:
                    section = res.find('p', attrs={'style':'padding-left:12px;margin:0;'})
                    definition = section.find_next('span', {'class':'def'}).text
                    options.append(definition)
                results.append(options)
        else:
            results.append(["Não foram encontrados resultados."])

        return results

if __name__ == "__main__":
    print('(Priberam) Insira a palavra a pesquisar: ')
    string = input()
    res = Priberam.scrap(string)
    print(res)

