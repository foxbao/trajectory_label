import cv2
import numpy as np
import matplotlib.pyplot as plt
from common.geographic import Geographic
from Viewer import Viewer
class Homography:
    def __init__(self) -> None:
        self.gps_list=[]
        self.imgpts_list=[]
        self.enu_list=[]
        self.geographic=Geographic()
        pass
    
    
    def gps2enu(self,gps_list):
        list_of_lists = []
        for gps in gps_list:
            # line_numbers = [gps_data for gps_data in gps]
            enu=self.geographic.llh2enu(gps)
            enu_pt=[enu[0],enu[1],enu[0]]
            list_of_lists.append(enu_pt)
        return list_of_lists
    
    def read_data(self,file_path):
        # 初始化一个空列表来保存每一行的三个浮点型数字
        # 初始化一个空列表来保存每一行的三个浮点型数字
        list_of_lists = []

        # 打开文件并逐行读取浮点型数字
        with open(file_path, 'r') as file:
            for line in file:
                # 将每行的数字拆分成一个列表（假设数字之间用逗号分隔）
                line_numbers = [float(num) for num in line.strip().split(',')]

                # 将每行的列表添加到总列表中
                list_of_lists.append(line_numbers)
        return list_of_lists
        
    def read_gps(self,file_path):
        self.gps_list=self.read_data(file_path)
        self.enu_list=self.gps2enu(self.gps_list)
        return self.gps_list
    
    def read_imgpts(self,file_path):
        self.imgpts_list=self.read_data(file_path)
        return self.imgpts_list
    
    def generate_sample_data(self):
        # Generate 25 random point pairs for demonstration
        np.random.seed(42)
        points_src = np.random.rand(25, 2) * 100  # Source points
        homography_matrix = np.array([[2, 0.5, 30], [0.1, 1.5, 20], [0.001, 0.002, 1]])  # Homography matrix
        points_dst = cv2.perspectiveTransform(points_src.reshape(-1, 1, 2), homography_matrix)[:, 0, :]

        return points_src, points_dst

    def homography_transform(self,points_src, points_dst):
        # Find homography matrix using OpenCV
        homography_matrix, _ = cv2.findHomography(points_src, points_dst)

        return homography_matrix

    def apply_homography_transform(self,points_src, homography_matrix):
        # Apply homography transformation
        points_transformed = cv2.perspectiveTransform(points_src.reshape(-1, 1, 2), homography_matrix)[:, 0, :]
        return points_transformed
    
    

def main():
    # Generate sample data
    homography=Homography()
    homography.read_gps("homo_data/dh-n2s_gps_all.txt")
    
    homography.read_imgpts("homo_data/dh-n2s_imgpts_all.txt")
    # points_src, points_dst = homography.generate_sample_data()
    en_list=[]
    for enu in homography.enu_list:
        en=enu[0:2]
        en_list.append(en)
    points_src = np.array(en_list)
    print(points_src)
    # points_src = np.array(homography.en_list)

    points_dst = np.array(homography.imgpts_list)


    # Find homography matrix
    homography_matrix = homography.homography_transform(points_src, points_dst)

    # Apply homography transformation to the source points
    points_transformed = homography.apply_homography_transform(points_src, homography_matrix)

    # Display the results
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(points_src[:, 0], points_src[:, 1], c='r', marker='o', label='Source Points')
    plt.scatter(points_dst[:, 0], points_dst[:, 1], c='b', marker='x', label='Destination Points')
    plt.title('Original Points')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(points_src[:, 0], points_src[:, 1], c='r', marker='o', label='Source Points')
    plt.scatter(points_transformed[:, 0], points_transformed[:, 1], c='g', marker='s', label='Transformed Points')
    plt.title('Homography Transformed Points')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

    