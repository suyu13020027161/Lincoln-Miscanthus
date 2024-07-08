#苏雨的读取二进制点云坐标并另存为ascii文件程序
from plyfile import PlyData


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






def write_ply(pointnum, file_path, output):
    ply = PlyData.read(file_path)
    #获取顶点信息（苏雨）
    vertex = ply['vertex']
    #PLY文件头（苏雨）
    header = f"""ply
format ascii 1.0
element vertex {pointnum}
property float x
property float y
property float z
end_header
"""

    #打开文件进行写入（苏雨）
    with open(output, 'w') as f:
        f.write(header)
        i = 0
        for data in vertex:
            x, y, z = data['x'], data['y'], data['z']
            f.write(f"{x} {y} {z}\n")
            progress = (i / pointnum)*100
            pp = str(progress)
            print("\rProgress: " + pp + "%", end="         ")
            i = i + 1

        
        



















file_path = '/home/ysu/Miscanthus/avg_high/miscanthus_23_08_09_UTM_binary.ply'
output = '/home/ysu/Miscanthus/avg_high/test.ply'
pointnum = read_vertex_count(file_path)
write_ply(pointnum, file_path, output)


print(pointnum)


































