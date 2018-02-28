#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:22:14 2018

@author: quinn
"""
from random import shuffle as rShuffle

def convert_data(fileName):
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
        line_split = line_.split(";")
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


redFile = "winequality-red.csv"
whiteFile = "winequality-white.csv"
trainFile = "wineTrainData.csv"
validFile = "wineValidData.csv"
testFile  = "wineTestData.csv"


if __name__=="__main__":
    (header,trD, vD, teD) = convert_data(redFile)
    # (ignore,trDw, vDw, teDw) = convert_data(redFile,"w")
    # trD = trDr + trDw
    # vD  = vDr + vDw
    # teD = teDr + teDw
    # rShuffle(trD)
    # rShuffle(teD)
    # rShuffle(vD)
    print(len(vD),len(trD),len(teD))
    print(vD)
    save_data(trainFile,trD,header)
    save_data(validFile,vD,header)
    save_data(testFile,teD,header)

