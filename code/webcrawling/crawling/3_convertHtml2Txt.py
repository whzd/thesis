import urllib.request
from bs4 import BeautifulSoup


with open("/home/autoclipping/projeto/beta/html_parser/files/files.txt") as p:
    filename = p.read()

    filename = filename.split('\n')

    for item in filename:

        try:

            with open("/home/autoclipping/projeto/beta/html_parser/files/"+item, "r") as f:

                contents = f.read()
            
        except:
            try:

                with open("/home/autoclipping/projeto/beta/html_parser/files/"+item, "r", encoding = "ISO-8859-1") as f:

                    contents = f.read()
            
            except:
    
                continue
        

        soup = BeautifulSoup(contents, 'lxml')


		# kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        try:
            text = soup.get_text(separator=' ')
        except:
            text = "CORPO DESCONHECIDO"

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # print(text)

        # get title
        try:
            titulo = soup.find('title').text.strip()
        except:
            titulo = "TITULO DESCONHECIDO"


        file1 = open("/home/autoclipping/projeto/beta/html_parser/results/"+item+".txt", "w")  # write mode
        file1.write(titulo)
        file1.write('\n')
        file1.write(text)
        file1.close()