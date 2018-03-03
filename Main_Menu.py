"""Main_Menu.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Main Menu, entry point to the project
"""


from Bagger import BaggerList
from RandomForest import RandomForest
from NNTestDriver import NNTestDriver
from Report import Report

# Welcome screen & description of program
# loop until quit
# Ask which dataset (give descriptions)
# Ask which learning agent
# run agent

# default choices to run the program
DATASET = 'w'
AGENT = 't'
BAGGING = 'y'
BAGSIZE = 1
REPORT = Report()


def main_menu():
    print("""
    --------------------------------------------------------------------------

    Welcome to Quinn Abrahams-Vaughn & Shannon Ladymon's Final Project
    (UWNetIDs: abrahq and sladymon)

    We have implemented two learning agents (a decision tree and a neural net)
    and have two datasets to test them on (Fischer Iris and Red Wine Quality)

    --------------------------------------------------------------------------""")
    dataset_menu()
    if DATASET=='q':return
    agent_menu()
    if AGENT=='q':return
    bagging_menu()
    if BAGGING=='q' or BAGSIZE=='q':return
    run_from_menu()
    print(REPORT)



def dataset_menu():
    global DATASET
    menu_message = """\nChoose one of the following options for the data set: 
          Fischer Iris Dataset (type 'i')
          \t The Iris dataset contains 150 samples of 3 types of iris flowers
          \t with data on 4 features (ex. petal width) for each sample
          Red Wine Quality Dataset (type 'w')
          \t The Wine dataset contains 1600 samples of red wine
          \t classified into 6 classes of quality (ratings 3-8)
          \t with data on 11 features (ex. residual sugar) for each sample
          Quit (type 'q') """

    while(True):
        DATASET = input(menu_message).lower()
        if len(DATASET)==1 and DATASET in 'iwq':
            break
        else:
            print("That's not a valid option.")


def agent_menu():
    global AGENT
    # TODO: add description of the decision tree
    menu_message = """\nChoose which learning agent to use: 
          Decision Tree (type 't')
          \t This learning agent builds a binary decision tree of semi-optimum 
          \t depth
          Neural Net (type 'n')
          \t This learning agent uses a 2-layer feedforward neural network
          \t and trains by running multiple epochs where it updates the weights
          \t and activations for each layer
          Quit (type 'q') """

    while(True):
        AGENT = input(menu_message).lower()
        if len(AGENT)==1 and AGENT in 'tnq':
            break
        else:
            print("That's not a valid option.")

def bagging_menu():
    global BAGGING, BAGSIZE
    menu_message = """\nBagging is a way to fight over fitting by breaking up the
                      \t data into smaller subsets. This is done by running the
                      \t agent on a subset of the atributes and a subset of the
                      \t total cases. Then the most common choice is returned.
                      Choose yes/no(type 'y'/'n') """
    while(True):
        BAGGING = input(menu_message).lower()
        if len(BAGGING)==1 and BAGGING in 'ynq':
            break
        else:
            print("That's not a valid option.")
    if BAGGING!='y': 
        BAGSIZE=1
        return
    menu_message = """\nBagging uses multiple agents, please input the desired number
                      \t of agents. The larger the number, the longer the program will
                      \t take to build a set. A larger number will also be more accurate
                      Choose a number greater than 1 (ex 20) """
    while(True):
        BAGSIZE = input(menu_message).lower()
        if BAGSIZE=='q':
            BAGSIZE=1
            return
        try:
            BAGSIZE = int(BAGSIZE)
            if BAGSIZE > 1:
                break
            elif BAGSIZE == 1:
                print("A size of 1 will produce no benefits from bagging.")
            else:
                print("Please choose a positive number greater than one.")
        except:
            print("That's not a valid number.")


def run_from_menu():
    global DATASET,AGENT,BAGGING,BAGSIZE,REPORT
    if 'q' in AGENT or 'q' in DATASET or 'q' in BAGGING:
        return
    BL = None
    if DATASET=='i':
        REPORT['dataset']="iris"
    elif DATASET=='w':
        REPORT['dataset']='wine'
    else:
        REPORT['dataset']=DATASET
    if BAGGING=='y':
        REPORT['bagging']=str(BAGSIZE)
    if AGENT == 't':
        REPORT['agent']="Decision Tree"
        BL = BaggerList(RandomForest,DATASET,BAGSIZE,REPORT)
    elif AGENT == 'n':
        REPORT['agent']="Neural Network"
        BL = BaggerList(NNTestDriver,DATASET,BAGSIZE,REPORT)
    else:
        print("Something went wrong, exiting ...")
        return
    BL.build()
    BL.predict()

if __name__ == "__main__":
    main_menu()




