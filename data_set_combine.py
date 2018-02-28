#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:22:14 2018

@author: quinn
"""
from random import shuffle as rShuffle

def convert_data(fileName,div=";"):
    num_lines = sum(1 for line in open(fileName))
    data = open(fileName)
    testing = int(num_lines*0.2)
    valid = int(num_lines*0.1)
    training = num_lines-testing-valid
    trD = []
    vD = []
    teD = []
    header = ""
    i = 0
    D = []
    for line in data:
        line_ = line.strip("\n")
        line_split = line_.split(div)
        if i < 1:
            header = line_split
        else:
            D.append(line_split)
        i+=1
    i = 0
    rShuffle(D)
    for line in D:
        if i < training:
            trD.append(line)
        elif i < training+valid:
            vD.append(line)
        else:
            teD.append(line)
        i+=1
    data.close()
    return (header,trD,vD,teD)

def save_data(fileName,data,header):
    file = open(fileName,"w")
    out = ""
    for ele in header:
        out += str(ele)+","
    file.write(out[:-1]+"\n")
    
    for line in data:
        out = ""
        for ele in line:
            out += str(ele)+","
        file.write(out[:-1]+"\n")
    file.close()

def combine(fileName,div,fileRoot):
    trainFile = fileRoot+"TrainData.csv"
    validFile = fileRoot+"ValidData.csv"
    testFile  = fileRoot+"TestData.csv"
    (header,trD, vD, teD) = convert_data(fileName,div)
    save_data(trainFile,trD,header)
    save_data(validFile,vD,header)
    save_data(testFile,teD,header)


if __name__=="__main__":
    combine("winequality-red.csv",";","wine")
    combine("iris.csv",",","iris")
    

