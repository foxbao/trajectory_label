import numpy as np
import pymap3d as pm

class Converter():
    def __init__(self):
        self.lat0=30.8831327
        self.lon0=121.9367197
        self.h0=100
        
        
    def llh2enu(self,llh):
        return pm.geodetic2enu(llh[0],llh[1],llh[2], self.lat0, self.lon0, self.h0)
    
    def enu2llh(self,enu):
        return pm.enu2geodetic(enu[0],enu[1],enu[2],self.lat0, self.lon0, self.h0)
        
    def enu2pixel(self,pos_enu):
        # The local coordinate origin (Zermatt, Switzerland)
        lat0 = 46.017 # deg
        lon0 = 7.750  # deg
        h0 = 1673     # meters

        # The point of interest
        lat = 45.976  # deg
        lon = 7.658   # deg
        h = 4531      # meters

        pm.geodetic2enu(lat, lon, h, lat0, lon0, h0)
        pos_world=np.array([1,2,1]).reshape(-1,1)
        rotation_matrix = np.eye(3)
        result=rotation_matrix*pos_world
        print(result)
        translation_vector = np.array([1,1,1]).reshape(-1,1)
        f1=1.1
        f2=2.2
        intrinsic_matrix=np.array([[f1,0,0],[0,f2,0],[0,0,1]])
        print(intrinsic_matrix)
        aaa=2
        
    def pixel2enu(self,pos_pixel):
        aaa=2

def main():
    converter=Converter()
    converter.enu2pixel()
    
    # data_root=input("please input the full path of data root folder:")
    # trajectoryLabel=TrajectoryLabel('.\data')
    # trajectoryLabel.label()
if __name__== "__main__" :
    main()