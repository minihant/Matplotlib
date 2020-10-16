import numpy as np
import matplotlib.pyplot as plt
# pip install opencv-python
import cv2
img_name = "picture/hant.jpg"
img_array = cv2.imread(img_name)
h,w,c = img_array.shape
R_img_array = np.zeros((h,w,3),dtype=np.uint8) #初始化Red图片，全部值为0
G_img_array = np.zeros((h,w,3),dtype=np.uint8) #初始化Green图片，全部值为0
B_img_array = np.zeros((h,w,3),dtype=np.uint8) #初始化Blue 图片，全部值为0

B_img_array[:,:,0] = img_array[:,:,0] 
G_img_array[:,:,1] = img_array[:,:,1]
R_img_array[:,:,2] = img_array[:,:,2]


plt.subplot(2,2,1)
plt.imshow(img_array)

plt.subplot(2,2,2)
plt.imshow(R_img_array)

plt.subplot(2,2,3)
plt.imshow(G_img_array)

plt.subplot(2,2,4)
plt.imshow(B_img_array)
plt.show()


# 可以把刚刚的图片保存下来
cv2.imwrite("./picture/out_R.jpg",R_img_array)
cv2.imwrite("./picture/out_G.jpg",G_img_array)
cv2.imwrite("./picture/out_B.jpg",B_img_array)