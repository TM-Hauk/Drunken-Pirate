##########################################
# CS 1110A - Programming in Python       #
# Module 3 - Exercise 3 - Drunken Pirate #
# Author: Toni_Hauk                      #
# Date:   09/19/2022                     #
##########################################

# Define Variables
prtSteps = 100 # Number of steps the pirate takes forward
angles =  [45, -75, 160, -43, 270, -97, -43, 200, -940, 17, -86, 150, 25, 75, -90, 20, -145, 30,-50, -70, -105]

import turtle

# Setup turtle window
trtlWindow  = turtle.Screen()
trtlWindow.bgcolor('black')
trtlWindow.title('Drunken Pirate')

# Setting up turtle pen
trtlPen = turtle.Turtle()
trtlPen.color('green') # set pen color
trtlPen.pensize(2) # set pen weight
trtlPen.speed(0) # set pen speed
trtlPen.penup() # pick up pen (don't draw)


trtlPen.goto(0,-100) # set up inital position
trtlPen.pendown() # put pen down (draw)
trtlPen.setheading(90) # set initial heading of pen
trtlPen.stamp() # Stamp turtle symbol
trtlPen.forward(prtSteps) # Draw number of steps
for a in angles: # go through list of angles
    trtlPen.stamp() # stamp turtle symbol
    trtlPen.right(a) # turn pen to angle that it was read in
    trtlPen.forward(prtSteps) # draw number of steps
trtlPen.stamp() # place final turtle stamp

trtlWindow.mainloop() # run program

