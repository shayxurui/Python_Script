import cv2
import numpy as np
import json
import os
# from pycocotools.coco import COCO

train_label_path=r'F:\dataset\coco\person_keypoints_val2017.json'

img_root=r'F:\dataset\coco\val2017'

save_img_root=r'E:\DataSet\human_pose_dataset\MSCOCO\save_images'

kps=['nose','L eye' ,'R eye', 'L ear','R ear','L sho' ,'R sho', 'L elb','R elb','L wri' ,
           'R wri','L hip','R hip' ,'L kne' ,'R kne','L ank','R ank']

if os.path.exists(save_img_root)==False:
    os.makedirs(save_img_root)

def read_json(json_path):

    with open(json_path) as anno_file:
        anno=json.load(anno_file)

    print(anno.keys())
    annotations=anno['annotations']

    # images=annotations['images']
    for annotation in annotations:
        bbox=annotation['bbox']
        keypoints=annotation['keypoints']
        image_id=annotation['image_id']


        image_name=str('%012d'%image_id)+'.jpg'
        image_path=os.path.join(img_root,image_name)
        if(os.path.exists(image_path)==False):
            continue

        img=cv2.imread(image_path)



        for k in range(0,len(keypoints),3):
            if(keypoints[k+2]==0):
                continue
            (x,y)=(int(keypoints[k]),int(keypoints[k+1]))
            cv2.circle(img,(x,y),3,(0,0,255),-1)
            # cv2.putText(img, kps[int(k / 3)], (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 255, 0), 1)


        (x1, y1,v1) = (int(keypoints[0]), int(keypoints[1]), int(keypoints[2]))
        (x2,y2,v2)=(int(keypoints[3]), int(keypoints[4]), int(keypoints[5]))
        if(v1!=0 and v2!=0):
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 1)
        (x3, y3, v3) = (int(keypoints[6]), int(keypoints[7]), int(keypoints[8]))
        if (v1 != 0 and v3 != 0):
            cv2.line(img, (x1, y1), (x3, y3), (255, 0, 255), 1)
        (x4,y4,v4)=(int(keypoints[9]), int(keypoints[10]), int(keypoints[11]))
        if (v2 != 0 and v4 != 0):
            cv2.line(img, (x2, y2), (x4, y4), (255, 0, 255), 1)
        (x5, y5, v5) = (int(keypoints[12]), int(keypoints[13]), int(keypoints[14]))
        if (v5 != 0 and v3 != 0):
            cv2.line(img, (x3, y3), (x5, y5), (255, 0, 255), 1)

        (x1, y1, v1) = (int(keypoints[15]), int(keypoints[16]), int(keypoints[17]))
        (x2, y2, v2) = (int(keypoints[18]), int(keypoints[19]), int(keypoints[20]))
        if (v1 != 0 and v2 != 0):
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 1)

        (x3, y3, v3) = (int(keypoints[21]), int(keypoints[22]), int(keypoints[23]))
        if (v1 != 0 and v3 != 0):
            cv2.line(img, (x1, y1), (x3, y3), (255, 0, 255), 1)

        (x4, y4, v4) = (int(keypoints[24]), int(keypoints[25]), int(keypoints[26]))
        if (v2 != 0 and v4 != 0):
            cv2.line(img, (x2, y2), (x4, y4), (255, 0, 255), 1)

        (x1, y1, v1) = (int(keypoints[27]), int(keypoints[28]), int(keypoints[29]))
        if (v1 != 0 and v3 != 0):
            cv2.line(img, (x1, y1), (x3, y3), (255, 0, 255), 1)

        (x2, y2, v2) = (int(keypoints[30]), int(keypoints[31]), int(keypoints[32]))
        if (v2 != 0 and v4 != 0):
            cv2.line(img, (x2, y2), (x4, y4), (255, 0, 255), 1)

        (x1, y1, v1) = (int(keypoints[33]), int(keypoints[34]), int(keypoints[35]))
        (x2, y2, v2) = (int(keypoints[36]), int(keypoints[37]), int(keypoints[38]))
        if (v1 != 0 and v2 != 0):
            cv2.line(img, (x1 ,y1), (x2, y2), (255, 0, 255), 1)

        (x3, y3, v3) = (int(keypoints[39]), int(keypoints[40]), int(keypoints[41]))
        if (v1 != 0 and v3 != 0):
            cv2.line(img, (x1, y1), (x3, y3), (255, 0, 255), 1)
        (x4, y4, v4) = (int(keypoints[42]), int(keypoints[43]), int(keypoints[44]))
        if (v2 != 0 and v4 != 0):
            cv2.line(img, (x2, y2), (x4, y4), (255, 0, 255), 1)

        (x1, y1, v1) = (int(keypoints[45]), int(keypoints[46]), int(keypoints[47]))
        if(v1!=0 and v3!=0):
            cv2.line(img, (x1, y1), (x3, y3), (255, 0, 255), 1)
        (x2, y2, v2) = (int(keypoints[48]), int(keypoints[49]), int(keypoints[50]))
        if(v2 != 0 and v4 != 0):
            cv2.line(img, (x2, y2), (x4, y4), (255, 0, 255), 1)






        cv2.rectangle(img, (int(bbox[0]),int(bbox[1])), (int(bbox[0])+int(bbox[2]), int(bbox[1])+int(bbox[3])), (10,0, 255), 1)
        cv2.putText(img,"Bounding Box",(int(bbox[0])-10,int(bbox[1])-10),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

        # save_img_path = os.path.join(save_img_root, image_name)
        # print(save_img_path)
        # cv2.imwrite(save_img_path, img)

        cv2.imshow('image',img)
        cv2.waitKey()





if __name__=='__main__':
    read_json(train_label_path)

