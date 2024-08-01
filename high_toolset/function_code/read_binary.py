#苏雨的读取并打印二进制点云坐标文件
from plyfile import PlyData

# 读取PLY文件
filepath = '/home/ysu/Miscanthus/toolset/data/coord_transfer/Walled Garden 24 07 29_utm.ply'
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
    x, y, z, r, g, b = data['x'], data['y'], data['z'], data['red'], data['green'], data['blue']
    print(f"X: {x}, Y: {y}, Z: {z}, R: {r}, G: {g}, B: {b}")
    x = float(x)
    progress = (i / pointnum)*100
    pp = str(progress)
    print("\rProgress: " + pp + "%", end="         ")
    i = i + 1

