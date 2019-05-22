from .creature import Creature
import random

class Human(Creature):

    class_name = "human"
    lifes = 10
    description = "Human"
    isAlive = True

    def __init__(self, name, age, sex, damage=1, job=None):
        super().__init__(name)
        
        self.age = age
        self.sex = sex
        self.damage = 1

        if job != None:
            self.job = job

    @property
    def description(self):
    	if self.isAlive:
    		return "{}, {}, age={}, sex={}, lifes={}".format(self.class_name, self.name, self.age, self.sex, self.lifes)
    	else:
    		return "Died"

    def hit(self, obj):
    	if obj.name in Creature.objects.keys():
    		obj.get_damage(damage)
    	else:
    		raise NameError("This character doesn't exist")


    def get_damage(self, damage_given):
    	self.lifes -= damage_given
    	print("Lifes left: {}".format(self.lifes))