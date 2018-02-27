""""TestDriver.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Test Driver to use in testing our learning agents
"""

import csv
import numpy as np

if __name__ == "__main__":

    # read the csv files and put wine data into numpy ndarrays
    train_reader = csv.reader(open('wineTrainData.csv'))
    test_reader = csv.reader(open('wineTestData.csv'))
    valid_reader = csv.reader(open('wineValidData.csv'))

    train_data = np.asarray(list(train_reader))
    test_data = np.asarray(list(test_reader))
    valid_data = np.asarray(list(valid_reader))

    # Create numpy ndarray matrices of samples and their attributes
    # leaving off the first row with the column names
    # and the last two columns, which hold the classification and an empty row
    X_train = train_data[1:, :-2]
    X_test = test_data[1:, :-2]
    X_valid = valid_data[1:, :-2]

    # Create numpy ndarray vectors for the classifications for the samples
    # with 0 for red, and 1 for white
    Y_train = np.asarray([int(row[-2] == 'w') for row in train_data[1:]])
    Y_test = np.asarray([int(row[-2] == 'w') for row in test_data[1:]])
    Y_valid = np.asarray([int(row[-2] == 'w') for row in valid_data[1:]])





