import os
import csv
from os import walk


def create_filenamecsv():
    data_folder = 'data/dlrdata/audio'
    class_folders = [x[0].split('/')[-1] for x in os.walk(data_folder)][1:]
    for_csv = []
    for index, folder in enumerate(class_folders):
        foldername = folder
        for (dirpath, dirnames, filenames) in walk(os.path.join(data_folder, folder)):
            wavfiles = [f for f in filenames if f.endswith('wav')]
        for wavfile in wavfiles:
            class_label = index
            for_csv.append([foldername, wavfile, class_label])
    with open("dlr_data_folder_meta.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerow(['folder', 'filename', 'label'])
        csvWriter.writerows(for_csv)

def create_class_labelcsv():
    data_folder = 'data/dlrdata/audio'
    class_folders = [x[0].split('/')[-1] for x in os.walk(data_folder)][1:]
    for_csv = []
    for index, folder in enumerate(class_folders):
        foldername = folder
        for (dirpath, dirnames, filenames) in walk(os.path.join(data_folder, folder)):
            wavfiles = [f for f in filenames if f.endswith('wav')]
        for wavfile in wavfiles:
            class_label = index
            for_csv.append([class_label, '/m/21rwj' + str(class_label).zfill(2), folder])
    with open("data/dlr_class_label.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerow(['index', 'mid', 'display_name'])
        csvWriter.writerows(for_csv)

create_class_labelcsv()

