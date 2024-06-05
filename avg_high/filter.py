#苏雨的点云直通滤波和体素滤波程序
import subprocess
import json

def create_pdal_pipeline(input_file, output_file, voxel_size):
    """
    创建 PDAL 处理流程的 JSON 配置。
    """
    pipeline = {
        "pipeline": [
            {
                "type": "readers.ply",
                "filename": input_file
            },
            {
                "type": "filters.voxelcenternearestneighbor",
                "cell":f"{voxel_size}"
            },
            {
                "type": "filters.range",
                "limits": f"Z[{z_min_threshold}:{z_max_threshold}]"
            },            
            {
                "type": "writers.ply",
                "filename": output_file
            }
        ]
    }
    return json.dumps(pipeline)

def run_pdal_pipeline(pipeline_json):
    """
    执行 PDAL pipeline，并打印执行结果。
    """
    try:
        result = subprocess.run(['pdal', 'pipeline', '--stdin'], input=pipeline_json, capture_output=True, text=True, check=True)
        print("PDAL pipeline executed successfully.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running PDAL:")
        print(e.stderr)

if __name__ == "__main__":
    # 定义输入和输出文件路径
    input_ply_path = '/home/ysu/Miscanthus/2D/small.ply'
    output_ply_path = '/home/ysu/Miscanthus/2D/filter.ply'
    voxel_size = 0.1  # 定义体素大小
    #底部，值越小越朝下（苏雨）
    z_min_threshold = -18  
    #顶部，值越大越朝上(15)（苏雨）
    z_max_threshold = -15

    # 创建 PDAL pipeline JSON 配置
    pdal_pipeline_json = create_pdal_pipeline(input_ply_path, output_ply_path, voxel_size)

    # 运行 PDAL pipeline
    run_pdal_pipeline(pdal_pipeline_json)











