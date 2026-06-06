import pgzrun ,random
WIDTH = 600
HEIGHT=480
TITLE = "catch the apple"
apple = Actor("apple")
apple.pos = (300,200)

silver = Actor("silver")
silver.pos=(80,80)

score = 0


def draw():
    screen.fill(color="skyblue")
    silver.draw()
    apple.draw()
    screen.draw.text(str(score),(20,20))

def update():
    global score
    if keyboard.a:
        silver.x -= 1
    
    if keyboard.d:
        silver.x += 1
    
    if keyboard.w:
        silver.y -= 1

    if keyboard.s:
        silver.y += 1
    
    if silver.colliderect(apple):
        apple.pos=(random.randint(0,WIDTH),random.randint(0,HEIGHT))
        score += 1
        








pgzrun.go()