import random

class Creature():
    class_name = "creature"
    body_parts = []
    damaged_body_parts = []
    _description = ""
    damage = 0
    max_lifes = 0
    lifes = 0
    objects = {}

    
    def __init__(self, name):
        self.name = name

        if not name in Creature.objects.keys():
            Creature.objects[name] = self
        else:
            raise KeyError("Object with name " + name + " already exists")


    @staticmethod
    def author_say(phrase):
        print("*" + phrase + "*", "\n")


    @property
    def description(self):
        return self._description
    

    @description.setter
    def description(self, desc):
        self._description = desc


    def say(self, phrase):
        print(self.name + ': ' + phrase + "\n")


    def hit(self, obj):
        if self.is_alive():
            if obj.name in Creature.objects.keys():
                Creature.author_say("{} hitted {} in {}".format(self.name, obj.name, obj.get_random_body_part()))
                obj.get_damage(self.damage)
            else:
                raise NameError("This character doesn't exist")
        else:
            raise NameError("{} id died".format(self.name))


    def get_damage(self, damage_given):
        self.lifes -= damage_given
        self.get_health()

    def get_random_body_part(self):
        part = random.choice(self.body_parts)
        del self.body_parts[self.body_parts.index(part)]
        self.damaged_body_parts.append(part)
        return part


    def get_health(self):
        if self.lifes > 1:
            Creature.author_say("{} has {} lifes".format(self.name, self.lifes))
        elif self.lifes == 1:
            Creature.author_say("{} has {} life".format(self.name, self.lifes))
        else:
            Creature.author_say("{} is died".format(self.name))


    def is_alive(self):
        return self.lifes > 0


    def heal(self, count):
        self.lifes += count
        if self.lifes > self.max_lifes:
            self.lifes = self.max_lifes


    def __str__(self):
        return "{}, {}".format(self.class_name, self.name)