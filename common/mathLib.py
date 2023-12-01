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
 
def distance_point_to_segment(P, P1, P2):
    # 计算线段的长度
    segment_length = math.sqrt((P2[0] - P1[0]) ** 2 + (P2[1] - P1[1]) ** 2)

    # 如果线段长度为零，返回点 P 到 P1 的距离
    if segment_length == 0:
        return math.sqrt((P[0] - P1[0]) ** 2 + (P[1] - P1[1]) ** 2)

    # 计算线段的单位向量
    u = ((P2[0] - P1[0]) / segment_length, (P2[1] - P1[1]) / segment_length)

    # 计算点 P 到 P1 的向量
    v = (P[0] - P1[0], P[1] - P1[1])

    # 计算点 P 到线段的投影长度
    projection_length = u[0] * v[0] + u[1] * v[1]

    # 如果投影在线段之前，返回点 P 到 P1 的距离
    if projection_length <= 0:
        return math.sqrt((P[0] - P1[0]) ** 2 + (P[1] - P1[1]) ** 2)

    # 如果投影在线段之后，返回点 P 到 P2 的距离
    if projection_length >= segment_length:
        return math.sqrt((P[0] - P2[0]) ** 2 + (P[1] - P2[1]) ** 2)

    # 计算点 P 到线段的垂直距离
    perpendicular_distance = math.sqrt((P[0] - (P1[0] + projection_length * u[0])) ** 2 +
                                       (P[1] - (P1[1] + projection_length * u[1])) ** 2)

    return perpendicular_distance


def main():
    
    # 示例
    P = (2, 3)
    P1 = (1, 1)
    P2 = (4, 5)

    result = distance_point_to_segment(P, P1, P2)
    print(f"点 P 到线段的距离为: {result}")
    
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
