def main (x):

	a = b = c = 0

	for i in x :
		if i.isalpha():
			a +=1
		elif i.isdigit():
			b +=1
		else :
			c += 1

	return "alphabets: " + str(a) + "  integers: " + str(b) +"  special char: " + str(c)

print (main ("robo123#"))