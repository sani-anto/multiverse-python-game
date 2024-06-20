from player import Player
from actions import slash, kick, heal, taunt

class Warrior(Player):
    def __init__(self,
                name: str, 
                strength: int, 
                dexterity: int, 
                constitution: int, 
                intelligence: int, 
                wisdom: int, 
                charisma: int):
        Player.__init__(self, 
                 name, 
                 strength, 
                 dexterity, 
                 constitution, 
                 intelligence, 
                 wisdom, 
                 charisma)
        self.vocation = "Warrior"
        self.actions = {"Slash": {
                            "func": slash,
                            "mod": self.get_modifier("strength")
                            },
                        "Kick": {
                            "func": kick,
                            "mod": self.get_modifier("strength")
                            }, 
                        "Heal": {
                            "func": heal,
                            "mod": self.get_modifier("wisdom")
                            },
                        "Taunt": {
                            "func": taunt,
                            "mod": self.get_modifier("charisma")
                            }
                        }


    def __str__(self):
        return f'''
---------------------------------------------
Hero Name: {self.name}
Vocation:  {self.vocation}
    HP:  {self.current_hp}/{self.max_hp}
    Str: {self.stats["strength"]["value"]}
    Dex: {self.stats["dexterity"]["value"]}
    Con: {self.stats["constitution"]["value"]}
    Int: {self.stats["intelligence"]["value"]}
    Wis: {self.stats["wisdom"]["value"]}
    Cha: {self.stats["charisma"]["value"]}
---------------------------------------------
        '''