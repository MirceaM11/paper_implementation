# Monte Carlo Tournament #

Implementation for Master's Thesis.

# Implementation #

Check monteCarlo_tour.py docstrings.

## Purpose ##

Pin strategies against each other for a random number of turns and matches.  
Outputs the results in a df which is further exported into csv format.  
Results in local tmp folder.

## Experiments ##

Run multiple automated tournaments to see how the strategies behave in the  
unknown random situations.


## Commands ##
detach:  
screen -D -R  
nohup python3 round_robin.py -r TURE --runs 30 > /dev/null 2>&1 &  
reaatach  
screen -D -R  
