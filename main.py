from objects.human import Human
from objects.main_character import MainCharacter


def author_say(phrase):
	print("*" + phrase + "*", "\n")


mc = MainCharacter("Leha", 45, "Male", damage=3,)

barman = Human("Barman", 25, "Male", damage=2, job="Barman")

mc.say("Barman, I want to be drunk today.")

barman.say("OK. One minute.")

author_say("After drinking a glass of whiskey")

mc.say("OK. Thanks. Bye.")

barman.say("Wait. That's your bill.")

mc.say("What? Bill? Ha-ha. I won't pay. Bye.")

author_say("But there were two guards near the exit")

print(mc.description)