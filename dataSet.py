#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 07:53:39 2018

@author: quinn
"""
from data import data
from random import sample as rSample
import numpy as np

class dataSet(list):
    """
    class to hold a data set for machine learning alogrithms in a standard way
    expands list with a way to read a  csv, and to print out in a
    format that is readable { [ atributes ] classifier }
    """
    def __init__(self,fileName=None):
        self.header = data()
        self.max = []
        self.min = []
        list.__init__(self)
        if fileName!=None:
            self.read(fileName)
            self.findMinMax()
            
    def __str__(self):
        """prints the data in readable format"""
        out = str(self.header)+"\n"
        for d in self:
            out += str(d)+"\n"
        out += "++"+str(self.max)+"\n"
        out += "--"+str(self.min)+"\n"
        return out
        
    def read(self,fileName):
        """reads a csv into the data set"""
        i = 0
        file = open(fileName)
        for line in file:
            if len(line)<=1:
                pass
            elif i >= 1:
                self.append(data(line))
            else:
                self.header = data(line)
            i|=1
        file.close()
    
    def findMinMax(self):
        """finds the minimum and maximum value for each attribute"""
        self.max = self[0].attributes()
        self.min = self[0].attributes()
        for i in range(1,len(self)):
            d = self[i]
            for j in range(len(d)-1):
                if d[j]>self.max[j]:
                    self.max[j] = d[j]
                elif d[j]<self.min[j]:
                    self.min[j] = d[j]

    def randSubSet(self,k=25):
        """returns a random sub set of size k from the data set"""
        out = dataSet()
        out.header = self.header
        out.extend(rSample(self,k))
        out.findMinMax()
        return out
    
if __name__=="__main__":
    dS = dataSet("wineValidData.csv")
    print(dS)
    new_dS = dS.randSubSet(25)
    print(new_dS)
    print(np.asarray(dS))

    
    
    
    