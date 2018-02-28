import extract_SVOs
import string


def is_occupation(occ):
	fh = open("../data/result.txt")
	for line in fh:
		toks = line.split(",")
		words = [tok.strip().lower() for tok in toks]
		if words[0] == occ.lower().strip():
			fh.close()
			return words[2]
	fh.close()
	return False

def is_male(subj):
	fm = open("../data/male.txt")
	for line in fm:
		if(line.strip().lower() == subj):
			fm.close()
			return True
	fm.close()
	return False

def is_female(subj):
	fm = open("../data/female.txt")
	for line in fm:
		if(line.strip().lower() == subj):
			fm.close()
			return True
	fm.close()
	return False

def check_for_bias(sentence):
	svos = extract_SVOs.extract_triplets(sentence)
	hits = [triples for triples in svos if is_occupation(triples[2]) == "neutral"]
	biased = [("male", triples[2]) for triples in hits if is_male(triples[0])]
	biased.extend([("female", triples[2]) for triples in hits if is_female(triples[0])])
	return biased

def extract_examples(word, gender):
	fe = open("../data/examples.txt")
	for line in fe:
		toks = line.split(";")
		if toks[0].lower() == word and gender == "male":
			return toks[1]
		elif toks[0].lower() == word and gender == "female":
			return toks[2]
	return None

def output(biased):
	fe = open("../data/examples.txt")
	examples = ""
	
	if len(biased) == 0:
		print("\nThis sentence is completely free from bias!\n")
	else:
		print("\nYour sentence seems to have some bias towards a gender. Here is where you can improve it:\n")

	for pair in biased:
		if(pair[0] == "male"):
			examples = extract_examples(pair[1], "female")
			show(pair[1], examples, "female")
		else:
			examples = extract_examples(pair[1], "male")
			show(pair[1], examples, "male")

def show(occupation, examples, gender):
	print("- %s can be a %s too. Here are some examples - \n\n" %(occupation.capitalize(), gender))
	examples = examples.split(",")
	for example in examples:
		nname = example.split("/")[-1]
		name = nname.replace("_", " ")
		print("\t- %s (%s)\n" %(name.strip(), example.strip()))
	print("\n")


def test():
	sentence = input("Please enter your sentence - \n\n\t")
	biased = check_for_bias(sentence)
	output(biased)

if __name__ == "__main__":
	test()





