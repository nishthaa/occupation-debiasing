from nltk.corpus import wordnet as wn

MALE_SPECIFIC = ["male", "he", "him", "man", "his", "masculine"]
FEMALE_SPECIFIC = ["female", "she", "woman","her", "feminine"]

def differentiator(word):

    try:
        word = word.lower()
        txt = wn.synsets(word)
        print(txt)
        defn = txt[0].definition()
        print(defn)
        tokenized_defn = defn.split()
        print(tokenized_defn)

        fh = open("result.txt", "a")

        for token in MALE_SPECIFIC:
            if(token in tokenized_defn):
                print(defn.find(token))
                addition = word + "," + "specific,male\n"
                fh.write(addition)
                return

        for token in FEMALE_SPECIFIC:
            if(token in tokenized_defn):
                addition = word + "," + "specific,female\n"
                fh.write(addition)
                return

        fh.write(word + ",neutral,none\n")
        fh.close()
    except:

        print("Definition not found for " + word)

def corpus_generator(filename):

    try:
        fhandle = open(filename)
        for line in fhandle:
            differentiator(line.strip())

        fhandle.close()

    except Exception as err:

        print(err)

corpus_generator("occupations.txt")

#differentiator("zoologist")
