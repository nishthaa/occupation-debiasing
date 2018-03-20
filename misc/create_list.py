fin1 = open('english_male.txt')
fin2 = open('english_female.txt')

males = []

for line in fin1:
	males.append(line.lower().strip())

print(males)

females = []
for line in fin2:
	females.append(line.lower().strip())

print(females)