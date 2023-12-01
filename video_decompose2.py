import cv2
import os
from datetime import datetime, timedelta

def extract_frames(input_video, output_folder, start_datetime_str, total_seconds,frame_interval=20):
    # 解析初始日期时间字符串
    start_datetime = datetime.strptime(start_datetime_str, "%Y%m%d%H%M%S%f")

    # 打开视频文件
    video_capture = cv2.VideoCapture(input_video)

    # 获取视频的帧率和总帧数
    fps=video_capture.get(cv2.CAP_PROP_FPS)
    # fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    real_fps=total_frames/total_seconds
    
    
    # 计算应该保存的帧数
    frames_to_save = list(range(0, total_frames, frame_interval))

    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 初始化日期时间
    current_datetime = start_datetime

    # 逐帧读取视频并保存
    for frame_number in frames_to_save:
        # 设置当前帧位置
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        
        # 读取当前帧
        ret, frame = video_capture.read()
        current_datetime=start_datetime+timedelta(milliseconds=frame_number* (1000 / real_fps))
        # print(current_datetime)
        if ret:
            # 生成输出文件名，使用给定的日期时间
            timestamp_str = (current_datetime).strftime("%Y%m%d%H%M%S%f")[:-3]
            output_file = os.path.join(output_folder, f"{timestamp_str}.jpg")
            print(output_file)
            # 保存当前帧为图片
            cv2.imwrite(output_file, frame)

            # 更新日期时间，增加帧间隔的毫秒数
            # current_datetime = timedelta(milliseconds=frame_number*frame_interval * (1000 / fps))
            # current_datetime=start_datetime+timedelta(milliseconds=frame_number*frame_interval * (1000 / fps))
            # current_datetime += timedelta(milliseconds=frame_interval * (1000 / fps))
    # 释放视频捕获对象
    video_capture.release()

# 示例：提取每20帧保存一帧，使用给定的初始日期时间命名
# input_video_path = "video_data/南港北向南1630-1730.mp4"  # 替换为你的视频文件路径
# output_folder_path = "output_images_ns"  # 替换为你的输出文件夹路径
# start_datetime_str = "20231129163000000"  # 替换为你的初始日期时间字符串

# total_seconds=3585

input_video_path = "video_data/南港南向北1630-1730.mp4"  # 替换为你的视频文件路径
output_folder_path = "output_images_sn"  # 替换为你的输出文件夹路径
total_seconds=3587

start_datetime_str = "20231129162958000"  # 替换为你的初始日期时间字符串

extract_frames(input_video_path, output_folder_path, start_datetime_str, total_seconds,frame_interval=20)
