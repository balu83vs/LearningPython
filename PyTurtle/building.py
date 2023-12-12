import turtle as t, random as r

t.Screen().bgcolor('#001E42')
t.speed(0)
t.penup()


def stars():
  t.speed(0)
  for _ in range(50):
    t.penup()
    t.goto(r.randint(-200, 200), r.randint(-180, 190))
    t.pendown()
    t.pencolor('yellow')
    t.dot(r.randint(2,5))
    t.penup()

    
def building():
  t.speed(0)
  temp = 0
  my_build_flour = []
  t.fillcolor('blue')
  for i in range(10):
    temp = r.randint(1, 4)
    my_build_flour.append(temp)
  t.goto(-200, -200)
  i = -200
  j = 0
  while i != 200:
    t.begin_fill()
    t.goto(i, my_build_flour[j] * 40 - 200)
    t.forward(40)
    t.goto(i + 40, -200)
    i += 40
    j += 1
    t.end_fill()
    
  return my_build_flour  

def windows(n):
    t.penup()
    t.fillcolor('yellow')
    j = -200
    for w in n:
      for i in range(r.randint(0, w+1)):
        t.goto(j+20, r.randrange(w)*40 - 180)
        t.shape('square')
        t.stamp()
      j +=40
    
stars()
windows(building())
