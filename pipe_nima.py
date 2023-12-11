import subprocess
from os import listdir, makedirs
from os.path import exists

master_path = 'F:/Medienprojekt_8K_Datensatz/Export/Master_2'
output_path = 'C:/Users/valle/Desktop/FFmpeg_Test/Still_Frames/'

file_list = listdir(master_path)
# file_list.remove('Balance_Forest.mov')

for clip in file_list:
    if not exists(f'{output_path}/{clip[:-4]}'):
        makedirs(f'{output_path}/{clip[:-4]}')
    cmd = f'ffmpeg -i {master_path}/{clip} -color_primaries bt2020 -color_trc smpte2084 -colorspace bt2020nc ' \
          f'-vf "select=not(mod(n\,10)), scale=in_range=full:out_range=full" -vsync vfr -q:v 1 -qmin 1 -qmax 1 ' \
          f'{output_path}/{clip[:-4]}/%3d.jpg'
    subprocess.run(cmd, shell=True)

