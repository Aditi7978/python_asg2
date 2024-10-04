num=int(input("enter a number:"))

'''for i in range (2,num):
	if num%i==0:
		for j in range(2,i):
			if i%j==0:
				break
			else:
				print(i)'''
				
i=2
while num>1:
	if num%i==0:
		print(i,end=" ")
		num=num//i
	else:
		i=i+1

