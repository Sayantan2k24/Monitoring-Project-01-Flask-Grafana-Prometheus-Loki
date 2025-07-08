import random
import time

def get_random_value(array):
    return random.choice(array) # picking random value

def do_some_heavy_task():
    ms = get_random_value([100, 150, 200, 300, 600, 500, 1000, 1400, 2500]) # getting random value
    should_throw_error = get_random_value([1, 2, 3, 4, 5, 6, 7, 8]) == 8 # comparision

    if should_throw_error: # bool value # as comparing the random value with 8
        
        # call the get_random_value function
        random_error = get_random_value([
            "DB Payment Failure", # these are the possible errors
            "DB Server is Down",
            "Access Denied",
            "Not Found Error"
        ])
        raise Exception(random_error) # raising the encounterred error as Exception

    time.sleep(ms / 1000.0)  # delay simulation
    return ms  # Returning the time taken in ms
