def main (ls , s):
	if s == "asc":
		ls.sort()
		return ls
	elif s =="d":
		ls.sort(reverse =True)
		return ls
	else: 
		return ls 

ls = [9 , 3, 52, 5 ,5,12,6]

print(main (ls , "asc"))
