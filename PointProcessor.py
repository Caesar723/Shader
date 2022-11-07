import numpy as np
import plane
import random
import create_script
import sphere

class PointProcessor:


    def __init__(self,maxindex) -> None:
        self.points_old=[]
        self.points_new=[]
        self.max_index=maxindex

        self.sphere=sphere.Sphere()

    
    def receive_point(self,point):#put the point first
        self.points_old.append(point)

    def change_point(self,point):# change the point stored
        self.points_new.append(point)

    def over_receive(self,point):#when don't need to receive point(first) 
        pass

    def over_change(self):# when don't need to change point
        self.points_old=self.points_new
        self.points_new=[]

    def process_point(self,point,index,end=False):# called after over_receive
        if len(self.points_old)==1:#top
            if self.points_new:
                pla=plane.Plane(point,self.points_new[index-1],self.points_old[0])
                self.sphere.store_planes(pla)
            if index==self.max_index-1:
                pla=plane.Plane(self.points_new[0],point,self.points_old[0])
                self.sphere.store_planes(pla)
        elif end:#end
            for i in range(self.max_index-1):
                pla=plane.Plane(point,self.points_old[i],self.points_old[i+1])
                self.sphere.store_planes(pla)
            pla=plane.Plane(point,self.points_old[i],self.points_old[0])
            self.sphere.store_planes(pla)
        else:#body
            if self.points_new:
                pla=plane.Plane(point,self.points_new[index-1],self.points_old[index])
                self.sphere.store_planes(pla)
            
            if index!=self.max_index-1:
                pla=plane.Plane(point,self.points_old[index],self.points_old[index+1])
                self.sphere.store_planes(pla)
                
                
            else:
                pla=plane.Plane(point,self.points_old[index],self.points_old[0])
                self.sphere.store_planes(pla)
                #print(self.points_new)
                pla=plane.Plane(self.points_new[0],point,self.points_old[0])
                self.sphere.store_planes(pla)
        self.change_point(point)

    # def c_script(self):
    #     create_script.planes(self.plants)
        