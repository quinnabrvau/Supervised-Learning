"""NeuralNet.py by Shannon Ladymon (UWNetID: sladymon)
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

    def __init__(self, num_features, num_classifications, alpha=10e-6, decay=False, layers=2.0):
        self.num_features = num_features
        self.num_classifications = num_classifications
        self.num_hidden_nodes = int(num_features * layers)
        self.alpha = alpha
        self.layers = layers
        self.decay = decay

        # initialize the weight matrices and bias vectors with random numbers
        self.W1 = np.random.randn(num_features, self.num_hidden_nodes)
        self.b1 = np.random.randn(self.num_hidden_nodes)
        self.W2 = np.random.randn(self.num_hidden_nodes, self.num_classifications)
        self.b2 = np.random.randn(self.num_classifications)

    def train(self, X_train, Y_train, X_valid, Y_valid):
        """Trains the neural net based on the numpy ndarray X matrix of samples and features
        using the numpy ndarray vector Y of associated classifications to update the model"""

        min_alpha = 0.00001  # the lowest alpha I want to use
        decay_rate = 0.001 # the amount to decay per epoch
        min_epochs = 100  # the fewest epochs I want to run
        max_epochs = 100000  # the most epochs I want to run
        previous_training_loss = 0  # initialize the loss for the training
        previous_valid_loss = 0  # initialize the loss for the validation
        train_loss_epsilon = 0.01  # small number for when to stop looking for better loss in training
        valid_loss_epsilon = -0.01  # small number for when we start getting more validation loss rather than less

        # create a one-hot-encoding matrix for the actual classification Y vector
        # where each row represents a sample, and each column represents a classification
        # and each row gets a 1 in the column that matches its classification
        one_hot_encodings = np.zeros((Y_train.shape[0], self.num_classifications))  # initialize to all zeros
        for i in range(Y_train.shape[0]):
            one_hot_encodings[i, Y_train[i]] = 1

        # run multiple epochs of training to get more accurate weights and predictions
        for epoch in range(max_epochs):

            # adjust alpha if decay is being used
            if self.decay and self.alpha > min_alpha:
                self.alpha = self.alpha * 1.0 / (1.0 + (decay_rate * epoch))

            # train for a single epoch and get the training loss (how wrong the model currently is)
            train_loss = self._train_single_epoch(X_train, one_hot_encodings)

            # get the difference (delta) between the previous and current training loss
            train_loss_delta = previous_training_loss - train_loss
            previous_training_loss = train_loss  # update the previous training loss

            # see how well this model predicts the validation set and get the validation loss
            Y_valid_predict, valid_loss = self.predict(X_valid, Y_valid)

            # get the difference (delta) between the previous and current validation loss
            valid_loss_delta = previous_valid_loss - valid_loss
            previous_valid_loss = valid_loss  # update the previous validation loss

            # as long as we have run at least the min_epochs
            # if our delta for training loss is too small or our delta for validation loss too big
            # stop training since we aren't gaining much
            if epoch > min_epochs and (train_loss_delta < train_loss_epsilon or valid_loss_delta < valid_loss_epsilon):
                # print("TESTING: stopped training at epoch: ", epoch)  # TODO: Delete
                # break  # stop running
                return epoch


    def _train_single_epoch(self, X, one_hot_encodings):
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

    def predict(self, X, Y):
        """Returns a numpy ndarray vector with predicted classifications for the X data"""
        # create a one-hot-encoding matrix for the actual classification Y vector
        # where each row represents a sample, and each column represents a classification
        # and each row gets a 1 in the column that matches its classification
        one_hot_encodings = np.zeros((Y.shape[0], self.num_classifications))  # initialize to all zeros
        for i in range(Y.shape[0]):
            one_hot_encodings[i, Y[i]] = 1

        # do a feed forward pass of the data to get predicted classifications
        A = sigmoid(np.dot(X, self.W1) + self.b1)  # gets an activation matrix for the hidden layer
        Y_hat = softmax(np.dot(A, self.W2) + self.b2)  # gets predicted classification values

        loss = np.sum(-one_hot_encodings * np.log(Y_hat))  # how wrong the model currently is

        # return predicted values for this dataset
        return np.argmax(Y_hat, axis=1), loss


def sigmoid(Z):  # TODO: consider changing to tanh instead
    """Sigmoid function to use between input and hidden layer for activation"""
    return 1.0 / (1.0 + np.exp(-Z))


def softmax(Z):
    """Softmax function to use between hidden and output layers to get a prediction for classifications"""
    expZ = np.exp(Z)
    return expZ / expZ.sum(axis=1, keepdims=True)
