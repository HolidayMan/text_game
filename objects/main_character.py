from creature import Creature

class MainCharacter(Creature):

	class_name = "main character"
	description = "Main character"


	def __init__(self, name, age):
		super().__init__(name)
		self.age = age