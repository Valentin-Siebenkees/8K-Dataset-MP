import subprocess
from os import listdir, makedirs
from os.path import exists
import time

"""
Script to encode Videos with different encoding standards to inspect encoding time and file size later on.

Encoding Standards used:
    - AV1
    - H.265 (HEVC)
    - VP9
"""


def encode_av1(input_dir, output_dir, filename, preset=4, crf=32):
    """
    Function to execute FFmpeg AV1 video encoding


    :param input_dir:
    :param output_dir:
    :param filename:
    :param preset:
    :param crf:
    """
    cmd_AV1 = f'ffmpeg -i {input_dir}/{filename} -c:v libaom-av1 ' \
              f'-preset {preset} -crf {crf} ' \
              f'-c:a aac -b:a 128k ' \
              f'{output_dir}/{filename[:filename.find(".")]}/{clip[:clip.find(".")]}_AV1.mp4'
              # f'-colorspace bt2020nc -color_trc smpte2084 -color_primaries bt2020 -pix_fmt yuv420p10le ' \
    subprocess.run(cmd_AV1, shell=True)


def encode_h265(input_dir, output_dir, filename, preset='medium', crf=32):
    """
    Function to execute FFmpeg h.265 encoding

    :param input_dir:
    :param output_dir:
    :param filename:
    :param preset:
    :param crf:
    """
    cmd_h265 = f'ffmpeg -i {input_dir}/{filename} -c:v libx265 -preset {preset} -crf {crf} ' \
               f'-c:a aac -b:a 128k ' \
               f'{output_dir}/{filename[:filename.find(".")]}/{filename[:filename.find(".")]}_h265.mp4'
    subprocess.run(cmd_h265, shell=True)


def encode_vp9(input_dir, output_dir, filename, crf=32):
    """
    Function to execute FFmpeg vp9 encoding

    :param input_dir:
    :param output_dir:
    :param filename:
    :param crf:
    """
    cmd_vp9 = f'ffmpeg -i {input_dir}/{filename} -c:v libvpx-vp9 -crf {crf} -b:v 0 ' \
              f'-c:a aac -b:a 128k ' \
              f'{output_dir}/{filename[:filename.find(".")]}/{filename[:filename.find(".")]}_vp9.mp4'
    subprocess.run(cmd_vp9, shell=True)


base_path = 'F:/Medienprojekt_8K_Datensatz/Export'
compression_path = 'F:/Medienprojekt_8K_Datensatz/Compression'

if not exists(compression_path):
    makedirs(compression_path)

start = time.time()

for clip in listdir(base_path):
    if not exists(f'{compression_path}/{clip[:clip.find(".")]}'):
        makedirs(f'{compression_path}/{clip[:clip.find(".")]}')

    print(f'AV1 encoding for {clip} starting..')
    start_AV1 = time.time()
    encode_av1(base_path, compression_path, clip)
    end_AV1 = time.time()
    print(f'AV1 encoding for {clip} finished in {end_AV1 - start_AV1} seconds')

    print(f'\nh265 encoding for {clip} starting..')
    start_h265 = time.time()
    encode_h265(base_path, compression_path, clip)
    end_h265 = time.time()
    print(f'h265 encoding for {clip} finished in {end_h265 - start_h265} seconds')

    print(f'\nvp9 encoding for {clip} starting..')
    start_vp9 = time.time()
    encode_vp9(base_path, compression_path, clip)
    end_vp9 = time.time()
    print(f'vp9 encoding for {clip} finished in {end_vp9 - start_vp9} seconds')

end = time.time()
print(f'Execution time: {(end - start)/60} Minutes')
