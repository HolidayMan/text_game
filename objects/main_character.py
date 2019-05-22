from .human import Human

class MainCharacter(Human):

    class_name = "main character"
    _description = "Main character"
    lifes = 15

    def __init__(self, name, age, sex, damage=2, job=None):
        super().__init__(name, age, sex, job=None)