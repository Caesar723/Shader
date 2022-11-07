import numpy as np
import os
import time


def point(element):
    return element[0]
class Map:

    def __init__(self) -> None:
        self.large=(160,40)
        self.map=[['*' for i in range(self.large[0])] for i in range(self.large[1])]
        self.level="·-～—=+*oa@"
        self.i=0
        
    def find_equation(self,point1,point2):
        k=(point2[1]-point1[1])/(point2[0]-point1[0]+0.01)
        b=point2[1]-k*point2[0]

        return (k,b)
    def sort_points(self,*args):
        args=list(args)
        args.sort(key=point)
        return args

    def drawLine(self,point1,point2,color_angle):
        char=self.level[round((len(self.level)-1)*(color_angle/255))]
        p1,p2=self.sort_points(point1,point2)
        
        k,b=self.find_equation(p1,p2)
        
        for i in range(p1[0],p2[0]):
            
            self.map[int(k*i+b)][i]=char

    def drawTriangle(self,point1,point2,point3,color_angle):
        #print(color_angle)
        char=self.level[round((len(self.level)-1)*(color_angle/255))]
        p1,p2,p3=self.sort_points(point1,point2,point3)
        k1,b1=self.find_equation(p1,p2)
        k2,b2=self.find_equation(p1,p3)
        k3,b3=self.find_equation(p2,p3)

        for row1 in range(p1[0],p2[0]):
            two_col=(int(k1*row1+b1),int(k2*row1+b2))
            for col1 in range(min(two_col),max(two_col)):
                self.map[col1][row1]=char

        for row2 in range(p2[0],p3[0]):
            two_col=(int(k3*row2+b3),int(k2*row2+b2))
            for col2 in range(min(two_col),max(two_col)):
                self.map[col2][row2]=char



        

    def clear(self):
        self.clear_screen()
        for i in range(len(self.map)):
            self.map[i]=[' ']*self.large[0]
        self.map[0][0]=f'{self.i}'
        self.i+=1
        
    def clear_screen(self):
        print("\33[2J")
        

    def display(self):
        #print()
        for row in self.map:
            print(''.join(row))
if __name__=="__main__":
    m=Map()

    while True:
        
        
        
        time.sleep(0.1)
        m.clear()
        
        m.drawLine((100,0),(150,30),255)
        m.drawTriangle((100,0),(120,30),(150,0),255)
        m.display()
    