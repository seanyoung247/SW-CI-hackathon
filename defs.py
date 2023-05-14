

CHARACTERS = {
    # Jedi: Obi-Wan Kenobi, Yoda, Luke Skywalker, Mace Windu, Qui-Gon Jin
    'obi_wan': {                            # Unique ID name
        'name': 'Obi-Wan Kenobi',           # Display name
        'image': 'image_name.jpg',          # Character image name
        'affiliation': 'jedi',              # Affiliation name
        'strength': 30,                     # Strength
        'skill': 25,                        # Weapon Skill
        'agility': 20,                      # Agility (Defence)
        'vitality': 50,                     # The full health value
        'health': 50,                       # Current health
        'weapon': 'red_sabre',              # Default Weapon
    },
    'yoda': {
        'name': 'Yoda',
        'affiliation': 'jedi',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'red_sabre',
    },
    'luke_skywalker': {
        'name': 'Luke Skywalker',
        'affiliation': 'jedi',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'red_sabre',
    },
    'mace_windu': {
        'name': 'Mace Windu',
        'affiliation': 'jedi',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'red_sabre',
    },
    'qui_gon': {
        'name': 'Qui Gon Jinn',
        'affiliation': 'jedi',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'red_sabre',
    },
    # Sith: Emperor Palpatine, Darth Vader, Darth Maul, Count Dooku, Kylo Ren
    'palpatine': {
        'name': 'Emperor Palpatine',
        'affiliation': 'sith',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'red_sabre',
    },
    'darth_vader': {
        'name': 'Darth Vader',
        'affiliation': 'sith',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'red_sabre',
    },
    'darth_maul': {
        'name': 'Darth Maul',
        'affiliation': 'sith',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'red_sabre',
    },
    'count_dooku': {
        'name': 'Count Dooku',
        'affiliation': 'sith',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'red_sabre',
    },
    'kylo_ren': {
        'name': 'Kylo Ren',
        'affiliation': 'sith',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'red_sabre',
    },
}


WEAPONS = {
    'jedi': {
        'blue_saber': {                     # Weapon Unique ID
            'name': 'Blue Light Sabre',     # Weapon display name
            'modifiers': [
                {
                    'stat': 'strength',         # Stat key to modify
                    'display': 'Strength -20%', # Display text
                    'value': 0.8,               # Modifier value to multiply stat by
                },
                {
                    'stat': 'agility',
                    'display': 'Agility +20%',
                    'value': 1.2, 
                }
            ]
        },
    },
    'sith': {
        'red_saber' : {
            'name': 'Red Light Sabre',
            'modifiers': [
                {
                    'stat': 'strength',
                    'display': 'Strength +20%',
                    'value': 1.2,
                },
                {
                    'stat': 'agility',
                    'display': 'Agility -20%',
                    'value': 0.8,
                }
            ]
        },
    }
}


MODIFIERS = {
    # Modifiers for any faction
    'any': {
        'strength': {                           # Modifier unique ID
            'name': 'Force Strength',           # Display name
            'affect': 'Increase Strength 20%',  # Affect description
            'modifiers': [
                {                               # Player modifier
                    'stat': 'strength',         # Stat to modify
                    'value': 1.2,               # The value to multiply the stat by
                },
                {                               # Challenger modifier
                    'stat': 'strength',
                    'value': 1                  # No change
                }
            ]
        },
        'skill': {
            'name': 'Force Skill',
            'affect': 'Increase Skill 20%',
            'modifiers': [
                {
                    'stat': 'skill',
                    'value': 1.2,
                },
                {
                    'stat': 'skill',
                    'value': 1
                }
            ]
        },
        'agility': {
            'name': 'Force Agility',
            'affect': 'Increase Agility 20%',
            'modifiers': [
                {
                    'stat': 'agility',
                    'value': 1.2,
                },
                {
                    'stat': 'agility',
                    'value': 1
                }
            ]
        },
    },
    # Jedi only modifiers
    'jedi': {
        'push': {
            'name': 'Force Push',
            'affect': 'Reduces opponent attack strength',
            'modifiers': [
                {
                    'stat': 'strength',
                    'value': 1,
                },
                {
                    'stat': 'strength',
                    'value': 0.5
                }
            ]
        },
        'heal': {
            'name': 'Force Heal',
            'affect': 'Increases health by 50%',
            'modifiers': [
                {
                    'stat': 'health',
                    'value': 1.5,
                },
                {
                    'stat': 'health',
                    'value': 1
                }
            ]
        },
    },
    # Sith only modifiers
    'sith': {
        'bolts': {
            'name': 'Force Lightning',
            'affect': 'Reduces opponent health by 50%',
            'modifiers': [
                {
                    'stat': 'health',
                    'value': 1,
                },
                {
                    'stat': 'health',
                    'value': 0.5
                }
            ]
        },
        'push': {
            'name': 'Force Choke',
            'affect': 'Reduces opponent defence agility',
            'modifiers': [
                {
                    'stat': 'agility',
                    'value': 1,
                },
                {
                    'stat': 'agility',
                    'value': 0.5
                }
            ]
        },
    }
}

