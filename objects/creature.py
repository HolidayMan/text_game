class Creature():
    class_name = ""
    description = ""
    lifes = 0
    objects = {}
    
    
    def __init__(self, name):
        self.name = name

        if not name in Creature.objects.keys():
        	Creature.objects[name] = self
        else:
        	raise KeyError("Object with name " + name + " already exists")


    def say(self, phrase):
        print(self.name + ': ' + phrase)


    def __str__(self):
    	return "{}, {}".format(self.class_name, self.name)
