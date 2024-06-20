from classes.dice import d20

# check if move hit
# might need to move function into main file so that enemies can also use it
def hit():
    # Can add Critical Hits in future
    if d20.roll()["result"] >= 10:
        return True
    else:
        return False

# list of different actions
# kept as seperate functions in-case special effects added later on (e.g. Slash not only damages, but also bleeds)
# also some actions can be used by multiple vocations (e.g. heal is used by both Warrior & Wizard) 
def slash(mod, roll):
    damage = mod + roll["result"]
    if hit():
        print(f"Slashed for {damage}!")
        return damage
    else:
        print("Missed!")
        return 0

def kick(mod, roll):
    damage = mod + roll["result"]
    if hit():
        print(f"Kicked for {damage}!")
        return damage
    else:
        print("Missed!")
        return 0

def heal(mod, roll):
    heal = mod, roll["result"]
    print(f"Healed for {heal}!")

def taunt(mod, roll):
    if roll["critical_success"]:
        print("Taunt success!")
    elif roll["critical_success"] or ((roll["result"] + mod) < 10):
        print("Taunt failed")

def fireball(mod, roll):
    damage = mod + roll["result"]
    if hit():
        print(f"Burned for {damage}!")
        return damage
    else:
        print("Missed!")
        return 0
    
def icefan(mod, roll):
    damage = mod + roll["result"]
    if hit():
        print(f"Frozen for {damage}!")
        return damage
    else:
        print("Missed!")
        return 0
    
def meteor(mod, roll):
    damage = mod + roll["result"]
    if hit():
        print(f"Demolished for {damage}!")
        return damage
    else:
        print("Missed!")
        return 0