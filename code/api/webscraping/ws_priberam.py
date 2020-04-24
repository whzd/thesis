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
        notFound = soup.find('div', {'class': 'alert alert-info'})
        if(notFound==None):
            test=soup.find('sup', string="1")
            if(test!=None):
                section = test.find_next('p', attrs={'style':'padding-left:12px;margin:0;'})
                definition = section.find_next('span', {'class':'def'}).text
            else:
                section = soup.find('p', attrs={'style':'padding-left:12px;margin:0;'})
                definition = section.find_next('span', {'class':'def'}).text
        else:
            definition = "Não foram encontrados resultados."

        return definition

if __name__ == "__main__":
    print('(Priberam) Insira a palavra a pesquisar: ')
    string = input()
    res = Priberam.scrap(string)
    print(res)

