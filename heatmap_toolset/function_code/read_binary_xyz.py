#苏雨的读取并打印二进制点云坐标文件
from plyfile import PlyData

# 读取PLY文件
filepath = '20240717_Aber.ply'
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






i = 0
# 打印每个点的XYZ坐标
for data in vertex:   
    x, y, z = data['x'], data['y'], data['z']
    print(f"X: {x}, Y: {y}, Z: {z}")
    x = float(x)
    progress = (i / pointnum)*100
    pp = str(progress)
    print("\rProgress: " + pp + "%", end="         ")
    i = i + 1

