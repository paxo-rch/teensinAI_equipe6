import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# Define our training input and output data with type 16 bit float
# Each input maps to an output

X = tf.constant([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=tf.float16)
Y = tf.constant([[0], [1], [1], [0]], dtype=tf.float16)


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
    inputTens = tf.constant([[a, b]])
    # model.predict(input) yields a 2d tensor
    return round(model.predict(inputTens)[0][0]) == 1


# Will yield a random value because model isn't yet trained
print(cleanPredict(1, 0))

model.fit(
    X,  # Input training data
    Y,  # Output training data
    epochs=2000,  # Amount of iterations we want to train for
    verbose=1  # Amount of detail you want shown in terminal while training
)

print(cleanPredict(1, 0))  # Should Yield True
