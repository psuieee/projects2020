#%% imports

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


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

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])


#%% setup model

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

#%% train model

model.fit(x_train, y_train, epochs=5)


#%% evaluate model

model.evaluate(x_test, y_test, verbose=2)

probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])

#%% plot a sample and model prediction

image = x_test[71]

fig = plt.figure()
plt.imshow(image, cmap='gray')
plt.show()

image = np.expand_dims(image,0)

print("Model predicted " + str(np.argmax(probability_model.predict(image))))