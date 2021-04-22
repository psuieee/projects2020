#%% imports

import csv
import tensorflow as tf
import matplotlib.pyplot as plt

#%% make dataset

x_train, y_train = [], []

with open('winequality-red.csv', newline='') as file:
    reader = csv.reader(file, delimiter=';', quotechar='|')

    firstRow = True
    for row in reader:
        if not firstRow:
            newdata = []

            for item in row[:-1]:
                newdata.append(float(item))

            x_train.append(newdata)

            y_train.append(int(row[-1]))
        else:
            firstRow = False

print(x_train)
print(y_train)

print(tf.shape(x_train))
print(tf.shape(y_train))

#%% make model

model = tf.keras.models.Sequential([
    tf.keras.layers.InputLayer(input_shape=11),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(9)
])

#%% setup model

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

#%% train model

history = model.fit(x_train, y_train, epochs=50)

#%% plot progress

acc = history.history['accuracy']
loss = history.history['loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.title('Training accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.title('Training loss')
plt.legend()

plt.show()

print("final accuracy " + str(acc[-1]))

#%% make probability model

probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])