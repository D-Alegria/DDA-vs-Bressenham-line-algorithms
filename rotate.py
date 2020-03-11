import turtle
import math

def getXAngle(angle, x, y):
    return (x * math.cos(rad2Deg(angle))) - (y * math.sin(rad2Deg(angle)))

def getYAngle(angle, x, y):
    return (x * math.sin(rad2Deg(angle))) + (y * math.cos(rad2Deg(angle)))

def rad2Deg(angle):
    return (angle * math.pi) / 180

def rotate(factor= 0):
    p = drawTriangle()
    for pos in range(0,len(p)):
        p[pos] = getXAngle(factor,p[pos][0], p[pos][1]), getYAngle(factor,p[pos][0], p[pos][1])
    drawTriangle(p)

def rotateAtPoint(factor = 0, point = [0,0]):
    p = drawTriangle()
    for pos in range(0,len(p)):
        p[pos] = point[0] + ((p[pos][0]-point[0])*math.cos(rad2Deg(factor))) - ((p[pos][1]-point[1])*math.sin(rad2Deg(factor))), point[1] + ((p[pos][0]-point[0])*math.sin(rad2Deg(factor))) + ((p[pos][1]-point[1])*math.cos(rad2Deg(factor))),#getXAngle(factor,p[pos][0], p[pos][1]), getYAngle(factor,p[pos][0], p[pos][1])
    drawTriangle(p) 

def drawTriangle(points = [(100,100), (50,150), (150,150)]):
    tri = turtle.Turtle()
    tri.pu()
    for p in range(0,len(points)+1):
        try:
            tri.goto(points[p])
            tri.pd()
        except IndexError:
            tri.goto(points[0])
    
    return points

# rotate(factor=90)
rotateAtPoint(factor=30,point=[100,100])
turtle.done()
