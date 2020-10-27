'''
One module to rule thema all!

TODO: Speed improvements.
'''

import time, os, operator
import argparse
import numpy as np
import pandas as pd

import axelrod as axl

###
### VARIABLES 
### DICTS FOR REPRESENTING STRATEGIES
###
winners_DF = pd.DataFrame()
normed_DF = pd.DataFrame()

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
#### ORDER MUST BE THE SAME AS FIRSTEN_STR TYPE
firstgen_str_text = ["Cooperator", "Alternator", "TitForTat", "TidemanAndChieruzzi", "Nydegger", "Grofman",
                "Shubik", "SteinAndRapoport", "Grudger", "Davis", "RevisedDowning", "Feld", "Joss","Tullock", "Random" ]

 #### ORDER MUST BE THE SAME AS FISTGEN STR STR(TEXT)
firstgen_str_type = [   axl.Cooperator(),   
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
        For playing M matches and N turns with random inputs.
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
def playall_random(run):
    '''
        Numpy random Gaussian used to generate random nr. of 
        matches and turns.
        Uses pandas dataframe objects for storing the results.
        Exports dataframes to csv files.
        TODO: Pandas obj are used quite inneficently.
    '''
    str_table =[]
    fixed_counter = 0
    rotating_counter = 0

    matches = int(np.random.default_rng().normal(200, 5, None))
    turns = int(np.random.default_rng().normal(100, 5, None))
    
    results = [0, 0, 0]

    winners_DF = pd.DataFrame(str_table, index=firstgen_str_type, columns=firstgen_str_text)
    normed_DF = pd.DataFrame(str_table, index=firstgen_str_type, columns=firstgen_str_text)

    for s1 in firstgen_str_type:
        fixed_s = s1
        rotating_counter = 0
        for s2 in firstgen_str_type:
            rotating_s = s2
            results = list(map(operator.add, results, custom_nrof_mathches(fixed_s, rotating_s, matches, turns)))
            normed_res = normalisation(results, matches)
            winners_DF.at[ firstgen_str_text[fixed_counter], firstgen_str_text[rotating_counter] ] = results
            normed_DF.at[ firstgen_str_text[fixed_counter], firstgen_str_text[rotating_counter]] = normed_res
            rotating_counter += 1
            results = [0, 0, 0]
        fixed_counter += 1
        results = [0, 0, 0]

    results_path = "/tmp/results/run_{}_{}_{}".format(run, matches, turns)
    print("Results for current run: {}".format(results_path))
    os.makedirs(results_path, exist_ok=True)
    os.chdir(results_path)
    normed_DF.to_csv("normed_m{}_t{}.csv".format(matches, turns))
    winners_DF.to_csv("m{}_t{}.csv".format(matches, turns))

###
###################### AUX FUNCTIONS 
### 

def sum_results():
    """
    Addition of elements in a pd object.
    """
    fixed_counter = 0
    for s1 in firstgen_str_type:
        fixed_s = s1
        rotating_counter = 0
        for s2 in firstgen_str_type:
            rotating_s = s2
            ### sum the elements of 2 lists inside the pd
            win_mem = winners_DF.at[firstgen_str_text[fixed_counter], firstgen_str_text[rotating_counter]]
            nor_mem = normed_DF.at[firstgen_str_text[fixed_counter], firstgen_str_text[rotating_counter]]
            
            #TODO: DO THE SUM OF LISTS

            rotating_counter += 1
        fixed_counter += 1
        results = [0, 0, 0]    

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
#################### MAIN LOGIC
###
def main(random, runs):
    if random == False:
        print("Only random mode available.")
    elif random == True:
        for el in range(runs):
            if el == 0:
                el = el + 1
                playall_random( firstgen_str_text,
                                firstgen_str_type,
                                el 
                                )         
            else:
                playall_random( firstgen_str_text,
                                firstgen_str_type,
                                el 
                                )
        sum_results()

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

    parser.add_argument("--random", "-r", help="For randomly generating a the number of matches and the numbers of turns in a match.", default=True, type=bool)
    parser.add_argument("--runs", "-R", help=" No. of times a Monte Carlo analysis is run. ", default=5, type=int)

    my_args = parser.parse_args()
    random = my_args.random
    runs = my_args.runs

    ### MAIN ###
    main(random, runs)
