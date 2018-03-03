"""Report.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Prints a report of relevant information on how the learning agent did
"""

# perhaps create class object which takes in the following info when called:
#   - dataset
#   - learning agent
#   - time to run
#   - # of training cycles
#   - X_test, Y_test

# print info on the dataset used and the expected benchmarksb

# print info on the learning agent and the time it took to learn

# print info on the accuracy of the classification
# percentages of false positives, false negatives, true positives, true negatives


class Report(dict):
    def __init__(self):
        dict.__init__(self)
        self.explainer = {
            "dataset":
            "This run used the XXXX dataset",
            "datasetTrainSize":
            "The size of the training data is XXXX",
            "datasetValidSize":
            "The size of the validation data is XXXX",
            "datasetTestSize":
            "The size of the testing data is XXXX",
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
            "It took XXXX seconds to run the program",
            "predictAccuracy":
            "The prediction accurately guessed XXXX%  of the test data",
            #Tree Specific Data Types
            "treeDepth":
            "The tree was built to a depth of XXXX",
            "treeMinSize":
            "Any node smaller then XXXX elements was automatically made a leaf",

            #Nueral Net Specific Data Types
            "netTrainCycle":
            "The nueral net performed XXXX training cycles",
            "netAlpha":
            "The nueral net used an alpha of XXXX",
            "netLayers":
            "The nueral net was made of XXXX layers",
            "netActivation":
            "The nueral net used an XXXX function for the activation function",
        }
        self.order = [
            "dataset",
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
