# coding: utf-8
x = set()
y = set()


def biGram(set, str):
    for i in range(0, len(str) - 1):
        set.add(str[i : i + 2])

biGram(x, "paraparaparadise")
biGram(y, "paragraph")

print "X" , x
print "Y" , y

print "和集合" , x.union(y)
print "差集合" , x.difference(y)
print "積集合" , x.intersection(y)
print "seが存在するか X" , "se" in x
print "seが存在するか Y" , "se" in y
