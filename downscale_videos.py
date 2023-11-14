import subprocess
from os import listdir, makedirs
from os.path import exists

base_path = 'E:/Medienprojekt_8K_Datensatz/Export'
output_path = 'E:/Medienprojekt_8K_Datensatz/Output'

# Downscaling algorithm exampels (For a list of available options see -sws_flags under -> ffmpeg -h filter=scale):
#    - fast_bilinear
#    - bilinear
#    - bicubic (Default)
#    - neighbour
#    - area
#    - lanczos
#    - sinc
#    - gauss
#    - spline
downscaling_algorithm = 'neighbour'

if not exists(output_path):
    makedirs(output_path)

output_width = 3840
output_height = 2160

for clip in listdir(base_path):
    cmd = f'ffmpeg -i {base_path}/{clip} -vf scale="{output_width}x{output_height}:flags={downscaling_algorithm}" {output_path}/downscaled_{clip}'
    subprocess.run(cmd, shell=True)
