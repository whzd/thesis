# API

This folder contains the files responsible for creating the Explanation API.
The API components are listed in the [Content](https://github.com/whzd/thesis/tree/master/code/api#content) section and can work as standalone projects.

## How to run the API

It is required to have [Pyhton3](https://www.python.org/download/releases/3.0/) installed for this API.

It is also recommended to create a virtual environment to install and run the files.
To create a virtual environment use the following command:

```bash
python3 -m venv venv
```

This will create a virtual environment folder named `venv`.
To activate the venv use the following command:

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
. venv/bin/activate
```

If successfully activated a `(venv)` will appear at the start of the terminal line.

The packages required to be able to run the API are the following:

* bs4
* flask
* flask-cors
* nltk
* requests
* sqlite3

To install this packages use the following command, after having the venv activated:

```bash
pip3 install bs4 flask flask-cors nltk requests sqlite3
```

With all the packages installed, the API can be started with the following command:

```bash
pyhton3 app.py
```

This will make the API start at `127.0.0.1:5000` as shown in the terminal.

## Content

* [DB](https://github.com/whzd/thesis/tree/master/code/api/db)

* [Formula](https://github.com/whzd/thesis/tree/master/code/api/formula)

* [Summarization](https://github.com/whzd/thesis/tree/master/code/api/summarization)

* [Webscraping](https://github.com/whzd/thesis/tree/master/code/api/webscraping)
