#%% imports

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline # uncomment this line if you're using a jupyter notebook

#%% load mnist

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

#%% show one of the numbers

image = x_test[0]

fig = plt.figure()
plt.imshow(image, cmap='gray')
plt.show()

#%% model definition


#%% setup model



#%% train model



#%% evaluate model



#%% plot a sample and model prediction

image = x_test[71]

fig = plt.figure()
plt.imshow(image, cmap='gray')
plt.show()

image = np.expand_dims(image,0)

print("Model predicted " + str(np.argmax(probability_model.predict(image))))
