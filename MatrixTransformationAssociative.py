import math,turtle
class MatrixTransformation():
    def __init__(self, vertices):
        self.vertices = vertices

    def transform(self, angle, factor=[]):
        v = self.vertices
        self.drawTriangle(v)
        B = [
            [math.cos(self._rad2Deg(angle)),-math.sin(self._rad2Deg(angle)),0],
            [math.sin(self._rad2Deg(angle)),math.cos(self._rad2Deg(angle)),0],
            [0,0,1]
            ]
        X = [
            [1,0,factor[0]],
            [0,1,factor[1]],
            [0,0,1]
        ]

        A = self._multiplyMatrixAB(X,B)
        for i in range(len(v)):
            x = self._multiplyMatrixAB(A,[[v[i][0]],[v[i][1]],[1]])
            v[i] = x[0][0],x[1][0]
        self.drawTriangle(v)

    def drawTriangle(self, points = [(0.00,0.00), (100.00,0.00), (50.00,86.60)]):
        tri = turtle.Turtle()
        tri.pu()
        for p in range(0,len(points)+1):
            try:
                tri.goto(points[p])
                tri.pd()
            except IndexError:
                tri.goto(points[0])
    

    def _rad2Deg(self,angle):
        return (angle * math.pi) / 180

    def _multiplyMatrixAB(self,A,B):
        result = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]

        return result

if __name__ == "__main__":
    x = MatrixTransformation([(0.00,0.00), (100.00,0.00), (50.00,86.60)])
    x.transform(angle = 45, factor=[100,0])
    turtle.done()