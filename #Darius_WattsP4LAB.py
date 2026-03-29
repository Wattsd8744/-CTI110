#Darius Watts
#P4LAB1
#3/19/2026
#practicing loops with  turtle coding

import turtle #allows us to summon the turtle(window)
wn = turtle.Screen() #This sets up the screen that will appear when ran.
wn.bgcolor("lightyellow") #changes the screen background to your chosen color
wn.title("Hello, Darius!") #adds the title on the upper corner
darius = turtle.Turtle() #our named given just to make it a variable

darius.color("cyan", "lightgray") #fills in the color for the trianhgle while also offering a outline color.  citing my source I Learn this by a tutorial from geeks tutorial and geeksforgeeks.org
darius.begin_fill() #adds the color fill to the shape

darius.begin_fill()
darius.forward(80)
darius.left(120) 
darius.forward(80)
darius.left(120)
darius.forward(80)
darius.end_fill() #putting it at the bottom of this line will stop at the triangle, if not added it would've been with the square as well.

#this recipe creates a triangle!

#onto making the square
darius.left(30)
darius.forward(90)
darius.left(90)
darius.forward(80)
darius.left(90)
darius.forward(90)

darius.penup
darius.goto(90,-250)
darius.pendown()

darius.left(90)
darius.forward(80)
darius.left(70)
darius.forward(50)
darius.left(-120)
darius.forward(90)
darius.left(120)
darius.forward(90)
darius.left(-120)
darius.forward(100)

darius.penup
darius.goto(-150,-220)
darius.pendown()

#this creates my initials. I used an alphabet tutorial from youtube to know how to make a DW initial the channel is called "tutorial tuts"
darius.right(45)
darius.circle(90,90)
darius.left(90)
darius.forward(103)
darius.left(90)
darius.forward(90)
#this is the recipe for the bottom half that continues from the triangle arrow left from the triangle into making a square
#that also makes the house
wn.mainloop() #this keeps the window open until you close it, otherwise it would pop up and disappear immediately 