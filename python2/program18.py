# coding: UTF-8
import codecs
hash = {}
f = codecs.open('hightemp.txt', 'r', 'utf-8')
for line in codecs.open('hightemp.txt', 'r', 'utf-8'):
    hash[float(line.split('\t')[2])] = line.replace('\n', '')
for key in sorted(hash, reverse=True):
    print hash[key]