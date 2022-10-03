from turtle import *

sc = Screen()
sc.setup(600, 600)
sc.bgcolor("green")
speed(12)

# Background
penup()
goto(-200, -250)
pendown()
color("yellow")
begin_fill()
for i in range(4):
  fd(400)
  circle(50, 90)
end_fill()

penup()
goto(15, -155)
pendown()
lt(45)
color("#4FCCFE")
begin_fill()
for i in range(4):
  fd(200)
  circle(20, 90)
end_fill()

# Triangle
penup()
rt(45)
goto(-150, 0)
pendown()


def triangle():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)


color("orange")
begin_fill()
triangle()
triangle()
triangle()
end_fill()

# Star
penup()
goto(-105, -45)
pendown()

a = 210
n = 11
m = 4

color("red")
begin_fill()
for i in range(n):
    forward(a)
    dot()
    left(360/n*m)
end_fill()
