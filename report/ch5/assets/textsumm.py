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
