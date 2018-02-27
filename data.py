#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 07:19:25 2018

@author: quinn
"""

class data(list):
    """
    class to hold data for machine learning alogrithms in a standard way
    expands list with a way to read a line of csv, and to print out in a
    format that is readable { { atributes } classifier }
    """
    def __init__(self,inString=None):
        list.__init__(self)
        if inString!=None:
            self.read(inString)
            
    def read(self,inString):
        """reads the line of a csv into the array"""
        self.clear()
        s_strip = inString.strip("\n")
        s_split = s_strip.split(",")
        for ele in s_split:
            try:
                if str(int(ele))==ele:
                    self.append(int(ele))
                else:
                    Exception()
            except:
                try:
                    if str(float(ele))==ele:
                        self.append(float(ele))
                    else:
                        Exception()
                except:
                    self.append(ele)
    
    def attributes(self):
        """returns just the attributes of the data"""
        return self[:len(self)-1]
    
    def classifier(self):
        """returns the classifier of the data"""
        return self[-1]
    
    def __str__(self):
        """prints the data in readable format"""
        if len(self) < 1: return "{ []  ]   }"
        out = "{ "
        out += str(self.attributes())+" "
        out += str(self[-1]) + " }"
        return out

if __name__ == "__main__":
    s1 = "1,2,3.456,r,gold,testingData"
    s2 = "2,1,r,3.456,gold,testingData"
    print("s1:",s1)
    print("s2:",s2)
    d1 = data(s1)
    print("d1:",d1)
    d1.read(s1)
    print("d1:",d1)
    print("d1 attributes",str(d1.attributes()))
    print("d1 classifier",str(d1.classifier()))
    d2 = data()
    print("d2:",d2)
    d2.read(s2)
    print("d2:",d2)
    
    
    
    