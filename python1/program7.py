# coding: utf-8
import sys
def customPrint(x, y, z):
    sys.stdout.write(str(x))
    sys.stdout.write("時の")
    sys.stdout.write(str(y))
    sys.stdout.write("は")
    sys.stdout.write(str(z))
    sys.stdout.write("\n")

customPrint(12, "気温", 22.4)