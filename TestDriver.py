""""TestDriver.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Test Driver to use in testing our learning agents
"""

import csv
import numpy as np

if __name__ == "__main__":



    # get wine training data into an numpy array
    train_reader = csv.reader(open('wineTrainDataUpdated.csv'))

    # l = list(train_reader)
    # print(len(l))
    # print(l[0])
    # print(len(l[0]))
    # print(l[0][1])
    # print("----choochoo-----")
    # train_data = np.asarray(l)
    # print(train_data.shape)
    # print(train_data[0])
    # print(type(train_data[0]))
    # print(train_data[0][1])
    # print("---eggs---")
    # eggs = train_data[:][:-2]
    # print(eggs.shape)
    # print(eggs[0])
    # print(eggs[0][1])


    train_data = np.asarray(list(train_reader))

    # TODO: Delete after testing
    print(train_data.shape)
    print(train_data[42][3])

    # Create matrix of samples and their attributes
    # leaving off the first row with the column names
    # and the last two columns, which hold the classification and an empty row
    X = train_data[1:][:-2]

    print(X[0])



    # TODO: Delete after testing
    # print(X.shape)
    # row_length = 0
    # for i in range(X.shape[0]):
    #     if len(X[i]) > row_length:
    #         row_length = len(X[i])
    #         print("Changing length to ", len(X[i]))
    #     if len(X[i]) < row_length:
    #         print("This row's length= ", len(X[i]), " is less than the row_length: ", row_length)



