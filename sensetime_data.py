import json
import preprocess
from visualize import visualizor
from common import geographic

class TrackedTargetDB:
    def __init__(self) -> None:
        self.dict={}
        self.time_trajectories_dict={}
        
        
    def matching_trajectory(self,label_trajectory):
        time_label=0
        
        # use the label time to match the roadside time trajectories
        
        # get the most matched
        
        
        pass
    
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
        aaaa=1
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
        pass
    
    def visualize_data(self):
        # plot all tracked trajectory
        for target_uuid in self.database.dict:
            trajectory=self.database.dict[target_uuid]
            example_coordinates=[]
            for single_pt in trajectory:
                example_coordinates.append((single_pt.enu[0],single_pt.enu[1]))
            visualizor.plot_trajectory(example_coordinates)
    
    def process_data(self,input_data):
        prepare_data=False
        if prepare_data:
            real_input = "./sensetime_data/real_input.json"
            preprocess.add_delimiter(input_data, real_input)
        # Example usage
        file_path = "./sensetime_data/real_input.json"
        device_data_instances = read_file_and_extract_data(file_path)

        # Access the extracted data
        for device_data_instance in device_data_instances:
            print("rcuId:",device_data_instance.rcuId,device_data_instance.deviceType)
            for target in device_data_instance.targets:
                uuid=target.uuid
                if uuid not in self.database.dict:
                    self.database.dict[uuid]=[]
                self.database.dict[uuid].append(target)

def main():
    sensetimeProcessor=SensetimeProcessor()
    input_data = "./sensetime_data/Edge_RCU_Data-1_1701262648047.json"
    sensetimeProcessor.process_data(input_data)
    sensetimeProcessor.visualize_data()
        
if __name__ == "__main__":
    main()
