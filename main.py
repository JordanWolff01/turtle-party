# Turtle Spiral Project
# Jordan Wolff
04/07/2024

# 1 Draw two squares
import turtle

def main():
    turtle.shape("turtle")
    # turtle.speed(0)
    turtle.color("blue")
    turtle.width(5)

def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)

def rect(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

main()
square(100)
turtle.penup()
turtle.forward(120)
turtle.pendown()
turtle.color("red")
rect(25,100)
turtle.Screen().exitonclick()
