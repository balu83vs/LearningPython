import turtle as t

t.hideturtle()
t.speed(0)

def w_square():
  t.fillcolor('white')
  t.begin_fill()
  for _ in range(4):
    t.forward(20)
    t.right(90)
  t.forward(20)
  t.end_fill()  
    
def b_square():
  t.fillcolor('black')
  t.begin_fill()
  for _ in range(4):
    t.forward(20)
    t.right(90)
  t.forward(20)
  t.end_fill()  
  
for i in range(5):
  t.penup()
  t.goto(0, -20 * i)
  t.pendown()
  for j in range(5):
    if i % 2 != 0:
      if j % 2 != 0:
        b_square()
      else:
        w_square()
    else:
      if j % 2 == 0:
        b_square()
      else:
        w_square()
    
