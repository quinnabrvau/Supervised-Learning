"""Report.py by Quinn Abrahams-Vaughn (UWNetID: abrahq)
in partnership with Shannon Ladymon (UWNetID: sladymon)

CSE 415 Winter 2018
Final Project

Prints a report of relevant information on how the learning agent did
"""


class Report(dict):
    """A class to create a report on the program that was run
    including information on the dataset with samples of the data,
    information on the learning agent and chosen parameters,
    information on the amount of time and number of training cycles used,
    and information on the accuracy and predictions the agent made"""
    def __init__(self):
        dict.__init__(self)

        # strings to explain data
        self.explainer = {
            "dataset":
            "This run used the XXXX dataset",
            "datasetTrainSize":
            "The size of the training data is XXXX",
            "datasetValidSize":
            "The size of the validation data is XXXX",
            "datasetTestSize":
            "The size of the testing data is XXXX\n",
            "agent":
            "This run used a XXXX agent\n",
            "bagging":
            "This agent was enhanced with bagging. XXXX total agents were used\n",
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
            "The neural net performed XXXX training cycles",
            "netAlpha":
            "The neural net used an alpha of XXXX",
            "netLayers":
            "The neural net was made of XXXXx layers\n",

            #Data set
            "input":"Raw Training Data Sample\nXXXX",
            "inputData":"Training Data Statistics\nXXXX",
            "inputNorm":"Normalized Training Data Sample\nXXXX",
        }

        # order to print output
        self.order = [
            "dataset",
            "input",
            "inputData",
            "inputNorm",
            "datasetTrainSize",
            "datasetValidSize",
            "datasetTestSize","openTime",
            "buildTime",
            "predictTime",
            "totalTime",
            "predictAccuracy",
            "expectedAccuracy",
            "agent",
            "bagging",
            
            #Tree Specific Data Types
            "tree"
            "treeDepth",
            "treeMinSize",

            #Nueral Net Specific Data Types
            "netTrainCycle",
            "netAlpha",
            "netLayers",
            "netActivation"
        ]

    def __str__(self):
        """Returns a string version of the report"""
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
