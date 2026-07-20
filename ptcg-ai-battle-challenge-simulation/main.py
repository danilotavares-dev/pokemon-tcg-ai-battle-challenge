# tar -czvf submission.tar.gz main.py deck.csv pokedex.py

import random

from pokedex import get_pokemon_attack_cost

def agent(obs_dict: dict, config_dict: dict) -> list[int]:
    if obs_dict.get('select') is None:
        return (
            [35] * 4 + 
            [101] * 4 + 
            [47] * 4 + 
            [50] * 4 + 
            [1086] * 4 +
            [1079] * 4 +
            [3] * 36 
        )

    try:
        # Contagem de opções disponíveis
        options_count = len(obs_dict["select"]["option"])
        max_count = obs_dict["select"]["maxCount"]
        
        # Escolher apenas a quantidade de carta permitida
        safe_max = min(options_count, max_count)

        # Meu PlayerIndex na partida
        my_index = obs_dict['current']['yourIndex']
        enemy_index = 1 - my_index

        if len(obs_dict['current']['players'][my_index]['active']) > 0:
            id_my_pokemon_active = obs_dict['current']['players'][my_index]['active'][0]['id']
            target_energies = get_pokemon_attack_cost(id_my_pokemon_active)
            current_energies = len(obs_dict['current']['players'][my_index]['active'][0]['energyCards'])
        else:
            target_energies = 0
            current_energies = 0

        best_score = -999999 
        best_option_index = 0

        for index, option in enumerate(obs_dict["select"]["option"]):
            score = 0
            
            if option["type"] == 8 and option.get("inPlayArea") == 4:
                
                if current_energies >= target_energies:
                    score = -1000
                else:
                    score = 500

            if score > best_score:
                best_score = score
                best_option_index = index 
        if safe_max == 1: 
            return [best_option_index]
        
        return random.sample(list(range(options_count)), safe_max)
            
    except Exception:
        return [0]
    

    