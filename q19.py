num=int(input("Enter a number"))
r=0
rev=0
while num>0:
	r=num%10
	rev=rev*10+r
	num=num//10
print(f"Reverse of number is {rev}")
