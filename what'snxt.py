# your code goes here
while(True):
	x,y,z=input().split()
	if(2*y==x+z):
		a=y-x
		print("AP ",str(z+a))
	elif(x==0 and y==0 and z==0):
		break
	else(y*y==x*z):
		b=y//x
		print("GP ",str(z*b))