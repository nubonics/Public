__author__ = "Nubonics"
__copyright__ = "Copyright 2019"
__credits__ = ["Nubonics"]
__license__ = "GPL"
__version__ = "0.0.0"
__maintainer__ = "Nubonics"
__email__ = "codyjquist@gmail.com"
__status__ = "Development"


import tensorflow as tf
if tf.__version__ != '2.0.0-alpha0':
    from os import system
    system("pip install tensorflow==2.0.0.0alpha0")
    import tensorflow as tf
else:
    import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.preprocessing import image


# module / cnn loader
model = keras.models.load_model('handwritten_digits.h5')

# load the image
path = r"C:\Users\Sylar\pyscripts3\freelancer\Bids\Test_Bids\Project_16\handwritten_digits\example.png"
img = image.load_img(path, target_size=(28, 28), color_mode = "grayscale")
x = image.img_to_array(img) / 255
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = model.predict(images, batch_size=10)[0]

print(classes)

for class_ in range(10):
    if classes[class_]>0.5:
        print(f'The program recognized this number as a {class_}')
