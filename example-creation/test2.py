from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    SELECT *
    WHERE{
    ?person rdf:type ?occupation .
    FILTER contains(str(?occupation),"http://dbpedia.org/class/yago/Engineer") .
    ?person foaf:gender "male"@en
    } LIMIT 2
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(results)
# print(results["results"]["bindings"][:5])

    # SELECT *
    # WHERE {
    #     ?person rdf:type yago:Chemist109913824 .
    #     ?person foaf:gender "male"@en
    # }
