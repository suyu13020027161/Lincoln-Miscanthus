import struct
import numpy as np

def read_and_print_ply(pointnum, filepath):
    print("Start reading and filtering the point cloud!")
    vertices_z = []
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
            #开始比大小，如果是第一位则以z为初始值（苏雨）
            if i == 0:
                maxz = z
                minz = z
            if maxz < z:
                maxz = z
            if minz > z:
                minz = z
                      
            progress = (i / pointnum)*100
            #print(f"(x={x}, y={y}, z={z}) Color: (red={red}, green={green}, blue={blue})")
            #print(data)
            #vertices_z.append(float(z))                                                                
            pp = str(progress)
            print("\rProgress: " + pp + "%", end="         ")
            i = i + 1            
    return (maxz, minz)
                        
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







def create_heat(pointnum, filepath, z_range, z_min):
    print("shang se!")
    #定义按照高度划分的过滤点云数组（苏雨）
    colordata = []
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
            #print(data)
            normalized_height = (z - z_min) / z_range
            green = int((1 - normalized_height) * 255)
            red = int(normalized_height * 255)
            blue = 0 
                      
            green_byte = struct.pack('B', green)
            red_byte = struct.pack('B', red)            
            blue_byte = struct.pack('B', 0)
            newdata = struct.pack(data_format, x, y, 0, red_byte, green_byte, blue_byte)
            colordata.append(newdata)
                                                              
            pp = str(progress)
            print("\rProgress: " + pp + "%", end="         ")
            i = i + 1            
    return (colordata)
                        
 
 
 
 
 
 
                        
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
    print("\nStart saving data!")
    #准备二进制PLY文件的头部信息（苏雨）
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
        #写入头部信息，每行后加入换行符，并编码为ascii（苏雨）
        for line in header:
            file.write((line + "\n").encode('ascii'))
        i = 0
        while i < len(vertices):
            datasave = vertices[i]
            file.write(datasave)
            i = i + 1

#替换下面的路径为你的PLY文件路径（苏雨）
file_path = "/home/suyu/Miscanthus/terra_point_ply/clouda2ec8f63304bcf62.ply"
save_file_path = "/home/suyu/Miscanthus/heat_map.ply"


pointnum = read_vertex_count(file_path)
maxz, minz = read_and_print_ply(pointnum, file_path)
print(maxz)
print(minz)
print(type(minz))


#z_min = np.min(vertices_z)
#z_max = np.max(vertices_z)
z_range = maxz - minz

print(z_range)
print(type(z_range))


colordata = create_heat(pointnum, file_path, z_range, minz)

write_ply_binary_with_colors(save_file_path, colordata)
print("All done!")


