def setup():
    global img
    fullScreen()
    img = loadImage("haunted-house-md.png")

def draw():
    background(255, 165, 46)
    noStroke()
    fill(255)
    ellipse(680, 468, 700, 700)
    image(img, 550, 175)
    fill(0)
    ellipse(680,768,1500,600)
    fill(255)
    ellipse(690,425,30,30)
    rect(675,425,30,40)
