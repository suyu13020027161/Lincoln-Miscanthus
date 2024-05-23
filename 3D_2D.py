import struct

def read_and_print_ply(pointnum, filepath):
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
            #print(type(data))
            redvalue = 155
            bytes_red = struct.pack('B', redvalue)
            greenvalue = 0
            bytes_green = struct.pack('B', greenvalue)            
            bluevalue = 0
            bytes_blue = struct.pack('B', bluevalue)
            #print((bytes_green))
            
            
            if 26.377 <= x <= 34.344 and -3.844 <= y <= -0.785:
                print('GNT14!')
                newdata = struct.pack(data_format, x, y, 0, bytes_red, bytes_green, bytes_blue)
                
            elif 34.505 <= x <= 41.104 and -2.234 <= y <= 0.343:
                print('GNT10!')
                newdata = struct.pack(data_format, x, y, 0, bytes_red, bytes_green, bytes_blue)

            elif 27.423 <= x <= 34.827 and -7.626 <= y <= -5.372:
                print('Gig!')
                newdata = struct.pack(data_format, x, y, 0, bytes_red, bytes_green, bytes_blue)

            elif 35.068 <= x <= 41.748 and -6.66 <= y <= -4.085:
                print('GNT 9!')
                newdata = struct.pack(data_format, x, y, 0, bytes_red, bytes_green, bytes_blue)

            elif 57.697 <= x <= 63.76 and -64.449 <= y <= -53.098:
                print('GNT 43!')
                newdata = struct.pack(data_format, x, y, 0, bytes_red, bytes_green, bytes_blue)

            elif 7.576 <= x <= 74.53 and -76.515 <= y <= -73.547:
                print('GNT 3!')
                newdata = struct.pack(data_format, x, y, 0, bytes_red, bytes_green, bytes_blue)


            elif 13.085 <= x <= 90.916 and -103.071 <= y <= -99.115:
                print('TV 1!')
                newdata = struct.pack(data_format, x, y, 0, bytes_red, bytes_green, bytes_blue)                
                                                                                        
            else:
                newdata = struct.pack(data_format, x, y, 0, red, green, blue)
            vertices_z.append(newdata)
            
            


                                                               
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
file_path = "/home/ysu/Miscanthus/cloud_merged.ply"
save_file_path = "/home/ysu/Miscanthus/area.ply"


pointnum = read_vertex_count(file_path)
vertices_z = read_and_print_ply(pointnum, file_path)
#write_ply_binary_with_colors(save_file_path, vertices_z)
print("All done!")


