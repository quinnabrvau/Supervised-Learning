"""RandomForest.py by Quinn Abrahams-Vaughn (UWNetID: abrahq)
in partnership with Shannon Ladymon (UWNetID: sladymon)

CSE 415 Winter 2018
Final Project

Builds a RandomForest class that wraps a Decision tree in a standard method
reference: https://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/
"""

from dataSet import getIrisData, getWineData
from DecisionTree import DecisionTree, findApproxDepth
from Report import Report


class RandomForest:
    def __init__(self, train, test, valid,p):
        self.train, self.test, self.valid = train, test, valid
        self.tree = DecisionTree(train)

    def params(self, p=None):
        if p == None or p == (0, 0) or len(p) < 2:
            p = findApproxDepth(self.train, self.valid)[:2]
        elif p[0] == 0:
            p = (findApproxDepth(self.train, self.valid, 0, p[1])[0], p[1])
        elif p[1] == 0:
            p = (p[0], findApproxDepth(self.train, self.valid, p[0], 0)[1])
        return p[0:2]

    def build(self, params=None, rep=None):
        mD = 4
        mS = 10
        if params != None:
            if rep != None:
                rep['treeDepth'] = params[0]
                rep['treeMinSize'] = params[1]
            mD = params[0]
            mS = params[1]
        self.tree.buildTree(mD, mS, True)

    def predict(self):
        out = []
        for d in self.test:
            out.append(self.tree.searchTree(d))
        return out

    def __str__(self):
        return str(self.tree)


if __name__ == "__main__":
    # train, test, valid = getWineData(1)
    train, test, valid = getIrisData(1)
    rf = RandomForest(train, test, valid)
    params = rf.params()
    print(params)
    rf.build(params)
    acc = rf.predict()
    print(acc)
    #print("acuracy:", ("%.2f" % (100*acc)) +"%"  )
