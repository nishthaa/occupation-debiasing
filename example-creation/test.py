import wikipedia



FEMALE_TOKENS = ["woman", "women", "female"]
MALE_TOKENS = ["man", "men", "male"]


occupation = "nurse"

fh = open("./neutral-words.txt")
fw = open("./examples.txt", "a")
search_token = ""
try:
    for line in fh:
        occupation = line.strip()
        results_women = []
        rw=""
        for i in FEMALE_TOKENS:
            search_token = i+" "+occupation
            search_result = wikipedia.search(search_token)
            #print(search_result)

            for j in range(0,3):
                if((i in str(search_result[j]).lower() or occupation in str(search_result[j]).lower()) and search_result[j] not in results_women):
                    #print(search_result[j])
                    results_women.append(search_result[j])
                    rw+=search_result[j]+","

        results_men = []
        rm=""
        for i in MALE_TOKENS:
            search_token = i+" "+occupation
            search_result = wikipedia.search(search_token)
            #print(search_result)

            for j in range(0,3):
                if((i in str(search_result[j]).lower() or occupation in str(search_result[j]).lower()) and search_result[j] not in results_men):
                    #print(search_result[j])
                    results_men.append(search_result[j])
                    rm+=search_result[j]+","

        #relevant_results = {"female":results_women,"male":results_men}

        fw.write(occupation + ";" + "FEMALE"+","+rw + ";" +"MALE"+","+rm+"\n")
except :
    print(search_token)
