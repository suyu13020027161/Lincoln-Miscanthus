#苏雨的根据经过比较的csv文件生成新的相对高度热力图程序自动版
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
from pathlib import Path

def plot_heatmap(csv_file, square_size, output_dir):
    # 读取 CSV 文件
    df = pd.read_csv(csv_file)
    
    # 提取 x, y, 和 values
    x = df.iloc[:, 0].values
    y = df.iloc[:, 1].values
    values = df.iloc[:, 2].values

    # 创建归一化颜色映射
    norm = mcolors.Normalize(vmin=0, vmax=3)
    cmap = mcolors.LinearSegmentedColormap.from_list("", ["green", "yellow", "red"])
    vmax=max(values)
    print(csv_file)
    print(vmax)
    # 设置图像和色标
    fig, ax = plt.subplots()
    sc = ax.scatter(x, y, c=values, s=square_size**2, cmap=cmap, norm=norm, marker='s', edgecolors='none')

    # 添加色标
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label('Relative height (m)')

    # 隐藏坐标轴
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # 隐藏坐标轴线
    ax.axis('off')

    # 设置标题
    ax.set_title('2D Relative Heatmap')

    # 图像保存路径
    output_path = Path(output_dir) / (Path(csv_file).name.replace('.csv', '.png'))
    plt.savefig(output_path, bbox_inches='tight')
    plt.close(fig)  # 关闭图形以节省内存
    #print(f"Heatmap saved to {output_path}")

def generate_heatmaps(input_dir, output_dir, square_size):
    # 确保输出目录存在
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # 遍历目录下的所有 CSV 文件
    for csv_file in os.listdir(input_dir):
        if csv_file.endswith('.csv'):
            csv_path = Path(input_dir) / csv_file
            plot_heatmap(csv_path, square_size, output_dir)

# 路径设置
input_dir = '/home/ysu/Miscanthus/toolset/data/comp_csv/Aber_filted/20241023_Aber'
output_dir = '/home/ysu/Miscanthus/toolset/heatmap_toolset/output_data/relative_map/Aber_filted/20241023_Aber'
square_size = 6.8  # 正方形边长

# 开始处理
generate_heatmaps(input_dir, output_dir, square_size)




