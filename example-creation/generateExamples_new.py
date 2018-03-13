from SPARQLWrapper import *

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

def generate_query(occupation,gender):
    occupation = "\""+occupation+"\""
    gender = "\""+gender+"\""
    query = """
        SELECT ?person (SAMPLE(?occupation) AS ?perOcc) (SAMPLE(?bcity) AS ?perBcity) (SAMPLE(?bcountry) AS ?perBcountry) (SAMPLE(?dcity) AS ?perDcity) (SAMPLE(?dcountry) AS ?perDcountry) (SAMPLE(?birthDate) AS ?perBdate) (SAMPLE(?deathDate) AS ?perDdate)
        WHERE {
            ?person rdf:type ?occupation .
            FILTER contains(str(?occupation),"""+occupation+""") .
            ?person foaf:gender """+gender+"""@en .
            ?person dbo:birthPlace ?bcity .
            ?bcity dbo:country ?bcountry .
            ?person dbo:deathPlace ?dcity .
            ?dcity dbo:country ?dcountry .
            ?person dbo:birthDate ?birthDate .
            ?person dbo:deathDate ?deathDate .
        } GROUP BY ?person
    """
    return query

def generate_result(occupation, gender):
    query = generate_query(occupation, gender)
    sparql.setQuery(query)
    sparql.setReturnFormat(CSV)
    results = sparql.query().convert().decode("utf-8")
    results = results[results.index('\n')+1:]
    results = results.replace("\n",";")
    results = results.replace("\"","")
    return results


fh = open("batch-2.txt","r")
fw = open("examples-new.txt",'a')
fe = open("not-found.txt",'a')
count = 51
for line in fh:
    occ = line.strip().capitalize()
    try:
        female_examples = generate_result(occ,"female")
        male_examples = generate_result(occ, "male")
        if female_examples=="" and male_examples=="":
            """fe.write("No examples found"+" "+occ+"\n")
            print(str(count)+" not found")
            count+=1
            continue"""
            raise Exception("No examples found")
        fw.write(occ + "|" + male_examples + "|" + female_examples + "\n")
        print(str(count)+" found")
        count+=1
    except Exception as err:
        fe.write(str(err)+" "+occ+"\n")
        print(str(count)+" not found")
        count+=1


fw.close()
fh.close()
fe.close()


#print(generate_result("Painter","female"))
