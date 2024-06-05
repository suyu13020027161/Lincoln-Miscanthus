#苏雨的读取打印ply文件程序
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
            print(f"(x={x}, y={y}, z={z}) Color: (red={red}, green={green}, blue={blue})")
            #print(data)
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


# 替换下面的路径为你的PLY文件路径
file_path = "/home/ysu/Miscanthus/avg_high/Miscanthus_23_11_23_arbitrary.ply"

rza = -27.21
rzb = -27.19
pointnum = read_vertex_count(file_path)
read_and_print_ply(pointnum, file_path, rza, rzb)



