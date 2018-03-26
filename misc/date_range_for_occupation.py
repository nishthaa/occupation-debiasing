# This script outputs the occupations
# for which an example exists for given 
# gender in a given time range

import sys

gender = sys.argv[1]
time_from = int(sys.argv[2])
time_to = int(sys.argv[3])


fh = open("../app/data/examples.txt")

for line in fh:

	toks = line.split("|")

	if gender == "m":
		i = 1
	else:
		i = 2

	examples = toks[i]

	example_list = examples.split(";")

	for example in example_list:

		try:
			fields = example.split("\t")
			
			b_date = fields[-2]
			b_year = int(b_date.split("-")[0])
			d_date = fields[-1]
			d_year = int(d_date.split("-")[0])

			if (b_year >= time_from and b_year <= time_to) or (d_year >= time_from and d_year <= time_to):
				
				print(toks[0], " ".join(fields[-3].split("/")[-1].split("_")), " ".join(fields[-5].split("/")[-1].split("_")))
				
		except:
			continue

