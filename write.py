import random
import struct

def generate_random_points_with_colors(num_points):
    # 生成随机点云数据及颜色
    vertices = []
    for _ in range(num_points):
        x = random.uniform(-10, 10)  # 生成-10到10之间的随机浮点数
        y = random.uniform(-10, 10)
        z = random.uniform(-10, 10)
        r = random.randint(0, 255)  # 生成0到255之间的随机整数
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        vertices.append((x, y, z, r, g, b))
    return vertices

def write_ply_binary_with_colors(filename, vertices):
    # 准备二进制PLY文件的头部信息
    header = [
        "ply",
        "format binary_little_endian 1.0",
        "comment REpJLUwxLUxBUl9TVUEu",
        "element vertex " + str(len(vertices)),
        "property float x",
        "property float y",
        "property float z",
        "property uchar red",
        "property uchar green",
        "property uchar blue",                
        "end_header"
    ]
    
    with open(filename, 'wb') as file:
        # 写入头部信息，每行后加入换行符，并编码为ascii
        for line in header:
            file.write((line + "\n").encode('ascii'))
        
        # 写入点坐标及颜色数据
        for x, y, z, r, g, b in vertices:
            # 使用struct将浮点数和整数转换为二进制格式
            packed_data = struct.pack('fffccc', x, y, z, bytes([r]), bytes([g]), bytes([b]))
            file.write(packed_data)

# 使用示例
num_points = 1  # 指定生成1000个随机点
filename = "random_points_with_colors_binary.ply"  # 定义文件名
vertices = generate_random_points_with_colors(num_points)  # 生成点云及颜色
write_ply_binary_with_colors(filename, vertices)  # 写入文件


























