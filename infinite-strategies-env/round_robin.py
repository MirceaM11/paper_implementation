'''
One function
'''

import time, os, operator, random
import argparse
import datetime
import pandas as pd

import axelrod as axl

###
### VARIABLES 
### MOVED FROM GLOBAL SCOPE
###
base_strategies =	{
    "coop": axl.Cooperator(),
    "alter": axl.Alternator(),
    "tft": axl.TitForTat(),
    "tac": axl.FirstByTidemanAndChieruzzi(),
    "nydg": axl.FirstByNydegger(),
    "grof": axl.FirstByGrofman(),
    "shub": axl.FirstByShubik(),
    "sara": axl.FirstBySteinAndRapoport(),
    "grudger": axl.Grudger(),
    "davis": axl.FirstByDavis(),
    "rdown": axl.RevisedDowning(),
    "feld": axl.FirstByFeld(),
    "joss": axl.FirstByJoss(),
    "tull": axl.FirstByTullock(),
    "rand": axl.Random()
}
# used by roundrobin_logic.py for creating the tables
# insert your lists below with your strategies to run your experiments

firstgen_strategies_str = ["Cooperator", "Alternator", "TitForTat", "TidemanAndChieruzzi", "Nydegger", "Grofman",
                "Shubik", "SteinAndRapoport", "Grudger", "Davis", "RevisedDowning", "Feld", "Joss","Tullock", "Random" ]

firstgen_strategies_axl = [  axl.Cooperator(),
                    axl.Alternator(),
                    axl.TitForTat(),
                    axl.FirstByTidemanAndChieruzzi(),
                    axl.FirstByNydegger(),
                    axl.FirstByGrofman(),
                    axl.FirstByShubik(),
                    axl.FirstBySteinAndRapoport(),
                    axl.Grudger(),
                    axl.FirstByDavis(),
                    axl.RevisedDowning(),
                    axl.FirstByFeld(),
                    axl.FirstByJoss(),
                    axl.FirstByTullock(),
                    axl.Random() ]
###
#################### FUNCTION FOR ONE MATCH      
###
def custom_nrof_mathches (p1, p2, matches, turns):
    ''' 
        For playing N number custom matches between 2 players.
        Also gathers different statistics. 
    '''

    players = (p1, p2) 
    turns =  turns
    match = axl.Match(players, turns=turns)
    p1_wins = 0
    p2_wins = 0
    eq = 0
    results = []

    for m in range(matches):
        match.play()
        if match.winner() == p1:
            p1_wins += 1
        if match.winner() == p2:
            p2_wins += 1
        elif match.winner() == False:
            eq += 1 
    results = [p1_wins, p2_wins, eq]

    return results

###
#################### PLAY A RAND. NUMBER OF MATCHES AND TURNS FOR A NUMBER OF RUNS      
###
def playall_random(strategies_text, strategies_type, run):
    '''
        Description:
            The same implementation as playall_fixed.py.
            It uses random generated number for the number of matches and turns.
        Motivation:
            To simulate the concept of infinity random generated numbers are used
            which are higher than 100k for matches and turns.
        Results:
            Inside the table at every specific column and row you will find a list having the 
            following format: [P1wins, P2wins, Equalities]
    '''
    # the no. of runs is used in order to 
    matches_min = run
    matches_max = run*1000
    turns_min = run
    turns_max =  run*100

    str_table =[]
    fixed_counter = 0
    rotating_counter = 0
    
    results = [0, 0, 0]
    winners_DF = pd.DataFrame(str_table, index=strategies_text, columns=strategies_text)
    normed_DF = pd.DataFrame(str_table, index=strategies_text, columns=strategies_text)

    for s1 in strategies_type:
        fixed_s = s1
        rotating_counter = 0
        for s2 in strategies_type:
            random_matches = random.randrange(matches_min, matches_max, 1)
            random_turns = random.randrange(turns_min, turns_max, 1)
            rotating_s = s2
            results = list(map(operator.add, results, custom_nrof_mathches(fixed_s, rotating_s, random_matches, random_turns)))
            normed_res = normalisation(results, random_matches)
            winners_DF.at[ strategies_text[fixed_counter], strategies_text[rotating_counter] ] = results
            normed_DF.at[ strategies_text[fixed_counter], strategies_text[rotating_counter]] = normed_res
            rotating_counter += 1
        fixed_counter += 1

    results_path = "/tmp/results/run_{}_{}_{}".format(run, random_matches, random_turns)
    print("Results for current run: {}".format(results_path))
    os.makedirs(results_path, exist_ok=True)
    os.chdir(results_path)
    normed_DF.to_csv("normed_m{}_t{}.csv".format(random_matches, random_turns))
    winners_DF.to_csv("m{}_t{}.csv".format(random_matches, random_turns))
###
###################### AUX FUNCTIONS 
### 
def normalisation(results, matches):
    """
    Normalize game results in percentage.
    """
    normed_results = []
    for res in results:
        norm = int(res)/sum(results)
        normed_results.append(norm*100)

    return normed_results
###
#################### MAIN DESCRIPTION
###
def main(random, runs):
    if random == False:
        print("Only random mode available.")
    elif random == True:
        for el in runs:
            if el == 0:
                el = el + 1
                playall_random( firstgen_strategies_str,
                                firstgen_strategies_axl,
                                el 
                                )
            else:
                playall_random( firstgen_strategies_str,
                                firstgen_strategies_axl,
                                el 
                                )

###
#################### MAIN EXECUTION
###
if __name__ == '__main__':
    """
    Main function for round robin tournaments between specified strategies.
    See help for better understanding and usability.
    See roundrobin_logic.py for how to use it properly or the README file.
    """

    # Create parser and add arguments.
    parser = argparse.ArgumentParser(description="Main function for runnnig round robin tournaments.")

    parser.add_argument("--random", "-r", help="For randomly generating a the number of matches and the numbers of turns in a match.", default=False, type=bool)
    parser.add_argument("--runs", "-it", help=" No. of times a Monte Carlo analysis is run. ", default=50, type=int)

    my_args = parser.parse_args()
    turns = my_args.turns
    matches = my_args.matches
    random = my_args.random
    runs = my_args.runs

    range_run = range(runs)

    ### MAIN ###
    main(random, range_run)
