#苏雨的比较csv文件的处理中间程序，计算两个网格csv文件的相同位置网格高度差，输出为新csv文件
import pandas as pd

def compare_csv(file1, file2, threshold, offset, output_file):
    # 加载CSV文件，跳过第一行
    df1 = pd.read_csv(file1, skiprows=1, header=None)
    df2 = pd.read_csv(file2, skiprows=1, header=None)
    
    # 初始化结果DataFrame
    result_data = {'FirstCol': [], 'SecondCol': [], 'Difference': []}

    # 遍历两个DataFrame
    i = 0
    for _, row1 in df1.iterrows():
        for _, row2 in df2.iterrows():
            # 计算第一列和第二列差的和
            diff_sum = abs(row1[0] - row2[0]) + abs(row1[1] - row2[1])
            
            # 检查差的和是否在阈值内
            if diff_sum <= threshold:
                # 计算第三列的差
                third_col_diff = abs(row1[2] - row2[2] - offset)
                
                # 存储结果
                result_data['FirstCol'].append(row1[0])
                result_data['SecondCol'].append(row1[1])
                result_data['Difference'].append(third_col_diff)
        progress = (i / len(df1))*100
        pp = str(progress)
        print("\rProgress: " + pp + "%", end="         ")
        i = i + 1 
    
    # 保存结果到新的CSV文件
    result_df = pd.DataFrame(result_data)
    result_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")




#基准不要改（苏雨）
file1 = '/home/ysu/Miscanthus/toolset/data/raw_csv/cut_Aber.csv'


file2 = '/home/ysu/Miscanthus/toolset/data/raw_csv/20240830_Aber.csv'

#不同z轴零点修复参数（苏雨）
offset = 124.0099754 - 124.1874905



threshold = 1  # 设定阈值
output_file = '/home/ysu/Miscanthus/toolset/data/comp_csv/20240830_Aber.csv'

compare_csv(file1, file2, threshold, offset, output_file)

