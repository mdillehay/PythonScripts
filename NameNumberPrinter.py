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
	
	return nameScramL
	
for i in nameScramble(namePrinter()):
	print(i, end='')
	
	
		
