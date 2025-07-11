#!/bin/bash
# this should be run in a system, in the same network where the flask app is.

# URL of your Flask app (use container DNS name if inside Docker Compose)
APP_URL="http://flask-metrics-logger:5000" # container name 

# RANDOM is a built-in shell variable in bash
# RANDOM returns a random integer between 0 and 32767 every time it's used.

# Infinite loop to simulate real traffic
while true; do
  # Randomly choose between / and /slow
  if (( RANDOM % 2 )); then
    ENDPOINT="/"
  else
    ENDPOINT="/slow"
  fi

  echo "Hitting endpoint: $ENDPOINT"
  
  # Make the request and discard output
  curl -s "$APP_URL$ENDPOINT" > /dev/null

  # Sleep for a random time between 1 and 5 seconds
  SLEEP_TIME=$((RANDOM % 5 + 1))
  echo "Sleeping for $SLEEP_TIME seconds..."
  sleep $SLEEP_TIME
done
