#%% imports

import csv
import tensorflow as tf
import matplotlib.pyplot as plt
# %matplotlib inline # uncomment this line if you're using a jupyter notebook

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



#%% setup model



#%% train model



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
