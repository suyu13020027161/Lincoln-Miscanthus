def read_ply(filepath):
    """ 从PLY文件中读取头部和顶点数据 """
    with open(filepath, 'r') as file:
        data = file.readlines()

    header = []
    end_header_index = 0
    for i, line in enumerate(data):
        header.append(line)
        if "end_header" in line:
            end_header_index = i + 1
            break

    vertices = data[end_header_index:]  # 获取顶点数据
    return header, vertices

def merge_ply_files(file1, file2, output_file):
    """ 合并两个PLY文件 """
    header1, vertices1 = read_ply(file1)
    header2, vertices2 = read_ply(file2)

    # 确保两个文件具有相同的头部结构，这里我们假设它们完全一致
    with open(output_file, 'w') as file:
        # 写入任一文件的头部
        for line in header1:
            if "element vertex" in line:
                # 更新顶点数量
                num_vertices = len(vertices1) + len(vertices2)
                file.write(f"element vertex {num_vertices}\n")
            else:
                file.write(line)
        
        # 写入第一个文件的顶点数据
        file.writelines(vertices1)
        # 写入第二个文件的顶点数据
        file.writelines(vertices2)

def main():
    file1 = '/home/ysu/Miscanthus/toolset/data/coord_transfer/arbitrary_ASCII.ply'  # 第一个文件路径
    file2 = '/home/ysu/Miscanthus/toolset/data/coord_transfer/UGV_ASCII_red.ply'  # 第二个文件路径
    output_file = '/home/ysu/Miscanthus/toolset/data/coord_transfer/comb_UGV.ply'  # 合并后的输出文件路径
    merge_ply_files(file1, file2, output_file)

if __name__ == "__main__":
    main()




















