ls = ['0','1','2','3','4','5','6','7','8','9']

def main (s):
	sum =0
	for i in s: 
		
		if i in ls:
			sum += int(i)

	return sum

print (main("hello13world57"))
