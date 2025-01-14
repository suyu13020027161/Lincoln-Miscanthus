#苏雨的根据经过比较的csv文件生成新的相对高度热力图程序
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def plot_heatmap(csv_file, square_size):
    # 读取 CSV 文件
    df = pd.read_csv(csv_file)
    
    # 提取 x, y, 和 values
    x = df.iloc[:, 0].values
    y = df.iloc[:, 1].values
    values = df.iloc[:, 2].values

    # 创建归一化颜色映射
    norm = mcolors.Normalize(vmin=min(values), vmax=max(values))
    cmap = mcolors.LinearSegmentedColormap.from_list("", ["green", "yellow", "red"])

    # 设置图像和色标
    fig, ax = plt.subplots()
    sc = ax.scatter(x, y, c=values, s=square_size**2, cmap=cmap, norm=norm, marker='s', edgecolors='none')


    # 添加色标
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label('Relative height (m)')
    #cbar.ax.invert_yaxis()  # 可以尝试注释或取消注释这行来看看效果



    # 隐藏坐标轴
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # 隐藏坐标轴线
    ax.axis('off')

    # 设置标题
    ax.set_title('2D relative heatmap')

    # 显示图表
    plt.show()


# 使用示例
csv_file = '/home/ysu/Miscanthus/toolset/data/comp_csv/Aber_filted/20240717_Aber/20240717_Aber_GNT3 r5c1.csv'
square_size = 7 # 正方形边长，可以根据需要设置
plot_heatmap(csv_file, square_size)

