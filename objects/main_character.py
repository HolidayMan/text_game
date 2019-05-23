from .human import Human

class MainCharacter(Human):

    class_name = "main character"
    _description = "Main character"

    def __init__(self, name, age, sex, damage=2, lifes=15, job=None):
        super().__init__(name, age, sex, damage=damage, lifes=lifes, job=None)