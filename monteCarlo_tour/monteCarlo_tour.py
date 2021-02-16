#/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

'''
One module to rule them all!
'''

import time, os, operator
import argparse
import numpy as np
import pandas as pd

import axelrod as axl

from players import secondgen_str_type_w_alt as strategy_type
from players import secondgen_str_text_w_alt as strategy_text

avrg_win_df = pd.DataFrame(index=strategy_text, columns=strategy_text)
avrg_norm_df = pd.DataFrame(index=strategy_text, columns=strategy_text)

#### VARS FOR PROBABILISTIC DISTRIBUTION
mean_m = 1000
#dev_m = 0
mean_t = 200
dev_t = 40

tour_type = "second_w_alt"
###
#################### FUNCTION FOR ONE MATCH      
###
def custom_nrof_mathches (p1, p2, matches):
    ''' 
        Plays N matches and N turns with random inputs.
        Also gathers statistics. 
    '''

    players = (p1, p2) 

    p1_wins = 0
    p2_wins = 0
    eq = 0
    results = []

    for m in range(matches):
        if dev_t is None:
            turns = mean_t
        else:
            turns = int(np.random.default_rng().normal(mean_t, dev_t, None))
        match = axl.Match(players, turns=turns)
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
    '''
    fc = 0

    #matches = int(np.random.default_rng().normal(mean_m, dev_m, None))
    matches = mean_m
    turns = mean_t
    
    winners_DF = pd.DataFrame( index=strategy_text, columns=strategy_text)
    normed_DF = pd.DataFrame( index=strategy_text, columns=strategy_text)
    
    results = [0, 0, 0]

    for s1 in strategy_type:
        fixed_s = s1
        rc = 0
        for s2 in strategy_type:
            rotating_s = s2
            results = list(map(operator.add, results, custom_nrof_mathches(fixed_s, rotating_s, matches)))
            normed_res = normalisation(results, matches)
            winners_DF.at[ strategy_text[fc], strategy_text[rc] ] = results
            normed_DF.at[ strategy_text[fc], strategy_text[rc]] = normed_res
            rc += 1
            results = [0, 0, 0]
        fc += 1
        results = [0, 0, 0]
    if not os.path.exists('results_{}/single_results_{}_{}_dev{}'.format(tour_type, mean_m, mean_t, dev_t)):
        os.makedirs('results_{}/single_results_{}_{}_dev{}'.format(tour_type, mean_m, mean_t, dev_t))
    local_results_path = "results_{}/single_results_{}_{}_dev{}".format(tour_type, mean_m, mean_t, dev_t)

    normed_DF.to_csv("{}/normed_m{}_t{}_dev{}.csv".format(local_results_path ,matches, turns, dev_t))
    winners_DF.to_csv("{}/winners_m{}_t{}_dev{}.csv".format(local_results_path, matches, turns, dev_t))

    sum_results(run ,winners_DF, normed_DF)

def sum_results(run, winners_DF, normed_DF):
    """ 
    Addition of elements in a pd object.
    """
    fc = 0
    for s1 in strategy_type: # fixed
        rc = 0
        for s2 in strategy_type: # rotating
            avrg_win_df.at[strategy_text[fc], strategy_text[rc]] = list( 
                map(operator.add, avrg_win_df.at[strategy_text[fc], strategy_text[rc]], 
                    winners_DF.at[strategy_text[fc], strategy_text[rc]] ))
            avrg_norm_df.at[strategy_text[fc], strategy_text[rc]] = list( 
                map(operator.add, avrg_norm_df.at[strategy_text[fc], strategy_text[rc]], 
                    normed_DF.at[strategy_text[fc], strategy_text[rc]] ))
            rc += 1
        fc += 1
###
###################### AUX FUNCTIONS 
### 

def avg_to_file(run):
    """
    Write pd objects containing the averages to csv file.
    """
    if not os.path.exists('results/avg_results_5000_200'):
        os.makedirs('results/avg_results_5000_200')
    avg_results_path = "results/avg_results_5000_200"
    
    avrg_win_df.to_csv("{}/winners_avg_{}.csv".format(avg_results_path, run))
    avrg_norm_df.to_csv("{}/normed_avg_{}.csv".format(avg_results_path, run))

def init_avg_pds():
    """
    Inits every element of the pd dataframe with: [0,0,0]
    """
    fc = 0
    for s1 in strategy_type:
        fixed_s = s1
        rc = 0
        for s2 in strategy_type:
            rotating_s = s2
            avrg_win_df.at[strategy_text[fc], strategy_text[rc]] = [0,0,0]
            avrg_norm_df.at[strategy_text[fc], strategy_text[rc]] = [0,0,0]
            rc += 1
        fc += 1

def pd_elements_division(runs):
    """
    Inits every element of the pd dataframe with: [0,0,0]
    """
    run_list = [runs, runs, runs]
    fc = 0
    for s1 in strategy_type:
        fixed_s = s1
        rc = 0
        for s2 in strategy_type:
            rotating_s = s2
            avrg_win_df.at[strategy_text[fc], strategy_text[rc]] = list( 
                map(operator.truediv, avrg_win_df.at[strategy_text[fc], strategy_text[rc]], run_list ))
            avrg_norm_df.at[strategy_text[fc], strategy_text[rc]] = list( 
                map(operator.truediv, avrg_norm_df.at[strategy_text[fc], strategy_text[rc]], run_list ))
            rc += 1
        fc += 1

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
    print(len(strategy_type))
    print(len(strategy_text))
    if random == False:
        print("Only random mode available.")
    elif random == True:
        print("Initializing pds for average results...")
        init_avg_pds()
        print("Running simulations...")
        for el in range(runs):
            if el == 0:
                el = el + 1
                playall_random(el)
            else:
                playall_random(el)
    print("Dividing elements...")
    pd_elements_division(runs)
    print("Writing to file...")
    avg_to_file(runs)

#    for strategy in strategy_text:
#        for i, row in avrg_norm_df.iterrows():
#            print(strategy_text)
#            print(type(row[strategy]))
#            print(row[strategy])

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
    parser = argparse.ArgumentParser(
        description="Main function for runnnig round robin tournaments.")

    parser.add_argument("--random", "-r", 
        help="For randomly generating a the number of matches and the numbers of turns in a match.", 
        default=True, type=bool)
    parser.add_argument("--runs", "-R", 
        help=" No. of times a Monte Carlo analysis is run. ", 
        default=1, type=int)
    
    my_args = parser.parse_args()
    random = my_args.random
    runs = my_args.runs

    ### MAIN ###
    main(random, runs)
