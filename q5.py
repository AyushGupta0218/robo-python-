def main (ls):
	ls2 = []
	for i in ls:
		if i in ls2 :
			return i 
		else:
			ls2.append(i)


ls = [1 , 3, 6, 8, 7, 2, 9 ,1]

print (main (ls))