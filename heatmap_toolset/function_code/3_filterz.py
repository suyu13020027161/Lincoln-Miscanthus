#苏雨的读取filterx程序输出二进制文件并进行高度滤波的程序
import open3d as o3d

def filter_and_save_ply(input_file, output_file, z_min, z_max):
    #加载原始的PLY文件（苏雨）
    point_cloud = o3d.io.read_point_cloud(input_file)
    print(f"Original number of points: {len(point_cloud.points)}")

    #裁剪点云以只保留特定的Z值范围（苏雨）
    filtered_cloud = point_cloud.crop(
        o3d.geometry.AxisAlignedBoundingBox(min_bound=(-float('inf'), -float('inf'), z_min),
                                            max_bound=(float('inf'), float('inf'), z_max))
    )
    print(f"Number of points after filtering: {len(filtered_cloud.points)}")

    #保存处理后的点云到新的PLY文件（苏雨）
    o3d.io.write_point_cloud(output_file, filtered_cloud)
    print(f"Filtered PLY file saved as: {output_file}")


input_ply = '/home/ysu/Miscanthus/toolset/data/filterx/new_24_09_06.ply'
output_ply = '/home/ysu/Miscanthus/toolset/data/filterz/new_24_09_06.ply'

#只要是2024年的文件滤波参数都一样，2023年的地面低3米（苏雨）
z_min = 58  
z_max = 61  

filter_and_save_ply(input_ply, output_ply, z_min, z_max)


