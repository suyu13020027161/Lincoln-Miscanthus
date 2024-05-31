import struct
import numpy as np
import pandas as pd
import csv

#计数函数（苏雨）
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

#点云读取和最大最小高度计算函数（苏雨）
def read_and_print_ply(pointnum, filepath):
    print("Start reading and filtering the point cloud!")
    vertices_z = []
    xycoord = []

    
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
            xycoord.append((x,y))
            vertices_z.append(z)

            
                      
            progress = (i / pointnum)*100
            #print(f"(x={x}, y={y}, z={z}) Color: (red={red}, green={green}, blue={blue})")
            #print(data)
            #vertices_z.append(float(z))                                                                
            pp = str(progress)
            print("\rProgress: " + pp + "%", end="         ")
            i = i + 1            
    return (xycoord, vertices_z)
                        
#重合点找寻函数（苏雨）
def find_same(pointnum, xycoord, vertices_z):   
    print("\nStart find same data!")
    with open(csv_path, mode='w', newline='') as file:    
        writer = csv.writer(file)        
        seen = set()
        duplicates = []
        i = 0   
        for x in xycoord:
            if x in seen:
                xy = list(x)
                row = [xy[0], xy[1], vertices_z[i]]
                writer.writerow(row) 
                row2 =  [xy[0], xy[1], vertices_z[xycoord.index(x)]]
                writer.writerow(row2)          
            else:
                seen.add(x)
                
            progress = (i / pointnum)*100
            pp = str(progress)
            print("\rProgress: " + pp + "%", end="         ")
            i = i + 1










                    



#替换下面的路径为你的PLY文件路径（苏雨）
file_path = "/home/ysu/Miscanthus/2D/small.ply"
csv_path = "/home/ysu/Miscanthus/2D/overlap.csv"


pointnum = read_vertex_count(file_path)
xycoord, vertices_z = read_and_print_ply(pointnum, file_path)

same = find_same(pointnum, xycoord, vertices_z)
#print(same)



print("All done!")


