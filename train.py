#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.chdir('/home/wschenst06g/Ming/MMSE_global/dodo/yolov4') 


# In[2]:


get_ipython().system(' nvidia-smi')


# In[114]:


get_ipython().system('wget https://github.com/WongKinYiu/ScaledYOLOv4/archive/yolov4-csp.zip')
get_ipython().system('unzip yolov4-csp.zip && rm yolov4-csp.zip')


# In[6]:


get_ipython().system('pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html')


# In[5]:


get_ipython().system('git clone https://github.com/thomasbrandon/mish-cuda')
get_ipython().run_line_magic('cd', 'mish-cuda')
get_ipython().system('python setup.py build install')
get_ipython().system('pip install -U PyYAML')


# In[115]:


get_ipython().system('ls')


# In[4]:


get_ipython().run_line_magic('cd', '/home/wschenst06g/Ming/MMSE_global/dodo/yolov4/ScaledYOLOv4-yolov4-csp')


# In[9]:


get_ipython().system('cp /home/wschenst06g/Ming/MMSE_global/dodo/yolov4/obj.zip ../')
get_ipython().system('unzip ../obj.zip -d data/')


# In[33]:


get_ipython().system('cp /home/wschenst06g/Ming/MMSE_global/dodo/yolov4/train_txt.zip ../')
get_ipython().system('unzip ../train_txt.zip -d data/')


# In[10]:


get_ipython().system('cp /home/wschenst06g/Ming/MMSE_global/dodo/yolov4/generate_train.py ./')


# In[11]:


get_ipython().system(' python /home/wschenst06g/Ming/MMSE_global/dodo/yolov4/generate_train.py')


# In[88]:


get_ipython().run_line_magic('cd', '/home/wschenst06g/Ming/MMSE_global/dodo/yolov4/ScaledYOLOv4-yolov4-csp/data')
get_ipython().system('touch digits.yaml')
get_ipython().run_line_magic('cd', '/home/wschenst06g/Ming/MMSE_global/dodo/yolov4/ScaledYOLOv4-yolov4-csp/data')


# In[89]:


get_ipython().run_cell_magic('writefile', 'digits.yaml', "train: /home/wschenst06g/Ming/MMSE_global/dodo/yolov4/ScaledYOLOv4-yolov4-csp/data/train.txt\nval: /home/wschenst06g/Ming/MMSE_global/dodo/yolov4/ScaledYOLOv4-yolov4-csp/data/valid.txt\ntest: /home/wschenst06g/Ming/MMSE_global/dodo/yolov4/ScaledYOLOv4-yolov4-csp/data/test.txt\nnc: 10\nnames: ['1.0','2.0','3.0','4.0','5.0','6.0','7.0','8.0','9.0','10.0']")


# In[7]:


get_ipython().run_line_magic('cd', '/home/wschenst06g/Ming/MMSE_global/dodo/yolov4/ScaledYOLOv4-yolov4-csp/')


# In[15]:


# 複製一個 cfg 檔
get_ipython().system('cp models/yolov4-csp.cfg models/yolov4-csp_416.cfg')
# 查看修改前的參數
get_ipython().system('sed -n -e 8p -e 9p -e 1022p -e 1029p -e 1131p -e 1138p -e 1240p -e 1247p models/yolov4-csp_416.cfg')


# In[16]:


get_ipython().system("sed -i '8s/512/448/' models/yolov4-csp_416.cfg")
get_ipython().system("sed -i '9s/512/448/' models/yolov4-csp_416.cfg")
get_ipython().system("sed -i '1022s/255/45/' models/yolov4-csp_416.cfg")
get_ipython().system("sed -i '1029s/80/10/' models/yolov4-csp_416.cfg")
get_ipython().system("sed -i '1131s/255/45/' models/yolov4-csp_416.cfg")
get_ipython().system("sed -i '1138s/80/10/' models/yolov4-csp_416.cfg")
get_ipython().system("sed -i '1240s/255/45/' models/yolov4-csp_416.cfg")
get_ipython().system("sed -i '1247s/80/10/' models/yolov4-csp_416.cfg")
# 查看修改後的參數
get_ipython().system('sed -n -e 8p -e 9p -e 1022p -e 1029p -e 1131p -e 1138p -e 1240p -e 1247p models/yolov4-csp_416.cfg')


# In[22]:


pip install opencv-python


# In[37]:


# !pip install -U opencv-python
# !apt-get upgrade
# !apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx


# In[9]:


get_ipython().system('sudo apt update')
get_ipython().system('sudo apt install libgl1-mesa-glx -y')


# In[10]:


get_ipython().system("python train.py --device 0 --img 576 --data data/digits.yaml --cfg models/yolov4-csp_416.cfg --weights '' --name yolov4-csp")


# In[ ]:


get_ipython().system('cp /home/wschenst06g/Ming/MMSE_global/dodo/yolov4/obj_test.zip ../')
get_ipython().system('unzip ../obj_test.zip -d data/')


# In[8]:


get_ipython().system('ls')


# In[17]:


get_ipython().system('python test.py --img 576 --conf 0.001 --batch 8 --device 0 --data data/digits.yaml --cfg models/yolov4-csp_416.cfg --names data/obj.names --weights runs/train/yolov4-csp14/weights/best.pt --task test --save-json')


# In[25]:


import glob
get_ipython().run_line_magic('cd', '/home/wschenst06g/Ming/MMSE_global/dodo/yolov4/ScaledYOLOv4-yolov4-csp')
a = glob.glob('../coco/annotations/instances_val*.json')
print(a)


# In[ ]:




