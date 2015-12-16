# heroes_and_monsters.py
# Author: Allen Sallinger
###########################
# A randomized fighting adventure. Travel across the land and fight different
# creatures that appear.
###########################

import random

class hero:
    # attributes of a hero
    name = ""
    htype = ""
    wtype = ""

    exp = 0
    level = (exp / 100) + 1 

    hp = 100

    damage_dealt = 25

    def add_health(self, health):
        self.hp = self.hp + health

    def take_damage(self, damage):
        self.hp = self.hp - damage

    def is_alive(self):
        if(self.hp >= 0):
            return True
        else:
            return False

    def exp_increase(self, increase):
        self.exp = self.exp + increase


class monster:
    # attributes of a monster
    name = ""
    
    hp = 100 # set just as a base can differ per type of monster

    damage_dealt = 10

    def add_health(self):
        self.hp = self.hp + 10

    def take_damage(self, damage):
        self.hp = self.hp - damage

    def is_alive(self):
        if(self.hp >= 0):
            return True

        else:
            return False


def main():

    smarr =  ["bat", "rat", "evilfrog"] # array of small monsters
    mmarr = ["thief", "bandit", "knave"] # array of medium monsters
    lmarr = ["dragon", "evil wizard", "hydra"] # array of large monsters

    character = hero()

    while(character.is_alive()):
        new_monster = monster()
        
        monster_level = character.level

        monster_choice = random.randint(0,2)

        if(monster_level < 5):
            new_monster.name = smarr[monster_choice]
            new_monster.hp = 100
            new_monster.damage_dealt = 10

        elif(monster_level > 5 and monster_level < 10):
            new_monster.name = mmarr[monster_choice]
            new_monster.hp = 300
            new_monster.damage_dealt = 25

        elif(new_monster_level > 10):
            new_monster.name = lmarr[monster_choice]
            new_monster.hp = 500
            new_monster.damage_dealt = 50

        print("You encoutered: " + new_monster.name + "\n")


        while(new_monster.is_alive() and character.is_alive()):
            if(not character.is_alive()):
                break

            print("Do you want to attack the " + monster.name)
            answer = input("Enter b for block or a for attack")

            if(answer == "a"):
                new_monster.take_damage(hero.damage_dealt)
                print("You dealt damage " + str(hero.damage_dealt))

            monster_attack_chance = random.random()

            # hero gets hit by attack
            if(monster_attack_chance > .75 and answer != "b"):
                character.take_damage(monster.damage_dealt)
                print("You took damage " + str(new_monster.damage_dealt))

            elif(answer == "b"):
                print("You blocked the attack")

            else:
                print("The monsters attack missed you.")

            print("\n\n")



        if(character.is_alive()):
            print("You defeated the monster" + new_monster.name + "\n")
            # swap later to choose see how much health to add
            character.add_health(100)
            
        else:
            print("You were defeated by the monster\n")
                

            

            
            
main()







