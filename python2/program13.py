# coding: UTF-8
import codecs
f_col1 = codecs.open('col1.txt', 'r', 'utf-8')
f_col2 = codecs.open('col2.txt', 'r', 'utf-8')
f_join = codecs.open('join.txt', 'w+', 'utf-8')
for i in range(0, 15):
    str = (f_col1.readline(0) + "\t" + f_col2.readline(0)).replace("\n", "")
    f_join.write(str + '\n')