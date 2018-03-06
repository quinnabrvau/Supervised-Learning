"""Bagger.py by Quinn Abrahams-Vaughn (UWNetID: abrahq)
in partnership with Shannon Ladymon (UWNetID: sladymon)

CSE 415 Winter 2018
Final Project

Bagger and BaggerList objects
"""

from dataSet import dataSet, getIrisData, getWineData
from data import data
from TreeDriver import TreeDriver
from Report import Report
from math import sqrt, ceil
from random import sample
import numpy as np
from time import time


class Bagger:
    def __init__(self, searcher, train, test, valid, shrink=True, report=None,p=None):
        """initializes an agent"""
        if report != None: self.REPORT = report
        else: self.REPORT = {}
        if not shrink:
            self.C = searcher(train, test, valid,p)
            return
        foo = ceil(sqrt(len(train[0]) - 1))
        attributes = [i for i in range(len(train[0]) - 1)]
        self.atr = sample(attributes, foo)
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
        sub_size = 200
        if sub_size > len(tmp):
            sub_size=int(len(tmp)/2)
        self.train = tmp.randSubSet(sub_size, True)
        self.train.header = train.header
        self.train.mut = train.mut
        self.train.classes = train.classes
        self.C = searcher(self.train, self.test, self.valid,p)

    def params(self, p=None):
        """sets and gets params for an agent"""
        return self.C.params(p)

    def build(self, params):
        """trains an agent"""
        self.C.build(params, self.REPORT)

    def predict(self):
        """guesses the classes for the test data, returns a list of guesses"""
        return self.C.predict()

    def __str__(self):
        """returns the string of the class"""
        return str(self.C)


class BaggerList(list):
    """list class to hold all of the bagged agent"""
    def __init__(self, searcher, ty="iris", size=100, report=None,p=None):
        start = time()
        if report != None: self.REPORT = report
        else: self.REPORT = {}
        list.__init__(self)
        if ty == 'iris' or ty == 'i':
            self.train, self.test, self.valid = getIrisData(1)
            tr, te, v = getIrisData(0)
        elif ty == 'wine' or ty == 'w':
            self.train, self.test, self.valid = getWineData(1)
            tr, te, v = getWineData(0)
        self.REPORT['datasetTrainSize'] = str(len(self.train))
        self.REPORT['datasetTestSize'] = str(len(self.test))
        self.REPORT['datasetValidSize'] = str(len(self.valid))

        self.REPORT['input']    =str(        tr.print_short())
        self.REPORT['inputData']=str(        tr.print_stats())
        self.REPORT['inputNorm']=str(self.train.print_short())
        self.C = searcher
        for i in range(size):
            self.append(
                Bagger(self.C, self.train, self.test, self.valid, size != 1,report,p))
        if p!=None:
            self.p = p
        self.REPORT['openTime'] = "%.4f" % ((time() - start))

    def params(self, p=None):
        """gets and sets params for the bagged agent"""
        for i in (range(len(self))):
            x = self[i].params(p)
            if x != None:
                p = x
        self.p = p

    def build(self):
        """trains all of the agents"""
        start = time()
        r = len(self)
        if r > 1: print("building a set of agents for bagging")
        else: print("building an agent")
        for i in range(r):
            self[i].build(self.p)
            if len(self) > 1:
                print("%.2f" % (100 * (i + 1) / r), "percent done")
        if len(self) > 1: print("agents built")
        else: print("agent built")
        self.REPORT['buildTime'] = "%.4f" % ((time() - start))

    def predict(self):
        """guesses the classes for the test data and returns the accuracy success/total"""
        start = time()
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
            g.append(np.argmax(np.bincount(foo[:, i])))
        success = 0
        self.REPORT['output']='predict, actual, correct\n'
        for i in range(len(g)):
            self.REPORT['output'] += str(g[i])+"\t "+str(actual[i])+"\t "
            if g[i] == actual[i]:
                success += 1
                self.REPORT['output'] += 'correct\n'
            else:
                self.REPORT['output'] += "wrong\n"
        self.REPORT['predictTime'] = "%.4f" % ((time() - start))
        self.REPORT['predictAccuracy'] = "%.3f" % (
            100 * success / len(self.test))
        return success / len(self.test)


if __name__ == "__main__":
    BL = BaggerList(TreeDriver, "wine", 1)
    # BL = BaggerList(TreeDriver,"iris",100)
    BL.build()
    print(BL.predict())
