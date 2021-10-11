from tensorflow.keras import layers
import numpy as tf
import matplotlib.pyplot as plt
from tensorflow import keras
import pandas


temperature = (25, 26, 27, 28, 28, 27, 26, 24, 24, 23, 22, 22, 21, 20, 18, 17)
vent = (10, 15, 30, 35, 36, 31, 16, 14, 13, 7,  6, 6, 5, 5, 5, 4)

#temperature_test = (26, 27)
#vent_test = (16, 31)


#a = 0.5
#b = 7


result = pandas.read_csv('data.csv')


# np.linspace(10, 30, num=100000)
x_data = (result["Fioul"])

# a * x_data + b + np.random.normal(size=100000)
y_data = (result["Charbon"])


# Create the model


X = temperature
Y = vent


# Create a new Sequential Model
model = keras.Sequential()

# Add our layers

model.add(layers.Dense(
    4,  # Amount of Neurons
    input_dim=2,  # Define an input dimension because this is the first layer
    activation='relu'  # Use relu activation function because all inputs are positive
))

model.add(layers.Dense(
    1,  # Amount of Neurons. We want one output
    activation='sigmoid'  # Use sigmoid because we want to output a binary classification
))


# Compile our layers into a model

model.compile(
    loss='mean_squared_error',  # The loss function that is being minimized
    optimizer='adam',  # Our optimization function
    # Metrics are different values that you want the model to track while training
    metrics=['binary_accuracy']
)


# Our function to take in two numerical inputs and output the relevant boolean
def cleanPredict(a, b):
    # model.predict(input) yields a 2d tensor
    return round(model.predict(0, 40)[0][0]) == 1


# Will yield a random value because model isn't yet trained
print(cleanPredict(40, 0))

model.fit(
    X,  # Input training data
    Y,  # Output training data
    epochs=2000,  # Amount of iterations we want to train for
    verbose=1  # Amount of detail you want shown in terminal while training
)

print(cleanPredict(40, 0))
