def setup():
    size(600,600)
    colorMode(HSB)
    
    for i in range(10): # for up to 
        print(i)
    
    for i in range(20, 30, 2): #for range
        print(i)
        
    for i in range(20,0, -1): #First value start, second value end, third value intervals
        print(i)
    
    
def draw():
    background(0)
    stroke(255)
    
    line(100, 100, 400, 100)
    line(100, 120, 400, 120)
    line(100, 140, 400, 140)
    line(100, 160, 400, 160)
    
    for y in range(200,261,20):
        line(100, y, 400, y)
        
    for i in range(4):
        y = 300 + (i * 20)
        line(100, y, 400, y)
        
    for i in range(4):
        y = map(i, 0, 3, 400, 430) #if i is 0 = 400. if i is 3 = 430
        line(100, y, 400, y)
        
    i = 0
    while 1 < 4: #infinite loop, never goes below 0
        y = map(i, 0, 3, 450, 480)
        line(100, y, 400, y)
        i+=1 
    

    

    
    
