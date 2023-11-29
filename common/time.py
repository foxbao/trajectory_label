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


def convert_unix_time_to_utc_int(unix_time_ms):
    # 将毫秒转换为秒和微秒
    unix_time_sec = unix_time_ms // 1000
    microsecond = (unix_time_ms % 1000) * 1000

    # 使用 datetime.utcfromtimestamp 将 Unix 时间戳转换为 datetime 对象
    utc_time = datetime.utcfromtimestamp(unix_time_sec).replace(microsecond=microsecond)

    # 将 UTC 时间格式化为整数表示
    int_representation = int(utc_time.strftime('%Y%m%d%H%M%S%f')[:-3])

    return int_representation

def main():

    # 示例：将精确到毫秒的 Unix 时间戳转换为整数表示的 UTC 时间
    unix_time_ms = 1638031265123  # 替换为你的 Unix 时间戳（精确到毫秒）
    int_representation = convert_unix_time_to_utc_int(unix_time_ms)

    print(f"整数表示的 UTC 时间：{int_representation}")

    # 示例：将输入时间字符串转换为Unix时间
    input_time_str = "20231128180613282"
    unix_time_result = convert_to_unix_time(input_time_str)

    print(f"Unix时间: {unix_time_result}")

if __name__== "__main__" :
    main()
