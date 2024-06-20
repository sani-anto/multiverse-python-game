import json
from random import randint

from classes.entity import Entity
from classes.vocations.warrior import Warrior
from classes.vocations.wizard import Wizard

def main_game():
    print("\nNEW ADVENTURE")
    player = create_player()
    print(player)
    begin_combat(player, create_creature())

def create_player():
    player_name = input("Please Enter Your Name: ")
    player_class = input("Are you a Wizard or a Warrior?\n").lower()

    while player_class not in ["wizard", "warrior"]:
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
    print("You've been ambushed!")
    print(enemy)
    turn_count = 0

    while player.current_hp != 0:
        turn_count += 1
        print(f"\nTurn {turn_count}:\nWhat do you do?")
        for action in player.actions:
            print(action)

        turn_action = input("\n").capitalize()
        while turn_action not in player.actions:
            input("Please choose a valid action\n").capitalize()
        
        player.actions[turn_action]["func"](
            player.actions[turn_action]["mod"], 
            player.actions[turn_action]["die"].roll())

f = open('data/first-names.json')
first_names = json.load(f)
f.close()

f = open('data/names.json')
surnames = json.load(f)
f.close()

main_game()
