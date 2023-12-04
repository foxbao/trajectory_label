import xml.etree.ElementTree as ET

def parse_xodr(file_path):
    # 解析XML文件
    tree = ET.parse(file_path)
    root = tree.getroot()

    # 命名空间
    ns = {'xodr': 'http://www.opendrive.org'}

    # 提取车道线信息
    lanes = root.findall(".//xodr:lanes/xodr:lane", namespaces=ns)

    for lane in lanes:
        lane_id = lane.attrib['id']
        lane_type = lane.attrib['type']
        
        # 获取车道标记
        lane_mark = lane.find("./xodr:center/xodr:line/xodr:lineSegment/xodr:lineMarking", namespaces=ns)
        if lane_mark is not None:
            mark_type = lane_mark.attrib['type']
            print(f"Lane {lane_id}, Type: {lane_type}, Marking: {mark_type}")
        else:
            print(f"Lane {lane_id}, Type: {lane_type}, No Marking")

if __name__ == "__main__":
    xodr_file_path = "your_xodr_file.xodr"  # 替换为实际的xodr文件路径
    parse_xodr(xodr_file_path)
