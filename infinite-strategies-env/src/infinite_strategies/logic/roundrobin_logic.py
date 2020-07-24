import axelrod as axl 
import pandas as pd
import datetime
import random
import operator
import os 


from vars import my_vars as gv 
from logic import singlematch_logic as sml 



def playall_fixed(strategies_text, strategies_type, matches, turns):
    """
        Description:
            In order to solve the problem of creating the dataframes and playing all matches,
            I created 2 lists:
                --  strategies_text: Contains the names in string format of the strategies;
                --  strategies_type: Contains the strategies in axelrod datatype format;
        Motivation:
            The types are needed in order to run the matches in an automated format.
            The strings are needed in order to create dataframes easier.
            This will enable the possibility of running this function for different lists of 
            strategies. ATTENTION is required when building lists in the file global_vars.py,
            it is MANDATORY to have the same order of strategies in both lists. 
            See firstgen_strategies_str & firstgen_strategies_axl as an example. 
        Results:
            Inside the table at every specific column and row you will find a list having the 
            following format: [P1wins, P2wins, Equalities]
    """
    results = [0, 0, 0]
    str_table =[]
    fixed_counter = 0
    rotating_counter = 0

    now = datetime.datetime.now()
    winners_DF = pd.DataFrame(str_table, index=strategies_text, columns=strategies_text)
    normed_DF = pd.DataFrame(str_table, index=strategies_text, columns=strategies_text)

    # print(winners_DF)
    # winners_DF.to_csv("csv_results/all_matches.csv")
    

    for s1 in strategies_type:
        fixed_s = s1
        #print("Playing all matches for the fixed strategy {}...".format(strategies_text[fixed_counter]))
        rotating_counter = 0
        for s2 in strategies_type:
            print("  ---- rotating strategy ---> {}".format(strategies_text[rotating_counter]))
            rotating_s = s2
            results = list(map(operator.add, results, sml.custom_nrof_mathches(fixed_s, rotating_s, matches, turns)))
            normed_res = normalisation(results, matches)
            winners_DF.at[ strategies_text[fixed_counter], strategies_text[rotating_counter] ] = results
            normed_DF.at[ strategies_text[fixed_counter], strategies_text[rotating_counter]] = normed_res
            rotating_counter += 1
            results = [0, 0, 0]
        fixed_counter += 1
        results = [0, 0, 0]

    print("Pushing results to file...")
    results_path = "/tmp/results/run_{}".format(now.isoformat())
    print("Results for current run: {}".format(results_path))
    os.makedirs(results_path, exist_ok=True)
    os.chdir(results_path)
    normed_DF.to_csv("normed_m{}_t{}.csv".format(matches, turns))
    winners_DF.to_csv("m{}_t{}.csv".format(matches, turns))
    #print("The numer of matches won by each strategy, in the first row")
    #print(winners_DF)

def playall_random(strategies_text, strategies_type, matches, turns):
    """
        Description:
            The same implementation as playall_fixed.py.
            It uses random generated number for the number of matches and turns.
        Motivation:
            To simulate the concept of infinity random generated numbers are used
            which are higher than 100k for matches and turns.
        Results:
            Inside the table at every specific column and row you will find a list having the 
            following format: [P1wins, P2wins, Equalities]
    """

    random_matches = random.randrange(100000, 300000, 1)
    random_turns = random.randrange(100000, 300000, 1)
    str_table =[]
    fixed_counter = 0
    rotating_counter = 0

    now = datetime.datetime.now()
    winners_DF = pd.DataFrame(str_table, index=strategies_text, columns=strategies_text)
    normed_DF = pd.DataFrame(str_table, index=strategies_text, columns=strategies_text)

    # print(winners_DF)
    # winners_DF.to_csv("csv_results/all_matches.csv")

    for s1 in strategies_type:
        fixed_s = s1
        print("Playing all matches for the fixed strategy {}...".format(strategies_text[fixed_counter]))
        rotating_counter = 0
        for s2 in strategies_type:
            print(" ---- rotating strategy ---> {}".format(strategies_text[rotating_counter]))
            rotating_s = s2
            results = list(map(operator.add, results, sml.custom_nrof_mathches(fixed_s, rotating_s, matches, turns)))
            normed_res = normalisation(results, matches)
            winners_DF.at[ strategies_text[fixed_counter], strategies_text[rotating_counter] ] = results
            normed_DF.at[ strategies_text[fixed_counter], strategies_text[rotating_counter]] = normed_res
            rotating_counter += 1
        fixed_counter += 1

    print("Pushing results to file...")
    results_path = "/tmp/results/run_{}".format(now.isoformat())
    print("Results for current run: {}".format(results_path))
    os.makedirs(results_path, exist_ok=True)
    os.chdir(results_path)
    normed_DF.to_csv("normed_m{}_t{}.csv".format(matches, turns))
    winners_DF.to_csv("m{}_t{}.csv".format(matches, turns))

def playall_pll_random(strategies_text, strategies_type, matches, turns):
    """
        Description:
            The same implementation as playall_fixed.py.
            It uses random generated number for the number of matches and turns.
        Motivation:
            To simulate the concept of infinity I decided to use random generated numbers 
            which are higher than 100k for matches and turns.
        Results:
            Inside the table at every specific column and row you will find a list having the 
            following format: [P1wins, P2wins, Equalities]
    """

    random_matches = random.randrange(100000, 300000, 1)
    random_turns = random.randrange(100000, 300000, 1)
    str_table =[]
    fixed_counter = 0
    rotating_counter = 0

    now = datetime.datetime.now()
    winners_DF = pd.DataFrame(str_table, index=strategies_text, columns=strategies_text)

    # print(winners_DF)
    # winners_DF.to_csv("csv_results/all_matches.csv")

    for s1 in strategies_type:
        fixed_s = s1
        print("Playing all matches for the fixed strategy {}...".format(strategies_text[fixed_counter]))
        rotating_counter = 0
        for s2 in strategies_type:
            print(" ---- rotating strategy ---> {}".format(strategies_text[rotating_counter]))
            rotating_s = s2
            results = list(map(operator.add, results, sml.custom_nrof_mathches(fixed_s, rotating_s, matches, turns)))
            winners_DF.at[ strategies_text[fixed_counter], strategies_text[rotating_counter] ] = results
            rotating_counter += 1
        fixed_counter += 1

    print("Pushing results to file...")
    print("CSV file at: {}".format("csv_results/matches_"+now.isoformat()+".csv"))

    winners_DF.to_csv("csv_results/rand_m"+str(matches)+"_t"+str(turns)+"_{}.csv".format(now.isoformat()))
    print(winners_DF)

def normalisation(results, matches):
    """
    Normalize game results in percentage.
    """
    normed_results = []
    for res in results:
        norm = int(res)/sum(results)
        normed_results.append(norm*100)

    #print(normed_results)
    return normed_results

