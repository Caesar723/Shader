import numpy as np


class Camera:

    def __init__(self) -> None:
        self.vision=np.array([0,0,-700])

    def resize(self,point):# ->(x,y)
        z=point[2][0]
        change_z=z-self.vision[2]
        ratio=-self.vision[2]/change_z

        x_screen=int(point[0][0]*ratio+500)
        y_screen=int(point[1][0]*ratio+500)

        return (x_screen,y_screen)