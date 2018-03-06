""""TestDriver.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Test Driver to use in testing our learning agents
"""

import numpy as np
from NeuralNet import NeuralNet
import time

class NNTestDriver:
    """Class which gets the data ready to be used in the neural net
    and calls the train and predict functions with the parameters specified by the user"""
    def __init__(self,train,test,valid,p):
        # get the data as ndarrays for training, testing, and validation
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

        # get the parameters needed to build the neural net
        num_train_samples, num_features = self.X_train.shape
        num_classifications = max(train.classes)
        layers,activation,alpha,decay = p  # get the user's choices for parameters
        self.NN = NeuralNet(num_features, num_classifications+1, alpha,decay,layers)

    def build(self,params=None,Report=None):
        """Calls the neural net's train function using the formatted training and validation data"""
        epoch = self.NN.train(self.X_train, self.Y_train, self.X_valid, self.Y_valid)

        # record the number of epochs run during training
        if Report != None:
            Report['netTrainCycle']=str(epoch)

    def predict(self):
        """Calls the neural net's predict function using the formatted test data"""
        Y_test_predict, test_loss = self.NN.predict(self.X_test, self.Y_test)
        return Y_test_predict

    def params(self,p=None):
        """Sets the parameters for the neural net based on the user's choices"""
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
