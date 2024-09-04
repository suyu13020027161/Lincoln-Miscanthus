#苏雨的读取并打印二进制点云坐标文件
from plyfile import PlyData

# 读取PLY文件
ply = PlyData.read('UGV_ASCII.ply')

# 获取顶点信息
vertex = ply['vertex']

print(vertex)


# 打印每个点的XYZ坐标
for data in vertex:
    x, y, z = data['x'], data['y'], data['z']
    print(f"X: {x}, Y: {y}, Z: {z}")
    x = float(x)
    print(x)

