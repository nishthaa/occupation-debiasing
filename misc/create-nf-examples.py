import sys

filename = sys.argv[1]


fh = open(filename)

string = ""

for line in fh:
	tokens = line.split("\t")
	for i in range(len(tokens)):
		tokens[i] = tokens[i].strip()
		tokens[i] = tokens[i].strip('"')
	example = "\t".join(tokens)
	example = example + ";"
	string = string + example


print(string)


