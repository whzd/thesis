# Summarization

This folder contains the files responsible for creating the summarization of text from web pages.

It is recomended to create a virtual enviroment to install and run the files.
To create virtual enviroment use the following command:

```bash
pyhton -m venv venv
```

After its creation, it requires to be activated with the following command (linux users):

```bash
source /venv/bin/activate
```

The packages that require installation to be able to run the files are:

* scrapy

* bs4

* nltk

To install this packages use the following command:

```bash
pip install scrapy bs4 nltk
```

## 1. Crawling the web

To set the starting starting websites edit the `./spiders/configs/default.txt` file.

To run a default spider use the following command:

```bash
scrapy runspider spiders/default-spider.py
```

## 2. Converting HTML to text

To run the HTML to txt converter use the following command:

```bash
python
```

## 3. Summarizing the converted text

To run the summarization use the following command:

```bash
pyhton summarization.py
```
