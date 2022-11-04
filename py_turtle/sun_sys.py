import turtle as t

t.hideturtle()

#t.Screen(800, 600)
  
sun_sys = {
'sun': {'color': (255,252,138), 'size': 90, 'position': (-100, 0)},
'merc': {'color': (229,189,87), 'size': 25, 'position': (0, 0)},
'vin': {'color': (229,189,87), 'size': 30, 'position': (35, 0)},
'eatch': {'color': (172,247,207), 'size': 25, 'position': (65, 0)},
'mars': {'color': (252,129,101), 'size': 20, 'position': (95, 0)},
'upi': {'color': (229,189,87), 'size': 60, 'position': (165, 0)},
'sat': {'color': (229,189,87), 'size': 60, 'position': (235, 0)},
'ura': {'color': (111,198,221), 'size': 40, 'position': (285, 0)},
'nep': {'color': (5,130,248), 'size': 35, 'position': (330, 0)},
'pluto': {'color': (229,189,87), 'size': 10, 'position': (350, 0)},
}  
  
for name in sun_sys:
  t.penup()
  t.goto(sun_sys[name]['position'])
  t.fillcolor(sun_sys[name]['color'])
  t.pendown()
  t.begin_fill()
  t.circle(sun_sys[name]['size'])
  t.end_fill()
