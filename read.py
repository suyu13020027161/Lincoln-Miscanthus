import struct

def read_and_print_ply(pointnum, filepath, rza, rzb):
    data_format = '<fffccc'
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
            #print(f"(x={x}, y={y}, z={z}) Color: (red={red}, green={green}, blue={blue})")
            print(data)
            if rza > rzb:
                if rzb <= z and z <= rza:
                    print('!')
            else:
                if rza <= z and z <= rzb:
                    print('!')             
            
            
            pp = str(progress)
            #print("\rProgress: " + pp + "%", end="         ")
            i = i + 1
            




def read_vertex_count(filepath):
    vertex_count = 0
    with open(filepath, 'rb') as file:
        while True:
            line = file.readline()
            if b"end_header" in line:
                break
            if b"element vertex" in line:
                parts = line.split()
                vertex_count = int(parts[2])  
    return vertex_count 




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
        file.write(packed_data)







# 替换下面的路径为你的PLY文件路径
file_path = "/home/suyu/Miscanthus/cloud_merged.ply"

rza = -27.21
rzb = -27.19
pointnum = read_vertex_count(file_path)
read_and_print_ply(pointnum, file_path, rza, rzb)



