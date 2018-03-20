import extract_SVOs
import string


COUNTRY_CODES = {'ae': 'united arab emirates', 'af': 'afghanistan', 'ag': 'antigua and barbuda', 'al': 'albania', 'am': 'armenia', 'ao': 'angola', 'ar': 'argentina', 'at': 'austria', 'au': 'australia', 'az': 'azerbaijan', 'ba': 'bosnia and herzegovina', 'bb': 'barbados', 'bd': 'bangladesh', 'be': 'belgium', 'bf': 'burkina faso', 'bg': 'bulgaria', 'bi': 'burundi', 'bj': 'benin', 'bn': 'brunei darussalam', 'bo': 'bolivia', 'br': 'brazil', 'bs': 'bahamas', 'bt': 'bhutan', 'bw': 'botswana', 'by': 'belarus', 'bz': 'belize', 'ca': 'canada', 'cd': 'congo', 'cf': 'central african republic', 'cg': 'congo', 'ch': 'switzerland', 'ci': "cote d'ivoire", 'cl': 'chile', 'cm': 'cameroon', 'cn': 'china', 'co': 'colombia', 'cr': 'costa rica', 'cu': 'cuba', 'cv': 'cape verde', 'cy': 'cyprus', 'cz': 'czech republic', 'de': 'germany', 'dj': 'djibouti', 'dk': 'denmark', 'dm': 'dominica', 'do': 'dominican republic', 'dz': 'algeria', 'ec': 'ecuador', 'ee': 'estonia', 'eg': 'egypt', 'er': 'eritrea', 'es': 'spain', 'et': 'ethiopia', 'fi': 'finland', 'fj': 'fiji', 'fk': 'falkland islands', 'fr': 'france', 'ga': 'gabon', 'gb': 'united kingdom', 'gd': 'grenada', 'ge': 'georgia', 'gf': 'french guiana', 'gh': 'ghana', 'gl': 'greenland', 'gm': 'gambia', 'gn': 'guinea', 'gq': 'equatorial guinea', 'gr': 'greece', 'gt': 'guatemala', 'gw': 'guinea-bissau', 'gy': 'guyana', 'hn': 'honduras', 'hr': 'croatia', 'ht': 'haiti', 'hu': 'hungary', 'id': 'indonesia', 'ie': 'ireland', 'il': 'israel', 'in': 'india', 'iq': 'iraq', 'ir': 'iran', 'is': 'iceland', 'it': 'italy', 'jm': 'jamaica', 'jo': 'jordan', 'jp': 'japan', 'ke': 'kenya', 'kg': 'kyrgyz republic', 'kh': 'cambodia', 'km': 'comoros', 'kn': 'saint kitts and nevis', 'kp': 'north korea', 'kr': 'south korea', 'kw': 'kuwait', 'kz': 'kazakhstan', 'la': "lao people's democratic republic", 'lb': 'lebanon', 'lc': 'saint lucia', 'lk': 'sri lanka', 'lr': 'liberia', 'ls': 'lesotho', 'lt': 'lithuania', 'lv': 'latvia', 'ly': 'libya', 'ma': 'morocco', 'md': 'moldova', 'mg': 'madagascar', 'mk': 'macedonia', 'ml': 'mali', 'mm': 'myanmar', 'mn': 'mongolia', 'mr': 'mauritania', 'mt': 'malta', 'mu': 'mauritius', 'mv': 'maldives', 'mw': 'malawi', 'mx': 'mexico', 'my': 'malaysia', 'mz': 'mozambique', 'na': 'namibia', 'nc': 'new caledonia', 'ne': 'niger', 'ng': 'nigeria', 'ni': 'nicaragua', 'nl': 'netherlands', 'no': 'norway', 'np': 'nepal', 'nz': 'new zealand', 'om': 'oman', 'pa': 'panama', 'pe': 'peru', 'pf': 'french polynesia', 'pg': 'papua new guinea', 'ph': 'philippines', 'pk': 'pakistan', 'pl': 'poland', 'pt': 'portugal', 'py': 'paraguay', 'qa': 'qatar', 're': 'reunion', 'ro': 'romania', 'rs': 'serbia', 'ru': 'russian federationß', 'rw': 'rwanda', 'sa': 'saudi arabia', 'sb': 'solomon islands', 'sc': 'seychelles', 'sd': 'sudan', 'se': 'sweden', 'si': 'slovenia', 'sk': 'slovakia', 'sl': 'sierra leone', 'sn': 'senegal', 'so': 'somalia', 'sr': 'suriname', 'st': 'sao tome and principe', 'sv': 'el salvador', 'sy': 'syrian arab republic', 'sz': 'swaziland', 'td': 'chad', 'tg': 'togo', 'th': 'thailand', 'tj': 'tajikistan', 'tl': 'timor-leste', 'tm': 'turkmenistan', 'tn': 'tunisia', 'tr': 'turkey', 'tt': 'trinidad and tobago', 'tw': 'taiwan', 'tz': 'tanzania', 'ua': 'ukraine', 'ug': 'uganda', 'us': 'united states of america', 'uy': 'uruguay', 'uz': 'uzbekistan', 've': 'venezuela', 'vn': 'vietnam', 'vu': 'vanuatu', 'ye': 'yemen', 'za': 'south africa', 'zm': 'zambia', 'zw': 'zimbabwe'}

