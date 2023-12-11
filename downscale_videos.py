import subprocess
from os import listdir, makedirs
from os.path import exists

base_path = 'F:/Medienprojekt_8K_Datensatz/Export/Master_1'
output_path = 'D:/Medienprojekt_8K_Datensatz/Output/Master_1_Downscaled'

# Downscaling algorithm exampels (For a list of available options see -sws_flags under -> ffmpeg -h filter=scale):
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
downscaling_algorithm = 'lanczos'

if not exists(output_path):
    makedirs(output_path)

output_width = 3840
output_height = 2160

for i, clip in enumerate(listdir(base_path)):
    if i == 0:
        cmd = f'ffmpeg -i {base_path}/{clip} -vf scale="{output_width}x{output_height}:flags={downscaling_algorithm}" ' \
              f'-c:v libx265 -crf 0 -preset slow {output_path}/downscaled_{clip}'
        subprocess.run(cmd, shell=True)


