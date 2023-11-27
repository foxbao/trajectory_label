import numpy as np
import pymap3d as pm
import common.mathLib as ml

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
        
        
    def pixel2world(self,u, v, K, R, t):
        # 1. 使用内参矩阵将像素坐标转换为归一化相机坐标系下的坐标
        normalized_coords = np.linalg.inv(K) @ np.array([u, v, 1])
        # 2. 将归一化相机坐标系下的坐标转换为相机坐标系下的坐标
        camera_coords = normalized_coords / normalized_coords[2]
        print(camera_coords)
        Q=np.array([[R[0,0],R[0,1],-camera_coords[0]],
                [R[1,0],R[1,1],-camera_coords[1]],
                [R[2,0],R[2,1],-1]])
        
        result=np.linalg.inv(Q).dot(-t) # Xw, Yw, Zc
        # 3. 使用旋转矩阵和平移向量将相机坐标系下的坐标转换为世界坐标系下的坐标
        world_coords = np.array([result[0,0],result[1,0],0])

        return world_coords[:2]  # 取前两个元素，即ENU坐标

    def enu2cam(self,pos_enu):
        pos_enu_vec=np.array(pos_enu).reshape(-1,1)
        pos_cam=self.rotation_matrix.dot(pos_enu_vec)+self.translation_vector
        return pos_cam
    
    def cam2pixel(self, pos_cam):
        x, y, z = pos_cam
        """
                          x                                y
            x_im = f_x * --- + offset_x      y_im = f_y * --- + offset_y
                          z                                z
        """
        x, y, z = pos_cam
        if z==0:
            return [0,0]
        return [x * self.fx / z + self.cx, y * self.fy / z + self.cy]

        
        pass
        
    def llh2enu(self, llh):
        lat, lon, h = llh
        return pm.geodetic2enu(lat, lon, h, self.lat0, self.lon0, self.h0)
    
    def enu2llh(self,enu):
        return pm.enu2geodetic(enu[0],enu[1],enu[2],self.lat0, self.lon0, self.h0)
        
    def enu2pixel(self,pos_enu):
        pos_enu_vec=np.array(pos_enu).reshape(-1,1)
        # M(Rx+t)
        ppp=self.rotation_matrix.dot(pos_enu_vec)
        pos_cam=self.rotation_matrix.dot(pos_enu_vec)+self.translation_vector
        
        tttt=self.cam2pixel(pos_cam)
        pos_pixel=self.intrinsic_matrix.dot(pos_cam)
        return pos_pixel
        
        
    def pixel2enu(self,pos_pixel):
        aaa=2

def main():
    converter=Converter()
    # pos_cam=[10,0,10]
    # pos_pixel=converter.cam2pixel(pos_cam)
    # print(pos_pixel)
    pos_enu=[0,10,0]
    aaa=converter.enu2pixel(pos_enu)
    
    bbb=1
    
    
    # data_root=input("please input the full path of data root folder:")
    # trajectoryLabel=TrajectoryLabel('.\data')
    # trajectoryLabel.label()
if __name__== "__main__" :
    main()