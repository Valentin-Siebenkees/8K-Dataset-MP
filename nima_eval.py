import numpy as np
from os import listdir
import matplotlib.pyplot as plt

base_path = 'F:/Medienprojekt_8K_Datensatz/Evaluation/MP_8K_output'

file_list = listdir(base_path)

clip_names = []
technical_nima_means = []
aesthetic_nima_means = []

for clip in file_list:
    technical_image_ids = []
    technical_nima_scores = []
    aesthetic_image_ids = []
    aesthetic_nima_scores = []
    with open(f'{base_path}/{clip}/technical_results.txt', 'r') as technical_file:
        for line in technical_file.readlines():
            if '"image_id":' in line:
                technical_image_ids.append(int(line[line.find(':') + 3:-3]))
            if '"mean_score_prediction":' in line:
                technical_nima_scores.append(float(line[line.find(':') + 2: -1]))
    technical_image_ids_sorted = np.array(technical_image_ids)[np.argsort(technical_image_ids)]
    technical_nima_scores_sorted = np.array(technical_nima_scores)[np.argsort(technical_image_ids)]
    technical_fig = plt.figure()
    plt.title(f'Technical NIMA Results for: {clip}')
    plt.plot(technical_image_ids_sorted, technical_nima_scores_sorted, 'x')
    plt.axhline(np.mean(technical_nima_scores_sorted), color='red', alpha=0.5)
    plt.xlabel('Image ID')
    plt.ylabel('NIMA Score')
    plt.ylim(1, 10.0)
    plt.savefig(f'{base_path}/{clip}/technical_results_plot.png')
    plt.close(technical_fig)

    with open(f'{base_path}/{clip}/aesthetic_results.txt', 'r') as aesthetic_file:
        for line in aesthetic_file.readlines():
            if '"image_id":' in line:
                aesthetic_image_ids.append(int(line[line.find(':') + 3:-3]))
            if '"mean_score_prediction":' in line:
                aesthetic_nima_scores.append(float(line[line.find(':') + 2: -1]))
    aesthetic_image_ids_sorted = np.array(aesthetic_image_ids)[np.argsort(aesthetic_image_ids)]
    aesthetic_nima_scores_sorted = np.array(aesthetic_nima_scores)[np.argsort(aesthetic_image_ids)]
    aesthetic_fig = plt.figure()
    plt.title(f'Technical NIMA Results for: {clip}')
    plt.plot(aesthetic_image_ids_sorted, aesthetic_nima_scores_sorted, 'x')
    plt.axhline(np.mean(aesthetic_nima_scores_sorted), color='red', alpha=0.5)
    plt.xlabel('Image ID')
    plt.ylabel('NIMA Score')
    plt.ylim(1, 10.0)
    plt.savefig(f'{base_path}/{clip}/aesthetic_results_plot.png')
    plt.close(aesthetic_fig)

    clip_names.append(clip)
    technical_nima_means.append(np.mean(technical_nima_scores_sorted))
    aesthetic_nima_means.append(np.mean(aesthetic_nima_scores_sorted))


plt.figure(figsize=(20, 5))
plt.title('Technical NIMA Mean Scores')
plt.ylabel('NIMA Score')
plt.ylim(1, 10.0)
plt.plot(np.array(clip_names), np.array(technical_nima_means), 'x')
plt.savefig(f'{base_path}/technical_means.png')

plt.figure(figsize=(20, 5))
plt.ylabel('NIMA Score')
plt.title('Aesthetic NIMA Mean Scores')
plt.ylim(1, 10.0)
plt.plot(np.array(clip_names), np.array(aesthetic_nima_means), 'x')
plt.savefig(f'{base_path}/aesthetic_means.png')
