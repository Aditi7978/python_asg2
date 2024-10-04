num=input("Enter a number:")
if num.isnumeric():
	remainder=int(int(num)%5)
	match remainder:
		case 0:
			print("remiander is 0")
		case 1:
			print("remiander is 1")
		case 2:
			print("remiander is 2")
		case 3:
			print("remiander is 3")
		case 4:
			print("remiander is 4")
		case _:
			print("invalid input")


