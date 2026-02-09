#Darius Watts
#PHW1
#2/10/26
#Coding integers into python for a calculated output
print("-------Calculating Exponents-------")
integer1 = int( input ("Enter a number: ")) #this coding helps calculate and will be readed by the result code
integer2 = int( input ("Enter a number: "))
result = integer1 ** integer2 #the "**" is for exponents and the result always offer the calculated answer
print(integer1, "raised to the power of", integer2, result, "!!")
#the basic + to separate the argument fail to work with this print so I used commas and it worked
print("-------Addition and Subtraction-------") #should be self explainatory for future me
number_1 = int( input ("Enter a starting number: ")) #same thing as above with integers only this is for addition/subtraction
number_2 = int( input ("Enter a number to add: "))
number_3 = int( input ("Enter a number to subtract: "))
result = number_1 + number_2 - number_3 #this shows results vital when attempting to calculate as it can offer different methods of math this mix of adding and subtraction is an example.
print("equals", result) #did not wanna go far the text only because it messed up when I inputted "the number equals this and this", so I just kept it simple
#tried to use the operator build from a youtube tutorial but it didn't come out exactly as the assignment so I removed it and kept the int for the integers
