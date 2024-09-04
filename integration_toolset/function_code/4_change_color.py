def load_and_modify_ply(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.readlines()

    header = []
    end_header_index = 0
    for i, line in enumerate(data):
        header.append(line)
        if "end_header" in line:
            end_header_index = i + 1
            break

    # 修改点云数据的颜色部分
    modified_data = []
    for line in data[end_header_index:]:  # 从结束头部之后开始读取点云数据
        parts = line.split()
        if len(parts) == 6:  # 确保该行有6个数据：x, y, z, red, green, blue
            new_color = '255 0 0'  # 设置颜色为红色
            modified_line = ' '.join(parts[:3] + [new_color]) + '\n'
            modified_data.append(modified_line)

    # 将修改后的数据写回新的 PLY 文件
    with open(output_file, 'w') as file:
        file.writelines(header)  # 先写入头部信息
        file.writelines(modified_data)  # 写入修改后的点云数据

def main():
    input_file = '/home/ysu/Miscanthus/toolset/data/coord_transfer/UGV_ASCII.ply'  # Path to your input PLY file
    output_file = '/home/ysu/Miscanthus/toolset/data/coord_transfer/UGV_ASCII_red.ply'  # Path to save the output PLY file
    load_and_modify_ply(input_file, output_file)

if __name__ == "__main__":
    main()






