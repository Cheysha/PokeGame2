from random import random
from Util import *
from Classes import *
from datetime import datetime
from time import sleep
import random



def get_pokemon(index):
    if type(index) == str:
        index = index.lower()
        index = int(poke_list.loc[poke_list['identifier'] == index]['id'].values[0])

    index = int(index)

    '''
            data frames for our pokemon
    '''
    p = poke_list.loc[poke_list['id'] == index]

    s = stat_list.loc[stat_list['pokemon_id'] == index]

    m = moveset_list.loc[moveset_list['pokemon_id'] == index]

    m = move_list.loc[move_list['id'].isin(m['move_id'])]

    '''
        setting up our pokemon
    '''
    level = 100
    name = p['identifier'].values[0]
    _type = TYPES(type_list.loc[type_list['pokemon_id'] == index]['type_id'].values[0])

    hp = int(s.loc[s['stat_id'] == STATS.HP.value]['base_stat'].values[0])
    attack = int(s.loc[s['stat_id'] == STATS.ATTACK.value]['base_stat'].values[0])
    defense = int(s.loc[s['stat_id'] == STATS.DEFENSE.value]['base_stat'].values[0])
    sp_attack = int(s.loc[s['stat_id'] == STATS.SPECIAL_ATTACK.value]['base_stat'].values[0])
    sp_defense = int(s.loc[s['stat_id'] == STATS.SPECIAL_DEFENSE.value]['base_stat'].values[0])
    speed = int(s.loc[s['stat_id'] == STATS.SPEED.value]['base_stat'].values[0])

    '''
        creating our pokemon
    '''
    generated_pokemon = Pokemon(name=name, index=index, type=_type, level=level, base_attack=attack, base_special_attack=sp_attack,
                   base_defense=defense, base_special_defense=sp_defense, base_speed=speed, base_hp=hp)

    '''
        adding moves to our pokemon, will need completly redone to use get_move
    '''
    for i in range(4): #gets 4 random moves
        temp = m.sample(1)['identifier'].values[0]
        move = get_move(temp)
        generated_pokemon.set_move(move)

    ''' 
        returning our pokemon
    '''

    return generated_pokemon
def get_move(index):
    if type(index) == str:
        index = index.lower()
        # replace spaces with -
        index = index.replace(' ', '-')
        index = int(move_list.loc[move_list['identifier'] == index]['id'].values[0])

    index = int(index)

    m = move_list.loc[move_list['id'] == index]

    move = Move(name=m['identifier'].values[0], index=int(m['id'].values[0]), type=TYPES(m['type_id'].values[0]),
                power=m['power'].values[0], accuracy=m['accuracy'].values[0], pp=m['pp'].values[0],
                category=CATEGORY(m['damage_class_id'].values[0]))

    return move

def new_player(name):
    BAG_SIZE = 3
    def gen_random_trainer():
        player = Trainer(name='random')
        for i in range(BAG_SIZE):
            player.add_pokemon(get_pokemon(random.randint(1, 340)))

        player.set_current_pokemon(player.pokemon_list[0])
        return player

    if name == 'random':
        return gen_random_trainer()

    ''' 
        creating a new player
    '''
    player = Trainer(name=name)

    '''
        asking for input
    '''
    i = 0
    while i < BAG_SIZE:
        player_input = input('Enter a Pokemon name: ')

        if player_input.isdigit():
            player_input = int(player_input)

        if player_input == 'random':
            player.add_pokemon(get_pokemon(random.randint(1, 340)))
            i += 1

        elif is_valid_pokemon(player_input):
            player.add_pokemon(get_pokemon(player_input))
            i += 1

        else:
            print('Invalid Pokemon')

    '''
        return the player
    '''
    player.set_current_pokemon(player.pokemon_list[0])
    return player




if __name__ == '__main__':
    pass