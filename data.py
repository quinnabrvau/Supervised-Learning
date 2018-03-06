"""data.py by Quinn Abrahams-Vaughn (UWNetID: abrahq)
in partnership with Shannon Ladymon (UWNetID: sladymon)

CSE 415 Winter 2018
Final Project

data class
"""


class data(list):
    """
    class to hold data for machine learning alogrithms in a standard way
    expands list with a way to read a line of csv, and to print out in a
    format that is readable { [ atributes ] classifier }
    """

    def __init__(self, In=None):
        list.__init__(self)
        if In == None:
            pass
        elif isinstance(In, str):
            self.read(In)
        elif isinstance(In, list):
            list.__init__(self, In)

    def read(self, inString):
        """reads the line of a csv into the array"""
        self.clear()
        s_strip = inString.strip("\n")
        s_split = s_strip.split(",")
        for ele in s_split:
            if ele == "":
                continue
            try:
                if str(int(ele)) == ele:
                    self.append(int(ele))
                else:
                    Exception()
            except:
                try:
                    if str(float(ele)) == ele:
                        self.append(float(ele))
                    else:
                        Exception()
                except:
                    self.append(ele)

    def attributes(self):
        """returns a copy of the attributes of the data"""
        return [i for i in self[0:-1]]

    def classifier(self):
        """returns the classifier of the data"""
        return self[-1]

    def __str__(self):
        """prints the data in readable format"""
        if len(self) < 1: return "{ [  ]   } error no data"
        out = "{   ["
        for j in self[0:-1]:
            if isinstance(j, float) or isinstance(j, int):
                d = ("%.2f" % j)
                out += d + " "*(8-len(d)) + ", "
            else:
                if len(str(j))<8:
                    out += str(j) + " "*(8-len(str(j))) + ", "
                else:
                    out += str(j)[:8] + ", "
        out = out[:-2] + "] "
        out += str(self[-1]) + " }"
        return out


if __name__ == "__main__":
    s1 = "1,2,3.456,r,gold,testingData"
    s2 = "2,1,r,3.456,gold,testingData"
    print("s1:", s1)
    print("s2:", s2)
    d1 = data(s1)
    print("d1:", d1)
    d1.read(s1)
    print("d1:", d1)
    print("d1 attributes", str(d1.attributes()))
    print("d1 classifier", str(d1.classifier()))
    d2 = data()
    print("d2:", d2)
    d2.read(s2)
    print("d2:", d2)