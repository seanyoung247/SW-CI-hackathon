
from random import randint
from defs import CHARACTERS, WEAPONS, MODIFIERS


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
    mod = MODIFIERS[modifier]['modifiers']
    char_stats[mod[0]['stat']] = char_stats[mod[0]['stat']] * mod[0]['value']


    return {
        'player': player['id'],
        'health': player['health'],
        'strength': char_stats['strength'],
        'skill': char_stats['skill'],
        'agility': char_stats['agility'],
        'modifier': mod[1]
    }


def resolve_round(players):
    """
    Takes player 1 and 2 stats and returns the battle results
    """
    for player in players:
        # Grab stats
        stats = player['round_stats']
        challenger = player['challenger']['round_stats']
        # print('cunt', stats, challenger)
        # Resolve modifiers
        mod = challenger['modifier']
        stats[mod['stat']] = stats[mod['stat']] * mod['value']
        # Roll hit
        roll = randint(1, 100)
        hit_percentage = (50 + (stats['skill'] - challenger['agility']))
        hit = stats['strength'] if hit_percentage < roll else 0
        player['challenger']['health'] = challenger['health'] - hit

    return players


def check_victory(players):
    if any(i <= 0 for i in (players[0]['health'], players[1]['health'])):
        # some player has died
        winner = (
            players[0]['id'] 
            if players[0]['health'] > players[1]['health'] 
            else players[1]['id']
        )
        return winner

    return False