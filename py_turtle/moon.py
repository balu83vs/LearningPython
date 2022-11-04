import turtle as t

t.Screen().bgcolor('blue')

def moon():
  t_moon = t.Turtle()
  t_moon.hideturtle()
  t_moon.speed(0)
  t_moon.pencolor('orange')
  t_moon.fillcolor('orange')
  t_moon.begin_fill()
  t_moon.circle(80)
  t_moon.end_fill()
  
  
t_shadow = t.Turtle()
t_shadow.hideturtle()
t_shadow.speed(10)

  
moon()


while True:
  for i in range(159, -160, -1):
    t_shadow.penup()
    t_shadow.goto(t.xcor() + i, t.ycor() + 80)
    t_shadow.pendown()
    t_shadow.pencolor('blue')
    t_shadow.dot(160)
    t_shadow._tracer(5,5)
    t_shadow.clear()
    t_shadow.dot(160)
