import pandas as pd

# 定义文件路径
file_path = '/home/ysu/Miscanthus/2D/raw.csv'

# 定义列名
column_names = ['Column1', 'Column2', 'Column3']

# 分块大小
chunk_size = 10000  # 根据你的内存情况调整块大小

# 创建一个字典来存储已处理的 (Column1, Column2) 组合及其对应的行
pair_to_rows = {}

# 分块读取CSV文件
chunks = pd.read_csv(file_path, names=column_names, header=None, chunksize=chunk_size)

for chunk in chunks:
    # 遍历每一行
    for index, row in chunk.iterrows():
        pair = (row['Column1'], row['Column2'])
        if pair in pair_to_rows:
            pair_to_rows[pair].append(row)
        else:
            pair_to_rows[pair] = [row]

# 提取所有重复的行，包括初始行
duplicate_rows = [row for rows in pair_to_rows.values() if len(rows) > 1 for row in rows]

# 如果找到重复行，保存到文件并输出结果
if duplicate_rows:
    duplicates_df = pd.DataFrame(duplicate_rows)
    duplicates_df.to_csv('duplicate_rows.csv', index=False, header=False)
    print(f"Found {len(duplicate_rows)} duplicate rows. Details saved to 'duplicate_rows.csv'.")
else:
    print("No duplicate rows found.")

# 显示结果
if duplicate_rows:
    print(pd.DataFrame(duplicate_rows))
else:
    print("No duplicate rows found.")
