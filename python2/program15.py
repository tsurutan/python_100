# coding: UTF-8
import codecs
import sys

f = codecs.open('hightemp.txt', 'r', 'utf-8')
param = sys.argv
max_size = sum(1 for line in open("hightemp.txt"))
for i, line in enumerate(codecs.open('hightemp.txt', 'r', 'utf-8')):
    if (i > sum(1 for line in open("hightemp.txt")) - int(param[1]) - 1):
        print line.replace('\n', '')
