import cv2

file_name = '3b59c8a5-f0b031cc.jpg'
image = cv2.imread('../data/images/' + file_name)

cv2.imshow('image', image)
cv2.waitKey(0)
