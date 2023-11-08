import subprocess
from os import listdir, makedirs
from os.path import exists

base_path = 'E:/Medienprojekt_8K_Datensatz/Export'
output_path = 'E:/Medienprojekt_8K_Datensatz/Output'

if not exists(output_path):
    makedirs(output_path)

output_width = 3840
output_height = 2160

for clip in listdir(base_path):
    cmd = f'ffmpeg -i {base_path}/{clip} -vf scale="{output_width}:{output_height}" {output_path}/downscaled_{clip}'
    subprocess.run(cmd, shell=True)
