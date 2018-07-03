primeList = []

def checkNum(bigNum):
	for smallNum in range(2, bigNum-1):

		if bigNum % smallNum == 0:
			return True
		else:
			continue
	return False

for i in range (100):
	
	if checkNum(i) == False:
		primeList.append(i)
	else:
		continue

for i in primeList:
	print (i)

