import random


def namePrinter():
	namevar = input('What is your name? ')
	return namevar
	
	
def nameScramble(name):
	nameList = []
	for i in name:
		nameList.append(i)
		
	nameScram = ()
	for j in nameList:
		nameScram += (j, random.randint(0, 101))
	nameScramL = list(nameScram)
	random.shuffle(nameScramL)
	output = ''
	for i in nameScramL:
		if i != ' ':
			output += str(i)
	return output
	
#for i in nameScramble(namePrinter()):
	#print(i, end='')
	
x = (nameScramble(namePrinter()))	

print(nameScramble(x))

		
