def setup():
    size(500,500)
    colorMode(HSB)

col = 0
    
def draw():
    global col
    global hw
    for i in range(0,500,50):
        fill(col,255,255)
        rect(i, 0, i+50, 500)
        col = i/2
    
    for i in range(0,500,50):
        fill(col,255,255)
        circle(i+50, 250, 50)
        col = i/2
    
    #Alternate way
    #num_cols = 1 + (mouseX / 10)
    #gap = width / float(num_cols)
    #cgap = 255 / float(num_cols)
    #noStroke()
    #for 1 in range(10):
        #x = gap * 1
        #c = cgap * 1
        #fill(c, 255, 255)
        #rect(x, 0, gap, height)
    
    #Alternate way for line circles
    #num_circles = 10
    #gap = width / float(num_circles)
    #rad = gap / 2
    #cgap = 10
    #start_c = mouseX / 2
    #for i in range(num_circles):
        #x = rad + (gap * i)
        #c = (start_c + (i + cgap)) % 256
        #fill(c, 255, 255)
        #circle(x, height / 2, gap)
        
    
        

    
    
