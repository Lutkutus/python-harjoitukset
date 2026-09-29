class Adventurer:
    def __init__(self, adventurer_name, health=100, stamina=100, atk_dmg=10):
        self.health = health
        self.stamina = stamina
        self.atk_dmg = atk_dmg
        self.adventurer_name = adventurer_name

    def gain_life(self, healingamount):
        self.health += healingamount
        print(f"{self.adventurer_name} saa {healingamount} elämäpistettä. HP: {self.health}")


    def lose_life(self, lostlife):

        if self.health <= 0:
            print(f"{self.adventurer_name} kuoli!")

        else:
            self.health -= lostlife
            print(f"{self.adventurer_name} menettää {self.health} elämäpistettä. HP: {self.health}")

playerlist = []




# for i in range(3):
#     player = Adventurer(input("Adventurer name: "))
#     playerlist.append(player)

# for player in playerlist:
#     print(player.adventurer_name)



adventurer1 = input("Tee ensimmäinen seikkailija: ")
adventurer2 = input("Tee toinen seikkailija: ")
adventurer3 = input("Tee kolmas seikkailija: ")

playerlist.append(adventurer1)
playerlist.append(adventurer2)
playerlist.append(adventurer3)

for player in playerlist:
    print(player.adventurer_name)

adventurer1 = 

# print(f"{adventurer1.adventurer_name} | {adventurer2.adventurer_name} | {adventurer3.adventurer_name}")