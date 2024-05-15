import struct

def read_and_print_ply(pointnum, filepath):
    data_format = '<fffBBB'
    with open(filepath, 'rb') as file:
        while True:
            line = file.readline()
            if b"end_header" in line:
                break
        byte_size = struct.calcsize(data_format)
        i = 0
        while True:       
            data = file.read(byte_size)                      
            if not data:
                break
            x, y, z, red, green, blue = struct.unpack(data_format, data)
            progress = (i / pointnum)*100
            print(f"(x={x}, y={y}, z={z}) Color: (red={red}, green={green}, blue={blue})")
            pp = str(progress)
            #print("\rProgress: " + pp + "%", end="         ")
            i = i + 1
            




def read_vertex_count(filepath):
    vertex_count = 0
    with open(filepath, 'rb') as file:
        # 逐行读取直到找到包含 'end_header' 的行
        while True:
            line = file.readline()
            if b"end_header" in line:
                break
            # 查找包含 'element vertex' 的行并提取顶点数
            if b"element vertex" in line:
                parts = line.split()
                vertex_count = int(parts[2])  # parts[2] 应该是顶点数
    return vertex_count 



# 替换下面的路径为你的PLY文件路径
file_path = "/home/suyu/Miscanthus/terra_point_ply/clouda2ec8f63304bcf62.ply"
pointnum = read_vertex_count(file_path)
read_and_print_ply(pointnum, file_path)



