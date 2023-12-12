import turtle as t, random

t.hideturtle()
t.Screen().setup(640,480)
t.speed(0)

def star(lenght, heading, position, color):
  t.penup()
  t.goto(position)
  t.pendown()
  t.fillcolor(color)
  t.pencolor(color)
  t.begin_fill()
  t.setheading(heading)
  for _ in range(5):
    t.forward(lenght)
    t.right(130)
    t.forward(lenght)
    t.left(60)
  t.end_fill()

def exit():
    pass

while t.Screen().onkey(exit, 'q') != True:
    color = (random.randrange(256), random.randrange(256), random.randrange(256))
    heading = random.randint(1, 360)
    position = (random.randrange(640), random.randrange(480))
    lenght = random.randint(2, 30)
    star(lenght, heading, position, color)
