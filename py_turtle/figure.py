import turtle as t, math, random
t.Screen().setup(640, 480)
t.speed(0)
t.hideturtle()


def figure(a, n):
  t.pendown()
  t.fillcolor(random.randrange(256), random.randrange(256), random.randrange(256))
  t.begin_fill()
  for _ in range(n):
    t.forward(a)
    t.right(360/n)
  t.end_fill()  


s = int(input())



for i in range(5):
  for j in range(5):
    n = random.randint(3, 8)
    
    
    a = math.sqrt((s * 4 * math.tan(math.radians(180) / n)) / n)
    
    
    t.penup()
    t.goto(j * s / 10 - 100, i * s / 10 - 30)
    figure(a, n)
    
