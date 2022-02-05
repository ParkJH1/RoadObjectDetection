import cv2
import os

file_name = 'ae7f4103-b1fbdc93.jpg'
image = cv2.imread('../data/images/' + file_name)

resize_image = cv2.resize(image, (224, 224))

if not os.path.exists('resize_image'):
    os.mkdir('resize_image')

cv2.imwrite('resize_image/0.jpg', resize_image)
