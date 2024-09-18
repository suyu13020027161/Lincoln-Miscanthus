import open3d as o3d
import numpy as np
from shapely.geometry import Point, MultiPoint
import matplotlib.pyplot as plt

def read_ply(file_path):
    return o3d.io.read_point_cloud(file_path)

def write_ply(ply_cloud, file_path):
    o3d.io.write_point_cloud(file_path, ply_cloud)

def create_convex_polygon(points):
    # 创建MultiPoint对象
    multi_point = MultiPoint(points)
    # 生成凸包
    convex_hull = multi_point.convex_hull
    return convex_hull

def filter_points_in_polygon(ply_cloud, polygon):
    points = np.asarray(ply_cloud.points)
    colors = np.asarray(ply_cloud.colors)
    
    filtered_indices = [i for i in range(points.shape[0]) if polygon.contains(Point(points[i][0], points[i][1]))]
    filtered_points = points[filtered_indices]
    filtered_colors = colors[filtered_indices]
    
    filtered_ply_cloud = o3d.geometry.PointCloud()
    filtered_ply_cloud.points = o3d.utility.Vector3dVector(filtered_points)
    filtered_ply_cloud.colors = o3d.utility.Vector3dVector(filtered_colors)
    
    return filtered_ply_cloud

def main():
    file_path = 'new_24_09_06.ply'  # 输入的PLY文件路径
    output_path = 'new_24_09_06_filted.ply'  # 输出的PLY文件路径
    
    # 读取点云
    ply_cloud = read_ply(file_path)
    
    # 定义四边形顶点
    vertices = [(668414.062500, 5912097), (668447.625000, 5912076), (668420.812500, 5912070), (668441.750000, 5912103)]  # 示例顶点，故意乱序
    polygon = create_convex_polygon(vertices)  # 创建凸多边形
    
    # 过滤点云
    filtered_ply_cloud = filter_points_in_polygon(ply_cloud, polygon)
    # 保存过滤后的点云
    write_ply(filtered_ply_cloud, output_path)
    
    print("Filtering complete. The output is saved to", output_path)

if __name__ == '__main__':
    main()




