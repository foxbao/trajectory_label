import matplotlib.pyplot as plt

def set_figure(title='Trajectory Plot'):
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)

def plot_trajectory(coordinates,color='blue',marker='o', markersize=1,linewidth=1,linestyle='-'):
    x_values, y_values = zip(*coordinates)  # 拆分 x 和 y 坐标
    plt.plot(x_values, y_values, color=color,marker=marker, markersize=markersize,linewidth=linewidth,linestyle=linestyle)
    plt.show()

def clear_figure():
    plt.clf()
    
def main():
    # 示例坐标数据
    example_coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

    # 调用函数绘制折线图
    plot_trajectory(example_coordinates)
    aa=1
if __name__ == "__main__":
    main()
