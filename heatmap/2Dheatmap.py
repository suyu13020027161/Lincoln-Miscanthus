#苏雨的二维高度热力图生成程序
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyntcloud import PyntCloud
from matplotlib.colors import ListedColormap



# 读取PLY文件
ply_file_path = '23_08_09_arbitrary.ply'  # 替换为你的PLY文件路径
cloud = PyntCloud.from_file(ply_file_path)

# 获取点云数据
points = cloud.points

# 压缩点云到二维（仅保留xy坐标和z坐标）
points_2d = points[['x', 'y', 'z']]

# 根据z坐标进行颜色映射（从绿到黄再到红）
z_min, z_max = points_2d['z'].min(), points_2d['z'].max()
z_normalized = (points_2d['z'] - z_min) / (z_max - z_min)

def color_map(z):
    if z < 0.5:
        return (2*z, 1, 0)  # 从绿到黄
    else:
        return (1, 2*(1-z), 0)  # 从黄到红

colors = np.array([color_map(z) for z in z_normalized])

# 创建自定义的颜色映射
cmap = ListedColormap([color_map(z) for z in np.linspace(0, 1, 256)])

# 绘制二维点云图
plt.figure(figsize=(10, 8))
scatter = plt.scatter(points_2d['x'], points_2d['y'], c=colors, s=1)
#plt.xlabel('X')
#plt.ylabel('Y')
#隐藏xy坐标
plt.xticks([]) 
plt.yticks([]) 

plt.title('2D miscanthus heat map')

# 创建颜色条
norm = plt.Normalize(0, z_max-z_min)
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=plt.gca(), orientation='vertical')
cbar.set_label('High Value')

plt.show()

