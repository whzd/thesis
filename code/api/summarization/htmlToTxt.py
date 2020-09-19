import os
from bs4 import BeautifulSoup
import re

directory = './raw-files/'

# Average number of character in a sentence in English (75-100)
# Minimum number of character a sentence must have in order to be accepted
MIN_CHAR = 50

for filename in os.listdir(directory):

    file_path = os.path.join(directory, filename)
    f = open(file_path, 'r')

    content = f.read()

    soup = BeautifulSoup(content, 'lxml')

    paragraphs = soup.find_all('p')
    text = ''
    for p in paragraphs:
        if (len(p.text) > MIN_CHAR):
            text += p.text

    #Cleaning data
    # Remove square brackets
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)


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
