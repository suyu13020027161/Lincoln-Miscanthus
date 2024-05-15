import struct

def read_and_print_ply(pointnum, filepath, rza, rzb):
    print("Start reading and filtering the point cloud!")
    #定义按照高度划分的过滤点云数组（苏雨）
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
            progress = (i / pointnum)*100
            #print(f"(x={x}, y={y}, z={z}) Color: (red={red}, green={green}, blue={blue})")
            #print(data)
            if rza > rzb:
                if rzb <= z and z <= rza:
                    vertices_z.append(data)

            else:
                if rza <= z and z <= rzb:
                    vertices_z.append(data)                                                                  
            pp = str(progress)
            print("\rProgress: " + pp + "%", end="         ")
            i = i + 1            
    return (vertices_z)
                        
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
    print("Start saving data!")
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
save_file_path = "/home/suyu/Miscanthus/terra_point_ply/processed_cloud.ply"
rza = -27.21
rzb = -27.19

pointnum = read_vertex_count(file_path)
vertices_z = read_and_print_ply(pointnum, file_path, rza, rzb)
write_ply_binary_with_colors(save_file_path, vertices_z)
print("All done!")


