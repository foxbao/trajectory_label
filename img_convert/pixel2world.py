import numpy as np

def pixel_to_enu(u, v, K, R, t):
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
focal_length_x=2000
focal_length_y=2000
principal_point_x=988
principal_point_y=553
# 例子：内参矩阵、旋转矩阵和平移向量（需要替换为实际的值）
K = np.array([[focal_length_x, 0, principal_point_x],
              [0, focal_length_y, principal_point_y],
              [0, 0, 1]])

R = np.array([[0.9949083037189511,-0.0994611394956592,0.016277251650814832],
[-0.0026019178060054104,-0.18680011282959813,-0.9823944970685555],
[0.10075066855763154,0.9773500905904057,-0.18610777309966356]])
t = np.array([1.082803377797102,6.248220239694936,1.2587117800968828]).reshape(-1,1)
# 示例地面点的像素坐标
u_pixel = 1418
v_pixel = 732

# 计算世界坐标
world_coordinates = pixel_to_enu(u_pixel, v_pixel, K, R, t)

# check

pt_enu=np.array([world_coordinates[0],world_coordinates[1],0]).reshape(-1,1)

pt_cam=R@pt_enu+t
print(pt_cam)
aaaa=K@((R@pt_enu+t)/pt_cam[2])



print("World Coordinates:", world_coordinates)
