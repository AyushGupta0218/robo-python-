def main (x):
	s = len(x)

	for i in range (s):
		if x[i] != x[s-i-1]:
			return "no"

	return "yes" 

print (main ("ayutuya"))