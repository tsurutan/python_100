# coding: UTF-8
import codecs
f_col1 = codecs.open('col1.txt', 'w+', 'utf-8')
f_col2 = codecs.open('col2.txt', 'w+', 'utf-8')
for line in codecs.open('hightemp.txt', 'r', 'utf-8'):
    f_col1.write(line[0] + '\n')
    f_col2.write(line[1] + '\n')
