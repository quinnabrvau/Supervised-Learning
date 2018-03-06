"""dataSet.py by Quinn Abrahams-Vaughn (UWNetID: abrahq)
in partnership with Shannon Ladymon (UWNetID: sladymon)

CSE 415 Winter 2018
Final Project

Stores data in a usable format
"""
from math import sqrt
from data import data
from random import sample as rSample


class dataSet(list):
    """
    class to hold a data set for machine learning alogrithms in a standard way
    expands list with a way to read a  csv, and to print out in a
    format that is readable { [ atributes ] classifier }
    """

    def __init__(self, In=None):
        self.header = data()
        self.max = []
        self.min = []
        self.mean = []
        self.std = []
        self.mut = {}
        self.classes = []
        list.__init__(self)
        if In != None:
            if isinstance(In, dataSet):
                list.__init__(self, In)
                self.mut = In.mut
                self.classes = In.classes
                self.header = In.header
            elif isinstance(In, list):
                list.__init__(self, In)
            elif isinstance(In, str):
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
        out = str(self.header) + "\n"
        for d in self:
            out += str(d) + "\n"
        if len(self.max):
            out += self.print_stats()
        if len(self.classes):
            out += "classes: "
            for c in self.classes:
                out += str(c) + ", "
            out = out[:-2]
        return out

    def print_stats(self):
        r1 = "max ["
        r2 = "min ["
        r3 = "mean["
        r4 = "std ["
        for i in range(len(self.max)):
            d = "%.2f" % self.max[i]
            r1 += d + " "*(8-len(d)) + ", "
            d = "%.2f" % self.min[i]
            r2 +=  d + " "*(8-len(d)) + ", "
            d = "%.2f" % self.mean[i]
            r3 +=  d + " "*(8-len(d)) + ", "
            d = "%.2f" % self.std[i]
            r4 +=  d + " "*(8-len(d)) + ", "
        return r1[:-3] + "\t]\n" + r2[:-3] + "\t]\n" + r3[:-3] + "\t]\n" + r4[:-3] + "\t]\n"

    def print_short(self,l = 3):
        out = str(self.header) + "\n"
        for i in range(l):
            out += str(self[i]) + "\n"  
        return out      

    def read(self, fileName):
        """reads a csv into the data set"""
        i = 0
        file = open(fileName)
        for line in file:
            if len(line) <= 1:
                pass
            elif i >= 1:
                self.append(data(line))
            else:
                self.header = data(line)
            i |= 1
        file.close()

    def findMinMax(self):
        """finds the minimum, maximum, mean, and stanard deviation for each attribute"""
        self.max = self[0].attributes()
        self.min = self[0].attributes()
        self.mean = [0 for i in self[0].attributes()]
        self.std = [i * i for i in self[0].attributes()]
        for i in range(1, len(self)):
            d = self[i]
            for j in range(len(d) - 1):
                if d[j] > self.max[j]: self.max[j] = d[j]
                elif d[j] < self.min[j]: self.min[j] = d[j]
                self.mean[j] += d[j]
        for j in range(len(self[0]) - 1):
            self.mean[j] /= len(self)
        for i in range(1, len(self)):
            d = self[i]
            for j in range(len(d) - 1):
                self.std[j] += (d[j] - self.mean[j])**2
        for j in range(len(self[0]) - 1):
            self.std[j] /= len(self)
            if self.std[j] < 0: self.std[j] = 0
            self.std[j] = sqrt(self.std[j])

    def normRange(self, small=0, large=1, lit=None, big=None):
        if lit != None: self.min = lit
        if big != None: self.max = big
        scalarM = self[0].attributes()
        for j in range(len(self.max)):
            scalarM[j] = (large - small) / (self.max[j] - self.min[j])
        for i in range(len(self)):
            for j in range(len(self[i]) - 1):
                self[i][j] = (self[i][j] - self.min[j]) * scalarM[j] + small
        self.findMinMax()

    def normStd(self, mean=None, std=None):
        if mean == None:
            mean = self.mean
        if std == None:
            std = self.std
        for i in range(len(self)):
            for j in range(len(self[i]) - 1):
                self[i][j] -= mean[j]
                self[i][j] /= std[j]
        self.findMinMax()

    def divide(self, split):
        for i in range(len(self)):
            for j in range(len(self[i]) - 1):
                if self[i][j] > split:
                    self[i][j] = 1
                else:
                    self[i][j] = 0
        self.findMinMax()

    def strings2Ints(self, mut=None):
        if mut != None:
            self.mut = mut
        else:
            self.mut = {}
        k = 0
        for i in range(len(self)):
            for j in range(len(self[i])):
                if isinstance(self[i][j], str):
                    if self[i][j] not in self.mut.keys():
                        if j == len(self[i]) - 1:
                            self.classes.append(k)
                        self.mut[self[i][j]] = k
                        self.mut[k] = self[i][j]
                        self[i][j] = k
                        k += 1
                    else:
                        self[i][j] = self.mut[self[i][j]]
        self.findClasses()

    def getString(self, val):
        if val in self.mut.keys():
            return self.mut[val]
        return str(val)

    def randSubSet(self, k=25, shhh=False):
        """returns a random sub set of size k from the data set"""
        if not shhh: print("building sub set")
        if k > len(self):
            if not shhh:                print("attempting to devide set into a set smaller " + \
       "then original set returning original set")
            return self
        out = dataSet()
        out.header = self.header
        out.extend(rSample(self, k))
        out.findMinMax()
        out.strings2Ints()
        out.findClasses()
        out.mut = self.mut
        return out

    def subSet(self, atr):
        out = dataSet()
        for d in self:
            d_ = data()
            for i in atr:
                d_.append(d[i])
            d_.append(d.classifier())
            out.append(d_)
        return out


def getIrisData(normalize=0):
    """returns the iris training, testing and validating data and normalized if normalize==True"""
    out = getData("iris", normalize)
    out[0].strings2Ints()
    out[1].strings2Ints(out[0].mut)
    out[2].strings2Ints(out[0].mut)
    return out


def getWineData(normalize=0):
    """returns the wine training, testing and validating data and normalized if normalize==True"""
    return getData("wine", normalize)


def getData(name="iris", normalize=0):
    """returns the data sets, normalized if normalize==True"""
    print("reading in files for:", name, "data set")
    out = [
        dataSet(name + "TrainData.csv"),
        dataSet(name + "TestData.csv"),
        dataSet(name + "ValidData.csv")
    ]
    if normalize == 1:
        print("normalizing to standard deviation")
        mean, std = out[0].mean, out[0].std
        out[0].normStd()
        out[1].normStd(mean, std)
        out[2].normStd(mean, std)
    elif normalize == 2:
        print("normalizing to range 0 to 1")
        lit, big = out[0].min, out[0].max
        out[0].normRange(0, 1)
        out[1].normRange(0, 1, lit, big)
        out[2].normRange(0, 1, lit, big)
    print("successfully read all files for:", name, "data set")
    return out


if __name__ == "__main__":
    import numpy as np
    dS = dataSet("wineValidData.csv")
    # print(dS)
    new_dS = dS.randSubSet(25)
    print(new_dS)

    #numpy array example
    print(np.asarray(dS))

    new_dS.normRange(-1, 1)
    print(new_dS)
    new_dS = dS.randSubSet(25)
    new_dS.normStd()
    print(new_dS)
    new_dS.divide(0)
    print(new_dS)

    dS = getIrisData(2)
    # for s in dS:
    #     print(s)
    print(dS[0].mut, dS[1].mut, dS[2].mut, sep="\n")
    # for s in getWineData():
    #     print(s)
