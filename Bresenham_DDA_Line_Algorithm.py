import turtle

class Pixel:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Bresenham:
    def __init__(self,pixel1,pixel2):
        self.pixel1 = pixel1
        self.pixel2 = pixel2

    def getLineCordinate(self):
        dx = self.pixel2.x - self.pixel1.x
        dy = self.pixel2.y - self.pixel1.y

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2*dy - dx
        y = 0
        
        for x in range(dx + 1):
            yield self.pixel1.x + x*xx + y*yx, self.pixel1.y + x*xy + y*yy
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy

    def drawline(self):
        turtle.Screen()
        turtle.title("Bresenham")
        for pos in list(self.getLineCordinate()):
            turtle.setposition(x=pos[0],y=pos[1])

class DDA:
    def __init__(self,pixel1,pixel2):
        self.pixel1 = pixel1
        self.pixel2 = pixel2

    def getLineCordinate(self):
        dx = self.pixel2.x - self.pixel1.x
        dy = self.pixel2.y - self.pixel1.y

        steps = 0 

        if abs(dx) >= abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)

        try:
            xInc = dx / steps
            yInc = dy / steps
        except ZeroDivisionError:
            print("err")
        
        
        
        for x in range(int(steps)):
            yield self.pixel1.x + xInc, self.pixel1.y + yInc
            self.pixel1.x += xInc
            self.pixel1.y += yInc
            

    def drawline(self):
        turtle.Screen()
        turtle.title("DDA")
        for pos in list(self.getLineCordinate()): 
            turtle.setposition(x=abs(pos[0]),y=abs(pos[1]))

def main():
    p1 = Pixel(0,0)
    p2 = Pixel(100,100)
    
    #bres = Bresenham(p1,p2)

    #bres.drawline()

    dda = DDA(p1,p2)
    dda.drawline()

main()
