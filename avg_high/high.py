#苏雨的检查区域位置并上色并输出平均高度程序
import struct
import matplotlib.pyplot as plt
from matplotlib.path import Path
import math
from plyfile import PlyData


def read_and_print_ply(pointnum, filepath, polygons):
    print("Start reading and filtering the point cloud!")
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
        
    #定义识别区域（苏雨）
    path0 = Path(polygons[0])       
    path1 = Path(polygons[1])
    path2 = Path(polygons[2])       
    path3 = Path(polygons[3])            
    path4 = Path(polygons[4])       
    path5 = Path(polygons[5])
    path6 = Path(polygons[6])     


    






    ply = PlyData.read(filepath)


    #获取顶点信息
    vertex = ply['vertex']

    i = 0
    for data in vertex:
        x, y, z = data['x'], data['y'], data['z']
        x = float(x)
        y = float(y)
        z = float(z)
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
            #print('GNT14')
            hs0 = hs0 + z
            hnum0 = hnum0 + 1
                         
        if inside1:
            #print('GNT10')
            hs1 = hs1 + z
            hnum1 = hnum1 + 1
               
        if inside2:
            #print('GNT9')            
            hs2 = hs2 + z
            hnum2 = hnum2 + 1
                             
        if inside3:
            #print('Gig')            
            hs3 = hs3 + z
            hnum3 = hnum3 + 1
                            
        if inside4:
            #print('GNT43')            
            hs4 = hs4 + z
            hnum4 = hnum4 + 1
                 
        if inside5:
            #print('GNT3')            
            hs5 = hs5 + z
            hnum5 = hnum5 + 1
                                                                                                          
        if inside6:
            #print('TV1')            
            hs6 = hs6 + z
            hnum6 = hnum6 + 1
                    
                                                                                      
        pp = str(progress)
        print("\rProgress: " + pp + "%", end="         ")
        i = i + 1 
    
  
    #平均高度（苏雨）
    if hnum0 > 0:
        avgh0 = hs0 / hnum0
    if hnum0 == 0:
        avgh0 = None
        
    if hnum1 > 0:
        avgh1 = hs1 / hnum1
    if hnum1 == 0:
        avgh1 = None
           
    if hnum2 > 0:
        avgh2 = hs2 / hnum2
    if hnum2 == 0:
        avgh2 = None
        
    if hnum3 > 0:
        avgh3 = hs3 / hnum3
    if hnum3 == 0:
        avgh3 = None         
       
    if hnum4 > 0:
        avgh4 = hs4 / hnum4
    if hnum4 == 0:
        avgh4 = None
        
    if hnum5 > 0:
        avgh5 = hs5 / hnum5
    if hnum5 == 0:
        avgh5 = None
           
    if hnum6 > 0:
        avgh6 = hs6 / hnum6 
    if hnum6 == 0:
        avgh6 = None    
    
    
    
    
                
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
file_path = "/home/ysu/Miscanthus/avg_high/miscanthus_24_06_25_UTM_binary.ply"



GNT14 = [(668425.824, 5912094.96), (668432.856, 5912096.436), (668426.216, 5912091.405), (668433.303, 5912092.854)]
GNT10 = [(668433.767, 5912096.28), (668439.704, 5912097.849), (668434.346, 5912092.732), (668440.533, 5912094.016)]
GNT9 = [(668434.563, 5912091.861), (668440.639, 5912093.274), (668435.195, 5912088.315), (668441.184, 5912089.911)]
Gig = [(668426.674, 5912090.516), (668433.602, 5912091.933), (668427.506, 5912086.577), (668434.37, 5912088.284)]
GNT43 = [(668459.093, 5912044.204), (668462.961, 5912045.13), (668461.24, 5912032.113), (668465.255, 5912032.813)]
GNT3 = [(668409.423, 5912018.831), (668474.788, 5912031.797), (668419.868, 5912011.168), (668476.487, 5912024.059)]
TV1 = [(668415.308, 5911992.375), (668493.72, 5912008.653), (668415.242, 5911982.393), (668495.037, 5911999.895)]


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



