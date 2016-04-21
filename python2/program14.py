# coding: UTF-8
import codecs
import sys
f = codecs.open('hightemp.txt', 'r', 'utf-8')
param = sys.argv
for i in range(0, int(param[1])):
    print f.readline().replace('\n', '')