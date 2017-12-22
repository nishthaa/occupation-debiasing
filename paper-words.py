import create_corpus

fh = open("neutral.txt", "r")

data = fh.read()

words = data.split(",")

fw = open("paper-words.txt", "a")

for word in words:
    word = word.strip()
    word = word.lower()
    fw.write(word+"\n")

fw.close()
fh.close()
