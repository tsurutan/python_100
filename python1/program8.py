# coding: utf-8
def cipher(string):
    char = ""
    for c in string:
        if c.islower():
            char += chr(219 - ord(c))
        else:
            char += c
    return char

print cipher("tsuruta atsuhiro")
print cipher(cipher("tsuruta atsuhiro"))
