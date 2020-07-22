import time
import axelrod as axl
import argparse


from logic import singlematch_logic as sinl
from vars import my_vars as gv 


"""
Main function for simple one-on-one matches implemented using argparse.
See help for better understanding and usability.
"""

# Create parser and add arguments.
parser = argparse.ArgumentParser(description="Main function for one-on-one matches.")
parser.add_argument("p1", help="The first player of a match, examples: coop, tft, tAc")
parser.add_argument("p2", help="The second player of a match, same as p1.")
parser.add_argument("--turns", help="The numbers of turns within a match, default = 200", default=200, type=int)
parser.add_argument("--matches", help="The numbers of turns within a match, default = 200", default=1, type=int)

my_args = parser.parse_args()
turns = my_args.turns
matches = my_args.matches

for s in gv.base_strategies :
    if s == my_args.p1:
        player1_str = gv.base_strategies[s]
        #print ("The players are: {} with the format {} ".format(player1_str, type(player1_str)))
    if s == my_args.p2:
        player2_str = gv.base_strategies[s]
        #print ("The players are: {} with the format {} ".format(player2_str, type(player2_str)))

print ("The strategy played by prisoner 1 is: {} and the type is {} ".format(player1_str, type(player1_str)))
print ("The strategy played by prisoner 2 is: {} and the type is {} ".format(player2_str, type(player2_str)))
print ("The number of turns is: {} and the type is {} ".format(turns, type(turns)))
print ("The number of matches is: {} and the type is {} ".format(matches, type(matches)))

if matches == 1:
    sinl.custom_match(player1_str, player2_str, turns)
else:
    sinl.custom_nrof_mathches(player1_str, player2_str, turns, matches)