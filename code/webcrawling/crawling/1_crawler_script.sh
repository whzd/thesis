#!/bin/bash

# download sites
wget \
--mirror  \
--recursive  \
--execute robots=off  \
--no-parent \
--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45' \
--random-wait \
--reject '*.js,*.css,*.ico,*.txt,*.gif,*.jpg,*.jpeg,*.png,*.mp3,*.pdf,*.tgz,*.flv,*.avi,*.mpeg,*.iso' \
--ignore-tags=img,link,script \
--header="Accept: text/html" \
--follow-tags=a \
--no-check-certificate \
--show-progress \
-l 2 \
--timestamping \
--adjust-extension \
-a /home/autoclipping/projeto/beta/crawler/log.txt \
--directory-prefix=/home/autoclipping/projeto/beta/crawler/files/ \
-i /home/autoclipping/projeto/beta/crawler/url_seed.txt

# apaga ficheiros nao html
cd /home/autoclipping/projeto/beta/crawler/files
find . -type f ! -name "*.html" -exec rm {} \;

# troca o ' por _ em alguns dos ficheiros descarregados
cd /home/autoclipping/projeto/beta/crawler/files
find . -type d -name "*'*" | while read f; do mv $f $(echo $f | sed "s/'/_/g"); done
find . -type f -name "*'*" | while read f; do mv $f $(echo $f | sed "s/'/_/g"); done

find . -type d -name "*’*" | while read f; do mv $f $(echo $f | sed "s/’/_/g"); done
find . -type f -name "*’*" | while read f; do mv $f $(echo $f | sed "s/’/_/g"); done

find . -type d -name "*º*" | while read f; do mv $f $(echo $f | sed "s/º/_/g"); done
find . -type f -name "*º*" | while read f; do mv $f $(echo $f | sed "s/º/_/g"); done

find . -type d -name '*\ *' | while read f; do mv "$f" $(echo $f | sed 's/\ /_/g'); done
find . -type f -name '*\ *' | while read f; do mv "$f" $(echo $f | sed 's/\ /_/g'); done