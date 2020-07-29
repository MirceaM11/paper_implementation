#!/bin/bash

RUNS=$1
for i in {1..$RUNS}; 
do
    WAIT=$((1 + RANDOM % 10))
    echo "Running script. Run number: ${RUNS} with wait time: ${WAIT}"
    sleep $WAIT
    python /srv/pyCode/infinite-strategies-env/src/infinite_strategies/round_robin.py -r TRUE
    echo "Done";
done