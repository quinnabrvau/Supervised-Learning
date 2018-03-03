""""TestDriver.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Test Driver to use in testing our learning agents
"""

import numpy as np
from dataSet import dataSet, getIrisData, getWineData
from NeuralNet import NeuralNet
import time


def calculate_accuracy(Y, Y_predict):  # TODO: Break into a separate Report class
    """Returns the percentage of accurate predictions"""
    total_entries = Y.shape[0]
    total_matching = 0

    for i in range(total_entries):
        if Y[i] == Y_predict[i]:
            total_matching += 1

    return total_matching / total_entries

class NNTestDriver:
    def __init__(self,train,test,valid):
        train_data = np.asarray(train)
        test_data = np.asarray(test)
        valid_data = np.asarray(valid)

        # Create the samples ndarray matrices with only the columns for the features
        # (leaving off the last column, which holds the classifications)
        self.X_train = train_data[:, :-1]
        self.X_valid = valid_data[:, :-1]
        self.X_test = test_data[:, :-1]

        # Create the classification ndarray vectors from the last column of the data
        self.Y_train = (train_data[:, -1]).astype(int)
        self.Y_valid = (valid_data[:, -1]).astype(int)
        self.Y_test  = (test_data[:, -1]).astype(int)

        num_train_samples, num_features = self.X_train.shape
        alpha = 10e-5  # learning rate
        num_classifications = len(train.classes)
        print("TESTING: num_classifications", num_classifications)
        self.NN = NeuralNet(num_features, num_classifications, alpha)


        # alpha = 10e-5  # learning rate
        # self.NN = NeuralNet(len(train[0])-1, len(train.classes), alpha)

    def build(self):
        start_time = time.time()  # TODO: Possibly format time?
        print("Starting Neural Net Training at time = ", start_time)
        self.NN.train(self.X_train, self.Y_train, self.X_valid, self.Y_valid)
        stop_time = time.time()
        total_time = stop_time - start_time
        print("Neural Net Training finished at time = ", stop_time, ", taking a total of ", time.time()-start_time, " seconds")

    def test(self):
        Y_test_predict, test_loss = self.NN.predict(self.X_test, self.Y_test)
        return Y_test_predict




if __name__ == "__main__":

    # Get training, testing, and validation data
    # and put into ndarray format

    # train, test, valid = getIrisData(1)
    # num_classifications = 3  # TODO: Fix this to call from data (add dataSet method?)

    train, test, valid = getWineData(1)

    searcher = NNTestDriver(train,test,valid)
    searcher.build()
    print(searcher(test))
    # num_classifications = 13

    # train_data = np.asarray(train)
    # test_data = np.asarray(test)
    # valid_data = np.asarray(valid)

    # # Create the samples ndarray matrices with only the columns for the features
    # # (leaving off the last column, which holds the classifications)
    # X_train = train_data[:, :-1]
    # X_test = test_data[:, :-1]
    # X_valid = valid_data[:, :-1]

    # # Create the classification ndarray vectors from the last column of the data
    # Y_train = (train_data[:, -1]).astype(int)
    # Y_test = (test_data[:, -1]).astype(int)
    # Y_valid = (valid_data[:, -1]).astype(int)

    # # Create a new neural net
    # num_train_samples, num_features = X_train.shape
    # alpha = 10e-5  # learning rate
    # nn = NeuralNet(num_features, num_classifications, alpha)

    # # Train the neural net on the training data
    # start_time = time.time()  # TODO: Possibly format time?
    # print("Starting Neural Net Training at time = ", start_time)
    # nn.train(X_train, Y_train, X_valid, Y_valid)
    # stop_time = time.time()
    # total_time = stop_time - start_time
    # print("Neural Net Training finished at time = ", stop_time, ", taking a total of ", total_time, " seconds")

    # # Use the test data to predict classes to see how well the neural net classifies
    # Y_train_predict, train_loss = nn.predict(X_train, Y_train)
    # Y_test_predict, test_loss = nn.predict(X_test, Y_test)

    # # TODO: Clean up after testing
    # # print(Y_train)
    # # print(Y_train_predict)
    # print("Neural Net Accuracy for Training Data: ", calculate_accuracy(Y_train, Y_train_predict))

    # # print(Y_test)
    # print(Y_test_predict)
    # print("Neural Net Accuracy for Test Data: ", calculate_accuracy(Y_test, Y_test_predict))









