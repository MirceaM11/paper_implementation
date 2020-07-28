#!/bin/bash

RUNS=$1
WAIT=$((1 + RANDOM % 60))
for i in {1..$RUNS}; 
do
    echo "Running script in $WAIT seconds."
    sleep $WAIT
    python /srv/pyCode/infinite-strategies-env/src/infinite_strategies/round_robin.py -r TRUE
    echo "Done";
done