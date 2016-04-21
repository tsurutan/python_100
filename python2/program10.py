f = open("hightemp.txt")
print len([None for l in f])
print sum(1 for line in open("hightemp.txt"))