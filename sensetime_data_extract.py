import json
import preprocess
import test_plot
from common import geographic

class TrackedTargetDB:
    def __init__(self) -> None:
        self.dict={}
    
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
        
class TargetDatabase:
    def __init__(self) -> None:
        pass
    
    def selectVehicle(self,uuid):
        pass
    
    def seleteTime(self,time0,time1):
        pass
    
    

def read_file_and_extract_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        device_data_list = [DeviceData(device_data) for device_data in data.get("data", [])]
    return device_data_list

def main():
    database=TrackedTargetDB()
    prepare_data=False
    if prepare_data:
        input_data = "./sensetime_data/Edge_RCU.json"
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
            if uuid not in database.dict:
                database.dict[uuid]=[]
            database.dict[uuid].append(target)
            # print("uuid:",target.uuid,"timestamp:",target.timestamp,"longitude:",target.longitude,"latitude:",target.latitude)
        # print(device_data_instance.kafkaTime)
        # print(device_data_instance.timestampOfDetOut)
        # Access other attributes as needed
    geog=geographic.Geographic()
    # plot all tracked trajectory
    for target_uuid in database.dict:
        print("uuid:",target_uuid)
        trajectory=database.dict[target_uuid]
        example_coordinates=[]
        sample=[]
        
        for single_pt in trajectory:
            llh=[single_pt.latitude,single_pt.longitude,0]
            enu=geog.llh2enu(llh)
            sample.append((single_pt.timestamp,enu[0],enu[1],llh))
            example_coordinates.append((enu[0],enu[1]))
        print(sample)
        test_plot.plot_trajectory(example_coordinates)
        
if __name__ == "__main__":
    main()
