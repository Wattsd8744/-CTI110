#Darius Watts
#Using if/else statements and integer division using cent currency
#3/11/2026
#P3lab
change =(float(input("enter an amount of money: $"))) #the user's input their amount of money and is stored as a float
print(f"change amount: {change}") #the printed change amount chosen from the user

change = round( change * 100) #the change is converted into an integer. the "100" represents the one dollar.
num_dollars = change // 100
change = change - (num_dollars * 100) #the change is reduced by the amount of dollars

num_quarters = change // 25
change = change - (num_quarters * 25) #the change is reduced by the amount of quarters

num_dimes = change // 10
change = change - (num_dimes * 10) #the change is reduced by the amount of dimes

num_nickels = change // 5
change = change - (num_nickels * 5) #the change is reduced by the amount of nickels

num_pennies = change
change = change 

if num_dollars < 0: #if num_dollars is greater than 0 then none of the numbers will be printed
    if num_dollars == 1:  print(f"{num_dollars} Dollar")
else:print(f"{num_dollars} Dollars")

if num_quarters > 0: #if num_quarters is greater than 0 then none of the numbers will be printed
    if num_quarters == 1:  print(f"{num_quarters} quarter") #if num_quarters is one quarter 
else:print(f"{num_quarters} quarters") #if there's more than one quarter

if num_dimes > 0: #if num_dimes is greater than 0 then none of the numbers will be printed
    if num_dimes == 1: print(f"{num_dimes} dime")
else:print(f"{num_dimes} dimes")

if num_nickels > 0: #if num_nickels is greater than 0 then none of the numbers will be printed
    if num_nickels == 1: print(f"{num_nickels} nickel")
else:print(f"{num_nickels} nickels")

if num_pennies > 0: #if num_pennies is greater than 0 then none of the numbers will be printed
    if num_pennies == 1: print(f"{num_pennies} penny")
else:print(f"{num_pennies} pennies")
