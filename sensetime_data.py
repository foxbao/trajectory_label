import json
import preprocess
from visualize import visualizor
from common import geographic
from common import timeLib
from vehicle_database import vehicle_database as vdb

class TrackedTargetDB:
    def __init__(self) -> None:
        self.dict={}
        self.time_trajectories_dict={}
    
class TrackedTarget:
    def __init__(self) -> None:
        self.uuid=0
        self.llh=[]
        self.timestamp=[]
        
class Target:
    def __init__(self, data):
        self.speedNorth = data.get("speedNorth", None)
        self.locEast = data.get("locEast", None)
        self.speedConfidence = data.get("speedConfidence", None)
        self.latitude=data.get("latitude",None)
        self.longitude=data.get("longitude",None)
        self.uuid=data.get("uuid",None)
        self.timestamp=data.get("timestamp",None)
        geog=geographic.Geographic()
        llh=(self.latitude,self.longitude,0)
        self.enu=geog.llh2enu(llh)
        self.utctime=timeLib.unix_to_utc_milliseconds(self.timestamp)
        # Add other attributes as needed

class DeviceData:
    def __init__(self, data):
        self.deviceType = data.get("deviceType", None)
        self.gnssType = data.get("gnssType", None)
        self.timestampOfDetIn = data.get("timestampOfDetIn", None)
        self.msgid = data.get("msgid", None)
        self.rcuId = data.get("rcuId", None)
        self.deviceId = data.get("deviceId", None)
        self.targets = [Target(target_data) for target_data in data.get("targets", [])]
        self.kafkaTime = data.get("kafkaTime", None)
        self.timestampOfDetOut = data.get("timestampOfDetOut", None)
        # Add other attributes as needed
    
def read_file_and_extract_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        device_data_list = [DeviceData(device_data) for device_data in data.get("data", [])]
    return device_data_list

class SensetimeProcessor:
    def __init__(self) -> None:
        self.database=TrackedTargetDB()
        self.db2=vdb.VehicleDB()
        pass
    
    def visualize_data(self):
        # plot all tracked trajectory
        for target_uuid in self.database.dict:
            trajectory=self.database.dict[target_uuid]
            example_coordinates=[]
            for single_pt in trajectory:
                example_coordinates.append((single_pt.enu[0],single_pt.enu[1]))
            visualizor.plot_trajectory(example_coordinates)
    
    def visualize_trajectory(self,sensetime_trajectory):
        coordinates=[]
        for pt in sensetime_trajectory:
            coordinates.append((pt[2],pt[3]))
        
        visualizor.plot_trajectory(coordinates)

    
    def get_vehicle_uuid_list(self):
        return self.db2.get_vehicle_uuid_list()
    
    def get_trajectory_uuid(self,uuid):
        return self.db2.get_trajectory_uuid(uuid)
    
    def get_trajectory_uuid_timestampe_range(self,uuid,timestamp0,timestamp1):
        return self.db2.get_trajectory_uuid_timestampe_range(uuid,timestamp0,timestamp1)
    
    def get_trajectory_timestamp_range(self,timestamp0,timestamp1):
        return self.db2.get_trajectory_timestamp_range(timestamp0,timestamp1)
    
    def get_matched_trajectory(self,label_trajectory):
        matched_uuid=0
        timestamp0=label_trajectory.pos_list[0].timestamp
        timestamp1=label_trajectory.pos_list[-1].timestamp
        uuids=self.get_trajectory_timestamp_range(timestamp0,timestamp1)
        
        # visulize label data
        max_error=1000000
        best_matched_uuid=-1
        
        for uuid_sensetime in uuids:
            # compare
            sensetime_trajectory=self.get_trajectory_uuid_timestampe_range(uuid_sensetime,timestamp0,timestamp1)
            # sensetime_trajectory=self.get_trajectory_uuid(uuid_sensetime)
            self.visualize_trajectory(sensetime_trajectory)
            error=self.compute_trajectory_error(label_trajectory,sensetime_trajectory)
            if error<max_error:
                max_error=error
                best_matched_uuid=uuid_sensetime
        
        return matched_uuid
    
    def compute_trajectory_error(self,label_trajectory, sensetime_trajectory):
        aaaa=1
        return 0
                
    
    def process_data(self,input_data,combine_json=True,load2database=False):
        
        if combine_json:
            real_input = "./sensetime_data/real_input.json"
            preprocess.add_delimiter(input_data, real_input)
        # Example usage
        
        self.db2.connect_db()
        file_path = "./sensetime_data/real_input.json"
        if load2database:
            self.db2.delete_table()
            self.db2.create_table()
            device_data_instances = read_file_and_extract_data(file_path)
            # Access the extracted data
            all_targets=[]
            for device_data_instance in device_data_instances:
                self.db2.add_data_targets(device_data_instance.targets)
                # all_targets=all_targets+device_data_instance.targets
            #     # print("rcuId:",device_data_instance.rcuId,device_data_instance.deviceType)
                # for target in device_data_instance.targets:
                #     self.db2.add_data(target)
                    # uuid=target.uuid
                    # if uuid not in self.database.dict:
                    #     self.database.dict[uuid]=[]
                    # self.database.dict[uuid].append(target)
            # self.db2.add_data_targets(all_targets)


def main():
    sensetimeProcessor=SensetimeProcessor()
    input_data = "./sensetime_data/Edge_RCU_Data-1_1701262648047.json"
    sensetimeProcessor.process_data(input_data,combine_json=False,load2database=False)
    uuid_list=sensetimeProcessor.get_vehicle_uuid_list()
    
    sensetimeProcessor.get_trajectory_timestamp_range(20231129162959986,20231129163000088)
    sensetimeProcessor.get_trajectory_uuid("st002_7119")
    sensetimeProcessor.visualize_data()
        
if __name__ == "__main__":
    main()
