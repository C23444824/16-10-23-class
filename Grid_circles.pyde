def setup():
    size(500,500)
    colorMode(HSB)
    background(0)

col = 0
    
def draw():
    global col
    noStroke()
    for y in range(0, 500, 50):
        for i in range(0,500,50):
            fill(col,255,255)
            circle(i+25, y+25, 50)
            col = i/2 + (y/10)
    
    
    
    
