import numpy as np
import pymap3d as pm

class Converter():
    def __init__(self):
        self.lat0=30.88365912
        self.lon0=121.93665448
        self.h0=100
        self.fx=2253.515223789205
        self.fy=2265.4789929629924
        self.cx=988.0523707419959
        self.cy=553.4837862698109
        self.intrinsic_matrix=np.array([[self.fx,0,self.cx],[0,self.fy,self.cy],[0,0,1]])
        self.rotation_matrix = np.array([[0.9949083037189511,-0.0994611394956592,0.016277251650814832],
        [-0.0026019178060054104,-0.18680011282959813,-0.9823944970685555],
        [0.10075066855763154,0.9773500905904057,-0.18610777309966356]])
        self.translation_vector = np.array([1.082803377797102,6.248220239694936,1.2587117800968828]).reshape(-1,1)
        
        
    def llh2enu(self, llh):
        lat, lon, h = llh
        return pm.geodetic2enu(lat, lon, h, self.lat0, self.lon0, self.h0)
    
    def enu2llh(self,enu):
        return pm.enu2geodetic(enu[0],enu[1],enu[2],self.lat0, self.lon0, self.h0)
        
    def enu2pixel(self,pos_enu):
        pos_cam=np.array([10,10,1]).reshape(-1,1)
        # M(Rx+t)
        
        pos_test=self.intrinsic_matrix.dot(pos_cam)
        pos_pixel=self.intrinsic_matrix.dot(self.rotation_matrix.dot(pos_world))+self.translation_vector
        print(pos_pixel)
        
        
    def pixel2enu(self,pos_pixel):
        aaa=2

def main():
    converter=Converter()
    pos_enu=[1,1,0]
    converter.enu2pixel(pos_enu)
    
    # data_root=input("please input the full path of data root folder:")
    # trajectoryLabel=TrajectoryLabel('.\data')
    # trajectoryLabel.label()
if __name__== "__main__" :
    main()