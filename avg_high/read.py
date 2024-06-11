#苏雨的读取打印ply文件程序
# 首先，定义PLY文件的路径
ply_file_path = 'Miscanthus2.ply'

# 打开文件并读取数据
with open(ply_file_path, 'r') as file:
    # 读取整个文件到一个列表中
    lines = file.readlines()
# 找到end_header的位置，因为数据从这之后开始
header_end_index = 0
for i, line in enumerate(lines):
    if "end_header" in line:
        header_end_index = i + 1
        break
# 遍历文件中的顶点数据部分
for line in lines[header_end_index:]:
    parts = line.split()
    if len(parts) < 3:
        continue  # 如果数据行不完整，跳过这行
    x, y, z = parts[:3]  # 只提取前三个元素，即XYZ坐标
    print(f'X: {x}, Y: {y}, Z: {z}')

