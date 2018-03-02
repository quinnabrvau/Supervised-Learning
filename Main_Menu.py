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
    menu_message = """Choose one of the following options for the data set: 
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
    menu_message = """Choose which learning agent to use: 
          Decision Tree (type 't')
          \t 
          Neural Net (type 'n')
          \t This learning agent uses a 2-layer feedforward neural network
          \t and trains by running multiple epochs where it updates the weights
          \t and activations for each layer
          Quit (type 'q') """
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
        elif letter_choice == 'q':
            continue_menu = False
        else:
            print("That's not a valid option. \n")


if __name__ == "__main__":
    main_menu()




