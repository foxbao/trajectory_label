import numpy as np
import math
from scipy.spatial.transform import Rotation as R
 
def euler2rot(euler):
    r = R.from_euler('xyz', euler, degrees=True)
    rotation_matrix = r.as_matrix()
    return rotation_matrix

def isRotationMatrix(R):
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype=R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6
 
 
def rot2euler(R):
    assert (isRotationMatrix(R))
 
    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])
 
    singular = sy < 1e-6
 
    if not singular:
        x = math.atan2(R[2, 1], R[2, 2]) * 180 / np.pi
        y = math.atan2(-R[2, 0], sy) * 180 / np.pi
        z = math.atan2(R[1, 0], R[0, 0]) * 180 / np.pi
    else:
        x = math.atan2(-R[1, 2], R[1, 1]) * 180 / np.pi
        y = math.atan2(-R[2, 0], sy) * 180 / np.pi
        z = 0
 
    return np.array([x, y, z])
 
def point_to_segment_distance(point, segment):
    p, p1, p2 = np.array(point), np.array(segment[0]), np.array(segment[1])
    
    # 计算线段的方向向量
    v = p2 - p1
    
    # 计算点到线段起点的向量
    w = p - p1
    
    # 计算点到线段的投影点的参数 t
    t = np.dot(w, v) / np.dot(v, v)
    
    # 如果 t 在 [0, 1] 之间，表示投影点在线段上
    if 0 <= t <= 1:
        # 计算投影点的坐标
        projection_point = p1 + t * v
        
        # 计算点到投影点的距离
        distance = np.linalg.norm(p - projection_point)
        
        return distance, projection_point
    
    # 如果 t < 0，则投影点在线段起点的反方向
    elif t < 0:
        distance = np.linalg.norm(p - p1)
        return distance, p1
    
    # 如果 t > 1，则投影点在线段终点的反方向
    else:
        distance = np.linalg.norm(p - p2)
        return distance, p2

# segments is composed with several 2D points
def point_to_segments_distance(point,segments):
    
    
    pass


def main():
    
# 示例使用
    point_P = (2, 3)
    segment_P1_P2 = ((1, 1), (5, 5))

    distance, nearest_point_on_segment = point_to_segment_distance(point_P, segment_P1_P2)

    print(f"点到线段的距离: {distance}")
    print(f"离开点最近的线段上的点: {nearest_point_on_segment}")
    
    euler=[0,0,30]
    rot=euler2rot(euler)
    print(rot)
    pos_enu=[10,0,0]
    euler = [-24.90053735,    6.599459,   -169.1003646]
    rot=euler2rot(euler)
    print(rot)
    
    # rot = np.array([[-1.01749712e-02,  9.99670705e-01, -2.35574076e-02],
    # [-9.99890780e-01, -1.04241019e-02, -1.04769347e-02],
    # [-1.07190495e-02,  2.34482322e-02,  9.99667586e-01]])
    
    
    print(rot2euler(rot))
    # 输出
    # [  1.34368509   0.61416806 -90.58302646]
    
    
if __name__== "__main__" :
    main()
