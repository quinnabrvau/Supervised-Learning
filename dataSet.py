#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 07:53:39 2018

@author: quinn
"""
from math import sqrt
from data import data
from random import sample as rSample
import numpy as np

class dataSet(list):
    """
    class to hold a data set for machine learning alogrithms in a standard way
    expands list with a way to read a  csv, and to print out in a
    format that is readable { [ atributes ] classifier }
    """
    def __init__(self,In=None):
        self.header = data()
        self.max = []
        self.min = []
        self.mean = []
        self.std = []
        self.mut = {}
        self.classes = []
        list.__init__(self)
        if In!=None:
            if isinstance(In,dataSet):
                list.__init__(self, In )
                self.mut = In.mut
                self.classes = In.classes
                self.header = In.header
            elif isinstance(In,list):
                list.__init__(self, In )
            elif isinstance(In,str):
                self.read(In)
            else:
                return
            self.findMinMax()
            self.findClasses()
            

    def findClasses(self):
        self.classes = []
        for i in range(len(self)):
            if self[i][-1] not in self.classes:
                self.classes.append(self[i][-1])
            
    def __str__(self):
        """prints the data in readable format"""
        out = str(self.header)+"\n"
        for d in self:
            out += str(d)+"\n"
        if len(self.max):
            r1 = "++++["
            r2 = "----["
            r3 = "mean["
            r4 = "std ["
            for i in range(len(self.max)):
                r1 += "%.2f" % self.max[i] + "\t, "
                r2 += "%.2f" % self.min[i] + "\t, "
                r3 += "%.2f" % self.mean[i] + "\t, "
                r4 += "%.2f" % self.std[i] + "\t, "
            out += r1[:-3]+"\t]\n"+r2[:-3]+"\t]\n"+r3[:-3]+"\t]\n"+r4[:-3]+"\t]\n"
        if len(self.classes):
            out += "classes: "
            for c in self.classes:
                out += str(c) + ", "
            out = out[:-2]
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
        """finds the minimum, maximum, mean, and stanard deviation for each attribute"""
        self.max = self[0].attributes()
        self.min = self[0].attributes()
        self.mean = [0 for i in self[0].attributes()]
        self.std = [i*i for i in self[0].attributes()]
        for i in range(1,len(self)):
            d = self[i]
            for j in range(len(d)-1):
                if d[j]>self.max[j]:
                    self.max[j] = d[j]
                elif d[j]<self.min[j]:
                    self.min[j] = d[j]
                self.mean[j]+=d[j]
        for j in range(len(self[0])-1):
            self.mean[j]/=len(self)
        for i in range(1,len(self)):
            d = self[i]
            for j in range(len(d)-1):
                self.std[j] += (d[j]-self.mean[j])**2
        for j in range(len(self[0])-1):
            self.std[j]/=len(self)
            if self.std[j]<0: self.std[j]=0
            self.std[j] =sqrt(self.std[j])

    def normRange(self,small,large):
        scalarM = self[0].attributes()
        for j in range(len(self.max)):
            scalarM[j] = (large-small)/(self.max[j]-self.min[j])
        for i in range(len(self)):
            for j in range(len(self[i])-1):
                self[i][j] = (self[i][j]-self.min[j])*scalarM[j]+small
        self.findMinMax()

    def normStd(self,mean=None,std=None):
        if mean==None:
            mean=self.mean
        if std==None:
            std=self.std
        for i in range(len(self)):
            for j in range(len(self[i])-1):
                self[i][j] -= mean[j]
                self[i][j] /= std[j]
        self.findMinMax()

    def devide(self,split):
        for i in range(len(self)):
            for j in range(len(self[i])-1):
                if self[i][j]>split:
                    self[i][j]=1
                else:
                    self[i][j]=0
        self.findMinMax()

    def strings2Ints(self,mut=None):
        if mut!=None:
            self.mut = mut
        k = 0
        self.mut = {}
        for i in range(len(self)):
            for j in range(len(self[i])):
                if isinstance(self[i][j],str):
                    if self[i][j] not in self.mut.keys():
                        if j == len(self[i])-1:
                            self.classes.append(k)
                        self.mut[self[i][j]] = k
                        self.mut[i] = self[i][j]
                        self[i][j] = k
                        k+=1
                    else:
                        self[i][j] = self.mut[self[i][j]]
        self.findClasses()

    def getString(self,val):
        return self.mut[val]

    def randSubSet(self,k=25):
        """returns a random sub set of size k from the data set"""
        out = dataSet()
        out.header = self.header
        out.extend(rSample(self,k))
        out.findMinMax()
        out.strings2Ints()
        out.findClasses()
        out.mut = self.mut
        return out

    def splitAttribute(self,atr,divider=0.5):
        big = dataSet()
        lit = dataSet()
        for i in range(len(self)):
            if self[i][atr] > divider:
                big.append(self[i])
            else:
                lit.append(self[i])
        big.header = self.header
        big.mut = self.mut
        lit.header = self.header
        lit.mut = self.mut
        return [big, lit]


if __name__=="__main__":
    dS = dataSet("wineValidData.csv")
    # print(dS)
    new_dS = dS.randSubSet(25)
    print(new_dS)
    print(np.asarray(dS))
    new_dS.normRange(-1,1)
    print(new_dS)
    new_dS = dS.randSubSet(25)
    new_dS.normStd()
    print(new_dS)
    new_dS.devide(0)
    print(new_dS)
    
    
    
    