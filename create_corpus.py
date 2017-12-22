from nltk.corpus import wordnet as wn

MALE_SPECIFIC = ["male", "he", "him", "man", "his", "masculine"]
FEMALE_SPECIFIC = ["female", "she", "woman","her", "feminine"]

OCCUPATIONS = []
OCCUPATION_NOT_FOUND = []
ALL_OCCUPATIONS = []
LOST_WORDS = []

def differentiator(word):

    male_score = 0
    female_score = 0

    try:

        # Pre-processing the words
        word = word.lower()
        word = word.strip()
        if word.find(" "):
            tmp = word.split()
            word = "_".join(tmp)


        if "-" in word:
            tmp = word.split("-")
            word = "_".join(tmp)

        ALL_OCCUPATIONS.append(word)

        # Finding the meanings from WordNet
        txt = wn.synsets(word)

        defn = txt[0].definition()
        tokenized_defn = defn.split()

        fh = open("result.txt", "a")



        for token in MALE_SPECIFIC:
            if(token in tokenized_defn):
                male_score+=1
                break

        for token in FEMALE_SPECIFIC:
            if(token in tokenized_defn):
                female_score+=1
                break

        data = open("result.txt").read()
        addition = ""
        if male_score > female_score:
            addition = word + "," + defn + ",specific,male\n"
        elif male_score < female_score:
            addition = word + "," + defn + ",specific,female\n"
        else:
            addition = word + "," + defn + ",neutral,none\n"


        if word not in OCCUPATIONS:
            OCCUPATIONS.append(word)
            fh.write(addition)

        fh.close()

    except Exception as err:

        OCCUPATION_NOT_FOUND.append(word)
        print("Definition not found for " + word,err)

def corpus_generator(filename):

    try:
        fhandle = open(filename)
        for line in fhandle:
            differentiator(line.strip())
        fhandle.close()




    except Exception as err:

        print(err)

corpus_generator("arcana-occupations.txt")
corpus_generator("occupations.txt")
corpus_generator("paper-words.txt")
