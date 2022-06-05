def main (a , b ):
	ls =[]
	for i in range (a , b):
		count = 0
		for j in range (a , b ):
			if (i%j == 0):
				count += 1

		if count == 2:
			ls.append(i)

	return ls 

print (main (1 , 100))
