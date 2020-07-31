import cv2
import numpy as np
import json
import os

train_label_path=r'E:\DataSet\human_pose_dataset\mpii\annot\train.json'

img_root=r'E:\DataSet\human_pose_dataset\mpii\images'

save_img_root=r'E:\DataSet\human_pose_dataset\mpii\save_images'


color1 = [(179,0,0),(228,26,28),(255,255,51),
    (49,163,84), (0,109,45), (255,255,51),
    (240,2,127),(240,2,127),(240,2,127), (240,2,127), (240,2,127),
    (217,95,14), (254,153,41),(255,255,51),
    (44,127,184),(0,0,255)]

link_pairs = [
        [15, 13], [13, 11], [11, 5],
        [12, 14], [14, 16], [12, 6],
        [3, 1],[1, 2],[1, 0],[0, 2],[2,4],
        [9, 7], [7,5], [5, 6],
        [6, 8], [8, 10],
]

point_color1 = [(240,2,127),(240,2,127),(240,2,127),
            (240,2,127), (240,2,127),
            (255,255,51),(255,255,51),
            (254,153,41),(44,127,184),
            (217,95,14),(0,0,255),
            (255,255,51),(255,255,51),(228,26,28),
            (49,163,84),(252,176,243),(0,176,240),
            (255,255,0),(169, 209, 142),
            (255,255,0),(169, 209, 142),
            (255,255,0),(169, 209, 142)]





if os.path.exists(save_img_root)==False:
    os.makedirs(save_img_root)

keypoints=['r ankle', 'r knee', 'r hip','l hip','l knee', 'l ankle', 'pelvis','thorax','upper neck', 'head top', 'r wrist','r elbow', 'r shoulder', 'l shoulder','l elbow','l wrist']
def read_json(json_path):

    with open(json_path) as anno_file:
        anno=json.load(anno_file)

    gt_db=list()

    for a in anno:
        image_name = a['image']
        print(image_name)
        if os.path.exists(os.path.join(img_root,image_name))==False:
            continue

        img=cv2.imread(os.path.join(img_root,image_name))

        c = np.array(a['center'], dtype=np.float)
        s = np.array([a['scale'], a['scale']], dtype=np.float)

        if c[0] != -1:
            c[1] = c[1] + 15 * s[1]
            s = s * 1.25

        c = c - 1

        joints_3d = np.zeros((16, 3), dtype=np.float)

        joints = np.array(a['joints'])

        pre_x=0
        pre_y=0

        min_x=65535
        min_y=65535

        max_x=0
        max_y=0


        for k,joint in enumerate(joints):
            (x,y)=(int(joint[0]),int(joint[1]))

            min_x=min(min_x,x)
            min_y=min(min_y,y)

            max_x=max(max_x,x)
            max_y=max(max_y,y)

            cv2.circle(img, (x, y), 3, (0, 0, 255), -1)


            if(pre_x!=0 or pre_y!=0):
                if (keypoints[k]=='pelvis' or keypoints[k]=='r wrist'):
                    pre_x=x
                    pre_y=y
                    continue
                cv2.line(img,(pre_x,pre_y),(x,y),(255,0,255),2)

            pre_x=x
            pre_y=y

        # cv2.rectangle(img,(min_x-10,min_y-30),(max_x+10,max_y+30),(100,100,10),2)

        # save_img_path = os.path.join(save_img_root, image_name)
        # cv2.imwrite(save_img_path,img)

        cv2.imshow('image',img)
        cv2.waitKey()





if __name__=='__main__':
    read_json(train_label_path)