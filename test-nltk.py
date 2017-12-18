from nltk.corpus import wordnet as wn

MALE_SPECIFIC = ["male", "he", "him", "man", "his", "masculine"]
FEMALE_SPECIFIC = ["female", "she", "woman","her", "feminine"]

def differentiator(word):

    male_score = 0
    female_score = 0

    try:
        word = word.lower()
        if word.find(" "):
            tmp = word.split()
            word = "_".join(tmp)
            print(word)
        txt = wn.synsets(word)
        #print(word.hyponyms())
        # #print(txt)
        # s1 = "zoologist"
        # print(s1 + " " +word + " " + str(s1==word))
        defn = txt[0].definition()
        tokenized_defn = defn.split()

        fh = open("result.txt", "a")



        for token in MALE_SPECIFIC:
            if(token in tokenized_defn):
                #print(defn.find(token))
                male_score+=1
                return

        for token in FEMALE_SPECIFIC:
            if(token in tokenized_defn):
                female_score+=1
                return

        if male_score > female_score:
            addition = word + "," + defn + ",specific,male\n"
        elif male_score < female_score:
            addition = word + "," + defn + ",specific,female\n"
        else:
            addition = word + "," + defn + ",neutral,none\n"
        fh.write(addition)
        fh.close()

    except Exception as err:

        #print("Definition not found for " + word)
        print("")

def corpus_generator(filename):

    try:
        fhandle = open(filename)
        for line in fhandle:
            differentiator(line.strip().strip("\r"))


        fhandle.close()

    except Exception as err:

        print(err)

corpus_generator("professions.txt")
# fh = open("occupations.txt", "r")
# fw = open("professions.txt", "a")
#
# for line in fh:
#     txt = line.strip('\s').strip('\t').strip('\n')
#     txt = txt.lower()
#     fw.write(line)
#differentiator("Music teacher")
#print(wn.synsets("music_teacher"))
