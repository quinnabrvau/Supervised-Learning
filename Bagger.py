#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fir Mar 2 12:30:18 2018

@author: quinn
"""

from dataSet import dataSet, getIrisData, getWineData
from data import data
from RandomForest import RandomForest
from math import sqrt,ceil
from random import sample, randint
import numpy as np

class Bagger:
    def __init__(self,searcher,train,test,valid,shrink=True):
        if not shrink:
            self.C = searcher(train,test,valid)
            print(self.C)
            return
        foo = ceil(sqrt(len(train[0])-1))
        attributes = [i for i in range(len(train[0])-1)]
        self.atr = sample(attributes,foo)
        self.train = dataSet()
        self.test = dataSet()
        self.valid = dataSet()
        tmp = dataSet()
        for d in train:
            d_ = data()
            for j in self.atr:
                d_.append(d[j])
            d_.append(d[-1])
            tmp.append(d_)
        for d in test:
            d_ = data()
            for j in self.atr:
                d_.append(d[j])
            d_.append(d[-1])
            self.test.append(d_)
        for d in valid:
            d_ = data()
            for j in self.atr:
                d_.append(d[j])
            d_.append(d[-1])
            self.valid.append(d_)
        self.train = tmp.randSubSet(int(len(tmp)/2),True)
        self.train.header    = train.header
        self.train.mut       = train.mut
        self.train.classes   = train.classes
        self.C = searcher(self.train,self.test,self.valid)

    def params(self):
        return self.C.params()

    def build(self,params):
        self.C.build(params)

    def predict(self):
        return self.C.predict()

    def __str__(self): return str(self.C)



class BaggerList(list):
    def __init__(self,searcher,ty="iris",size=100):
        list.__init__(self)
        if   ty=='iris': self.train, self.test, self.valid = getIrisData(1)
        elif ty=='wine': self.train, self.test, self.valid = getWineData(1)
        self.C = searcher
        for i in range(size):
            self.append(Bagger(self.C,self.train,self.test,self.valid,size==1))

    
    def build(self):
        params = self[0].params()
        r = len(self)
        if r>1:print("building a set of operators for boosting")
        else: print("building an operator")
        for i in range(r):
            self[i].build(params)
            if len(self.C)>1:print( "%.2f"%(100*(i+1)/r) ,"percent done")
            else: print("operator built")

    def predict(self):
        guess = []
        actual = []
        for i in range(len(self)):
            guess.append(self[i].predict())
        r = len(self.test)
        for i in range(r):
            
            actual.append(self.test[i][-1])
        foo = np.asarray(guess)
        g = []
        for i in range(len(guess[0])):
            g.append(np.argmax(np.bincount(foo[:,i])))
        # for gu in guess:
        #     print("t",gu)
        # print("g",g)
        # print("a",actual)
        success = 0
        for i in range(len(g)):
            if g[i]==actual[i]:
                success+=1
        return success/len(self.test)


if __name__=="__main__":
    BL = BaggerList(RandomForest,"wine",1)
    # BL = BaggerList(RandomForest,"iris",100)
    BL.build()
    print(BL.predict())


