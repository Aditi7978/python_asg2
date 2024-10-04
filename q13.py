move=input('Enter the move')
column=move[0].lower()
row=int(move[1])
num_col=ord(column)-ord('a')+1
if (row+num_col)%2==0:
	print('Black')
else:
	print('white')
