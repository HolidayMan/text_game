from .creature import Creature
import random

class Human(Creature):

    class_name = "human"
    body_parts = ['right arm', 'left arm', 'right leg', 'left leg', 'head', 'body']
    _description = "Human"

    def __init__(self, name, age, sex, damage=1, lifes=10, job=None):
        super().__init__(name)
        
        self.age = age
        self.sex = sex
        self.damage = damage
        self.max_lifes = lifes
        self.lifes = lifes

        if job != None:
            self.job = job


