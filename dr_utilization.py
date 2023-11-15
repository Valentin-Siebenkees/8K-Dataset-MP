from os import listdir, makedirs
from os.path import exists
from skvideo.io import vread, FFmpegReader
import numpy as np

video_directory = f'E:/Medienprojekt_8K_Datensatz/Export'

# TODO:
#   numpy.core._exceptions._ArrayMemoryError: Unable to allocate 29.7 GiB for an array with shape (900, 4320, 8192, 1)
#                                             and data type uint8
#   15s x 60 frames/s = 900 frames
#   900 frames x 4320 x 8192 x 1 Channel (Y) [uint8] = 31.850.496.000 Bytes
#   31.850.496.000 / 1024**3 = 29,7 GiB

lower_percentile = 10
upper_percentile = 99

for video in listdir(video_directory):
    (frame_number, _, _, _) = FFmpegReader(f'{video_directory}/{video}').getShape()
    frame_array = vread(f'{video_directory}/{video}', num_frames=5, outputdict={"-pix_fmt": "gray"})[:, :, :, 0]
    print(f'Video: {video} with {frame_number} frames')
    for frame_number, frame in enumerate(frame_array):
        DR = np.log10(np.percentile(frame, upper_percentile) / np.percentile(frame, lower_percentile))
        IK = (np.log(np.mean(frame)) - np.log(np.percentile(frame, lower_percentile))) / \
             (np.log(np.percentile(frame, upper_percentile)) - np.log(np.percentile(frame, lower_percentile)))
        print(f'Frame: {frame_number} DR={DR}, IK={IK}')
