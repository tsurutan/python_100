col1 = [line.split("\t")[0] for line in open("hightemp.txt")]
count = {word: col1.count(word) for word in col1}
for word, freq in sorted(count.items(), key=lambda x: x[1], reverse=True):
    print freq, word
