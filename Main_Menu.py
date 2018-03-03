"""Main_Menu.py by Shannon Ladymon (UWNetID: sladymon)
in partnership with Quinn Abrahams-Vaughn (UWNetID: abrahq)

CSE 415 Winter 2018
Final Project

Main Menu, entry point to the project
"""

# Welcome screen & description of program
# loop until quit
# Ask which dataset (give descriptions)
# Ask which learning agent
# run agent

# default choices to run the program
DATASET = 'wine'
AGENT = 'tree'
BAGGING = False


def main_menu():
    print("""
    --------------------------------------------------------------------------

    Welcome to Quinn Abrahams-Vaughn & Shannon Ladymon's Final Project
    (UWNetIDs: abrahq and sladymon)

    We have implemented two learning agents (a decision tree and a neural net)
    and have two datasets to test them on (Fischer Iris and Red Wine Quality)

    --------------------------------------------------------------------------""")
    dataset_menu()
    agent_menu()


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
    letter_choice = ''
    continue_menu = True

    while(continue_menu):
        letter_choice = input(menu_message).lower()
        if letter_choice == 'i':
            DATASET = 'iris'
            continue_menu = False
        elif letter_choice == 'w':
            DATASET = 'wine'
            continue_menu = False
        elif letter_choice == 'q':
            continue_menu = False
        else:
            print("That's not a valid option. \n")


def agent_menu():
    global AGENT
    # TODO: add description of the decision tree
    menu_message = """\nChoose which learning agent to use: 
          Decision Tree (type 't')
          \t 
          Neural Net (type 'n')
          \t This learning agent uses a 2-layer feedforward neural network
          \t and trains by running multiple epochs where it updates the weights
          \t and activations for each layer"""
    letter_choice = ''
    continue_menu = True

    while(continue_menu):
        letter_choice = input(menu_message).lower()
        if letter_choice == 't':
            AGENT = 'tree'
            tree_menu()
            continue_menu = False
        elif letter_choice == 'n':
            AGENT = 'net'
            net_menu()
            continue_menu = False
        else:
            print("That's not a valid option. \n")

def net_menu():
    # TODO: add more description of bagging
    bagging_message = """\nDo you want to use bagging (which can improve performance)? (type 'y' or 'n'):"""
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

    while(continue_menu):
        letter_choice = input(menu_message).lower()
        if letter_choice == 't':
            AGENT = 'tree'
            continue_menu = False
        elif letter_choice == 'n':
            AGENT = 'net'
            continue_menu = False
        else:
            print("That's not a valid option. \n")


def tree_menu():
    print("Add in whatever parameters users can choose here")

if __name__ == "__main__":
    main_menu()




