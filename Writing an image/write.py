import cv2

img = cv2.imread('lena.jpg', 1)
cv2.imshow('image', img)

cv2.imwrite('lena_copy.jpg', img)
#The above function will create a copy of the lena.jpg image and write it in a new file

cv2.waitKey(0)
cv2.destroyAllWindows()
