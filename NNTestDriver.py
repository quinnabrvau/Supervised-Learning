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
    train,test,valid = getIrisData(1)
    train,test,valid = getWineData(1)
    train_data = np.asarray(train)
    test_data = np.asarray(test)
    valid_data = np.asarray(valid)

    # Create numpy ndarray matrices of samples and their attributes (as floats)
    # leaving off the first row with the column names
    # and the last two columns, which hold the classification and an empty row
    X_train = train_data[1:, :-1]
    X_train = X_train.astype(float)
    X_test = test_data[1:, :-1]
    X_test = X_test.astype(float)
    X_valid = valid_data[1:, :-1]
    X_valid = X_valid.astype(float)

    # Create numpy ndarray vectors for the classifications for the samples
    # with 0 for red, and 1 for white
    Y_train = np.asarray([int(row[-1] == 'w') for row in train_data[1:]])
    Y_test = np.asarray([int(row[-1] == 'w') for row in test_data[1:]])
    Y_valid = np.asarray([int(row[-1] == 'w') for row in valid_data[1:]])

    # Create a new neural net
    num_train_samples, num_features = X_train.shape
    num_classifications = 2
    alpha = 10e-5  # learning rate
    nn = NeuralNet(num_features, num_classifications, alpha)

    # Train the neural net on the training data
    nn.train(X_train, Y_train)

    # # Use the test data to predict classes to see how well the neural net classifies
    Y_train_predict = nn.predict(X_train)
    Y_test_predict = nn.predict(X_test)

    print(Y_test)
    print(Y_test_predict)
    print(calculate_accuracy(Y_test, Y_test_predict))









