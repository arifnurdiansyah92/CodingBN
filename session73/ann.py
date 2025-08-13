import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Flatten images to 1D vectors of size 784 (28*28)
x_train = x_train.reshape(-1, 28 * 28)
x_test = x_test.reshape(-1, 28 * 28)

# One-hot encode the labels (e.g., 5 -> [0,0,0,0,0,1,0,0,0,0])
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Build the model layer by layer
model = models.Sequential([
    # Input Layer + First Hidden Layer: 128 neurons, using ReLU activation
    layers.Dense(128, activation='relu', input_shape=(784,)),
    
    # Second Hidden Layer: 64 neurons, also using ReLU
    layers.Dense(64, activation='relu'),
    
    # Output Layer: 10 neurons (one for each digit 0-9)
    # Softmax activation gives us the probability for each class.
    layers.Dense(10, activation='softmax')
])

# Print a summary of our model's architecture
model.summary()

# Compile the model with its learning instructions
model.compile(
    optimizer='adam',                      # The algorithm to use for backpropagation
    loss='categorical_crossentropy',       # The function to measure the model's error
    metrics=['accuracy']                   # The metric we want to track
)

# Train the model!
# An "epoch" is one full pass through the entire training dataset.
print("\nStarting model training...")
history = model.fit(
    x_train, 
    y_train, 
    epochs=10, 
    batch_size=32, 
    validation_split=0.1 # Use 10% of training data for validation
)
print("Model training complete!")
