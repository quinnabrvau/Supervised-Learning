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
    global DATASET, AGENT, BAGSIZE, BAGGING, REPORT
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
        if AGENT == 't':
            break
        elif AGENT == 'n':
            break
        elif AGENT == 'q':
            break
        else:
            print("That's not a valid option.")

def net_menu():
    hidden_layer_message = """\nHow many nodes do you want to use in the hidden layer? 
                    Typically, you use about 1-2x the number of nodes in your input layer.
                    The more nodes you have, the better the neural net can predict, 
                    but the more slowly it runs. Enter an integer between 1 and 2:"""
    activation_message = """\nWhich activation function would you like to use?
                    You can use a sigmoid function or a tanh function.
                    Sigmoid functions have a range of [0, 1] and Tanh functions have a range of [-1, 1].
                    Tanh functions usually give better performance. Type 's' for sigmoid, or 't' for tanh:"""
    alpha_start_message = """\nWhat value for alpha (learning rate) do you want to use? 
                    Typically alpha is in the range [0.1, 0.00001].
                    If you have a large alpha [0.1], your model may jump around too much.
                    If you have a small alpha [0.00001], your model may learn too slowly.
                    Enter a decimal between 0.1 and 0.00001:"""
    alpha_decay_message = """\nDo you want your alpha (learning rate) to decay over time?
                    Decaying alpha allows the learning agent to be more aggressive in the beginning.
                    (type 'y' or 'n'):"""
    # Generally you optimize your model with a large learning rate (0.1 or so),
    # and then progressively reduce this rate, often by an order of magnitude
    # (so to 0.01, then 0.001, 0.0001, etc.).
    # Typical learning rates are in [0.1, 0.00001]
    # alpha decay = alpha / sqrt(t) where t= current iteration number


    letter_choice = ''
    continue_menu = True
    layers = 2
    activation = ''
    alpha = 0.1
    decay = ''
    while(continue_menu):
        letter_choice = input(hidden_layer_message).lower()
        if letter_choice == '1':
            layers = 1
            continue_menu = False
        elif letter_choice == '2':
            continue_menu = False
        else:
            print("That's not a valid option. \n")
    continue_menu = True
    while(continue_menu):
        activation = input(activation_message).lower()
        if activation=='s':
            break
        elif activation=='t':
            break
        else:
            print("That's not a valid option. \n")
    while(continue_menu):
        alpha = input(alpha_start_message).lower()
        try:
            alpha = float(alpha)
            if alpha < 0.1 and alpha > 0.00001:
                break
            else:
                print("That's not a valid number.")
        except:
            print("That's not a valid number.")
    while(continue_menu):
        decay = input(alpha_decay_message).lower()
        if decay=='y':
            break
        elif decay=='n':
            break
        else:
            print("That's not a valid option. \n")
    return layers,activation,alpha,decay


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

def tree_menu():
    menu_message = """\nTree's are usually built to a specific depth, please provide
                      \t a depth to be used. If 0 is provided, the tree will try and 
                      \t find a near optimal depth to use.
                      Choose an integer >= 0: """
    depth = ""
    while (True):
        depth = input(menu_message).lower()
        try:
            depth = int(depth)
            if depth >= 1:
                break
            elif depth == 0:
                print("The system will try and find a near optimal depth")
                break
            else:
                print("Please choose a positive number >= 0.")
        except:
            print("That's not a valid number.")

    menu_message = """\nA node in the tree is considered a leaf if it is at the max
                      \t depth or if it has a minimum number of elements. Please
                      \t provide the number of elements that will define a minimume
                      \t size. If 0 is provided, the tree will attempt to fine
                      \t a near optimal size
                      Choose an integer >= 0: """
    size = ""
    while (True):
        size = input(menu_message).lower()
        try:
            size = int(size)
            if size > 1:
                break
            elif size == 0:
                print("The system will try and find a near optimal depth")
                break
            else:
                print("Please choose a positive number >= 0.")
        except:
            print("That's not a valid number.")
    return depth, size

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
        BL.params( tree_menu() )
    elif AGENT == 'n':
        REPORT['agent']="Neural Network"
        BL = BaggerList(NNTestDriver,DATASET,BAGSIZE,REPORT)
        BL.params( net_menu() )
    else:
        print("Something went wrong, exiting ...")
        return
    BL.build()
    BL.predict()



if __name__ == "__main__":
    main_menu()




