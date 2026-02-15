#Darius Watts
# #2/15/24
#P1HW2
#coding a budget calculator for accomidations.

print("This Program calculates your budget and display your travel expenses creating")
integer1 = int(input("Please enter your budget:")) #This is suppose to display your current budget that will be subtracted from the expenses
destination = input("input your destination:") #this is the location that will be used for the trip
print("Now to calculate your potential spending for your trip")
integer3 = int(input("How much do you predict you will spend on the gas:"))
integer4 = int(input("how much do you predict you spend on accomondations such as hotels:"))
integer5 = int(input("lastly, how much do you prdict on dining expenses:"))
print("-----------------travel expenses calculated-----------------")
print("Location:", destination) #the location you chose for the calculation
print("your budget", integer1)#your current budget that will be used for the calculation
print("your gas expenses:", integer3) #the predicted gas expense for the trip
print("your accomodation expense:", integer4) #predicted accomodation expense for the trip
print("your dining expense:", integer5) #predicted dining expense for the trip
result = integer1 - integer3 - integer4 - integer5 #the calculation for the remaining budget after the expenses
print("remaining", result) #the remaining budget after the expenses are subtracted from the original budget