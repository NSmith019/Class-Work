x = -80
y = 320
def setup():
    size(640,480)
    
def draw():
    global x
    if x > 720:
        x = -80
    x += 1
    background(135, 206, 235)
    noStroke()
    fill(255, 255, 0)
    ellipse(x, 60, 80, 80)
    fill(50, 255, 0)
    rect(0, 340, 775, 150)
    fill(62)
    rect(0, 375, 700, 75)
    fill(150)
    rect(100, 150, 70, 200)
    triangle(300, 350, 340, 350, 320, 75)
    ellipse(320, 145, 75, 40)
    fill(171, 206, 219)
    rect(110, 160, 20, 30)
    rect(110, 200, 20, 30)
    rect(110, 240, 20, 30)
    rect(110, 280, 20, 30)
    rect(140, 160, 20, 30)
    rect(140, 200, 20, 30)
    rect(140, 240, 20, 30)
    rect(140, 280, 20, 30)
    fill(190)
    global y
    if y == 150:
        y = 320
    y -= 2
    rect(316, y, 8, 16)
