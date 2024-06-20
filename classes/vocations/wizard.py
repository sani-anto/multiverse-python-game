from classes.entity import Entity
from classes.actions import fireball, icefan, meteor, heal
from classes.dice import d4, d6, d8, d10, d12, d20

class Wizard(Entity):
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
        self.vocation = "Wizard"
        self.actions = {"Fireball": {
                            "func": fireball,
                            "mod": self.get_modifier("intelligence"),
                            "die": d8
                            },
                        "Ice Fan": {
                            "func": icefan,
                            "mod": self.get_modifier("wisdom"),
                            "die": d4
                            }, 
                        "Meteor": {
                            "func": meteor,
                            "mod": self.get_modifier("intelligence"),
                            "die": d12
                            },
                        "Heal": {
                            "func": heal,
                            "mod": self.get_modifier("wisdom"),
                            "die": d6
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