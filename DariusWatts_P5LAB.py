#Darius Watts
#P3LAB
#Program prompts user to enter a dollar amount and calculates the most
#4/20/26
import random #readying up our owed mount
whats_owed = round(random.uniform(0.01, 100.00), 2)
print(f"you owe {whats_owed}")
user_amount = float(input("Enter a dollar amount: $"))
user_money_int = int(round(user_amount, 2))

change = user_amount - whats_owed #this is to be here so the print can represent our calculate change.
print(f'heres your change: {change}') #printing what we get back

user_money_int = int(round(change * 100, 0)) #for the coins to represent our change

# Calculate subsequent denominations utilizing floor division and modulus
#################################################################### Dollars

dollars = user_money_int // 100
user_money_int = user_money_int % 100

#################################################################### Quarters

quarters = user_money_int // 25
user_money_int = user_money_int % 25

#################################################################### Dimes

dimes = user_money_int // 10
user_money_int = user_money_int % 10

#################################################################### Nickles

nickels = user_money_int // 5
user_money_int = user_money_int % 5

#################################################################### Pennies

pennies = user_money_int

# Print conditional results with subject-verb agreement
if dollars > 0:
    if dollars == 1:
        print(f"{dollars} dollar")
    if dollars > 1:
        print(f"{dollars} dollars")
if quarters > 0:
    if quarters == 1:
        print(f"{quarters} quarter")
    if quarters > 1:
        print(f"{quarters} quarters")
if dimes > 0:
    if dimes == 1:
        print(f"{dimes} dime")
    if dimes > 1:
        print(f"{dimes} dimes")
if nickels > 0:
    print(f"{nickels} nickel")
if pennies > 0:
    if pennies == 1:
        print(f"{pennies} penny")
    if pennies > 1:
        print(f"{pennies} pennies")

# Keep terminal window open for review before closing
input("Press Enter to quit program")