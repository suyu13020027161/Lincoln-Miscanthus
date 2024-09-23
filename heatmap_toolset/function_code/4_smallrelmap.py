#苏雨的相对高度热力处理中间程序，将地图网格化，输出csv格式网格信息并绘制网格热力图
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_and_save_filtered_height_distribution(file_path, grid_size, csv_path):
    # 读取点云数据
    point_cloud = o3d.io.read_point_cloud(file_path)
    points = np.asarray(point_cloud.points)

    # 确定网格的大小
    x_min, y_min = np.min(points, axis=0)[:2]
    x_max, y_max = np.max(points, axis=0)[:2]

    # 创建网格的X和Y范围
    x_range = np.arange(x_min, x_max, grid_size)
    y_range = np.arange(y_min, y_max, grid_size)

    # 初始化Z值矩阵
    z_values = np.full((len(y_range)-1, len(x_range)-1), np.nan)

    # 计算每个网格内点的平均高度
    for i in range(len(x_range) - 1):
        for j in range(len(y_range) - 1):
            # 找到当前网格内的所有点
            mask = (points[:, 0] >= x_range[i]) & (points[:, 0] < x_range[i + 1]) & \
                   (points[:, 1] >= y_range[j]) & (points[:, 1] < y_range[j + 1])
            grid_points = points[mask]
            # 计算平均高度
            if len(grid_points) > 0:
                average_height = np.mean(grid_points[:, 2])
                if average_height > 0:
                    z_values[j, i] = average_height

    # 将有数据的网格保存到CSV文件
    grid_data = {'x_center': [], 'y_center': [], 'average_height': []}
    for i in range(z_values.shape[1]):
        for j in range(z_values.shape[0]):
            if not np.isnan(z_values[j, i]):
                grid_data['x_center'].append((x_range[i] + x_range[i+1]) / 2)
                grid_data['y_center'].append((y_range[j] + y_range[j+1]) / 2)
                grid_data['average_height'].append(z_values[j, i])
    grid_df = pd.DataFrame(grid_data)
    grid_df.to_csv(csv_path, index=False)
    print(f"Grid data saved to {csv_path}")

    # 绘制高度分布图
    plt.figure(figsize=(10, 8))
    plt.pcolormesh(x_range, y_range, z_values, cmap='RdYlGn_r', shading='auto')
    plt.colorbar(label='Average Height (m)')
    plt.title('Filtered 2D Point Height Distribution Grid')
    plt.xlabel('X Coordinate (m)')
    plt.ylabel('Y Coordinate (m)')
    plt.grid(True)
    plt.show()

# 使用示例
file_path = '/home/ysu/Miscanthus/toolset/data/filterz/new_24_09_06_filted.ply'
grid_size = 0.5  # 网格大小，单位与UTM坐标相同
csv_path = '/home/ysu/Miscanthus/toolset/data/raw_csv/new_24_09_06_filted.csv'
plot_and_save_filtered_height_distribution(file_path, grid_size, csv_path)










