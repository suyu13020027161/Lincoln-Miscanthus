#苏雨的区域平均高度求解程序
import struct
import matplotlib.pyplot as plt
from matplotlib.path import Path

def read_and_print_ply(pointnum, filepath, polygons):
    
    
    
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
        
        #定义总高度统计（苏雨）
        hs0 = 0
        hs1 = 0
        hs2 = 0
        hs3 = 0
        hs4 = 0
        hs5 = 0
        hs6 = 0        
        
        
        #定义高度数据个数（苏雨）
        hnum0 = 0
        hnum1 = 0
        hnum2 = 0
        hnum3 = 0
        hnum4 = 0
        hnum5 = 0
        hnum6 = 0
                
        
        
        path0 = Path(polygons[0])       
        path1 = Path(polygons[1])
        path2 = Path(polygons[2])       
        path3 = Path(polygons[3])            
        path4 = Path(polygons[4])       
        path5 = Path(polygons[5])
        path6 = Path(polygons[6])         

               
        while True:       
            data = file.read(byte_size)                      
            if not data:
                break
            x, y, z, red, green, blue = struct.unpack(data_format, data)
            progress = (i / pointnum)*100
            point = (x, y)

            inside0 = path0.contains_point(point)            
            inside1 = path1.contains_point(point)
            inside2 = path2.contains_point(point)            
            inside3 = path3.contains_point(point)      
            inside4 = path4.contains_point(point)            
            inside5 = path5.contains_point(point)
            inside6 = path6.contains_point(point)            
          

            
            
            
            
            if inside0:
                hs0 = hs0 + z
                hnum0 = hnum0 + 1           
            if inside1:
                hs1 = hs1 + z
                hnum1 = hnum1 + 1
            if inside2:
                hs2 = hs2 + z
                hnum2 = hnum2 + 1             
            if inside3:
                hs3 = hs3 + z
                hnum3 = hnum3 + 1           
            if inside4:
                hs4 = hs4 + z
                hnum4 = hnum4 + 1
            if inside5:
                hs5 = hs5 + z
                hnum5 = hnum5 + 1                                                                                          
            if inside6:
                hs6 = hs6 + z
                hnum6 = hnum6 + 1   
                       
                                                               
            pp = str(progress)
            print("\rProgress: " + pp + "%", end="         ")
            i = i + 1 
    
    
    #平均高度（苏雨）
    avgh0 = hs0 / hnum0
    avgh1 = hs1 / hnum1
    avgh2 = hs2 / hnum2
    avgh3 = hs3 / hnum3
    avgh4 = hs4 / hnum4
    avgh5 = hs5 / hnum5
    avgh6 = hs6 / hnum6             
    return (avgh0, avgh1, avgh2, avgh3, avgh4, avgh5, avgh6)
                        
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



#替换下面的路径为你的PLY文件路径（苏雨）
file_path = "/home/ysu/Miscanthus/avg_high/Miscanthus_23_11_23_arbitrary.ply"


GNT14 = [(26.41, -0.801), (33.394, 0.216), (26.875, -4.293), (34.335, -3.725)]
GNT10 = [(34.477, 0.001), (40.484, 0.771), (34.999, -3.153), (40.663, -2.439)]
GNT9 = [(35.219, -4.145), (41.301, -3.206), (35.825, -7.234), (41.692, -6.511)]
Gig = [(27.612, -5.436), (34.046, -4.204), (28.081, -8.917), (34.515, -7.704)]
GNT43 = [(57.625, -54.581), (61.776, -53.574), (59.441, -65.133), (63.807, -64.544)]
GNT3 = [(8.197, -75.795), (73.431, -65.738), (8.789, -83.485), (75.037, -73.513)]
TV1 = [(16.855, -95.306), (87.938, -82.484), (17.991, -101.067), (89.155, -88.733)]


polygons = [GNT14, GNT10, GNT9, Gig, GNT43, GNT3, TV1]


pointnum = read_vertex_count(file_path)

avgh0, avgh1, avgh2, avgh3, avgh4, avgh5, avgh6 = read_and_print_ply(pointnum, file_path, polygons)

print('\nGNT14 = ' + str(avgh0))
print('GNT10 = ' + str(avgh1))
print('GNT9 = ' + str(avgh2))
print('Gig = ' + str(avgh3))
print('GNT43 = ' + str(avgh4))
print('GNT3 = ' + str(avgh5))
print('TV1 = ' + str(avgh6))




print("All done!")


