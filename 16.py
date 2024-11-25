import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Feedforward Neural Network class
class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases for the layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Random initialization of weights
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        
        # Bias initialization
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.bias_output = np.zeros((1, self.output_size))

    # Forward pass: input -> hidden layer -> output layer
    def forward(self, X):
        # Input to hidden layer
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)
        
        # Hidden to output layer
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.output = sigmoid(self.output_input)
        
        return self.output

    # Backpropagation and weight updates
    def backward(self, X, y, learning_rate):
        # Compute the error at the output
        output_error = y - self.output
        output_delta = output_error * sigmoid_derivative(self.output)
        
        # Compute error at hidden layer
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output)
        
        # Update weights and biases using gradient descent
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
        
        # Update biases
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    # Training the neural network
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            self.forward(X)   # Forward pass
            self.backward(X, y, learning_rate)  # Backward pass and weight update
            if (epoch + 1) % 1000 == 0:
                loss = np.mean(np.square(y - self.output))  # Mean squared error
                print(f'Epoch {epoch+1}/{epochs}, Loss: {loss}')

    # Predict using the trained network
    def predict(self, X):
        return self.forward(X)

# Example: XOR Problem
# Input (X) and Output (y)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],  # XOR output for 0,0
              [1],  # XOR output for 0,1
              [1],  # XOR output for 1,0
              [0]])  # XOR output for 1,1

# Initialize the neural network with 2 inputs, 2 hidden neurons, and 1 output
nn = FeedForwardNN(input_size=2, hidden_size=2, output_size=1)

# Train the network
nn.train(X, y, epochs=10000, learning_rate=0.1)

# Test the trained model
print("Predictions after training:")
for input_data in X:
    prediction = nn.predict(input_data.reshape(1, -1))
    print(f'Input: {input_data}, Prediction: {prediction}')
