from os import listdir, makedirs
from os.path import exists
import subprocess
import time

base_path = 'E:/Medienprojekt_8K_Datensatz/Export'
result_path = 'E:/Medienprojekt_8K_Datensatz/SI_TI_Results'

if not exists(result_path):
    makedirs(result_path)

start = time.time()

"""
To handle 12-bit input: 
    --bit-depth 12
    
To handle "full range" input: 
    --color-range full

Only HLG or HDR10  encoded HDR input is supported:
    --hdr-mode hlg
    --hdr-mode hdr10
"""
for clip in listdir(base_path):
    cmd = f'siti-tools {base_path}/{clip} --bit-depth 12 --color-range full --hdr-mode hlg ' \
          f'> {result_path}/{clip}_si_ti.json'
    subprocess.run(cmd, shell=True)

end = time.time()

print(f'Execution time: {start - end} seconds')
