import numpy as np 


class Sphere:

    def __init__(self) -> None:
        self.planes=[]
        

    def store_planes(self,plane):
        self.planes.append(plane)

    def draw(self,screen,light,camera):
        for plane in self.planes:
            plane.drawArea(screen,light,camera)

    def rotate(self,x,y,z):
        for plane in self.planes:
            plane.rotate(x,y,z)