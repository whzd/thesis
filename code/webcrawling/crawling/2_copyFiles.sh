#!/bin/bash

find  /home/autoclipping/projeto/beta/crawler/files/ -name "*.html" | while IFS= read -r NAME; do
    flag_random=$(date '+%Y%m%d%H%M%S%N')$RANDOM
    cp -v "$NAME" /home/autoclipping/projeto/beta/html_parser/files/"$flag_random"
    echo "$NAME","$flag_random" >> /home/autoclipping/projeto/beta/html_parser/renameURL.txt
done
ls /home/autoclipping/projeto/beta/html_parser/files -I "*.txt" > /home/autoclipping/projeto/beta/html_parser/files/files.txt