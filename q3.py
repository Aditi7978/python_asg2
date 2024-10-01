score=int(input("enter marks scored"))
grade=""
if score>=90 and score<=100:
	grade="A"	
elif score>=80 and score<=89:
	grade="B"
elif score>=70 and score<=79:
	grade="C"
elif score>=60 and score<=69:
	grade="D"
else:
	grade="F"
if grade=="A":
	print("Excellent you got GRADE A")
elif grade=="B":
	print("Good you got GRADE B")
elif grade=="C":
	print("Average you got GRADE C")
elif grade=="D":
	print("Needs improvement you got GRADE D")
else:
	print("You are failing you got GRADE F")
