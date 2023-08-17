import cv2
import matplotlib.pyplot as plt

img = cv2.imread('car.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray, 125, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

copy_img = img.copy()

cv2.drawContours(copy_img, contours, -1, (0, 0, 255), 2)
titles = ['original', 'contours']

imgs = [img, copy_img]
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.title(titles[i])
    plt.imshow(imgs[i])
plt.show()
