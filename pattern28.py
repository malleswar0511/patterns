for i in range(1,6):
	for j in range(5,i,-1):
		print(" ",end="")
	for z in range(1,i+1):
		print(chr(z+64),end="")
	print()
