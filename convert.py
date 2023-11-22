import numpy as np

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