import convert as conv
from visualize import visualizor

class Pos:
    def __init__(self) -> None:
        self.uv=[]
        self.enu=[]
        self.timestamp=0
        pass
    
class Trajectory:
    def __init__(self,uuid=0):
        self.pos_list=[]
        self.uuid=uuid
        
    def add_pos(self,pos):
        self.pos_list.append(pos)
        
class TrajectoryDB:
    def __init__(self):
        # self.trajectories=[]
        self.trajectories={}
        self.count=0
        self.converter=conv.Converter()
    
    def add_trajectory(self,trajectory):
        trajectory.uuid=self.count
        self.trajectories[trajectory.uuid]=trajectory
        self.count+=1
        
    def read_trajectory_from_file(self,file_path):
        trajectory = Trajectory()

        with open(file_path, 'r') as file:
            for line in file:
                # 假设每行数据是以逗号分隔的
                data= line.strip().split(',')
                timestamp=int(data[0])
                u=float(data[1])
                v=float(data[2])
                # timestamp,u, v = map(int, line.strip().split(','))
                pos=Pos()
                pos.timestamp=timestamp
                pos.uv=[u,v]
                enu=self.converter.pixel2enu(u,v)
                pos.enu=[enu[0],enu[1],0]
                trajectory.add_pos(pos)

        return trajectory
        
    def read_folder(self,data_folder):
        import os
        for filename in os.listdir(data_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(data_folder, filename)

                # 读取文件并创建trajectory对象
                trajectory = self.read_trajectory_from_file(file_path)
                # 将trajectory对象添加到列表中
                self.add_trajectory(trajectory)
                
    def visualize_data(self):
        # plot all tracked trajectory
        for key,trajectory in self.trajectories.items():
            example_coordinates=[]
            for single_pt in trajectory.pos_list:
                example_coordinates.append((single_pt.enu[0],single_pt.enu[1]))
            
            visualizor.plot_trajectory(example_coordinates)
        # for target_uuid in self.database.dict:
        #     print("uuid:",target_uuid)
        #     trajectory=self.database.dict[target_uuid]
        #     example_coordinates=[]
        #     for single_pt in trajectory:
        #         example_coordinates.append((single_pt.enu[0],single_pt.enu[1]))
        #     visualizor.plot_trajectory(example_coordinates)
        