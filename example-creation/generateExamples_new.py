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

query = generate_query("Painter","female")
sparql.setQuery(query)
sparql.setReturnFormat(CSV)
results = sparql.query().convert().decode("utf-8")
print(results)
# print(results["results"]["bindings"][:5])

    # SELECT *
    # WHERE {
    #     ?person rdf:type yago:Chemist109913824 .
    #     ?person foaf:gender "male"@en
    # }