def is_occupation(occ):
	fh = open("data/result.txt")
	for line in fh:
		toks = line.split(",")
		words = [tok.strip().lower() for tok in toks]
		if words[0] == occ.lower().strip():
			fh.close()
			return words[2]
	fh.close()
	return False

def is_male(subj):
	fm = open("data/male.txt")
	for line in fm:
		if(line.strip().lower() == subj):
			fm.close()
			return True
	fm.close()
	return False

def is_female(subj):
	fm = open("data/female.txt")
	for line in fm:
		if(line.strip().lower() == subj):
			fm.close()
			return True
	fm.close()
	return False

def check_for_bias(sentence):
	svos = extract_SVOs.extract_triplets(sentence)
	hits = [triples for triples in svos if is_occupation(triples[2]) == "neutral"]
	biased = [("male", triples[2]) for triples in hits if is_male(triples[0].lower())]
	biased.extend([("female", triples[2]) for triples in hits if is_female(triples[0].lower())])
	#print(svos)
	#print(biased)
	return biased

def extract_examples(word, gender):
	fe = open("data/examples-new2.txt")
	for line in fe:
		toks = line.split("|")
		if toks[0].lower() == word and gender == "male":
			return toks[1]
		elif toks[0].lower() == word and gender == "female":
			return toks[2]
	return None

def output(biased, time_from, time_to, place):
	fe = open("data/examples-new2.txt")
	examples = ""
	
	if len(biased) == 0:
		start = "This sentence is completely free from bias!\n"
		return start
	else:
		start = "Your sentence seems to have some bias towards a gender. Here is where you can improve it:\n"

	s = ""

	for pair in biased:
		if(pair[0] == "male"):
			examples = extract_examples(pair[1], "female")
			ans = show(pair[1], examples, "female", start, time_from, time_to, place)
			if ans != None: s = s + ans 
		else:
			examples = extract_examples(pair[1], "male")
			ans = show(pair[1], examples, "male", start, time_from, time_to, place)
			if ans != None: s = s + ans
	

	if s != "":
		return s
	else:
		start = "This sentence is completely free from bias!\n"
		return start

def show(occupation, examples, gender, start, time_from, time_to, place):

	place = COUNTRY_CODES[place.lower()]
	s = start + occupation.capitalize() + " can be a " + gender + " too. Here are some examples - "
	examples = examples.rstrip(";")
	examples = examples.split(";")
	count = 0
	for example in examples:
		if len(example) > 1:

			fields = example.split("\t")
			nname = fields[0].split("/")[-1]
			name = nname.replace("_", " ")
			birth_country = fields[3].split("/")[-1].lower().replace("_"," ")
			death_country = fields[5].split("/")[-1].lower().replace("_"," ")
			birth_year = int(fields[6].split("-")[0])
			death_year = int(fields[7].split("-")[0])

			if birth_year >= time_from and birth_year <= time_to and (birth_country == place or death_country == place):
				s = s + ";" + name.strip() + " [" + fields[0].strip() + "]"	   
				count+=1
		
		 
	s = s + "\n"
	if count != 0:
		return s
	else:
		return None


def test():
	sentence = input("Please enter your sentence - \n\n\t")
	time_from = int(input("Please enter start of time period - \n\n\t"))
	time_to = int(input("Please enter end of time period - \n\n\t"))
	country = input("Please enter country - \n\n\t")
	biased = check_for_bias(sentence)
	print(output(biased, time_from, time_to, country))

if __name__ == "__main__":
	test()






