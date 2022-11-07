import pygame
import camera
import sun
import rotate
import numpy as np
import map



class Surface:

    def __init__(self) -> None:
        self.screen=pygame.display.set_mode((1160, 800))
        #self.screen=map.Map()
        self.camera=camera.Camera()
        self.run=True
        self.sun=sun.Sun()

    def Update(self):
        self.screen.fill((0 ,0 ,0))
        #self.screen.clear()
    
    


    def drawSphere(self,sphere,light):
        sphere.draw(self.screen,-self.sun.pos,self.camera)
        #print(self.camera.resize(self.sun.pos))
        
        pygame.draw.circle(self.screen,(255,255,0),self.camera.resize(self.sun.pos),10)

    def event(self):
        for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                self.run=False
            if eve.type == pygame.TEXTINPUT:
                if eve.text=="h":
                    self.sun.pos=np.array(rotate.Rz(-3)*self.sun.pos)
                elif eve.text=="l":
                    self.sun.pos=np.array(rotate.Rz(3)*self.sun.pos)

        