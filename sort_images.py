import argparse
import os
import shutil

import cv2

parser = argparse.ArgumentParser(description='')
parser.add_argument('--source_folder', dest='source_folder', default='sources',
                    help='path to unsorted images')
parser.add_argument('--res_folder', dest='res_folder', default='results',
                    help='path result classes folders')
args = parser.parse_args()

key_map = {
    ord('1'): "OK",
    ord('2'): "BigAngle",
    ord('3'): "BigInpaintingArea",
    ord('4'): "HairsOnEyes",
    ord('5'): "HandsOnHead",
    ord('6'): "Hat",
    ord('7'): "ObjectInFrontOfFace",
    ord('8'): "OtherProblems",
    ord('9'): "TwoAndMorePeople",
    ord('0'): "WrongAngle",
    ord(' '): "NotOK",
    ord('q'): "Exit",
}

for folder_name in key_map.values():
    os.makedirs(os.path.join(args.res_folder, folder_name), exist_ok=True)

for image_name in os.listdir(args.source_folder):
    image_path = os.path.join(args.source_folder, image_name)
    image = cv2.imread(image_path)
    cv2.imshow(image_name, image)
    while True:
        code = cv2.waitKeyEx()
        if code not in key_map:
            continue
        if key_map[code] == "Exit":
            exit(0)
        folder_name = key_map[code]
        shutil.copy2(image_path, os.path.join(args.res_folder, folder_name, image_name))
        if folder_name == 'NotOK' or folder_name == 'OK':
            os.remove(image_path)
            cv2.destroyAllWindows()
            break
