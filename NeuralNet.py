""""NeuralNet.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Neural Net learning agent
which uses a 2-layer feedforward neural network
Based on the resource:
"Neural Networks from Scratch in Python," by Cristian Dima
available online at: http://www.cristiandima.com/neural-networks-from-scratch-in-python/
"""

import numpy as np

class NeuralNet:
    """A neural net class which can be trained on ndarrays of data and classifications."""

    def __init__(self, num_features, num_classifications, alpha=10e-6):
        self.num_features = num_features
        self.num_classifications = num_classifications
        self.num_hidden_nodes = num_features * 2  # have twice as many nodes in each hidden layer as features
        self.alpha = alpha

        # initialize the weight matrices and bias vectors with random numbers
        self.W1 = np.random.randn(num_features, self.num_hidden_nodes)
        self.b1 = np.random.randn(self.num_hidden_nodes)
        self.W2 = np.random.randn(self.num_hidden_nodes, self.num_classifications)
        self.b2 = np.random.randn(self.num_classifications)

    # TODO: try to fix the overflow error for exp
    # C:\Users\shann\Documents\dev\py\cse415\slearning\NeuralNet.py:82: RuntimeWarning: overflow encountered in exp return 1.0 / (1.0 + np.exp(-Z))
    def train(self, X, Y):
        """Trains the neural net based on the numpy ndarray X matrix of samples and features
        using the numpy ndarray vector Y of associated classifications to update the model"""

        # create a one-hot-encoding matrix for the actual classification Y vector
        # where each row represents a sample, and each column represents a classification
        # and each row gets a 1 in the column that matches its classification
        one_hot_encodings = np.zeros((Y.shape[0], self.num_classifications))  # initialize to all zeros
        for i in range(Y.shape[0]):
            one_hot_encodings[i, Y[i]] = 1

        # run 10000 training steps to get more accurate weights and predictions
        for epoch in range(10000):  # TODO: Change to loop until loss stops changing much?
            loss = self._train_single_step(X, one_hot_encodings)

            # # TODO: Delete after testing
            # if epoch % 100 == 0:
            #     print("Loss function value: ", loss)


    def _train_single_step(self, X, one_hot_encodings):  # TODO: Change to "single_epoch" instead?
        """Does a single step of feedforward and backpropogation"""

        # do a feed forward pass of the data to get predicted classifications
        A = sigmoid(np.dot(X, self.W1) + self.b1)  # gets an activation matrix for the hidden layer
        Y_hat = softmax(np.dot(A, self.W2) + self.b2)  # gets predicted classification values

        # do a backpropogation to update W1, W2, b1, and b2 with more accurate values
        output_layer_error = Y_hat - one_hot_encodings
        hidden_layer_error = np.dot(output_layer_error, self.W2.T) * A * (1 - A)

        self.W2 -= self.alpha * np.dot(A.T, output_layer_error)
        self.b2 -= self.alpha * (output_layer_error).sum(axis=0)

        self.W1 -= self.alpha * np.dot(X.T, hidden_layer_error)
        self.b1 -= self.alpha * (hidden_layer_error).sum(axis=0)

        loss = np.sum(-one_hot_encodings * np.log(Y_hat))  # how wrong the model currently is
        return loss



    def predict(self, X):
        """Returns a numpy ndarray vector with predicted classifications for the X data"""
        # do a feed forward pass of the data to get predicted classifications
        A = sigmoid(np.dot(X, self.W1) + self.b1)  # gets an activation matrix for the hidden layer
        Y_hat = softmax(np.dot(A, self.W2) + self.b2)  # gets predicted classification values

        # return predicted values for this dataset
        return np.argmax(Y_hat, axis=1)


def sigmoid(Z):  # TODO: consider changing to tanh instead
    return 1.0 / (1.0 + np.exp(-Z))


def softmax(Z):
    expZ = np.exp(Z)
    return expZ / expZ.sum(axis=1, keepdims=True)
