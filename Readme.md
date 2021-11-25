## README

    import os
    from google.colab import drive
    drive.mount('/content/gdrive')

File in coco/annotations in mydrive（https://drive.google.com/drive/folders/1G18BWENqpOMPfMxKhLCxSSq5vfHEVtYe?usp=sharing）: 

instances_val2017.json

File in yolov4 in mydrive（https://drive.google.com/drive/folders/1FjZW9NP1hTWR-oXqIgeF2GmzVJfUTMdj?usp=sharing）：

png_to_jpg.py / generate_txt.py / generate_train.py / generate_test.py / test.txt / boxes.csv / obj.zip / obj_test.zip / train_txt.zip / obj.names / weights－best.pt

## Use GPU

Step1: Use GPU. Set up the environment.

    !sudo apt update
    !sudo apt install libgl1-mesa-glx -y
    ! nvidia-smi

## Git clone

Step2: Git clone the project：https://github.com/WongKinYiu/ScaledYOLOv4

    %cd /content/gdrive/My Drive
    !wget https://github.com/WongKinYiu/ScaledYOLOv4/archive/yolov4-csp.zip
    !unzip yolov4-csp.zip && rm yolov4-csp.zip

## Install requirements

Step3: Install torch==1.6.0+cu101, torchvision==0.7.0+cu101

    !pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
    import os
    import cv2
    import time
    from tqdm import tqdm
    from google_drive_downloader import GoogleDriveDownloader as gdd

Step4: Git clone https://github.com/thomasbrandon/mish-cuda, then install.

    !git clone https://github.com/thomasbrandon/mish-cuda
    %cd mish-cuda
    !python setup.py build install

Step5: Update YAML
    
    !pip install -U PyYAML

Step6: Create a digits.yaml in the data folder, which stores the training set, validation set and test set paths, the number of categories and the category names.

    %cd /content/gdrive/MyDrive/ScaledYOLOv4-yolov4-csp/data
    !touch digits.yaml
    %cd /content/gdrive/MyDrive/ScaledYOLOv4-yolov4-csp/data
    
    %%writefile digits.yaml
    # train: /content/gdrive/MyDrive/ScaledYOLOv4-yolov4-csp/data/train.txt
    # val: /content/gdrive/MyDrive/ScaledYOLOv4-yolov4-csp/data/valid.txt
    test: /content/gdrive/MyDrive/ScaledYOLOv4-yolov4-csp/data/test.txt
    nc: 10
    names: ['1.0','2.0','3.0','4.0','5.0','6.0','7.0','8.0','9.0','10.0']

Step7: Modify cfg file. Copy a original cfg file and change the image width and height to 576, filters to 45(filters=(classes + 5)*3, and classes to 10.


    !cp models/yolov4-csp.cfg models/yolov4-csp_416.cfg
    !sed -n -e 8p -e 9p -e 1022p -e 1029p -e 1131p -e 1138p -e 1240p -e 1247p models/yolov4-csp_416.cfg

    !sed -i '8s/512/576/' models/yolov4-csp_416.cfg
    !sed -i '9s/512/576/' models/yolov4-csp_416.cfg
    !sed -i '1022s/255/45/' models/yolov4-csp_416.cfg
    !sed -i '1029s/80/10/' models/yolov4-csp_416.cfg
    !sed -i '1131s/255/45/' models/yolov4-csp_416.cfg
    !sed -i '1138s/80/10/' models/yolov4-csp_416.cfg
    !sed -i '1240s/255/45/' models/yolov4-csp_416.cfg
    !sed -i '1247s/80/10/' models/yolov4-csp_416.cfg
    # 查看修改後的參數
    !sed -n -e 8p -e 9p -e 1022p -e 1029p -e 1131p -e 1138p -e 1240p -e 1247p models/yolov4-csp_416.cfg
    
## Wget testing data

Step8: Upload the zip file（obj_test.zip） of all of the test images. Unzip it to the data folder that is in ScaledYOLOv4-yolov4-csp file. Copy gerenate_test.py to ScaledYOLOv4-yolov4-csp file. Then, run it. It will generate test.txt.

## Run inference and benchmark

Step9: Copy weights(best.pt) to ScaledYOLOv4-yolov4-csp file and obj.names to the data folder that is in ScaledYOLOv4-yolov4-csp file.

Step10: Test.

    !python test.py --img 576 --conf 0.001 --batch 8 --device 0 --data data/digits.yaml --names data/obj.names --cfg models/yolov4-csp_416.cfg --weights best.pt --task test --save-json
    
## Generate answer.json for submission on Codalab

Colab link : https://colab.research.google.com/drive/1ZydftPlARDwjBYslWqYspbx88jjIczGL?usp=sharing


<img width="1315" alt="image" src="https://user-images.githubusercontent.com/77607182/143197747-f54dcc55-2470-4485-ac90-b86552c21c76.png">
