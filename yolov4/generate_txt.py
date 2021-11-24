import pandas as  pd
from PIL import Image
data = pd.read_csv('/Users/dodo/Desktop/深度學習之視覺辨識/VRDL_HW2_RELEASED_DATASET/boxes.csv')
data.rename(columns={'Unnamed: 0':'name'},inplace=True)
# image_name = df['name'].unique()
# for i in image_name:
#     records = df[df['name'] == i]
#     boxes = records[['xmin', 'ymin', 'xmax', 'ymax']].values
for index in range(len(data)):
    df = data.iloc[index].values
    records = data[data['name'] == df[0]]
    im1 = Image.open('/Users/dodo/Desktop/深度學習之視覺辨識/VRDL_HW2_RELEASED_DATASET/train/' + df[0])
    w = im1.size[0]
    h = im1.size[1]
    file = open('/Users/dodo/Desktop/深度學習之視覺辨識/VRDL_HW2_RELEASED_DATASET/train_txt/'+ df[0].split('.')[0] +'.txt', 'wt')
    for i in range(len(records)):
        print([str(int(list(records['label'])[i])-1)," ",str((list(records['xmin'])[i]+list(records['xmax'])[i])/2.0/w)," ",str((list(records['ymin'])[i]+list(records['ymax'])[i])/2.0/h)," ",str(list(records['width'])[i]/w)," ",str(list(records['height'])[i]/h),"\n"])
        file.writelines([str(int(list(records['label'])[i])-1)," ",str((list(records['xmin'])[i]+list(records['xmax'])[i])/2.0/w)," ",str((list(records['ymin'])[i]+list(records['ymax'])[i])/2.0/h)," ",str(list(records['width'])[i]/w)," ",str(list(records['height'])[i]/h),"\n"]) 
    file.close()
