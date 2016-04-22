# coding:utf-8

import json
import re

temp={}

f = open('jawiki-country.json', 'r')
for i,line in enumerate(f):
        temp[i]=json.loads(line)
f.close()

for k1,v1 in temp.iteritems():
        if temp[k1]["title"]==u"イギリス":
                temp_text_arr = temp[k1]["text"].split("\n")
                break

pos_start=""
pos_end=""
for i,line in enumerate(temp_text_arr):
        if line == u"{{基礎情報 国":
                pos_start = i
        if line == "}}":
                pos_end = i
                break

tmp=[]
temp_ans ={}
last_field=""
for i in range(pos_start+1,pos_end):
        if re.search('^\*', temp_text_arr[i]):
                temp_ans[last_field] += temp_text_arr[i]
        else:
                tmp = temp_text_arr[i].lstrip("|").split(" = ")
                temp_ans[tmp[0]]=tmp[1]
                last_field = tmp[0]

for k,v in temp_ans.iteritems():
        print k,'=',v
