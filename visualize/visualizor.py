import matplotlib.pyplot as plt

def plot_trajectory(coordinates):
    x_values, y_values = zip(*coordinates)  # 拆分 x 和 y 坐标
    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.title('Trajectory Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

def main():
    # 示例坐标数据
    example_coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

    # 调用函数绘制折线图
    plot_trajectory(example_coordinates)

if __name__ == "__main__":
    main()
