from classes.entity import Entity
from classes.actions import slash, kick, heal, taunt
from classes.dice import d4, d6, d8, d10, d12, d20

class Warrior(Entity):
    def __init__(self,
                name: str, 
                strength: int, 
                dexterity: int, 
                constitution: int, 
                intelligence: int, 
                wisdom: int, 
                charisma: int):
        Entity.__init__(self, 
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
                            "mod": self.get_modifier("strength"),
                            "die": d8
                            },
                        "Kick": {
                            "func": kick,
                            "mod": self.get_modifier("strength"),
                            "die": d4
                            }, 
                        "Heal": {
                            "func": heal,
                            "mod": self.get_modifier("wisdom"),
                            "die": d6
                            },
                        "Taunt": {
                            "func": taunt,
                            "mod": self.get_modifier("charisma"),
                            "die": d20
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
