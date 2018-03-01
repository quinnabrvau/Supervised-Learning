#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:27:14 2018

@author: quinn
"""

from dataSet import dataSet, getIrisData, getWineData
from DecisionTree import DecisionTree

class RandomForest(list):
    def __init__(self,ty="iris",le=80,s=None):
        self.train, self.test, self.valid = None,None,None
        if   ty=='iris': self.train, self.test, self.valid = getIrisData(1)
        elif ty=='wine': self.train, self.test, self.valid = getWineData(1)
        if s==None: s=int(len(self.train)*10/le)
        self.sub_size = s
        print("size of sub sets",self.sub_size)
        list.__init__( self )
        print("building random sub sets")
        for i in range(le):
            self.append(DecisionTree(self.train.randSubSet(self.sub_size,True)))
        self.buildForest()

    def buildForest(self):
        print("building forests")
        mD = len(self.train[0].attributes())*2
        mS = int(self.sub_size/20)+1
        for i in range(len(self)):
            # if i%int(len(self)/10)==0: print( "%.2" % 100*i/len(self)  , "%  built",sep="")
            self[i].buildTree(mD,mS,True)
        print("forest built")

    def searchForest(self,d):
        p = []
        print("searching forest")
        for i in range(len(self)):
            # if i%int(le/10)==0:print( "%.2" % 100*i/le , "%  searcherd",sep="")
            p.append(self[i].searchTree(d))
        print("search complete")
        return max(set(p),key=p.count )

    def getString(self,r):
        return self.train.getString(r)


if __name__=="__main__":
    rf = RandomForest('wine',20,60)
    error,success = 0,0
    for d in rf.test:
        r = rf.searchForest(d)
        print(d,"?=",r)
        if r==d.classifier():
            success+=1
        else:
            error+=1
    print("success:",success,"error:",error,"acuracy:", ("%.2f" % (100*(success/(error+success)))) +"%"  )
        




