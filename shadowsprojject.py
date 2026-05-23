
import pgzrun,random

WIDTH=700
HEIGHT=500


TITLE="catputure the headhog"
shadow = Actor("shadow")
sonic = Actor("sonic-the-hedgehog")
sonic.pos = (350,250)

score = 0





def draw():
    screen.fill(color="white")
    shadow.draw()
    sonic.draw()
    screen.draw.text(str(score),(500,50),color = "black",fontsize=30)

def on_mouse_down(pos):
    global score


    if shadow.collidepoint(pos):
        score+=1
        shadow.x = random.randint(50, WIDTH -50)
        shadow.y = random.randint(50, HEIGHT -50)
    else:
        shadow.x = random.randint(50, WIDTH -50)
        shadow.y = random.randint(50, HEIGHT -50)

    if sonic.collidepoint(pos):
        score-=1
        sonic.x = random.randint(50, WIDTH -50)
        sonic.y = random.randint(50, HEIGHT -50)
    else:
        sonic.x = random.randint(50, WIDTH -50)
        sonic.y = random.randint(50, HEIGHT -50)


        


        
        
        
        
        
        
        











pgzrun.go()#create an output screen
