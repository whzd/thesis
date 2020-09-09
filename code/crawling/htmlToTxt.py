import os
from bs4 import BeautifulSoup

directory = './raw-files/'

for filename in os.listdir(directory):

    file_path = os.path.join(directory, filename)
    f = open(file_path, 'r')

    content = f.read()

    soup = BeautifulSoup(content, 'lxml')

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text(separator=' ')

    lines = (line.strip() for line in text.splitlines())

    chunks = (line.strip() for line in lines)
    #chunks = (phrase.strip() for line in lines for phrase in line.split(' '))

    text = '\n'.join(chunk for chunk in chunks if chunk)


    title = soup.find('title').text.strip()

    newDirectory = './files/'
    newFilename = '%s.txt' % filename.split('.')[0]
    new_file_path = os.path.join(newDirectory, newFilename)
    if not os.path.isdir(newDirectory):
        os.mkdir(newDirectory)
    with open(new_file_path, 'w') as f:
        f.write(title)
        f.write('\n')
        f.write(text)
