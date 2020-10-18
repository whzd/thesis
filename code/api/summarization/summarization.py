import os
import nltk
from string import punctuation
from heapq import nlargest
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# Get nltk tokenizer resource
nltk.download('punkt')
# Get nltk stopwords resource
nltk.download('stopwords')

# File source origin
directory = './files/'
# Set number of sentences the summary should have
MAX_SUMM_LENGHT = 7
# Set maximum sentence length
#MAX_SENT_LENGTH = 30

for filename in os.listdir(directory):

    file_path = os.path.join(directory, filename)
    f = open(file_path, 'r')

    title = f.readline()
    content = f.read()

    punctuation = punctuation + '\n'

    tokens = word_tokenize(content, language='portuguese')

    stop_words = stopwords.words('portuguese')

    word_frequencies = {}
    for word in tokens:
        if word.lower() not in stop_words:
            if word.lower() not in punctuation:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

    max_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    sentence_token = sent_tokenize(content, language='portuguese')

    sentence_scores = {}
    for s in sentence_token:
        sentence = s.split(" ")
        #Set maximum sentence length
        #if len(sentence) < MAX_SENT_LENGTH:
        for word in sentence:
            if word.lower() in word_frequencies.keys():
                if s not in sentence_scores.keys():
                    sentence_scores[s] = word_frequencies[word.lower()]
                else:
                    sentence_scores[s] += word_frequencies[word.lower()]

    final_summary = nlargest(MAX_SUMM_LENGHT, sentence_scores, key = sentence_scores.get)

    summary = '\n'.join(final_summary)

    newDirectory = './summaries/'
    newFilename = '%s.txt' % filename.split('.')[0]
    new_file_path = os.path.join(newDirectory, newFilename)
    if not os.path.isdir(newDirectory):
        os.mkdir(newDirectory)
    with open(new_file_path, 'w') as f:
        f.write(title)
        f.write('\n')
        f.write(summary)
