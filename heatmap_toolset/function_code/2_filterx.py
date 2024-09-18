#苏雨的读取ascii文件并进行体素滤波缩小文件大小，并另存为二进制新文件的程序，之所以读ascii因为直接读二进制文件会出现读取错误
import open3d as o3d

def compress_ply(input_file, output_file, voxel_size):
    #加载原始PLY文件（苏雨）
    point_cloud = o3d.io.read_point_cloud(input_file)
    print(f"Original number of points: {len(point_cloud.points)}")

    #应用体素下采样（苏雨）
    voxel_down_pcd = point_cloud.voxel_down_sample(voxel_size=voxel_size)
    print(f"Number of points after voxel down sampling: {len(voxel_down_pcd.points)}")

    #保存处理后的点云到新的PLY文件（苏雨）
    o3d.io.write_point_cloud(output_file, voxel_down_pcd)
    print(f"Compressed PLY file saved as: {output_file}")

input_ply = '/home/ysu/Miscanthus/toolset/data/ascii_utm/new_24_06_25.ply'
output_ply = '/home/ysu/Miscanthus/toolset/data/filterx/new_24_06_25.ply'
voxel_size = 0.1

compress_ply(input_ply, output_ply, voxel_size)

