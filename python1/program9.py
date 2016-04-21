# coding: utf-8
import random
def randomString(value):
    string = ""
    for s in value.replace(".", " .").split():
        string += " " + typo(s)
    print string

def typo(word):
    if len(word) > 4:
        wordTmp = list(word[1 : -1])
        random.shuffle(wordTmp)
        return word[0] + ''.join(wordTmp) + word[-1]
    else:
        return word

randomString("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")