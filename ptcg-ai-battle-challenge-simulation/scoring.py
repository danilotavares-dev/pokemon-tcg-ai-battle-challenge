
def score_attack(option: dict, state: dict) -> int:
    if state["can_evolve"]:
        return 7000
        
    return 10000

def score_evolution(option: dict, state: dict) -> int:
    return 8000

def score_play_basic(option: dict, state: dict) -> int:
    return 1000

def score_end_turn(option: dict, state: dict) -> int:
    return 100

def score_energy_active_pokemon(option: dict, state: dict) -> int:
    if option.get("inPlayArea") == 4:
        if state['current_energies'] < state['target_energies']:
            return 1000
        
        return -1000

    return 400
