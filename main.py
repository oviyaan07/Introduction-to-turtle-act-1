import turtle

screen=turtle.Screen()
screen.bgcolor("blue")
screen.title("my first turtle")

t=turtle.Turtle()
t.color("green")
t.speed(2)
t.width(5)

t.forward(300)
t.left(90)
t.forward(100)
t.left(90)
t.forward(300)
t.left(90)
t.forward(100)
t.left(90)

screen.mainloop()