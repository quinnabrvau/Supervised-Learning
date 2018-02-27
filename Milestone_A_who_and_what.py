#!/usr/bin/python3
'''Milestone_A_who_and_what.py
This runnable file will provide a representation of
answers to key questions about your project in CSE 415.

'''

# DO NOT EDIT THE BOILERPLATE PART OF THIS FILE HERE:

CATEGORIES=['Baroque Chess Agent','Feature-Based Reinforcement Learning for the Rubik Cube Puzzle',\
  'Supervised Learning: Comparing Trainable Classifiers']

class Partner():
  def __init__(self, lastname, firstname, uwnetid):
    self.uwnetid=uwnetid
    self.lastname=lastname
    self.firstname=firstname

  def __lt__(self, other):
    return (self.lastname+","+self.firstname).__lt__(other.lastname+","+other.firstname)

  def __str__(self):
    return self.lastname+", "+self.firstname+" ("+self.uwnetid+")"

class Who_and_what():
  def __init__(self, team, option, title, approach, workload_distribution, references):
    self.team=team
    self.option=option
    self.title=title
    self.approach = approach
    self.workload_distribution = workload_distribution
    self.references = references

  def report(self):
    rpt = 80*"#"+"\n"
    rpt += '''The Who and What for This Submission

Final Project in CSE 415, University of Washington, Winter, 2018
Milestone A

Team: 
'''
    team_sorted = sorted(self.team)
    # Note that the partner whose name comes first alphabetically
    # must do the turn-in.
    # The other partner(s) should NOT turn anything in.
    rpt += "    "+ str(team_sorted[0])+" (the partner who must turn in all files in Catalyst)\n"
    for p in team_sorted[1:]:
      rpt += "    "+str(p) + " (partner who should NOT turn anything in)\n\n"

    rpt += "Option: "+str(self.option)+"\n\n"
    rpt += "Title: "+self.title + "\n\n"
    rpt += "Approach: "+self.approach + "\n\n"
    rpt += "Workload Distribution: "+self.workload_distribution+"\n\n"
    rpt += "References: \n"
    for i in range(len(self.references)):
      rpt += "  Ref. "+str(i+1)+": "+self.references[i] + "\n"

    rpt += "\n\nThe information here indicates that the following file will need\n"+\
     "to be submitted (in addition to code and possible data files):\n"
    rpt += "    "+\
     {'1':"Baroque_Chess_Agent_Report",'2':"Rubik_Cube_Solver_Report",\
      '3':"Trainable_Classifiers_Report"}\
        [self.option]+".pdf\n"

    rpt += "\n"+80*"#"+"\n"
    return rpt

# END OF BOILERPLATE.

# Change the following to represent your own information:

quinn = Partner("Abrahams-Vaughn", "Quinn", "abrahq")
shannon = Partner("Ladymon", "Shannon", "sladymon")
team = [quinn, shannon]

OPTION = '3'
# Legal options are 1, 2, and 3.

title = "Supervised Learning System"
 # In this case, the Python file for the formulation would be named End_Poverty.py.

approach = '''We will be using the Fisher Iris Dataset and an original dataset which
combines two datasets on white an red wines (classifying white/red based on features of the wine). 
We will develop a decision tree learning agent using random forests, 
and a neural network learning agent. Next we will implement bagging. 
Finally we will create a command line interface and reporting system.'''

workload_distribution = '''Quinn will be responsible for creating the decision tree learning agent. 
Shannon will be responsible for creating the neural network learning agent.
We will work together to implement bagging.
Finally, we will work together on the command line interface and reporting system.'''

reference1 = '''"What is the Difference Between Bagging and Boosting," on QuantDare.com,
    available online at: https://quantdare.com/what-is-the-difference-between-bagging-and-boosting/'''

reference2 = '''"Neural Networks from Scratch in Python," by Cristian Dima,
    available online at: http://www.cristiandima.com/neural-networks-from-scratch-in-python/'''

reference3 = ''''"Random Forests for Regression and Classification," by Adele Cutler, Utah State University,
    available online at: http://www.math.usu.edu/adele/RandomForests/Ovronnaz.pdf'''

our_submission = Who_and_what(team, OPTION, title, approach, workload_distribution, [reference1, reference2, reference3])

# You can run this file from the command line by typing:
# python3 who_and_what.py

# Running this file by itself should produce a report that seems correct to you.
if __name__ == '__main__':
  print(our_submission.report())
