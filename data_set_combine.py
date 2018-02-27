#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:22:14 2018

@author: quinn
"""
from random import shuffle as rShuffle

def convert_data(fileName,classifier):
    C = [classifier]
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
    for line in data:
        line_ = line.strip("\n")
        line_split = line_.split(";")
        if i < 1:
            header = line_split
        elif i < training:
            trD.append(line_split+C)
        elif i < training+valid:
            vD.append(line_split+C)
        else:
            teD.append(line_split+C)
        i+=1
    data.close()
    return (header,trD,vD,teD)


redFile = "winequality-red.csv"
whiteFile = "winequality-white.csv"
trainFile = "wineTrainData.csv"
validFile = "wineValidData.csv"
testFile  = "wineTestData.csv"


if __name__=="__main__":
    (header,trDr, vDr, teDr) = convert_data(redFile,"r")
    (ignore,trDw, vDw, teDw) = convert_data(redFile,"w")
    trD = trDr + trDw
    vD  = vDr + vDw
    teD = teDr + teDw
    rShuffle(trD)
    rShuffle(teD)
    rShuffle(vD)
    
    file = open(trainFile,"w")
    for ele in header:
        file.write(ele+",")
    file.write("color\n")
    for line in trD:
        for ele in line:
            file.write(ele+",")
        file.write("\n")
    file.close()
    file = open(validFile,"w")
    for ele in header:
        file.write(ele+",")
    file.write("color\n")
    for line in vD:
        for ele in line:
            file.write(ele+",")
        file.write("\n")
    file.close()
    file = open(testFile,"w")
    for ele in header:
        file.write(ele+",")
    file.write("color\n")
    for line in teD:
        for ele in line:
            file.write(ele+",")
        file.write("\n")
    file.close()
