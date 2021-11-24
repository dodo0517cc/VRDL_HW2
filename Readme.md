##README

Step1: Use GPU. Set up the environment.

`
!sudo apt update
!sudo apt install libgl1-mesa-glx -y
`

Step2: Git clone the project：https://github.com/WongKinYiu/ScaledYOLOv4

Step3: Install torch==1.6.0+cu101, torchvision==0.7.0+cu101

Step4: Git clone https://github.com/thomasbrandon/mish-cuda, then install.

Step5: Update YAML

Step6: Create a digits.yaml in the data folder, which stores the training set, validation set and test set paths, the number of categories and the category names.

Step7: Modify cfg file. Copy a original cfg file and change the image width and height to 576, filters to 45(filters=(classes + 5)*3, and classes to 10.

Step8: Upload the zip file（obj_test.zip） of all of the test images. Unzip it to the data folder that is in ScaledYOLOv4-yolov4-csp file. Copy gerenate_test.py to ScaledYOLOv4-yolov4-csp file. Then, run it. It will generate test.txt.

Step9: Copy weights(best.pt) to ScaledYOLOv4-yolov4-csp file and obj.names to the data folder that is in ScaledYOLOv4-yolov4-csp file.

Step10: Test.

Colab link : https://colab.research.google.com/drive/1nuD7Wjm8eQZ_GffDrEoYmo5zeGP2vNBj#scrollTo=Lx6jYnaLaj1q



<img width="415" alt="image" src="https://user-images.githubusercontent.com/77607182/143190090-1158eb9b-a954-460c-9f24-c467da86bea0.png">
