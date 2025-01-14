#苏雨的比较csv文件的处理中间程序，计算两个网格csv文件的相同位置网格高度差，输出为新csv文件
import pandas as pd
import os
from pathlib import Path

def compare_csv(file1, file2, threshold, offset, output_file):
    # 加载CSV文件
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # 初始化结果DataFrame
    result_data = {'FirstCol': [], 'SecondCol': [], 'Difference': []}

    # 遍历两个DataFrame
    for _, row1 in df1.iterrows():
        for _, row2 in df2.iterrows():
            # 计算第一列和第二列差的和
            diff_sum = abs(row1['x_center'] - row2['x_center']) + abs(row1['y_center'] - row2['y_center'])
            
            # 检查差的和是否在阈值内
            if diff_sum <= threshold:
                # 计算第三列的差
                third_col_diff = abs(row1['average_height'] - row2['average_height'] - offset)
                
                # 存储结果
                result_data['FirstCol'].append(row1['x_center'])
                result_data['SecondCol'].append(row1['y_center'])
                result_data['Difference'].append(third_col_diff)
    
    # 保存结果到新的CSV文件
    result_df = pd.DataFrame(result_data)
    result_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

def find_matching_files(dir1, dir2, output_dir):
    # 创建输出目录
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # 遍历第一个目录
    for file1 in os.listdir(dir1):
        base_name1 = Path(file1).stem
        part1 = '_'.join(base_name1.split('_')[2:])  # 提取第二个下划线之后的名称
        
        # 在第二个目录中寻找匹配的文件
        for file2 in os.listdir(dir2):
            base_name2 = Path(file2).stem
            part2 = '_'.join(base_name2.split('_')[2:])  # 提取第二个下划线之后的名称
            
            # 检查文件名是否匹配
            if part1 == part2:
                file_path1 = os.path.join(dir1, file1)
                file_path2 = os.path.join(dir2, file2)
                output_file = os.path.join(output_dir, base_name2 + '.csv')
                # 比较文件
                compare_csv(file_path1, file_path2, threshold, offset, output_file)

# 路径设置
dir1 = '/home/ysu/Miscanthus/toolset/data/raw_csv/Aber_filted/cut_Aber'
dir2 = '/home/ysu/Miscanthus/toolset/data/raw_csv/Aber_filted/20241023_Aber'
output_dir = '/home/ysu/Miscanthus/toolset/data/comp_csv/Aber_filted/20241023_Aber'
threshold = 1  # 设定阈值
offset = 124.0099754 - 123.0094160  # 不同z轴零点修复参数

# 开始处理
find_matching_files(dir1, dir2, output_dir)

