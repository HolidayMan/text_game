from objects.human import Human
from objects.main_character import MainCharacter
from objects.creature import Creature


author = Creature("Author")

mc = MainCharacter("Leha", 45, "Male", damage=9, lifes=10)

barman = Human("Barman", 25, "Male", damage=2, job="Barman")

mc.say("Barman, I want to be drunk today.")

barman.say("OK. One minute.")

author.author_say("After drinking a glass of whiskey")

mc.say("OK. Thanks. Bye.")

barman.say("Wait. That's your bill.")

mc.say("What? Bill? Ha-ha. I won't pay. Bye.")

author.author_say("But there were two guards near the exit.")

mc.hit(barman)

mc.hit(barman)

mc.heal(8)

mc.description = "Shit"

