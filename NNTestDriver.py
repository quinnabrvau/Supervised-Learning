""""TestDriver.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Test Driver to use in testing our learning agents
"""

import numpy as np
from dataSet import dataSet, getIrisData, getWineData
from NeuralNet import NeuralNet


def calculate_accuracy(Y, Y_predict):
    total_entries = Y.shape[0]
    total_matching = 0

    # TODO: Delete after testing
    # print(type(Y))
    # print(type(Y_predict))
    # print(Y.shape)
    # print(Y_predict.shape)

    for i in range(total_entries):
        if Y[i] == Y_predict[i]:
            total_matching += 1

    return total_matching / total_entries


if __name__ == "__main__":

    # Get training, testing, and validation data
    # and put into ndarray format

    #train, test, valid = getIrisData(1)
    #num_classifications = 3  # TODO: Fix this to call from data (add dataSet method?)

    train, test, valid = getWineData(1)
    num_classifications = 13

    train_data = np.asarray(train)
    test_data = np.asarray(test)
    valid_data = np.asarray(valid)

    # Create the samples ndarray matrices with only the columns for the features
    # (leaving off the last column, which holds the classifications)
    X_train = train_data[:, :-1]
    X_test = test_data[:, :-1]
    X_valid = valid_data[:, :-1]

    # Create the classification ndarray vectors from the last column of the data
    Y_train = (train_data[:, -1]).astype(int)
    Y_test = (test_data[:, -1]).astype(int)
    Y_valid = (valid_data[:, -1]).astype(int)

    # Create a new neural net
    num_train_samples, num_features = X_train.shape
    alpha = 10e-5  # learning rate
    nn = NeuralNet(num_features, num_classifications, alpha)

    # Train the neural net on the training data
    nn.train(X_train, Y_train)

    # Use the test data to predict classes to see how well the neural net classifies
    Y_train_predict = nn.predict(X_train)
    Y_test_predict = nn.predict(X_test)

    # TODO: Clean up after testing
    print(Y_train)
    print(Y_train_predict)
    print(calculate_accuracy(Y_train, Y_train_predict))

    print(Y_test)
    print(Y_test_predict)
    print(calculate_accuracy(Y_test, Y_test_predict))









