

fh = open("./corpus-creation/result.txt")
fw = open("./neutral-words.txt","a")
for line in fh:

    tokens = line.split(",")
    gender = tokens[2]
    if(gender == "neutral"):
        fw.write(tokens[0]+"\n")

fh.close()
fw.close()


