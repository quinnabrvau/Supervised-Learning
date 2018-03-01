#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:48:26 2018

@author: quinn
reference: https://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/
"""
from dataSet import dataSet, getIrisData, getWineData
from data import data
from math import sqrt

NN=5 #MAX DEPTH
MM=3 #MIN SIZE

class DecisionTree(dataSet):
    def __init__(self,dS = None,atr = None):
        if dS == None or len(dS) == 0:
            dataSet.__init__(self)
        else:
            dataSet.__init__(self,dS)
        self.lt = None
        self.gt = None
        if atr != None:
            self.atr = [i for i in atr]
        else:
            self.atr = []
        self.v = 0
        self.i = -1

    def mostCommon(self):
        d = [r[-1] for r in self]
        return max(set(d),key=d.count )

    def searchTree(self,d):
        """self, d(data to predict with), n(depth)"""
        return searchTreeF(self,d)

    def split(self,mD,mS,depth=0):
        print(depth)
        self.i, self.v, groups, score = self.getSplit()
        #print(len(groups),groups[0],groups[1])
        self.lt, self.gt = groups[0], groups[1]
        if self.lt==None or self.gt==None:
            print("NULL")
            self.lt = self.gt = self.mostCommon()
            return
        if depth>mD:
            print("MAX DEPTH")
        if len(self.lt) <= mS or depth>mD:
            if len(self.lt)==0: self.lt=self.mostCommon()
            else: self.lt=self.lt.mostCommon()
        else:
            self.lt.split(mD,mS,depth+1)
        if len(self.gt) <= mS or depth>mD:
            if len(self.gt)==0: self.gt=self.mostCommon()
            else: self.gt=self.gt.mostCommon()
        else:
            self.gt.split(mD,mS,depth+1)

    def buildTree(self):
        print("building tree:")
        self.split(NN,MM)
        print("tree built")

    def giniIndex(self,groups):
        n = sum([len(g) for g in groups])
        gini = 0.0
        for g in groups:
            if len(g)==0: continue
            score = 0
            for c in self.classes:
                p = [r[-1] for r in g].count(c)/len(g)
                score += p*p
            gini += (1-score)*len(g)/n
        return gini

    def getSplit(self):
        b_index, b_value, b_score, b_groups = 999, 999, 999, None
        for j in range(len(self[0])-1):
            if j in self.atr:
                continue
            for i in range(len(self)):
                groups = self.splitAttribute(j,self[i][j]) # lit, big
                gini = self.giniIndex(groups)
                if gini < b_score:
                    b_index, b_value, b_score, b_groups = j, self[i][j], gini, groups
        return b_index, b_value, b_groups, b_score

    def splitAttribute(self,atr,divider=0.5):
        big, lit = DecisionTree(), DecisionTree()
        for d in self:
            if d[atr] > divider: big.append(d)
            else:                lit.append(d)
        big.header, big.mut = self.header, self.mut
        lit.header, lit.mut = self.header, self.mut
        return lit, big

    def printTree(self):
        printTreeF(self,0,self)

def printTreeF(node,n,root):
    if isinstance(node,DecisionTree):
        print(".."*n,"[atr ",node.i," < ",node.v,"]",sep='')
        printTreeF(node.lt,n+1,root)
        printTreeF(node.gt,n+1,root)
    else:
        print(".."*n,root.getString(node),sep='')

def searchTreeF(node,d):
    if isinstance(node,DecisionTree):
        if d[node.i] < node.v:
            return searchTreeF(node.lt,d)
        else:
            return searchTreeF(node.gt,d)
    else:
        return node
    

if __name__=="__main__":
    # f = "wine"
    # dS = dataSet(f+"TrainData.csv")
    # mean = [i for i in dS.mean]
    # std = [i for i in dS.std]
    # dS.normStd()
    # dS.strings2Ints()
    # dSs = dS.randSubSet(200)
    # tree = DecisionTree(dSs)
    # print(tree)
    # i,v,g,s = tree.getSplit()
    # print("index",i)
    # print("value",v)
    # print("score",s)
    # for G in g:
    #     print("new group")
    #     print(G)

    # tree.buildTree()
    # #print(tree.isLeaf())
    # print("\n\n\n")
    # tree.printTree()
    # dS = dataSet(f+"TestData.csv")
    # # dS = dS.randSubSet(25)
    # # print(tree.mean)
    # # print(tree.std)
    # # print(dS.mean)
    # # print(dS.std)
    # dS.normStd(mean,std)
    # dS.strings2Ints(tree.mut)
    #train, test, valid = getIrisData()
    train, test, valid = getWineData()
    e = 99999
    for i in range(1):
        tree = DecisionTree(train.randSubSet(200))
        tree.buildTree()
        # print(tree)
        # print(tree.mut)
        tree.printTree()
        # print(dS)
        errorE = 0
        successE = 0
        for d in test:
            r = tree.searchTree(d)
            print("guess:",r,"actual:",d.classifier())
            if r==d.classifier():
                successE+=1
            else:
                errorE+=1
            print("success:",successE,"error:",errorE,"acuracy:", ("%.2f" % (100*(successE/(errorE+successE)))) +"%"  )
        if errorE < e:
            e = errorE
    print("best error",e)






