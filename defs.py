

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
        'weapon': 'blue_sabre',             # Default Weapon
    },
    'yoda': {
        'name': 'Yoda',
        'image': 'image_name.jpg',
        'affiliation': 'jedi',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'blue_sabre',
    },
    'luke_skywalker': {
        'name': 'Luke Skywalker',
        'image': 'image_name.jpg',
        'affiliation': 'jedi',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'blue_sabre',
    },
    'mace_windu': {
        'name': 'Mace Windu',
        'image': 'image_name.jpg',
        'affiliation': 'jedi',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'blue_sabre',
    },
    'qui_gon': {
        'name': 'Qui Gon Jinn',
        'image': 'image_name.jpg',
        'affiliation': 'jedi',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'blue_sabre',
    },
    # Sith: Emperor Palpatine, Darth Vader, Darth Maul, Count Dooku, Kylo Ren
    'palpatine': {
        'name': 'Emperor Palpatine',
        'image': 'image_name.jpg',
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
        'image': 'image_name.jpg',
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
        'image': 'image_name.jpg',
        'affiliation': 'sith',
        'strength': 30,
        'skill': 25,
        'agility': 20,
        'vitality': 50,
        'health': 50,
        'weapon': 'red_double',
    },
    'count_dooku': {
        'name': 'Count Dooku',
        'image': 'image_name.jpg',
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
        'image': 'image_name.jpg',
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
        'red_double' : {
            'name': 'Double Red Light Sabre',
            'modifiers': [
                {
                    'stat': 'strength',
                    'display': 'Strength +10%',
                    'value': 1.1,
                },
                {
                    'stat': 'agility',
                    'display': 'Agility -10%',
                    'value': 0.9,
                }
            ]
        },
    }
}


MODIFIERS = {
    # Modifiers for any faction
    'strength': {                           # Modifier unique ID
        'name': 'Force Strength',           # Display name
        'affiliation': None,                # Power affiliation. Only Jedi can use jedi power etc
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
        'affiliation': None,
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
        'affiliation': None,
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
    # Jedi only powers
    'push': {
        'name': 'Force Push',
        'affiliation': 'jedi',
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
        'affiliation': 'jedi',
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
    # Sith only modifiers
    'bolts': {
        'name': 'Force Lightning',
        'affiliation': 'sith',
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
        'affiliation': 'sith',
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

