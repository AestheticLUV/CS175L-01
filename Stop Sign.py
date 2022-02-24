#CS-175LAB
#Jarek Torres
#STOP Sign.py

import math #from the math import
from math import sqrt #sqrt in order to work needs to be import from math
import turtle #turtle


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8 #stop sign has 8 sides 
LENGTH = 100 #length is your s 
ANGLE = 45 
TEXT_X = -5
TEXT_Y = -10

jarek = turtle.getscreen() #normal turtle.screen() will not work on 3.10 python mac as of now .getscreen() works only for my pc 
jarek.setup(400,400)# same as WINDOW_WIDTH, WINDOW_HEIGHT #400,400
#we know s is 100
s = LENGTH
x = s / sqrt(2)
x = s / math.sqrt(2)
diameter = s + (2 * x)#what is the diameter
print(f"The diameter is: {diameter:.2f}") #2f is for the decimals places

turtle.up()
turtle.goto(-40,120)# x = -40 and y = 120 #starting point
turtle.down()
# Now draw an octagon
for oreo in range(8):  #we know a octagon has 8 sides so in range 8 times the loop will happen
    turtle.shape("turtle")
    turtle.forward(100)  #move forward 100 pixels
    turtle.right(45) #turn right 45 degrees
turtle.up()
turtle.goto(0,0)#center for the word STOP to print
turtle.down()

turtle.hideturtle() #hide turtle so that only STOP would show


turtle.write("STOP") #to print out STOP



turtle.mainloop()
