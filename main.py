from vocations.warrior import Warrior
from vocations.wizard import Wizard
from random import randint



def main_game():
    print("NEW ADVENTURE")
    player = create_player()
    print(player)
    begin_combat(player)

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

def begin_combat(player):
    print("You've been ambushed!")
    turn_count = 0

    while player.current_hp != 0:
        turn_count += 1
        print(f"\nTurn {turn_count}:\nWhat do you do?")
        for action in player.actions:
            print(action)

        turn_action = input("\n").capitalize()
        while turn_action not in player.actions:
            input("Please choose a valid action\n").capitalize()
        
        player.actions[turn_action]["func"](player.actions[turn_action]["mod"])



main_game()
