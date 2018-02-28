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

class DecisionTree(dataSet):
    def __init__(self,dS = None,atr = None):
        if dS == None or len(dS) == 0:
            dataSet.__init__(self)
        else:
            dataSet.__init__(self,dS)
        self.children = []
        if atr != None:
            self.atr = [i for i in atr]
        else:
            self.atr = []
        self.v = 0
        self.i = -1

    def isLeaf(self):
        if self == None or len(self)==0 :
            return True
        if len(self.atr)==(len(self[0])-1):
            self.v = self.mostCommon()
            return True
        for d in self:
            #print(d)
            if d[-1] != self[0][-1]:
                #print("false")
                return False
        self.v = self[0][-1]
        return True

    def mostCommon(self):
        com = {}
        for i in range(len(self)):
            if self[i][-1] in com.keys():
                com[self[i][-1]]+=1
            else:
                com[self[i][-1]] =1
        i,v = 0,0
        for key in com.keys():
            if com[key]>v:
                i,v = key,com[key]
        return i

    def buildTree(self,n=0):
        if n==0:
            print("building tree:")
            self.children = []
        self.i,self.v,gr,s = self.getSplit()
        self.atr.append(self.i)
        for g in gr:
            self.children.append(DecisionTree(g,self.atr))
        for c in self.children:
            if not c.isLeaf():
                c.buildTree(n+1)
        if n==0:
            print("tree built")

    def printTree(self,n=0):
        if self.isLeaf():
            if self==None or len(self)==0:
                print(".."*n,"NULL",sep=' < ')
            else:
                try:
                    print(".."*n,self.getString(self.v),sep='')
                except:
                    print(".."*n,self.v,sep='')
        else:
            print(".."*n,"index",self.i,"value < ",self.v,sep='')
            for c in self.children:
                c.printTree(n+1)
        if n == 0:
            i = self.mostCommon()
            try:
                print(self.getString(i))
            except:
                print(i)

    def searchTree(self,d,n=0):
        if n==0 and self.i==-1:
            self.buildTree()
        if self.isLeaf():
            if self==None or len(self)==0:
                return None
            else:
                return self.v
        else:
            val = None
            if d[self.i] > self.v:
                val = self.children[0].searchTree(d,n+1)
            else:
                val = self.children[1].searchTree(d,n+1)
            if val != None:
                return val
        if n:
            return None
        return self.mostCommon()

    def giniIndex(self,groups):
        gini = 0.0
        for g in groups:
            if len(self)==0: return 0
            props = {}
            for c in self.classes:
                props[c] = 0
            for i in range(len(g)):
                props[ g[i][len(g[i])-1] ] += 1
            for i in range(len(g)):
                props[ g[i][len(g[i])-1] ] /= len(g)
            score = 0
            for c in self.classes:
                score += props[c] * props[c]
            gini += (1-score)*len(g)/len(self)
        return gini

    def getSplit(self):
        b_index, b_value, b_score, b_groups = 999, 999, 999, None
        for j in range(len(self[0])-1):
            if j in self.atr:
                continue
            for i in range(len(self)):
                groups = self.splitAttribute(j,self[i][j]) # [big, little]
                gini = self.giniIndex(groups)
                if gini < b_score:
                    b_index, b_value, b_score, b_groups = j, self[i][j], gini, groups
        return b_index, b_value, b_groups, b_score

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
    tree = DecisionTree(train.randSubSet(100))
    tree.buildTree()
    print(tree)
    print(tree.mut)
    tree.printTree()
    #print(dS)
    errorE = 0
    successE = 0
    for d in test:
        r = tree.searchTree(d)
        #print("guess:",r,"actual:",d.classifier())
        if r==d.classifier():
            successE+=1
        else:
            errorE+=1
    print("success:",successE,"error:",errorE,"acuracy:", ("%.2f" % (100*(successE/(errorE+successE)))) +"%"  )







