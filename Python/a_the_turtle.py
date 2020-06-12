import turtle
a=turtle.Turtle()
a.color('green')
how_fast=input('How fast would you like me to go?')
a.speed(how_fast)
for i in range(1, 6):
    a.forward(50)
    a.write(i)
    a.circle(10)
    a.right(144)
    
