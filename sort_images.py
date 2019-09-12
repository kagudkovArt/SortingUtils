import argparse
import os
import shutil

import cv2

parser = argparse.ArgumentParser(description='')
parser.add_argument('--source_folder', dest='source_folder',
                    help='path to unsorted images')
parser.add_argument('--res_folder', dest='res_folder',
                    help='path result classes folders')
args = parser.parse_args()

key_map = {
    ord('1'): "OK",
    ord('2'): "BigAngle",
    ord('3'): "BigInpaintingArea",
    ord('4'): "BlueBlobs",
    ord('5'): "HairsOnEyes",
    ord('6'): "HalfEyeBlending",
    ord('7'): "HandsOnHead",
    ord('8'): "Hat",
    ord('9'): "HolesInHead",
    ord('0'): "Lashes",
    ord('q'): "OtherProblems",
    ord('w'): "ThingsBeforeFace",
    ord('e'): "WrongAngle",
    ord(' '): "AlreadyOperated"
}
for folder_name in key_map.values():
    os.makedirs(os.path.join(args.res_folder, folder_name), exist_ok=True)

for image_name in os.listdir(args.source_folder):
    image_path = os.path.join(args.source_folder, image_name)
    image = cv2.imread(image_path)
    cv2.imshow('', image)
    while True:
        code = cv2.waitKeyEx()
        if code not in key_map:
            continue
        folder_name = key_map[code]
        shutil.copy2(image_path, os.path.join(args.res_folder, folder_name, image_name))
        if folder_name == 'AlreadyOperated':
            break
