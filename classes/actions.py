def slash(mod, roll):
    damage = mod + roll.result
    print(f"Slashed for {damage}!")

def kick(mod, roll):
    damage = mod + roll.result
    print(f"Kicked for {damage}!")

def heal(mod, roll):
    heal = mod, roll.result
    print(f"Healed for {heal}!")

def taunt(mod, roll):
    if roll.critical_success:
        print("Taunt success!")
    elif roll.critical_success or ((roll.result + mod) < 10):
        print("Taunt failed")