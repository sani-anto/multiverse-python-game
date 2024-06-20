class Player:
    def __init__(self, 
                 name: str, 
                 strength: int, 
                 dexterity: int, 
                 constitution: int, 
                 intelligence: int, 
                 wisdom: int, 
                 charisma: int):
        self.name = name
        self.stats = {
        "strength": {
            "value": strength,
            "modifier": calculate_modifier(strength)
            },
        "dexterity": {
            "value": dexterity,
            "modifier": calculate_modifier(dexterity)
            },
        "constitution": {
            "value": constitution,
            "modifier": calculate_modifier(constitution)
            },
        "intelligence": {
            "value": intelligence,
            "modifier": calculate_modifier(intelligence)
            },
        "wisdom": {
            "value": wisdom,
            "modifier": calculate_modifier(wisdom)
            },
        "charisma": {
            "value": charisma,
            "modifier": calculate_modifier(charisma)
            }
        }
        self.max_hp = 15 + self.stats["constitution"]["modifier"]
        self.current_hp = self.max_hp


    def __str__(self):
        return f'''
---------------------------------------------
Hero Name: {self.name}
    HP:  {self.current_hp}/{self.max_hp}
    Str: {self.stats["strength"]["value"]}
    Dex: {self.stats["dexterity"]["value"]}
    Con: {self.stats["constitution"]["value"]}
    Int: {self.stats["intelligence"]["value"]}
    Wis: {self.stats["wisdom"]["value"]}
    Cha: {self.stats["charisma"]["value"]}
---------------------------------------------
        '''
    

    def get_stat(self, attribute: str):
        return self.stats[attribute]["value"]
    

    def get_modifier(self, attribute: str):
        return self.stats[attribute]["modifier"]
    

    def change_stat(self, attribute: str, value: int):
        self.stats.update({
            attribute: {
            "value": value,
            "modifier": calculate_modifier(value)
            }
        })

        if attribute == "consitution":
            self.max_hp = 15 + self.stats["constitution"]["modifier"]
        
        return self.stats
    

    def lose_hp(self, dmg: int) -> int:
        self.current_hp -= dmg
        return self.current_hp

    
    
def calculate_modifier(attribute):
    modifier = (attribute - 10) // 2
    return modifier
    