import time
import argparse
import datetime

import axelrod as axl


from vars import my_vars as gv 
from logic import roundrobin_logic as rrl

"""
PROBLEMS:
1. Only the last df is displayed 
2. If DFs are agregated, they need to be normalized (in what manner???)

3. How much should the number get for random matches and turns

"""

def main(turns, matches, random, runs ):
    if random == False:
        start = time.time()
        print("Running in with the values provided by you or the default ones.")
        #print("no. of matches: {}".format(matches))
        #print("no. of turns: {}".format(turns))
        rrl.playall_fixed(  gv.firstgen_strategies_str, 
                            gv.firstgen_strategies_axl,
                            matches,
                            turns )
        end = time.time()
        print("The elapsed time for this tournament is: {} seconds".format(end-start))
    elif random == True:
        for el in runs:
            if el == 0:
                rrl.playall_random( gv.firstgen_strategies_str,
                                    gv.firstgen_strategies_axl,
                                    el )


if __name__ == '__main__':
    """
    Main function for round robin tournaments between specified strategies.
    See help for better understanding and usability.
    See roundrobin_logic.py for how to use it properly or the README file.
    """

    # Create parser and add arguments.
    parser = argparse.ArgumentParser(description="Main function for runnnig round robin tournaments.")
    # parser.add_argument("strategies_stringlist", help="The list of all the strategies in string format, ")
    # parser.add_argument("strategies_axltype", help="The second player of a match, same as p1.")
    parser.add_argument("--turns", "-t", help="The number of turns within a match, default is 200", default=200, type=int)
    parser.add_argument("--matches", "-m", help="The number of matches, default is 1", default=1, type=int)
    parser.add_argument("--random", "-r", help="For randomly generating a the number of matches and the numbers of turns in a match.", default=False, type=bool)
    parser.add_argument("--runs", "-it", help=" No. of times a Monte Carlo analysis is run. ", default=50, type=int)

    my_args = parser.parse_args()
    turns = my_args.turns
    matches = my_args.matches
    random = my_args.random
    runs = my_args.runs

    range_run = range(runs)

    ### MAIN ###
    main(turns, matches, random, range_run)
