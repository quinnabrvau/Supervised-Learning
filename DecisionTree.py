"""DecisionTree.py by Quinn Abrahams-Vaughn (UWNetID: abrahq)
in partnership with Shannon Ladymon (UWNetID: sladymon)

CSE 415 Winter 2018
Final Project

Builds a DecisionTree
reference: https://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/
"""
from dataSet import dataSet, getIrisData, getWineData
from data import data
from math import sqrt
from random import randint

NN = 20  #MAX DEPTH
MM = 3  #MIN SIZE


class DecisionTree(dataSet):
    def __init__(self, dS=None, atr=None):
        if dS == None or len(dS) == 0:
            dataSet.__init__(self)
        else:
            dataSet.__init__(self, dS)
        self.lt = None
        self.gt = None
        if atr != None:
            self.atr = [i for i in atr]
        else:
            self.atr = []
        self.v = 0
        self.i = -1

    def mostCommon(self):
        """returns the most common class in a given data set"""
        d = [r[-1] for r in self]
        return max(set(d), key=d.count)

    def searchTree(self, d):
        """searches a tree for the class of given attributes d"""
        return searchTreeF(self, d)

    def split(self, mD, mS, depth=0):
        """splits a tree into two trees lt - less than, gt - greater than
        Then the program recursively searches the new trees"""
        self.i, self.v, groups, score = self.getSplit()
        if groups == None:
            return
        self.lt, self.gt = groups[0], groups[1]
        self.lt.atr.append((self.i, "%.1f" % self.v))
        self.gt.atr.append((self.i, "%.1f" % self.v))
        self.gt.header, self.gt.mut = self.header, self.mut
        self.lt.header, self.lt.mut = self.header, self.mut
        if self.lt == None or self.gt == None:
            self.lt = self.gt = self.mostCommon()
            return
        if len(self.lt) <= mS or depth > mD:
            if len(self.lt) == 0: self.lt = self.mostCommon()
            else: self.lt = self.lt.mostCommon()
        else:
            self.lt.split(mD, mS, depth + 1)
        if len(self.gt) <= mS or depth > mD:
            if len(self.gt) == 0: self.gt = self.mostCommon()
            else: self.gt = self.gt.mostCommon()
        else:
            self.gt.split(mD, mS, depth + 1)

    def buildTree(self, mD=NN, mS=MM, shhh=False):
        """builds a tree, finds the split for the root and proceeds recursively"""
        if not shhh: print("building tree:")
        self.split(mD, mS)
        if not shhh: print("tree built")

    def giniIndex(self, groups):
        """finds the gini index for a given split, the gini index is a measure of
        how evenly distributed resources are in set. The smaller the value, the more
        even and the better the place to split a tree"""
        n = sum([len(g) for g in groups])
        gini = 0.0
        for g in groups:
            if len(g) == 0: continue
            score = 0
            for c in self.classes:
                p = [r[-1] for r in g].count(c) / len(g)
                score += p * p
            gini += (1 - score) * len(g) / n
        return gini

    def getSplit(self):
        """finds where to split a node in the tree. Tries all values given for all attributes"""
        b_index, b_value, b_score, b_groups = 999, 999, 999, None
        for j in range(len(self[0]) - 1):
            for i in range(len(self)):
                groups = self.splitAttribute(j, self[i][j])  # lit, big
                gini = self.giniIndex(groups)
                if gini < b_score and (j, "%.1f" % self[i][j]) not in self.atr:
                    b_index, b_value, b_score, b_groups = j, self[i][
                        j], gini, groups
        return b_index, b_value, b_groups, b_score

    def splitAttribute(self, atr, divider=0.5):
        """splits a data set by attribute atr and value divider"""
        big, lit = DecisionTree(None, self.atr), DecisionTree(None, self.atr)
        for d in self:
            if d[atr] > divider: big.append(d)
            else: lit.append(d)
        return lit, big

    def printTree(self):
        """prints the tree in a neat format"""
        printTreeF(self, 0, self)

    def testTree(self, valid):
        """calls the test tree function"""
        return testTreeF(self, valid)


def printTreeF(node, n, root):
    """prints the tree in a neat format"""
    if isinstance(node, DecisionTree):
        print(".." * n, "[atr ", node.i, " < ", "%.2f" % node.v, "]", sep='')
        printTreeF(node.lt, n + 1, root)
        printTreeF(node.gt, n + 1, root)
    else:
        print(".." * n, root.getString(node), sep='')


def searchTreeF(node, d):
    """recursively searches the tree for the class of given data d"""
    if isinstance(node, DecisionTree):
        if node.i == 999: return node.mostCommon()
        if d[node.i] < node.v:
            return searchTreeF(node.lt, d)
        else:
            return searchTreeF(node.gt, d)
    else:
        return node


def testTreeF(node, test):
    """checks the accuracy of a tree against the test data"""
    total = len(test)
    success = 0
    for d in test:
        i = searchTreeF(node, d)
        if i == d[-1]:
            success += 1
    return success / total


def findApproxDepth(train, valid, mD=0, mS=0):
    """tries and find a near optimal depth and min size to build a tree to"""
    print(
        "Building a random set of small trees to geuss the max depth and min set size values"
    )
    res = []
    tree = DecisionTree(train.randSubSet(120, True))
    r = 10
    s = 3
    if mD != 0:
        s = mD - 1
        r = 1
    for i in range(
            s,
            r + s,
    ):
        depth = i + 1  # depth = randint(2,(len(train[0])-1)*3)
        a = 2
        b = 15
        if mS != 0:
            a = mS
            b = mS + 1
        for min_size in range(a, b, 2):
            # min_size = randint(2,(len(train[0])-1)*2)
            tree.buildTree(depth, min_size, True)
            acc = testTreeF(tree, valid)
            res.append([depth, min_size, acc])
        print("%.2f" % (100 * (i - s + 1) / r), "percent done")
    best = max(res, key=lambda r: r[-1])
    # res.sort(key=lambda r: r[-1])
    # for r in res:
    #     print(r)
    print("found a depth of", best[0], "and min size of", best[1])
    return best


def guessTreeOpt(train, test, valid):
    """test function for decision tree class"""
    best = findApproxDepth(train, valid, 5, 5)
    tree = DecisionTree(train)
    print("building tree from full set")
    tree.buildTree(best[0], best[1], True)
    print("tree built, testing tree")
    acc = testTreeF(tree, test)
    print("accuracy of:", "%.2f" % (acc * 100))
    return tree


if __name__ == "__main__":
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
    # train, test, valid = getWineData(1)
    train, test, valid = getIrisData(1)
    # tree = guessTreeOpt(train, test, valid)
    tree = guessTreeOpt(train, test, valid)

    # e = 99999
    # for i in range(1):
    #     tree = DecisionTree(train.randSubSet(400))
    #     tree.buildTree()
    #     # print(tree)
    #     # print(tree.mut)
    #     tree.printTree()
    #     # print(dS)
    #     errorE = 0
    #     successE = 0
    #     for d in test:
    #         r = tree.searchTree(d)
    #         #print("guess:",r,"actual:",d.classifier())
    #         if r==d.classifier():
    #             successE+=1
    #         else:
    #             errorE+=1
    #     if errorE < e:
    #         e = errorE
    #     print("success:",successE,"error:",errorE,"accuracy:", ("%.2f" % (100*(successE/(errorE+successE)))) +"%"  )
    # print("best error",e)
