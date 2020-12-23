inc=1
num=1
for i in range(5,0,-1):
	for j in range(i,0,-1):
		print(" ",end="")
	print(str(num)*inc)
	inc+=2
	num+=2



