"""Report.py by Quinn Abrahams-Vaughn (UWNetID: abrahq)
in partnership with Shannon Ladymon (UWNetID: sladymon)

CSE 415 Winter 2018
Final Project

Prints a report of relevant information on how the learning agent did
"""


class Report(dict):
    def __init__(self):
        dict.__init__(self)
        self.explainer = { # strings to explain data
            "dataset":
            "This run used the XXXX dataset",
            "datasetTrainSize":
            "The size of the training data is XXXX",
            "datasetValidSize":
            "The size of the validation data is XXXX",
            "datasetTestSize":
            "The size of the testing data is XXXX\n",
            "agent":
            "This run used a XXXX agent",
            "bagging":
            "This agent was enhanced with bagging. XXXX total agents were used",
            "openTime":
            "It took XXXX seconds to prepare the agent(s)",
            "buildTime":
            "It took XXXX seconds to train the agent(s)",
            "predictTime":
            "It took XXXX seconds to predict the test set",
            "totalTime":
            "It took XXXX seconds to run the program\n",
            "predictAccuracy":
            "The prediction accurately guessed XXXX%  of the test data",
            'expectedAccuracy':"The benchmark accuracy for this data set is XXXX%\n",
            #Tree Specific Data Types
            "treeDepth":
            "The tree was built to a depth of XXXX",
            "treeMinSize":
            "Any node smaller then XXXX elements was automatically made a leaf\n",

            #Nueral Net Specific Data Types
            "netTrainCycle":
            "The nueral net performed XXXX training cycles",
            "netAlpha":
            "The nueral net used an alpha of XXXX",
            "netLayers":
            "The nueral net was made of XXXXx layers\n",

            #Data set
            "input":"Raw Training Data Sample\nXXXX",
            "inputData":"Training Data Statistics\nXXXX",
            "inputNorm":"Normalized Training Data Sample\nXXXX",
        }
        self.order = [ # order to print output
            "dataset",
            "input",
            "inputData",
            "inputNorm",
            "datasetTrainSize",
            "datasetValidSize",
            "datasetTestSize",
            "agent",
            "bagging",
            "openTime",
            "buildTime",
            "predictTime",
            "totalTime",
            "predictAccuracy",
            "expectedAccuracy",
            #Tree Specific Data Types
            "treeDepth",
            "treeMinSize",
            #Nueral Net Specific Data Types
            "netTrainCycle",
            "netAlpha",
            "netLayers",
            "netActivation"
        ]

    def __str__(self):
        out = "!!!!!!! REPORTED STATISTICS !!!!!!!\n"
        for k in self.order:
            if k in self.keys():
                if k in self.explainer.keys():
                    out += self.explainer[k].replace('XXXX', str(
                        self[k])) + "\n"
                else:
                    out += self[k] + "\n"
        for k in self.keys():
            if k not in self.order:
                out += str(self[k])
        return out

    def add(self, key, val):
        self[key] = val
