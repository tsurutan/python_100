# coding: UTF-8
import json
import re

with open("jawiki-country.json") as f:
    article_json = f.readline()
    while article_json:
        article_dict = json.loads(article_json)
        if article_dict["title"] == u"イギリス":
            text = article_dict["text"]
        article_json = f.readline()


strings = text.split('\n')
for line in strings:
    section_line = re.search(u"(File|ファイル):(.*?)\|", line)
    if section_line is not None:
        print section_line.group()
