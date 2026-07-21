import scoring

def calculate_score(option: dict, state: dict) -> int:

    option_type = option["type"]

    if option_type == 8:
        return scoring.score_energy_active_pokemon(option, state)

    if option_type == 7:
        return scoring.score_play_basic(option, state)

    if option_type == 9:
        return scoring.score_evolution(option, state)

    if option_type == 13:
        return scoring.score_attack(option, state)

    if option_type == 14:
        return scoring.score_end_turn(option, state)

    return 0