import pandas as pd

def get_pokemon_attack_cost(pokemon_id: int) -> int:
    
    pokemon_info = pd.read_csv('./utils/Card_Data.csv')

    all_attack_costs = pokemon_info.loc[pokemon_info['Card ID'] == pokemon_id, 'Cost']

    int_costs = []

    for cost_string in all_attack_costs:
        if pd.isna(cost_string):
            int_costs.append(0)
        else:
            total_energy = cost_string.count('{') + cost_string.count('●')
            int_costs.append(total_energy)

    biggest_attack_cost = max(int_costs)

    return biggest_attack_cost