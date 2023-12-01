from data_structure import trajectory as tr
import sensetime_data as sd

class validator:
    def __init__(self) -> None:
        pass
    
    def validate(self):
        pass
    
    def RMSE(self):
        pass



def main():
    # Label database
    label_data_folder_path = 'label_ns'  # 替换为你的文件夹路径
    label_trajectory_DB=tr.TrajectoryDB() # 保存所有trajectory对象的列表
    label_trajectory_DB.read_folder(label_data_folder_path)
    label_trajectory_DB.visualize_data()
    # Roadside database
    sensetime_data_folder_path = "./sensetime_data/Edge_RCU.json"
    sensetimeProcessor=sd.SensetimeProcessor()
    sensetimeProcessor.process_data(sensetime_data_folder_path)
    # sensetimeProcessor.visualize_data()
    aaaa=2

if __name__ == "__main__":
    main()

