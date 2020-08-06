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

docker build --cpuset-cpus 1 -t paper:test0.1 .  
docker run -it [name][tag]
/srv/pyCode/infinite-strategies-env/src/infinite_strategies/logic

## Runtime ##

main.sh -- responsible for running multiple simulations
docker-compose -- to start the container and run it independently

'''
random_matches = random.randrange(10000, 50000, 1)
random_turns = random.randrange(80000, 100000, 1)
'''