while True:
	yes_no=input("do you want to use calculator")
	if yes_no!='exit':
		num1=float(input("Enter 1st number"))
		num2=float(input("Enter 2nd number"))
		op=input("Enter operator:")
		if op=='+':
			print(f"sum is {num1+num2}")
		elif op=='-':
			print(f"difference is {num1-num2}")
		elif op=='*':
			print(f"Product is {num1*num2}")
		else:
			if num2==0:
				print("division by zero")
			else:
				print(f"Quotient is {num1/num2}")
	else:
		print("exits program")
		break
