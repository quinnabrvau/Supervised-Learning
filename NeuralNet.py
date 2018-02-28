""""NeuralNet.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Neural Net learning agent
which uses a 2-layer feedforward neural network
"""

import numpy as np

class NeuralNet:
    """A neural net class which can be trained on ndarrays of data and classifications."""

    def __init__(self, num_features, num_classifications):
        self.num_features = num_features
        self.num_classifications = num_classifications
        self.num_hidden_nodes = num_features * 2  # have twice as many nodes in each hidden layer as features

        # initialize the weight matrices and bias vectors with random numbers
        self.W1 = np.random.randn(num_features, self.num_hidden_nodes)
        self.b1 = np.random.randn(self.num_hidden_nodes)
        self.W2 = np.random.randn(self.num_hidden_nodes, self.num_classifications)
        self.b2 = np.random.randn(self.num_classifications)

    def train(self, X, Y):
        """Trains the neural net based on the numpy ndarray X matrix of samples and features
        using the numpy ndarray vector Y of associated classifications to update the model"""

        # create a one-hot-encoding matrix for the actual classification Y vector
        # where each row represents a sample, and each column represents a classification
        # and each row gets a 1 in the column that matches its classification
        one_hot_encodings = np.zeros((Y.shape[0], self.num_classifications))  # initialize to all zeros
        for i in range(Y.shape[0]):
            one_hot_encodings[i, Y[i]] = 1

        print(one_hot_encodings)

        # # do a feed forward pass of the data to get predicted classifications
        # A = sigmoid(X.dot(self.W1) + self.b1)  # gets an activation matrix for the hidden layer
        # Y_hat = softmax(A.dot(self.W2) + self.b2)  # gets predicted classification values


    def predict(self, X):
        """Returns a numpy ndarray vector with predicted classifications for the X data"""
        return None  # TODO: return the predicted classification


def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))


def softmax(Z):
    expZ = np.exp(Z)
    return expZ / expZ.sum(axis=1, keepdims=True)
