from os import listdir, makedirs
from os.path import exists
from ffmpeg_quality_metrics import FfmpegQualityMetrics

reference_path = 'E:/Medienprojekt_8K_Datensatz/Export'
downscaled_path = 'E:/Medienprojekt_8K_Datensatz/Output'
result_path = 'E:/Medienprojekt_8K_Datensatz/Objective_Metric_Results'

if not exists(result_path):
    makedirs(result_path)

reference_clips = listdir(reference_path)
downscaled_clips = listdir(downscaled_path)

for i in range(len(reference_clips)):
    ffqm = FfmpegQualityMetrics(f'{reference_path}/{reference_clips[i]}', f'{downscaled_path}/{downscaled_clips[i]}')
    metrics = ffqm.calculate(["ssim", "psnr"])
    json_dump = ffqm.get_results_json()
    with open(f'{result_path}/{reference_clips[i]}_res.json', 'w') as f:
        f.write(json_dump)
