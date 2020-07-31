import os
import csv
from matplotlib import pyplot as plt
import cv2
from PIL import Image
import numpy as np

train_label_path=r'E:\DataSet\人体关键点数据集\FLIC\FLIC-full\train_joints.csv'
img_root=r'E:\DataSet\人体关键点数据集\FLIC\FLIC-full\images'
save_labeled_img_path=r'.\FLIC\FLIC-full\labeled_img'


if os.path.exists(save_labeled_img_path)==False:
    os.makedirs(save_labeled_img_path)


keypoints=['left wrist','left elbow','left shoulder','head','right shoulder','right elbow','right wrist']

def read_csv(csv_path):
    csvfile=open(csv_path,'r')
    plots = csv.reader(csvfile, delimiter=',')

    files=list()
    labels=list()

    for i,rows in enumerate(plots):
        files.append(rows[0])
        tmp=list()
        for row in rows[1:]:
            tmp.append(float(row))

        labels.append(tmp)



    return files,labels






if __name__=='__main__':
    (files,labels)=read_csv(train_label_path)
    #
    #
    #
    # for i,file in enumerate(files):
    #     label=labels[i]
    #     img_file=os.path.join(img_root,file)
    #
    #     if(os.path.exists(img_file)==False):
    #         continue
    #     # img=cv2.imread(img_file)
    #     img=Image.open(img_file)
    #     # img.show()
    #
    #     img=cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
    #
    #     pre_x=0
    #     pre_y=0
    #     for k in range(0,len(label),2):
    #         # print(label[k],label[k+1],type(label[k]),type(label[k+1]))
    #         x=int(label[k])
    #         y=int(label[k+1])
    #         # print(x,y)
    #
    #         cv2.circle(img,(x,y),5,(0,0,255),-1)
    #         cv2.putText(img,keypoints[int(k/2)],(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,0.8,(0,255,0),1)
    #
    #         if(pre_x!=0 and pre_y!=0):
    #             cv2.line(img,(pre_x,pre_y),(x,y),(255,0,255),1)
    #         pre_x=x
    #         pre_y=y
    #
    #     save_img_path=os.path.join(save_labeled_img_path,file)
    #     cv2.imwrite(save_img_path,img)
    #
    #     print(save_img_path)

        # cv2.imshow('image',img)
        # cv2.waitKey()




