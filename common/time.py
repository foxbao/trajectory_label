from datetime import datetime, timezone, timedelta

def convert_to_unix_time(eastern_eight_time_str):
    # 解析输入的时间字符串
    year = int(eastern_eight_time_str[0:4])
    month = int(eastern_eight_time_str[4:6])
    day = int(eastern_eight_time_str[6:8])
    hour = int(eastern_eight_time_str[8:10])
    minute = int(eastern_eight_time_str[10:12])
    second = int(eastern_eight_time_str[12:14])
    microsecond = int(eastern_eight_time_str[14:]) * 1000  # 转换为微秒

    # 创建datetime对象
    eastern_eight_time = datetime(year, month, day, hour, minute, second, microsecond)

    # 创建时区对象（东八区时区）
    eastern_eight_tz = timezone(timedelta(hours=8))

    # 将时间对象转换为东八区时间
    eastern_eight_time = eastern_eight_time.replace(tzinfo=eastern_eight_tz)

    # 转换为Unix时间
    unix_time=eastern_eight_time.timestamp()

    return unix_time

# 示例：将输入时间字符串转换为Unix时间
input_time_str = "20231128180613282"
unix_time_result = convert_to_unix_time(input_time_str)

print(f"Unix时间: {unix_time_result}")
