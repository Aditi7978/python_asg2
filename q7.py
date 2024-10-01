sum=0
input_no=int(input("enter user no."))
for index in range(2,input_no+1):
	count=0
	for i in range(2,index):
		if index%i==0:
			count=1
			break
	if count==0:
		sum=sum+index
print(f"sum is {sum}")
