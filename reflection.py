import turtle

def reflect(direction):
    p = drawTriangle()
    for pos in range(0,len(p)):
        if (direction == 'x' or direction == 'X'):
            p[pos] = p[pos][0] * -1, p[pos][1]
        elif (direction == 'y', direction == 'Y'):
            p[pos] = p[pos][0], p[pos][1] * -1
        else:
            raise ValueError("Dimension not found")
        
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

reflect('y')
turtle.done()
