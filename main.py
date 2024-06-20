import json
from random import randint
from time import sleep

from classes.entity import Entity
from classes.vocations.warrior import Warrior
from classes.vocations.wizard import Wizard
from classes.dice import d4, d6, d8, d10, d12, d20


def main_game():
    score = 0

    sleep(text_delay)
    print("\nNEW ADVENTURE")
    player = create_player()
    sleep(text_delay)
    print(player)

    while player.current_hp > 0:
        begin_combat(player, create_creature())
        score += 10

    print(f"Score: {score}")


def create_player():
    sleep(text_delay)
    player_name = input("Please Enter Your Name: ")
    sleep(text_delay)
    player_class = input("Are you a Wizard or a Warrior?\n").lower()

    while player_class not in ["wizard", "warrior"]:
        sleep(text_delay)
        player_class = input("Please choose Wizard or Warrior\n").lower()
    
    if player_class == "warrior":
        player = Warrior(name=player_name, 
                        strength=randint(8, 18), 
                        dexterity=randint(8, 18), 
                        constitution=randint(8, 18), 
                        intelligence=randint(8, 18), 
                        wisdom=randint(8, 18), 
                        charisma=randint(8, 18))
        
    elif player_class == "wizard":
        player = Wizard(name=player_name, 
                strength=randint(8, 18), 
                dexterity=randint(8, 18), 
                constitution=randint(8, 18), 
                intelligence=randint(8, 18), 
                wisdom=randint(8, 18), 
                charisma=randint(8, 18))

    return player


def create_creature():
    creature_name = f"{first_names[randint(0, len(first_names) - 1)]} {surnames[randint(0, len(surnames) - 1)]}"

    return Entity(name=creature_name, 
            strength=randint(8, 18), 
            dexterity=randint(8, 18), 
            constitution=randint(8, 18), 
            intelligence=randint(8, 18), 
            wisdom=randint(8, 18), 
            charisma=randint(8, 18))


def begin_combat(player, enemy):
    sleep(text_delay)
    print("You've been ambushed!")
    print(enemy)
    turn_count = 0

    while player.current_hp > 0 and enemy.current_hp > 0:
        turn_count += 1
        sleep(text_delay)
        print(f"\nTurn {turn_count}:\nWhat do you do?")
        for action in player.actions:
            print(action)

        turn_action = input("\n").title()
        while turn_action not in player.actions:
            turn_action = input("Please choose a valid action\n").title()
        
        # currently only works for damage actions. 
        # need to figure out system for misc actions e.g. healing, taunting
        damage = player.actions[turn_action]["func"](
            player.actions[turn_action]["mod"], 
            player.actions[turn_action]["die"].roll())
        enemy.current_hp -= damage
        sleep(text_delay)
        print(f"Enemy HP: {enemy.current_hp}/{enemy.max_hp}")

        # need to implement hit chance for enemies
        if enemy.current_hp > 0:
            damage_received = d6.roll()["result"]
            sleep(text_delay)
            print(f"You were hit for {damage_received}!")
            player.current_hp -= damage_received
            sleep(text_delay)
            print(f"Player HP: {player.current_hp}/{player.max_hp}")

    if enemy.current_hp <= 0:
        sleep(text_delay)
        print('''
       _      _                   
      (_)    | |                  
__   ___  ___| |_ ___  _ __ _   _ 
\ \ / / |/ __| __/ _ \| '__| | | |
 \ V /| | (__| || (_) | |  | |_| |
  \_/ |_|\___|\__\___/|_|   \__, |
                             __/ |
                            |___/ 
''')

    if player.current_hp <= 0:
        sleep(text_delay)
        print('''
    
    _       __           _   
    | |     / _|         | |  
__| | ___| |_ ___  __ _| |_ 
/ _` |/ _ \  _/ _ \/ _` | __|
| (_| |  __/ ||  __/ (_| | |_ 
\__,_|\___|_| \___|\__,_|\__|
                            
                            
''')



# DEFINE GLOBAL VARIABLES HERE
text_delay = 0.75

f = open('data/first-names.json')
first_names = json.load(f)
f.close()

f = open('data/names.json')
surnames = json.load(f)
f.close()

while True:
    main_game()
