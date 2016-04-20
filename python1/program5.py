# coding: utf-8
def nGram(n, str):
    for i in range(0, len(str) - 1):
        print str[i: i + n]

def biGram(str):
    nGram(2, str)

def nGramWord(n, str):
    words = str.split(" ")
    for i in range(0, len(words) - n + 1):
        word = ""
        for j in range(0, n):
            word += words[i + j]
        print word

def biGramWord(str):
    nGramWord(2, str)

biGramWord("I am an NLPer")
biGram("I am an NLPer")
