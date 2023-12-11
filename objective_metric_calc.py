from os import listdir, makedirs
from os.path import exists
from ffmpeg_quality_metrics import FfmpegQualityMetrics
import time

reference_path = 'F:/Medienprojekt_8K_Datensatz/Export/Master_1'
downscaled_path = 'D:/Medienprojekt_8K_Datensatz/Output/Master_1_Downscaled'
result_path = 'D:/Medienprojekt_8K_Datensatz/Objective_Metric_Results'

# Scaling algorithm examples:
#    - fast_bilinear
#    - bilinear
#    - bicubic (Default)
#    - bicublin
#    - neighbour
#    - area
#    - lanczos
#    - sinc
#    - gauss
#    - spline
#    - experimental

scaling_algorithm = 'neighbor'

if not exists(result_path):
    makedirs(result_path)

reference_clips = listdir(reference_path)
downscaled_clips = listdir(downscaled_path)

start = time.time()

for i in range(len(reference_clips)):
    if i == 0:
        ffqm = FfmpegQualityMetrics(f'{reference_path}/{reference_clips[i]}', f'{downscaled_path}/{downscaled_clips[i]}',
                                    scaling_algorithm=scaling_algorithm)
        metrics = ffqm.calculate(["ssim", "psnr"])
        json_dump = ffqm.get_results_json()
        with open(f'{result_path}/{reference_clips[i]}_res.json', 'w') as f:
            f.write(json_dump)

end = time.time()

print(f'Execution time: {end - start} seconds')
