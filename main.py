'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle as turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
sides_square = 4
int_angle_square = 90
east = 0

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  turtle.penup()
  turtle.setheading(east)
  turtle.goto(top_left_x, top_left_y)
  turtle.pendown()
  for side in range(sides_square):
    turtle.forward(width)
    turtle.right(int_angle_square)
  turtle.penup()

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
    turtle.penup()
    turtle.goto(x_start, y_start)
    turtle.pendown()
    turtle.goto(x_end, y_end)
    turtle.penup()

def drawCircle(myturtle=None, radius=0):
    turtle.setheading(east)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()

def setUpDartboard(myscreen=None, myturtle=None):
    turtle.setworldcoordinates(-2,-2,2,2)
    drawSquare(turtle,2,-1,1)
    drawLine(turtle, -1,0,1,0)
    drawLine(turtle,0,1,0,-1)
    drawCircle(turtle,1)

def throwDart(myturtle=None):
  turtle.penup()
  turtle.goto(random.uniform(-1,1),random.uniform(-1,1))
  if isInCircle(turtle):
        turtle.dot(.1, "red")
  else:
        turtle.dot(.1, "green")

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  return turtle.distance(0,0)<=1


def montePi(myturtle=None, num_darts=0):
    count_inside = 0
    for dart in range(num_darts):
        throwDart(turtle)
        if isInCircle(turtle):
            count_inside = count_inside+1
    return (count_inside/num_darts)*sides_square

  



#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(myscreen=window, myturtle=darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
        if isInCircle(myturtle=darty, radius=1):
          print("You hit the dartboard!")
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty)
    playDarts(myturtle=darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(myturtle=darty, num_darts=number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
