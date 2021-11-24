import os

image_files = []
os.chdir(os.path.join("data","train_jpg"))
# os.chdir(os.path.join("/Users/dodo/Desktop/深度學習之視覺辨識/VRDL_HW2_RELEASED_DATASET","train_jpg"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/train_jpg/" + filename)
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files[:26722]:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
with open("valid.txt", "w") as outfile:
    for image in image_files[26722:]:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")

