import random
import pgzrun
WIDTH = 700
HEIGHT = 500
TITLE = "CIRCLE PATTERN"

def draw():
    screen.fill(color = "navy")
    for i in range(5):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        screen.draw.circle((350,250),250-50*i,(r,g,b))

pgzrun.go()
