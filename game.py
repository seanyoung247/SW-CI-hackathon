
from random import randint
from defs import CHARACTERS, WEAPONS, MODIFIERS


# Stat Sheet:
# stats = {
#   player:         player unique id
#   strength:       calculated strength
#   skill:          calculated skill
#   agility:        calculated agility
#   modifiers: [
#       {
#           stat:   The player stat to modify
#           value:  Modification percentage (0 - 1)
#       },
#       {
#           stat:   The challenger stat to modify
#           value:  Modification percentage (0 - 1)
#       }
#   ]
# }


def create_stat_sheet(player, character, weapon, modifier):
    """ 
    Creates the final round stat and modifier stat to be sent to resolver function 
    """
    char_stats = CHARACTERS[character]
    weapon_stats = WEAPONS.get(char_stats['affiliation']).get(weapon)
    # Add weapon modifiers to character stats:
    if weapon_stats:
        for mod in weapon_stats['modifiers']:
            mod_stat = mod['stat']
            char_stats[mod_stat] = char_stats[mod_stat] * mod['value']

    # Retrieve the modifier in use
    mod = MODIFIERS[modifier]

    return {
        'player': player['id'],
        'strength': char_stats['strength'],
        'skill': char_stats['skill'],
        'agility': char_stats['agility'],
        'modifiers': mod[modifier]
    }


def resolve_round(player1, player2):
    """
    Takes player 1 and 2 stats and returns the battle results
    """
    pass


def check_victory(round_result):
    pass