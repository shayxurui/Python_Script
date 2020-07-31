import cv2
import numpy as np
import matplotlib.pyplot as plt



img=cv2.imread('1.jpg')

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
result = 20*np.log(cv2.magnitude(dftShift[:,:,0], dftShift[:,:,1]))



plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('original')
plt.axis('off')

plt.subplot(122)
plt.imshow(result, cmap = 'gray')
plt.title('result')
plt.axis('off')

plt.show()


