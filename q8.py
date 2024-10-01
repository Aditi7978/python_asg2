final_num=0
while True:
	num=int(input("enter a no.,stops when positive no. given"))
	if num>0:
		final_num=num
		break
if final_num%2==0:
	print(final_num*2)
else:
	print(final_num*final_num)
