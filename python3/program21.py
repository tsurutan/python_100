# coding: UTF-8
import json
import codecs
text = ''
with codecs.open("jawiki-country.json", 'r', 'utf-8') as f:
    article_json = f.readline()
    while article_json:
        article_dict = json.loads(article_json)
        if article_dict["title"] == u"イギリス":
            text = article_dict["text"]
        article_json = f.readline()

strings = text.split("\n")
for string in strings:
    if u"Category" in string:
        print string