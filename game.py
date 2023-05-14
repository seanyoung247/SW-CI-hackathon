
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


def create_stat_sheet(player, character, weapon, modifer):
    """ 
    Creates the final round stat and modifier stat to be sent to resolver function 
    """
    pass


def resolve_round(player1, player2):
    """
    Takes player 1 and 2 stats and returns the battle results
    """
    pass


def check_victory(round_result):
    pass