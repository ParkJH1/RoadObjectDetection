import cv2

file_name = '00e9be89-00001215.jpg'
image = cv2.imread('../data/images/' + file_name)

print(image)
print(image.shape)
print(type(image))
