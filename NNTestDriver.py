""""TestDriver.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Test Driver to use in testing our learning agents
"""

import numpy as np
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
    def __init__(self,train,test,valid,p):
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
        num_classifications = max(train.classes)
        layers,activation,alpha,decay = p
        self.NN = NeuralNet(num_features, num_classifications+1, alpha,decay,layers)

    def build(self,params=None,Report=None):
        # start_time = time.time()  # TODO: Possibly format time?
        # print("Starting Neural Net Training at time = ", start_time)
        epoch = self.NN.train(self.X_train, self.Y_train, self.X_valid, self.Y_valid)
        if Report != None:
            Report['netTrainCycle']=str(epoch)
        # stop_time = time.time()
        # total_time = stop_time - start_time
        # print("Neural Net Training finished at time = ", stop_time, ", taking a total of ", time.time()-start_time, " seconds")

    def predict(self):
        Y_test_predict, test_loss = self.NN.predict(self.X_test, self.Y_test)
        return Y_test_predict

    def params(self,p=None):
        if p!=None:
            self.NN.alpha = p[2]
            self.NN.activation = p[1]
            self.NN.layers = p[0]
            self.NN.deacy = p[3]
        return None


if __name__ == "__main__":
    # Get training, testing, and validation data
    train, test, valid = getWineData(1)


    searcher = NNTestDriver(train,test,valid)
    searcher.build()
    print(searcher.predict())
