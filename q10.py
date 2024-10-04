s=input("Enter a string: ")
n=len(s)
for i in range(n):
	sub_s=" "
	for j in range(i,n):
		sub_s=sub_s +s[j]
		print(sub_s)
