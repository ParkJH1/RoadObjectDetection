import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('../models/mymodel.h5')

image = np.random.rand(224, 224, 3)
print(image.shape)

data = np.array([image])
print(data.shape)

predict = model.predict(data)
print(predict)

index = np.argmax(predict)
print(index)

class_names = ['bike', 'bus', 'car', 'motor']

print(class_names[index])
