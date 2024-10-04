num=int(input("Enter a natural no."))
sum=0
for i in range(1,num):
	if num%i==0:
		sum=sum+i
if sum==num:
	print("It is a perfect no.")
else:
	print("It is not a perfect number.")
	
