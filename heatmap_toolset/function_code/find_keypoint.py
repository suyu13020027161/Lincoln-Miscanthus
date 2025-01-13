#苏雨的读取并打印二进制点云某个点坐标的文件
import math
from plyfile import PlyData

# 读取PLY文件
filepath = '20241023_Aber.ply'
target_x = 435382.108 - 435000
target_y = 5798993.339 - 5798000



ply = PlyData.read(filepath)

# 获取顶点信息
vertex = ply['vertex']


vertex_count = 0
with open(filepath, 'rb') as file:
    while True:
        line = file.readline()
        if b"end_header" in line:
            break
        if b"element vertex" in line:
            parts = line.split()
            pointnum = int(parts[2])  





closest_distance = float('inf')  # 初始化最小距离为无限大
closest_x = 0
closest_y = 0
closest_z = 0
i = 0
# 打印每个点的XYZ坐标
for data in vertex:   
    x, y, z, r, g, b = data['x'], data['y'], data['z'], data['red'], data['green'], data['blue']
    #print(f"X: {x}, Y: {y}, Z: {z}, R: {r}, G: {g}, B: {b}")    
    x = float(x)
    y = float(y)
    z = float(z) 
    # 计算当前点和目标点之间的欧几里得距离
    distance = math.sqrt((x - target_x) ** 2 + (y - target_y) ** 2)
    # 如果当前距离小于之前记录的最小距离，则更新最小距离和最接近的行
    if distance < closest_distance:
        closest_x = x
        closest_y = y          
        closest_z = z 
        closest_distance = distance   
    progress = (i / pointnum)*100
    pp = str(progress)
    print("\rProgress: " + pp + "%", end="         ")
    i = i + 1

closest_z = closest_z + 100
out = 'z='+str(closest_z)
print(out)











