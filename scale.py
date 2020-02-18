import turtle  

def scale(factor= [0,0]):
    p = drawTriangle()
    for pos in range(0,len(p)):
        p[pos] = p[pos][0] * factor[0], p[pos][1] * factor[1]
    drawTriangle(p)

def drawTriangle(points = [(0.00,0.00), (100.00,0.00), (50.00,86.60)]):
    tri = turtle.Turtle()
    tri.pu()
    for p in range(0,len(points)+1):
        try:
            tri.goto(points[p])
            tri.pd()
        except IndexError:
            tri.goto(points[0])
    
    return points

scale(factor=[3,3])
turtle.done()
