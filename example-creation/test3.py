import requests as r
import pandas as p



def get_url_string(occ,gender):
    return 'http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=SELECT+*%0D%0A++++WHERE%7B%0D%0A++++%3Fperson+rdf%3Atype+%3Foccupation+.%0D%0A++++FILTER+contains%28str%28%3Foccupation%29%2C%22http%3A%2F%2Fdbpedia.org%2Fclass%2Fyago%2F'+occ+'%22%29+.%0D%0A++++%3Fperson+foaf%3Agender+%22'+gender+'%22%40en%0D%0A++++%7D+LIMIT+5&format=text%2Fhtml&CXML_redir_for_subjs=121&CXML_redir_for_hrefs=&timeout=30000&debug=on&run=+Run+Query+'


def get_example_urls(occ,gender):
    url = get_url_string(occ,gender)
    html = r.get(url).content
    df_list = p.read_html(html)
    print (occ)
    print (df_list[0][0])


fh = open("neutral-words.txt","r")
for line in fh:
    occ = " ".join(w.capitalize() for w in line.strip().split("_")[0])
    print (occ)

# df.to_csv('my data.csv')



# http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=SELECT+*%0D%0A++++WHERE%7B%0D%0A++++%3Fperson+rdf%3Atype+%3Foccupation+.%0D%0A++++FILTER+contains%28str%28%3Foccupation%29%2C%22http%3A%2F%2Fdbpedia.org%2Fclass%2Fyago%2FActor%22%29+.%0D%0A++++%3Fperson+foaf%3Agender+%22male%22%40en%0D%0A++++%7D+LIMIT+5&format=text%2Fhtml&CXML_redir_for_subjs=121&CXML_redir_for_hrefs=&timeout=30000&debug=on&run=+Run+Query+

# " ".join(w.capitalize() for w in s.split()[0])
