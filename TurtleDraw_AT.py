# TurtleDraw

# BY: Anthony Trejo 



import turtle
import math

TEXTFILENAME = 'turtle-draw.txt'

#inputFileName = input('turtle-draw.txt') # To Do: Ask user for the file name.


print('TurtleDraw')

turtleDraw = turtle.Turtle()
turtleDraw.speed(10)
turtleDraw.penup()



turtleDrawTextFIle = open(TEXTFILENAME, 'r')
line = turtleDrawTextFIle.readline()

totalDistance = 0
previousPoint = [0, 0]
# currentPoint = [1, 1]
# print(math.dist(previousPoint, currentPoint))

while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])
   
        currentPoint = [x, y]
        totalDistance = totalDistance + math.dist(previousPoint, currentPoint)
        print(math.dist(previousPoint, currentPoint))
        print(previousPoint)
        print(currentPoint)
        print('totalDistance=' + str(totalDistance))

        previousPoint = currentPoint

        turtleDraw.color(color)
        turtleDraw.goto(x,y)
        
        turtleDraw.pendown()

    if (len(parts) == 1):
        turtleDraw.penup()

    line = turtleDrawTextFIle.readline()

# To Do: Print the total near the bottom.
turtle.done()
input("\nPress 'ENTER' to close application")
turtleDrawTextFIle.close()

print('\nEnd')