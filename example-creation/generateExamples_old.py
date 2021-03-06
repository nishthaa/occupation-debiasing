import requests as r
import pandas as p



def get_url_string(occ,gender):
    return ('http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.'
    'org&query=SELECT+*%0D%0A++++WHERE%7B%0D%0A++++%3Fperson+rdf%3Atype+%3Foccu'
    'pation+.%0D%0A++++FILTER+contains%28str%28%3Foccupation%29%2C%22http%3A%2F'
    '%2Fdbpedia.org%2Fclass%2Fyago%2F' + occ + '%22%29+.%0D%0A++++%3Fperson+foaf%3A'
    'gender+%22' + gender + '%22%40en%0D%0A++++%7D+LIMIT+5&format=text%2Fhtml&CXML_'
    'redir_for_subjs=121&CXML_redir_for_hrefs=&timeout=30000&debug=on&run=+Run+'
    'Query+')


def get_example_urls(occ,gender):
    url = get_url_string(occ,gender)
    html = r.get(url).content
    df_list = p.read_html(html)
    examples=""
    for i in range(1,len(df_list[0][0])):
        if (i==1):
            examples = examples+df_list[0][0][i]
        else:
            examples=examples+","+df_list[0][0][i]
    examples = examples.encode('latin1').decode('utf8')
    return examples


fh = open("not-found-1.txt","r")
fw = open("examples.txt",'a')
fe = open("not-found-2.txt",'a')
count = 1
for line in fh:
    occ = line.strip().capitalize()
    try:
        female_examples = get_example_urls(occ,'female')
        male_examples = get_example_urls(occ, 'male')
        if (female_examples == "" and male_examples == ""):
            fe.write(occ+"\n")
        else:
            fw.write(occ + ";" + male_examples + ";" + female_examples + "\n")
        print(count)
        count+=1
    except Exception as err:
        fe.write(str(err)+" "+occ+"\n")
        print(count)
        count+=1


fw.close()
fh.close()
fe.close()

# print(get_example_urls("Neurosurgeon","female"))
