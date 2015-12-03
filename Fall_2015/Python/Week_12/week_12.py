# week_12.py
# Author: Allen Sallinger
###########################
# A randomized fighting adventure. Travel across the land and fight different
# creatures that appear.
###########################

class hero:
    # attributes of a hero
    name = ""
    htype = ""
    wtype = ""

    hp = 100

    def add_health(self):
        self.hp = self.hp + 10

    def take_damage(self, damage):
        self.hp = self.hp - damage

    def is_alive(self):
        if(self.hp > 0):
            return True
        else:
            return False
            

def main():
    character = hero()

    print("Name before assignment: " + character.name)
    character.name = "Allen"
    print("Name after assignment: " + character.name)

    print("Current health: " + str(character.hp))
    character.add_health()
    print("Current health: " + str(character.hp))
    character.take_damage(30)
    print("Current health: " + str(character.hp))

    print("Character is alive: " + str(character.is_alive()))
    character.take_damage(80)
    print("Character is alive: " + str(character.is_alive()));

main()
