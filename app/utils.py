import numpy as np

def preprocess_input(data):
    array = np.array(data)
    array = array.reshape((1, -1))  # Adjust shape as needed
    array = array / 255.0           # Normalize if required
    return array