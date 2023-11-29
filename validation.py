from data_structure import trajectory as tr

def main():
    label_data_folder_path = 'label_data'  # 替换为你的文件夹路径
    label_trajectory_DB=tr.TrajectoryDB() # 保存所有trajectory对象的列表
    label_trajectory_DB.read_folder(label_data_folder_path)
    
    sensetime_data_folder_path=''

if __name__ == "__main__":
    main()

