import PointProcessor
import numpy as np
import rotate
import create_script

#x y z


def create_sphere(position,size,separate_degree):
    new_pos_ver=np.array([[0],[size],[0]]).round(decimals=3)
    num_segment=int(180//separate_degree)  #3n=degree degree<180
    
    circle=int(360//separate_degree)
    record=[]

    point_pro=PointProcessor.PointProcessor(circle)

    point_pro.receive_point(new_pos_ver)

    for ver in range(1,num_segment+1):
        new_pos_ver=new_pos_hor=(rotate.Rx(separate_degree)*new_pos_ver).round(decimals=1)
        record.append((new_pos_ver,(0,ver*30,0)))


        if ver ==num_segment:
            point_pro.process_point(new_pos_ver,0,True)

        elif  ver :
            for hor in range(circle):
                point_pro.process_point(new_pos_hor,hor)
                new_pos_hor=(rotate.Ry(separate_degree)*new_pos_hor).round(decimals=1)
                
                record.append((new_pos_hor,(0,ver*30,0)))
            point_pro.over_change()

    return point_pro.sphere


        
            
    # for i in range(len(point_pro.plants)):
    #     create_script.points(point_pro.plants[i].p,i)
    #point_pro.c_script()
if __name__=="__main__":
    create_sphere(None,2,30)
    