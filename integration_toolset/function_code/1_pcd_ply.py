import open3d as o3d

def convert_pcd_to_ply(pcd_file_path, ply_file_path):
    # 读取PCD文件
    pcd = o3d.io.read_point_cloud(pcd_file_path)

    # 保存为PLY文件
    o3d.io.write_point_cloud(ply_file_path, pcd)

    print(f"Converted {pcd_file_path} to {ply_file_path}")

# 使用示例
pcd_file_path = '/home/ysu/Miscanthus/toolset/data/coord_transfer/front_transformed.pcd'  # 这里替换为你的PCD文件路径
ply_file_path = '/home/ysu/Miscanthus/toolset/data/coord_transfer/UGV.ply'   # 输出的PLY文件路径
convert_pcd_to_ply(pcd_file_path, ply_file_path)

