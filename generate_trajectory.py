class Trajectory:
    def __init__(self):
        self.coordinates = []

def read_trajectory_from_file(file_path):
    trajectory = Trajectory()

    with open(file_path, 'r') as file:
        for line in file:
            # 假设每行数据是以逗号分隔的
            x, y = map(int, line.strip().split(','))

            # 将坐标点添加到trajectory对象中
            trajectory.coordinates.append((x, y))

    return trajectory

def main():
    folder_path = 'label_data'  # 替换为你的文件夹路径

    trajectories = []  # 保存所有trajectory对象的列表

    # 遍历文件夹中的每个txt文件
    import os
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)

            # 读取文件并创建trajectory对象
            trajectory = read_trajectory_from_file(file_path)

            # 将trajectory对象添加到列表中
            trajectories.append(trajectory)

    # 打印每个trajectory对象的坐标数据
    for i, trajectory in enumerate(trajectories, start=1):
        print(f'Trajectory {i} coordinates:')
        for x, y in trajectory.coordinates:
            print(f'({x}, {y})')



if __name__ == "__main__":
    main()

