
import random

from deck import DECK
from pokedex import get_pokemon_attack_cost
from calculator import calculate_score

def agent(obs_dict: dict, config_dict: dict) -> list[int]:
    if obs_dict.get('select') is None:
        return DECK

    try:
        # Contagem de opções disponíveis
        options_count = len(obs_dict["select"]["option"])
        max_count = obs_dict["select"]["maxCount"]
        
        # Escolher apenas a quantidade de carta permitida
        safe_max = min(options_count, max_count)

        # Meu PlayerIndex na partida
        my_index = obs_dict['current']['yourIndex']
        #enemy_index = 1 - my_index

        if len(obs_dict['current']['players'][my_index]['active']) > 0:
            id_my_pokemon_active = obs_dict['current']['players'][my_index]['active'][0]['id']
            target_energies = get_pokemon_attack_cost(id_my_pokemon_active)
            active_pokemon = obs_dict['current']['players'][my_index]['active'][0]
            current_energies = len(active_pokemon.get('energyCards', []))
        else:
            target_energies = 0
            current_energies = 0

        state = {
            "current_energies": current_energies,
            "target_energies": target_energies,
            "options": obs_dict["select"]["option"],
            "obs": obs_dict,
            "can_attack": current_energies >= target_energies,
            "can_evolve": any(o["type"] == 9 for o in obs_dict["select"]["option"]),
            "can_play_basic": any(o["type"] == 7 for o in obs_dict["select"]["option"]),
            "bench_full": len(obs_dict["current"]["players"][my_index]["bench"]) == 5,
        }

        best_score = -999999 
        best_option_index = 0

        for index, option in enumerate(obs_dict["select"]["option"]):
            score = calculate_score(option, state)

            if score > best_score:
                best_score = score
                best_option_index = index 

        if safe_max == 1: 
            return [best_option_index]
        
        return random.sample(list(range(options_count)), safe_max)
            
    except Exception as e:
        print(f"FATAL CRASH: {e}")
        return [0]
    

    