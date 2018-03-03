#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:27:14 2018

@author: quinn
"""

from dataSet import dataSet, getIrisData, getWineData
from DecisionTree import DecisionTree, findApproxDepth
from random import sample, randint
from math import sqrt,ceil

class RandomForest:
    def __init__(self,train,test,valid):
        self.train,self.test,self.valid = train,test,valid
        self.tree = DecisionTree(train)

    def params(self):
        return findApproxDepth(self.train,self.valid)[:2]

    def build(self,params=None,Report=None):
        if Report!=None:
            Report['treeDepth']  =str(params[0])
            Report['treeMinSize']=str(params[1])
        mD = 4
        mS = 10
        if params != None:
            mD = params[0]
            mS = params[1]
        self.tree.buildTree(mD,mS,True)

    def predict(self):
        out = []
        for d in self.test:
            out.append(self.tree.searchTree(d))
        return out

    def __str__(self):
        return str(self.tree)



if __name__=="__main__":
    # train, test, valid = getWineData(1)
    train, test, valid = getIrisData(1)
    rf = RandomForest(train,test,valid)
    params = rf.params()
    print(params)
    rf.build(params)
    acc = rf.predict()
    print(acc)
    #print("acuracy:", ("%.2f" % (100*acc)) +"%"  )
        




