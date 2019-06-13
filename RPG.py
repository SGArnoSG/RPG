from random import randint

class Dice(object):
    def die(num):
        die = randint(1,num)
        return die


class Character(object):
    def __init__(self, name, hp, chance, accuracy, exp):
        self.name = name
        self.hp = hp
        self.chance = chance
        self.accuracy = accuracy
        self.exp = exp


class Boy_next_door(Character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?\n"), chance=20, accuracy=10, hp=10, exp=10)
    prof = "Boy next door"
    maxhp = 10
    level = 1
    hd = 10
    level2 = 20


class Leatherman(Character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?\n"),chance=20,accuracy=10, hp=8, exp=8)
    prof= "Leatherman"
    maxhp = 8
    level = 1
    hd = 8
    level2 = 15


class Ricardo(Character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?\n"), chance=20, accuracy=10, hp=4, exp=4)
    prof = "Ricardo"
    mana = 1
    maxmana = 1
    maxhp = 4
    level = 1
    hd = 4
    level2 = 10


class Slave(Character):
    def __init__(self):
        super().__init__(name="Slave", hp=7, chance=20, accuracy=6, exp=7)


class Boss_of_this_gym(Character):
    def __init__(self):
        super().__init__(name="Boss of this gym", hp=8, chance=18, accuracy=6, exp=8)


def profession():
    print('Hello and welcome to my game "Dungeon Master".\nYou enter a dark dungeon. The walls are covered in blood, screams are heard, and the whole world is red. And you...')
    print("Choose your race:\nWrite 1 for Boy next door\nWrite 2 for Leatherman\nWrite 3 for Ricardo\n")
    pclass=input('Enter here:\n')
    if pclass == "1":
        Prof = Boy_next_door()
    elif pclass == "2":
        Prof = Leatherman()
    elif pclass == "3":
        Prof = Ricardo()
    else:
        Prof = Boy_next_door()
    return Prof

def random_mob():
    mob = Slave() if Dice.die(2) < 2 else Boss_of_this_gym()
    return mob

def playerAttack():
    roll = Dice.die(20)
    if roll >= hero.chance-mob.accuracy:
        print("You spanking!")
        if hero.prof == "Boy next door":
            rollD = Dice.die(10)
        if hero.prof == "Leatherman":
            rollD = Dice.die(6)
        if hero.prof == "Ricardo":
            rollD = Dice.die(4)
        print("for", rollD, "damage")
        mob.hp -= rollD
        print("The", mob.name, "has", mob.hp, "HP left")
    else:
        print("You miss!")

def enemyAttack():
    roll = Dice.die(20)
    if roll >= mob.chance-hero.accuracy:
        print("Enemy hit!")
        if mob.name == "Slave":
            rollD = Dice.die(4)
        elif mob.name == "Boss of this gym":
            rollD = Dice.die(6)
        print("For", rollD, "damage")
        hero.hp -= rollD
        print(hero.name, "has", hero.hp, "HP left")
    else:
        print("Enemy misses!")

def levelUp():

    while hero.exp >= hero.level2:
        levelGain = False
        hero.level += 1
        levelGain = True
        hero.level2 = hero.level2*2
        if levelGain == True:
            hero.maxhp += Dice.die(hero.hd)
            hero.hp = hero.maxhp
            if hero.prof == "Ricardo":
                hero.maxmana += 1
                hero.mana = hero.maxmana

            print("Level Up!\nHP:", hero.hp, "\nLevel:", hero.level)
            levelGain = False
    while hero.level >= 3:
        hero.level -= 3
        hero.chance -= 1
        print("Chance:", hero.chance)

def commands():
    if hero.prof == "Boy next door":
        command=input("Write 1 to use your whip\nPress Enter to pass")
        if command == "1":
            playerAttack()
        if command == "":
            pass

    if hero.prof == "Leatherman":
        print("Write 1 to use your knout\nWrite 2 to relax\nPress Enter to pass")
        command = input('Enter here:\n')
        if command == "1":
            playerAttack()
        elif command == "2":
            if hero.hp < hero.maxhp:
                hero.hp += Dice.die(8)
                if hero.hp > hero.maxhp:
                    hero.hp = hero.hp-(hero.hp-hero.maxhp)
                print("You now have:", hero.hp, "HP")
            else:
                print("Your health points are full")
                commands()
        elif command == "":
            pass
    if hero.prof == "Ricardo":
        print("Write 1 to use your horsewhip\nWrite 2 for singing\nWrite 3 to dance\nPress Enter to pass")
        command = input('Enter here:\n')
        if command == "1":
            playerAttack()
        elif command =="2":
            print("You have", hero.mana, "mana")
            if hero.mana >= 1 and hero.mana < 3:
                print("Write 2 for sleepy track\nWrite 3 for powerful smash")
                command = input('Enter here:\n')
                if command == "2":
                    print("Your enemy sleep. It is easy kill for you!")
                    mob.hp -= mob.hp
                    hero.mana -= 1
                if command == "3":
                    if hero.mana < hero.maxmana:
                        hero.mana += Dice.die(4)
                        if hero.mana > hero.maxmana:
                            hero.mana -= (hero.mana-hero.maxmana)
                    dam = Dice.die(4) * hero.mana
                    mob.hp -= dam
                    print("You use all your flex points! and do", dam, "damage!")
                    hero.mana -= hero.mana
            elif hero.mana >= 3:
                print("Press 2 for sleepy track\nPress 3 for powerful smash\nPress 1 for collateral damage")
                command=input('Enter here:\n')
                if command  == "2":
                    print("Your enemy sleep. It is easy kill for you!")
                    mob.hp -= mob.hp
                    hero.mana -= 1
                if command == "3":
                    dam=Dice.die(4) * hero.mana
                    mob.hp -= dam
                    print("You use all your flex points! and do", dam, "damage!")
                    hero.mana -= hero.mana
                if command == "1":
                    print("You jumped in the sky and fall with great power!")
                    dam=0
                    dam += Dice.die(6)
                    dam += Dice.die(6)
                    dam += Dice.die(6)
                    mob.hp -= dam
                    print("You did", dam, "points of damage")

                    hero.mana -= 3
            else:
                print("Your flex points is empty")
                commands()
        elif command == "2":
            if hero.mana < hero.maxmana:
                hero.mana += 1
                print("You have", hero.mana, "flex points")
            elif hero.mana >= hero.maxmana:
                print("Your flex points is full.")
                print("You have", hero.mana, "flex points")
                commands()

        elif command == "":
            pass

mob = random_mob()
hero = profession()
while True:
    if mob.hp <= 0:
        print('The', mob.name, 'is obeyed!\n')
        hero.exp += mob.exp
        print('Hero xp', hero.exp)
        mob = random_mob()
    if hero.hp <= 0:
        mob.exp += hero.exp
        print("Enemy xp:", mob.exp)
        print(hero.name, 'died!\n')
        hero = profession()

    levelUp()

    print("You see", mob.name+",", mob.name, "has", mob.hp, "HP.")
    if hero.hp > 0:
        commands()
    if mob.hp > 0:
        enemyAttack()