import time
import axelrod as axl
import argparse
import pprint

def custom_match(p1, p2, t):
    """ Function for playing custom matches between 2 players.
        Displays stats like:
            - rounds won by a strategy
            - the winner
            - final scores based on utility
            - final scores per turn
            - number of cooperations
            - number of cooperations normalized/turn
    """
    
    #print ("The players are: {} with the format {} ".format(p1, type(p1)))
    #print ("The players are: {} with the format {} ".format(p2, type(p2)))

    players = (p1, p2) 
    turns =  t

    print ("The players are: {} ".format(players))
    print ("The players are: {} ".format(turns))
    
    match = axl.Match(players, turns=turns)
    match.play()
    print(match.sparklines(c_symbol='|', d_symbol='-'))
    print ("The statistics for 200 rounds are: ")
    winner = match.winner()
    print ("---> The winner is: {}".format(match.winner()))
    final_score  = match.final_score()
    print ("---> Final scores are: {} ".format(final_score))
    fs_per_turn = match.final_score_per_turn()
    print ("---> Final scores per turn are: {} ".format(fs_per_turn))
    coop = match.cooperation()
    print ("---> The number of times each strategy cooperated: {}".format(coop))
    normed_coop =match.normalised_cooperation()
    print ("---> Coopertation normalized per turn: {}".format(normed_coop))

def custom_nrof_mathches (p1, p2, matches, turns):
    """For playing N number custom matches between 2 players.
        Also gathers different statistics."""
    #print("Inside sml & custom_nrof ")
    #print("no. of matches: {}".format(matches))
    #print("no. of turns: {}".format(turns))
    players = (p1, p2) 
    turns =  turns
    match = axl.Match(players, turns=turns)
    p1_wins = 0
    p2_wins = 0
    eq = 0
    results = []

    for m in range(matches):
        #print(m)
        match.play()
        #print(match.sparklines(c_symbol='|', d_symbol='-'))
        #print (" The winner is: {}".format(match.winner()))
        if match.winner() == p1:
            p1_wins += 1
        if match.winner() == p2:
            p2_wins += 1
        elif match.winner() == False:
            eq += 1 
        #print ("---> Final scores are: {}".format(match.final_score()))
    #print ("P1 has won: {}, P2 has won: {}, Equality: {}".format(p1_wins, p2_wins, eq))
    results = [p1_wins, p2_wins, eq]
    print(results)
    return results
    #print ("Total final scores per matches : {}".format())
             
def custom_nrof_mathches_output (p1, p2, c_turns, nr_m):
    """For playing N number custom matches & T number of turns between 2 players.
        Also gathers different statistics."""
    
    players = (p1, p2) 
    turns =  c_turns
    match = axl.Match(players, turns=turns)
    p1_wins = 0
    p2_wins = 0
    eq = 0
    results = []

    for m in range(nr_m):
        match.play()
        print(match.sparklines(c_symbol='|', d_symbol='-'))
        print (" The winner is: {}".format(match.winner()))
        if match.winner() == p1:
            p1_wins += 1
        if match.winner() == p2:
            p2_wins += 1
        elif match.winner() == False:
            eq += 1 
        print ("---> Final scores are: {}".format(match.final_score()))

    print ("P1 has won: {}, P2 has won: {}, Equality: {}".format(p1_wins, p2_wins, eq))
    results = [p1_wins, p2_wins, eq]
    return results
    print ("Total final scores per matches : {}".format())
             