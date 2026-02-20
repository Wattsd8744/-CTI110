#Darius Watts
#2/17/2026
#P2LAB1
#Testing the skills to create mathmatical calculations and showcase information to users
#I am following the tutorial and following the notes she inputted in hers to study

import math #import the math module, to use the constant math.pi

#get radius from user
radius = float(input("what is the radius of the circle? :")) #this helps input your starting radius
print("here's the radius you entered: ", radius) #the output

#time to calculate the diameter
diameter = 2 * radius

#display the diameter with 1 decimal point
print(f"the diameter of the circle is:{diameter:.1f}")

#Calculate the circumference
circumference = 2 * math.pi * radius

#now display the circumference with 2 decimal points
print(f"the circumference of the circle is: {circumference:.2f}")

#now to calculate the area
area = math.pi * radius**2

#display the calculations
print(f"the area of the circle is {area:.3f}")

