from random import randint

class Dice():
    def __init__(self, sides: int):
        self.sides = sides

    
    def __str__(self):
        return f"d{self.sides}"
    

    def roll(self):
        result = randint(1, self.sides)
        critical_failure, critical_success = False, False
        if self.sides == 20:
            if result == 1:
                critical_failure = True
            elif result == 2:
                critical_success = True

        return {"result": result, 
                "critical_failure": critical_failure, 
                "critical_success": critical_success}
    
d4, d6, d8, d10, d12, d20 = Dice(4), Dice(6), Dice(8), Dice(10), Dice(12), Dice(20)