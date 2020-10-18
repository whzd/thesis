class Priberam:
    URL = "https://dicionario.priberam.org/"
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def scrap(string):
        path = (Priberam.URL+string)
        source = requests.get(path, headers=Priberam.HEADERS).content
        soup = BeautifulSoup(source, "lxml")
        results = []

        ...

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
