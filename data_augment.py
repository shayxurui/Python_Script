import cv2
import os
import numpy as np
import random
import copy





save_img_path=r'./save_data_augment'

if os.path.exists(save_img_path)==False:
    os.makedirs(save_img_path)


def InvertImg(img):

    img=255-img

    # cv2.imwrite(os.path.join(save_img_path,'InvertImg.jpg'),img)

    return img



def ADDRand(img):

    (hs,ws,cs)=img.shape

    for h in range(hs):
        for w in range(ws):
            for c in range(cs):
                img[h][w][c]+=random.randint(0,100)

    # cv2.imwrite(os.path.join(save_img_path, 'ADDRand.jpg'), img)

    return img

def HorizontalFlip(img):

    img=cv2.flip(img,1)

    # cv2.imwrite(os.path.join(save_img_path, 'HorizontalFlip.jpg'), img)

    return img


def RandomBrightnessContrast(img):
    blank = np.zeros(img.shape, img.dtype)

    alpha=1.2
    beta=100
    img=cv2.addWeighted(img,alpha,blank,1-alpha,beta)

    # cv2.imwrite(os.path.join(save_img_path, 'RandomBrightnessContrast.jpg'), img)

    return img


def gasuss_noise(image, mean=0, var=0.001):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)

    return out




def GaussNoise(img):

    img=gasuss_noise(img)

    # cv2.imwrite(os.path.join(save_img_path, 'GaussNoise.jpg'), img)

    return img


def sp_noise(image,prob=0.1):
    '''
    添加椒盐噪声
    prob:噪声比例
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def SaltAndPepperNoise(img):
    img=sp_noise(img)

    # cv2.imwrite(os.path.join(save_img_path, 'SaltAndPepperNoise.jpg'), img)

    return img


def GaussianBlur(img):
    img = cv2.GaussianBlur(img,(5, 5),2)

    # cv2.imwrite(os.path.join(save_img_path, 'GaussianBlur.jpg'), img)

    return img

def MedianBlur(img):

    img=cv2.medianBlur(img,5)
    cv2.imwrite(os.path.join(save_img_path, 'MedianBlur.jpg'), img)

    return img

def CLAHE(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(ycrcb)
    cv2.equalizeHist(channels[0], channels[0])
    cv2.merge(channels, ycrcb)
    cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)

    # cv2.imwrite(os.path.join(save_img_path, 'CLAHE.jpg'), img)

    return img






if __name__=='__main__':
    img_path=r'1.jpg'

    img=cv2.imread(img_path)


    img1=copy.deepcopy(img)

    MedianBlur(img)
    # invert_img=InvertImg(img1)
    #
    # img2 = copy.deepcopy(img)
    # add_rand_img=ADDRand(img2)
    #
    # img3 = copy.deepcopy(img)
    # horizontal_flip_img=HorizontalFlip(img3)
    #
    # img4 = copy.deepcopy(img)
    # random_brightness_contrast_img=RandomBrightnessContrast(img4)
    #
    # img5 = copy.deepcopy(img)
    # gaussian_blur_img=GaussianBlur(img5)
    #
    # img6 = copy.deepcopy(img)
    # gauss_noise_img=GaussNoise(img6)
    #
    # img7 = copy.deepcopy(img)
    # salt_and_pepper_noise_img=SaltAndPepperNoise(img7)
    #
    # img8 = copy.deepcopy(img)
    # CLAHE_img=CLAHE(img8)
    #
    #
    #
    # img_1=np.hstack((img,invert_img,add_rand_img))
    #
    # img_2 = np.hstack((horizontal_flip_img, random_brightness_contrast_img,gaussian_blur_img))
    #
    # img_3=np.hstack((gauss_noise_img,salt_and_pepper_noise_img,CLAHE_img))
    #
    # img_res=np.vstack((img_1,img_2,img_3))


    # cv2.imwrite(os.path.join(save_img_path,'img_res.png'),img_res)
    # img_1=cv2.resize(img,(256,256))
    # cv2.imwrite(os.path.join(save_img_path, 'img1.png'), img_1)
    # cv2.imshow('image',img_res)
    # cv2.waitKey()
