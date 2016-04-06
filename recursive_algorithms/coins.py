import random
from functools import partial

def is_even(elem):
    return elem % 2 == 0

def is_odd(elem):
    return not is_even(elem)

def even_exists(listing):
    return any([is_even(elem) for elem in listing])

def odd_exists(listing):
    return not even_exists(listing)

def is_bound(lower_bound,upper_bound,value):
    if value != lower_bound and value != upper_bound:
        return False
    return True
    
def get_coins(lower_bound,upper_bound):
    is_bound = partial(is_bound,lower_bound,upper_bound)
    configuration_of_coins = []
    while len(configuration_of_coins) < 5:
        potential_coin_value = random.randint(lower_bound,upper_bound)
        if is_bound(potential_coin_value): continue
        if not potential_coin_value in configuration_of_coins:
            if len(configuration_of_coins) >= 3:
                if even_exists(configuration_of_coins) and odd_exists(configuration_of_coins):
                    configuration_of_coins.append(potential_coin_value)
                elif even_exists(configuration_of_coins):
                    while is_even(potential_coin_value):
                        potential_coin_value = random.randint(lower_bound,upper_bound)
                    configuration_of_coins.append(potential_coin_value)
                elif odd_exists(configuration_of_coins):
                    while is_odd(potential_coin_value):
                        potential_coin_value = random.randint(lower_bound,upper_bound)
                    configuration_of_coins.append(potential_coin_value)
            else:    
                configuration_of_coins.append(potential_coin_value)
    return configuration_of_coins

upper_bound,lower_bound = 100,0
size_of_bound = upper_bound - lower_bound
coins = get_coins(lower_bound,upper_bound)
amount = random.randint(lower_bound+size_of_bound,upper_bound+size_of_bound)
