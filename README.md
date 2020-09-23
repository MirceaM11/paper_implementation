# Master's thesis implementation #

Implementation for Master's Thesis.

# Implementation #

## Purpose ##

Pin strategies against each other for a random number of turns and matches.  
Outputs the results in a df which is further exported into csv format.  
Results can be found in src/csv_results.

Check code and docstrings for more.

## Experiments ##

Run multiple automated tournaments to see how the strategies behave in the  
unknown random situations.

## Operations ##

Use docker to run simulations with random numbers for turns and matches.  
See Dockerfile and docker-compose.

## Commands ##
detach:  
screen -D -R  
nohup python3 round_robin.py -r TURE --runs 30 > /dev/null 2>&1 &  
reaatach  
screen -D -R  
## Runtime ##

'''
random_matches = random.randrange(matches_min, matches_max, 1)
random_turns = random.randrange(tuns_min, turns_max, 1)
'''