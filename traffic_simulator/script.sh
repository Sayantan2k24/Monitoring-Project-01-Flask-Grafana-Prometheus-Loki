#!/bin/bash
while true; do

    # Run 10 instances and kill after 30 seconds
    for i in {1..10}; do
    ./simulate_traffic.sh &
    sleep 2
    pids[$i]=$!
    done

    sleep 30

    # Kill all
    for pid in "${pids[@]}"; do
    kill "$pid"
    done

    # sleep for 1 minute
    echo "sleeping for 2 minutes"
    # as we used 2 minutes window frame in the HighLatency Alert Rule
    sleep 120

done

