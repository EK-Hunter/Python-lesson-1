import pgzrun,random

WIDTH = 600
HEIGHT = 500

rainList = []
for i in range(10):
    rain = Actor("raindrop")
    rain.pos =(random.randint(0,WIDTH),130)
    rainList.append(rain)


def draw():
    screen.fill(color = "blue")
    for rain in rainList:
        rain.draw()

def update():
    for rain in rainList:
        rain.y+=10
        if rain.y > HEIGHT:
            rain.y = random.randint(-100,0)
            rain.x = random.randint(0,WIDTH)






pgzrun.go()