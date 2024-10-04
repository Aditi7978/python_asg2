cost=0
room_type=input("Enter room type:standard,deluxe or suite: ")
if room_type.lower()=="standard":
	cost=100
elif room_type.lower()=="deluxe":
	cost=150
elif room_type.lower()=="suite":
	cost=250
length_of_stay=int(input("enter no . of days stayed: "))
if length_of_stay>3 and length_of_stay<=7:
	cost=cost-0.1*cost
elif length_of_stay>7:
	cost=cost-0.2*cost
season=input("Enter type of season:peak or off: ")
if season.lower()=="peak":
	cost=cost+0.2*cost
elif season.lower()=="off":
	cost=cost-0.15*cost
royalty=input("is the customer a royalty member? ")
if royalty.lower()=="yes":
	cost=cost-0.05*cost
print(f"Final cost of booking is {cost}")
