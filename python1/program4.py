# coding: utf-8
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split(
    " ")
dic = {}
for i in range(0, len(str)):
    if i == 1 or (i > 4 and i < 10) or i == 15 or i == 16 or i == 19:
        dic[i] = str[i][0]
    else:
        dic[i] = str[i][0: 2]
print dic
