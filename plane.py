import numpy as np
import create_script
import random
import pygame
import rotate



class Plane:

    def __init__(self,vec_1,vec_2,vec_3) -> None:# position vector
        #create_script.points([vec_1,vec_2,vec_3])
        #self.points=[vec_1,vec_2,vec_3]
        self.vec_1=vec_1
        self.vec_2=vec_2
        self.vec_3=vec_3

        
        #self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    @property
    def line_1(self):
        return self.vec_1-self.vec_2

    @property
    def line_2(self):
        return self.vec_3-self.vec_2

    @property
    def normal(self)->np.ndarray:#the normal of the plane
        
        return np.cross(
            np.reshape(self.line_1,(1,3)),
            np.reshape(self.line_2,(1,3)))

    def drawArea(self,screen,sun_light,camera):#triangle
        point1=camera.resize(self.vec_1)
        point2=camera.resize(self.vec_2)
        point3=camera.resize(self.vec_3)
        

        if self.cal_angle(np.array([[0],[0],[1]]))<75:
            angle=self.cal_angle(sun_light)
            color=200-255*angle/(180)
            

            #screen.drawTriangle(point1, point2, point3,color[0][0])

            pygame.draw.polygon(screen, (color,color,color), [point1, point2, point3], 0)
            # pygame.draw.line( screen, (0,0,0), point1, point2, 1 )
            # pygame.draw.line( screen, (0,0,0), point3, point2, 1 )
            # pygame.draw.line( screen, (0,0,0), point1, point3, 1 )

        

    def cal_angle(self,vector):
        cos=self.normal.dot(vector)/(np.linalg.norm(self.normal)*np.linalg.norm(vector))
        angle=360*np.arccos(cos)/(2*np.pi)
        
        return angle
        

    def rotate(self,x,y,z):
        self.vec_1=np.array( rotate.Rotate(x,y,z)*self.vec_1)
        self.vec_2=np.array(rotate.Rotate(x,y,z)*self.vec_2)
        self.vec_3=np.array(rotate.Rotate(x,y,z)*self.vec_3)