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

class RandomForest(list):
    def __init__(self,ty="iris",le=80,s=None):
        self.train, self.test, self.valid = None,None,None
        if   ty=='iris': self.train, self.test, self.valid = getIrisData(1)
        elif ty=='wine': self.train, self.test, self.valid = getWineData(1)
        if s==None: s=int(len(self.train)*10/le)
        self.sub_size = s
        self.le = le
        print("size of sub sets",self.sub_size)
        list.__init__( self )        
        self.buildForest()

    def buildForest(self):
        print("building forests")
        attributes = [i for i in range(len(self.train[0])-1)]
        foo = ceil(sqrt(len(attributes))) #number of attributes to use
        mD,mS,a = findApproxDepth(self.train,self.valid)
        while (len(self)<self.le):
            tree = (DecisionTree(self.train.randSubSet(self.sub_size,True)))
            atr = sample(attributes,foo)
            # mD = randint(2,(len(self.train[0])-1)*3)
            # mS = randint(2,(len(self.train[0])-1)*2)
            tree.buildTreeFor(mD,mS,atr,True)
            if tree.testTree(self.train)>0.50:
                self.append(tree)
                print( "%.2f" % (100*len(self)/self.le),"percent built")
        print("forest built")

    def searchForest(self,d,shhh=False):
        p = []
        if not shhh: print("searching forest")
        for i in range(len(self)):
            # if i%int(le/10)==0:print( "%.2" % 100*i/le , "%  searcherd",sep="")

            p.append(self[i].searchTree(d))
        if not shhh: print("search complete")
        return max(set(p),key=p.count )

    def testForest(self):
        total,success = 0,0
        for d in self.test:
            r = self.searchForest(d,True)
            if r==d.classifier():
                success+=1
            total+=1
        return success/total

    def getString(self,r):
        return self.train.getString(r)


if __name__=="__main__":
    rf = RandomForest('iris',400,200)
    acc = rf.testForest()
    print("acuracy:", ("%.2f" % (100*acc)) +"%"  )
        




