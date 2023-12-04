from data_structure import trajectory as tr
import sensetime_data as sd
from visualize import visualizor
from common import mathLib

class Validator:
    def __init__(self) -> None:
        pass
    
    def validate(self):
        # Label database
        label_data_folder_path = 'label_ns'  # 替换为你的文件夹路径
        label_trajectory_DB=tr.TrajectoryDB() # 保存所有trajectory对象的列表
        label_trajectory_DB.read_folder(label_data_folder_path)
        # label_trajectory_DB.visualize_data()
        
        
        # Roadside database
        sensetime_data_folder_path = "./sensetime_data/Edge_RCU_Data-1_1701262648047.json"
        sensetimeProcessor=sd.SensetimeProcessor()
        sensetimeProcessor.process_data(sensetime_data_folder_path,combine_json=False,load2database=False)
        # uuid_list=sensetimeProcessor.get_vehicle_uuid_list()
        
        # sensetimeProcessor.get_trajectory_timestamp_range(20231129162959986,20231129163000088)
        # sensetimeProcessor.get_trajectory_uuid("st002_7119")
        # sensetimeProcessor.process_data(sensetime_data_folder_path,combine_json=False)
        
        for key,label_trajectory in label_trajectory_DB.trajectories.items():
            timestamp0=label_trajectory.pos_list[0].timestamp
            timestamp1=label_trajectory.pos_list[-1].timestamp
            visualizor.clear_figure()
            visualizor.set_figure(str(timestamp0)+" to\n"+str(timestamp1))
            sensetimeProcessor.get_matched_trajectory(label_trajectory)
            #visualize label data
            coordinates=[]
            for pos in label_trajectory.pos_list:
                coordinates.append((pos.enu[0],pos.enu[1]))
                visualizor.plot_trajectory(coordinates,color='red')
                pass
        sensetimeProcessor.visualize_data()
    
    def RMSE(self,trajecoty0,trajecoty1):
        pass


def main():
    validator=Validator()
    validator.validate()



if __name__ == "__main__":
    main()

