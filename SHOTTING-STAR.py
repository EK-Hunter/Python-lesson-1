import pgzrun
WIDTH = 500
HEIGHT = 340
TITLE = "SHOOTING STAR"


twilight = Actor("star")
twilight.pos = (50,50)



def draw():
    screen.blit("sky",(0,0))
    twilight.draw()



def update():
    twilight.x += 1
    twilight.y += 1.5
































pgzrun.go()