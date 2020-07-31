import os
import csv
from matplotlib import pyplot as plt
import cv2
from PIL import Image
import numpy as np
from scipy.io import loadmat

train_label_path=r'E:\DataSet\human_pose_dataset\lsp\joints.mat'
img_root=r'E:\DataSet\human_pose_dataset\lsp\images'
save_img_root=r'E:\DataSet\human_pose_dataset\lsp\save_images'

if os.path.exists(save_img_root)==False:
    os.makedirs(save_img_root)

keypoints=['Right ankle',
'Right knee',
'Right hip',
'Left hip',
'Left knee',
'Left ankle',
'Right wrist',
'Right elbow',
'Right shoulder',
'Left shoulder',
'Left elbow',
'Left wrist',
'Neck',
'Head top',]

def read_mat(mat_path):

    files=os.listdir(img_root)

    matfile=loadmat(mat_path)

    joints=matfile['joints'].transpose(2,1,0)[:,:,:2]

    print(joints.shape)


    for k,file in enumerate(files):
        img_path=os.path.join(img_root,file)
        img=cv2.imread(img_path)

        joint=joints[k]

        pre_x=0
        pre_y=0
        for i,coord in enumerate(joint):

            if(keypoints[i]=='Right wrist' or keypoints[i]=='Neck'):
                pre_x = 0
                pre_y = 0

            (x,y)=(int(coord[0]),int(coord[1]))

            cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
            # cv2.putText(img, keypoints[i], (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 255, 0), 1)
            if(pre_x!=0):
                cv2.line(img, (pre_x, pre_y), (x, y), (255, 0, 255), 1)

            pre_x=x
            pre_y=y


        (x1,y1)=(int(joint[3][0]),int(joint[3][1]))
        (x2, y2) = (int(joint[9][0]),int(joint[9][1]))

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 1)

        (x1,y1)=(int(joint[2][0]),int(joint[2][1]))
        (x2, y2) = (int(joint[8][0]),int(joint[8][1]))

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 1)

        save_img_path = os.path.join(save_img_root, file)
        print(save_img_path)
        # cv2.imwrite(save_img_path, img)
        cv2.imshow('image',img)
        cv2.waitKey()


    labels=list()





    return files,labels






if __name__=='__main__':
    (files,labels)=read_mat(train_label_path)




