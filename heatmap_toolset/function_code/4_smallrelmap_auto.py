#苏雨的相对高度热力处理中间程序，将地图网格化，输出csv格式网格信息并绘制网格热力图，自动处理路径下所有文件版
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path

def plot_and_save_filtered_height_distribution(file_path, grid_size, output_dir):
    # 读取点云数据
    point_cloud = o3d.io.read_point_cloud(file_path)
    points = np.asarray(point_cloud.points)

    # 确定网格的大小
    x_min, y_min = np.min(points, axis=0)[:2]
    x_max, y_max = np.max(points, axis=0)[:2]
    x_range = np.arange(x_min, x_max, grid_size)
    y_range = np.arange(y_min, y_max, grid_size)
    z_values = np.full((len(y_range)-1, len(x_range)-1), np.nan)

    # 计算每个网格内点的平均高度
    for i in range(len(x_range) - 1):
        for j in range(len(y_range) - 1):
            mask = (points[:, 0] >= x_range[i]) & (points[:, 0] < x_range[i + 1]) & \
                   (points[:, 1] >= y_range[j]) & (points[:, 1] < y_range[j + 1])
            grid_points = points[mask]
            if len(grid_points) > 0:
                average_height = np.mean(grid_points[:, 2])
                if average_height > 0:
                    z_values[j, i] = average_height

    # 保存网格数据到CSV
    grid_data = {'x_center': [], 'y_center': [], 'average_height': []}
    for i in range(z_values.shape[1]):
        for j in range(z_values.shape[0]):
            if not np.isnan(z_values[j, i]):
                grid_data['x_center'].append((x_range[i] + x_range[i+1]) / 2)
                grid_data['y_center'].append((y_range[j] + y_range[j+1]) / 2)
                grid_data['average_height'].append(z_values[j, i])
    grid_df = pd.DataFrame(grid_data)
    csv_path = Path(output_dir) / (Path(file_path).stem + '.csv')
    grid_df.to_csv(csv_path, index=False)
    print(f"Grid data saved to {csv_path}")

    # 绘制高度分布图并保存
    plt.figure(figsize=(10, 8))
    plt.pcolormesh(x_range, y_range, z_values, cmap='RdYlGn_r', shading='auto')
    plt.colorbar(label='Average Height (m)')
    plt.title('Filtered 2D Point Height Distribution Grid')
    plt.xlabel('X Coordinate (m)')
    plt.ylabel('Y Coordinate (m)')
    plt.grid(True)
    plt_path = Path(outputimg_dir) / (Path(file_path).stem + '.png')
    plt.savefig(plt_path, bbox_inches='tight')
    plt.close()  # Close the figure to free memory
    print(f"Heatmap saved to {plt_path}")



    # 绘制高度分布图
    plt.figure(figsize=(10, 8))
    plt.pcolormesh(x_range, y_range, z_values, cmap='RdYlGn_r', shading='auto')
    plt.colorbar(label='Average Height (m)')
    plt.title('Filtered 2D Point Height Distribution Grid')
    plt.xlabel('X Coordinate (m)')
    plt.ylabel('Y Coordinate (m)')
    plt.grid(True)
    plt.show()

# 路径设置
input_dir = '/home/ysu/Miscanthus/toolset/data/filterz/Aber_filted/20241023_Aber'  # 输入文件夹路径
output_dir = '/home/ysu/Miscanthus/toolset/data/raw_csv/Aber_filted/20241023_Aber'  # 输出CSV文件夹路径
outputimg_dir = '/home/ysu/Miscanthus/toolset/heatmap_toolset/output_data/rawgrid_map/Aber_filted/20241023_Aber'  # 输出图像文件夹路径

grid_size = 0.25  # 网格大小

# 处理文件夹中的所有ply文件
for filename in os.listdir(input_dir):
    if filename.endswith('.ply'):
        file_path = os.path.join(input_dir, filename)
        plot_and_save_filtered_height_distribution(file_path, grid_size, output_dir)











