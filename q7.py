def main(ls):
	ls2 =[]
	for i in ls:
		if i not in ls2:
			ls2.append(i)

	for i in ls :

		maxcount = 0 
		count =0
		if i in ls2:
			if i in ls:
				count +=1 
			if count > maxcount:
				maxcount = count 
				element = i
		count = 0

	return element  

ls =[1 , 2 ,3,4,5,1 ,5,5,2,2]

print (main(ls))