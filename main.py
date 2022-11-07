import create_sphere
import numpy as np
import screen
import pygame


if __name__=="__main__":
    shpere=create_sphere.create_sphere(0,200,20)
    surface=screen.Surface()
    

    while surface.run:
        
        surface.Update()
        surface.event()
        shpere.rotate(1,1,1)

        surface.drawSphere(shpere,np.array([[2],[-1],[2]]))
        
        
        pygame.display.flip()
