#Darius Watts
# #2/15/24
#P2LAB
#this assignment helps emphasize the teaching of inputs and outputs when coding

#this sets up the dictionary
cars = {
  "Camero": "18.21",
  "Prius": "52.36",
  "Model S": "110",
  "Silverado": "26",
  } #this sets up the directory that contains our values
keys = cars.keys()
print(keys) #shows the list of options

#This code set up is for choosing a vehicle, but be aware this is case sensitive it has to match the listed 
selection = input("Enter the listed vehicle to see its mpg:")

#this code is the output for each vehicle, depending on which is chosen. I had no other ways to do this without if statement and it took me almost an entire week to just settle with this
if "Camero" in selection: print(f'the', selection, "gets", cars["Camero"], "MPG"),
if "Prius" in selection: print(f'the', selection, "gets", cars["Prius"], "MPG"),
if "Model S" in selection: print(f'the', selection, "gets", cars["Model S"], "MPG"),
if "Silverado" in selection: print(f'the', selection, "gets", cars["Silverado"], "MPG"),
#the same set up as the prior code but I was able to impress myself with using the same input, but including the selection2 for the second half of the assignment, I'm impressed it worked!

#overall this is for the second part which allows you to choose the miles you think you'll drive with your vehicle and it will calculate.
if "Camero" in selection: selection2 = int(input("How many miles do you plan  to drive the Camero?: "))
if "Prius" in selection: selection2 = int(input("How many miles do you plan  to drive the Prius?: "))
if "Model S" in selection: selection2 = int(input("How many miles do you plan  to drive the Model S?: "))
if "Silverado" in selection: selection2 = int(input("How many miles do you plan  to drive the Silverado?: "))

#Hopefully this is how I use the round function right, I was unsure to use the divison /, but I see it gave me a different answer than just setting round so...
 #this is the calculation for the amount of gas needed to drive the miles inputted
if "Camero" in selection: print(f'amount of gas needed are', {round (18.21/selection2, 2)}, "gallon(s) to drive the Camero", selection2, "miles" ) 
if "Prius" in selection: print(f'amount of gas needed are', {round (52.36/selection2, 2)}, "gallon(s) to drive the Camero", selection2, "miles" )
if "Model S" in selection: print(f'amount of gas needed are', {round (110/selection2, 2)}, "gallon(s) to drive the Camero", selection2, "miles" )
if "Silverado" in selection: print(f'amount of gas needed are', {round (26/selection2, 2)}, "gallon(s) to drive the Camero", selection2, "miles" )

#this was strssful but I did enjoy it in a twisted way! thanks w3schools and codeacademy!

#note to self use If function more often to set up different outputs for listed inputs.