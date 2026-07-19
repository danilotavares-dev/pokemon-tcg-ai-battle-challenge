import random

def agent(obs, config):
    available_options = [0, 1, 2]
    random_choice = random.choice(available_options)

    move = random_choice

    return move