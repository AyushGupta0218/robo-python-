
def main (x , y):
	x = x ^ y 
	y = x ^ y 
	x = x ^ y 
	
	return x , y 

print (main ( 1, 2))