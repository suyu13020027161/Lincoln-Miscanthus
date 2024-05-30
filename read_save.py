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
def read_and_print_ply(pointnum, filepath, csv_path):
    print("Start reading and saving the point cloud!")
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        

    
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
                row = [x, y, z]
                writer.writerow(row)


            
                #开始比大小，如果是第一位则以z为初始值（苏雨）
                if i == 0:
                    maxz = z
                    minz = z
                if maxz < z:
                    maxz = z
                if minz > z:
                    minz = z
                      
                progress = (i / pointnum)*100
                                                             
                pp = str(progress)
                print("\rProgress: " + pp + "%", end="         ")
                i = i + 1            
    return (maxz, minz)
      


    
    
file_path = "/home/ysu/Miscanthus/small.ply"
csv_path = "/home/ysu/Miscanthus/test.csv"

pointnum = read_vertex_count(file_path)
maxz, minz = read_and_print_ply(pointnum, file_path, csv_path)    




