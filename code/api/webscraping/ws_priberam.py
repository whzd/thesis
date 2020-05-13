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
        notFound = soup.find('div', {'class': 'alert alert-info'})
        if(notFound==None):
            context=soup.find('sup')
            options = []
            if(context!=None):
                section = context.find_next('p', attrs={'style':'padding-left:12px;margin:0;'})
                definition = section.find_next('span', {'class':'def'}).text
                options.append(definition)
                results.append(options)
                options = []
                newContext = context.find_next('sup')
                while newContext!=None:
                    section = newContext.find_next('p', attrs={'style':'padding-left:12px;margin:0;'})
                    definition = section.find_next('span', {'class':'def'}).text
                    options.append(definition)
                    results.append(options)
                    options =[]
                    newContext = newContext.find_next('sup')
            else:
                options = []
                res = soup.find('div', {'id': 'resultados'})
                sections = res.find_all('p', attrs={'style':'padding-left:12px;margin:0;'})
                for x in sections:
                    number = x.find_next('span', attrs={'style': 'font-size:0.9em; color:#999;'})
                    if(number!=None):
                        definition = x.find_next('span', {'class':'def'}).text
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

