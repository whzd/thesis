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
