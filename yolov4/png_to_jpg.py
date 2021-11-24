from PIL import Image
import os
import numpy as np
def find_dir(path):
  for fd in os.listdir(path):
    full_path=os.path.join(path,fd)
    if os.path.isdir(full_path):
      # print('資料夾:',full_path)
        find_dir(full_path)
    else:
      # print('檔案:',full_path)
        data_path.append(full_path)  
data_path = []
find_dir(r'/Users/dodo/Desktop/深度學習之視覺辨識/VRDL_HW2_RELEASED_DATASET/test/')

for i in data_path:
    if i.split('.')[-1] == 'png':
        image_name = i.split('.')[0].split('/')[-1]
        im1 = Image.open(i)
        im1.save(r'/Users/dodo/Desktop/深度學習之視覺辨識/VRDL_HW2_RELEASED_DATASET/test_jpg/' + str(image_name) + '.jpg')
