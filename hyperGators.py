#Karan A. Faldu, Jose Reynaldo
#Contains Guardian Monsters Artwork by Georg Eckert / limbusdev
import math
import random
from pyscript import document


print("hellp")


def startGame(event):
    numRuns = 0
    points = 0
    health = 5
    attack = 5
    defense = 5
    speed = 5
    skills=["Ram", "-", "-"]

    stats = [points, health, attack, defense, speed, skills, numRuns]

    print("Welcome to HyperGator!\n")
    print("We hired you to bring back unobtainium from the end of the Black Hole.")
    print("The universsssal council doesn't like ussss trying to obtain that material.")
    print("Ya know... on account of it being unobtainium and all.")
    print("Anywayssss, that's why we hired you.... What was your name again? \n")
    print("Enter player name: ", end ='')

    input_text = document.querySelector("#textInput")
    player_name = input_text.value

    print(f'Ah yes, the infamoussss Gator Pirate {player_name} \n')

    print("Next time you pop around, I'll have a sssshop open for you")
    print("You don't have any money?")
    print("...")
    print("...")
    print("Well if you find any unobtainium sssshardssss in there, you can buy my waressss with those")
    print("Go on then! Go get me some unobtainium\n")
    openStart(stats)

def openStart(stats):
    print("Start Menu")
    print("----------")
    print("1. Start Run")
    print("2. Shop")
    print("3. Player Stats")
    print("4. Exit")
    print("\nEnter Menu Selection: ", end='')
    menu_option = input()
    while not menu_option.isnumeric() or menu_option not in {"1", "2", "3", "4"}:
        print("Invalid input! Please enter an integer from the menu selection: ", end='')
        menu_option = input()
    menu_option = int(menu_option)
    if menu_option == 4:
        print("\nGoodbye! Please come work for HyperGator again!", end='')
    while (menu_option != 4):
        match menu_option:
            case 1:
                startRun(stats)
            case 2:
                openShop(stats)
            case 3:
                print("\nStatistics")
                print("----------")
                print(f'Shards: {stats[0]}')
                print(f'Health: {stats[1]}')
                print(f'Attack: {stats[2]}')
                print(f'Defense: {stats[3]}')
                print(f'Speed: {stats[4]}')
                print("Skills: ", end='')
                for i in range(len(stats[5]) - 1):
                    print(f'{stats[5][i]}, ', end='')
                print(f'{stats[5][-1]}')
                print(f'Number of runs: {stats[6]}')
                print(f'Enter 0 to exit: ', end='')
                stat_option = input()
                while stat_option not in {"0"}:
                    print("Invalid input! Please enter an integer from the menu selection: ", end='')
                    stat_option = input()
                stat_option = int(stat_option)
                print("")
                if(stat_option==0):
                    openStart(stats)
            case 4:
                continue

def startRun(stats):
    player = Player(stats)
    i=1
    while(stats[1]!=0):
        print(f'Wave {i} incoming...')
        print(f'{i} baby monsters, {i//5} adult monsters, and {i//10} boss monsters have appeared')
        monster_wave = []
        for j in range (i):
            monster_wave.append(Baby(i))
        for k in range (i//5):
            monster_wave.append(Adult(i))
        for l in range (i//10):
            monster_wave.append(Boss(i))
        if (monster_wave[0].speed > player.speed):
            turn = 0
        else:
            turn = 1
        while(len(monster_wave) != 0):
            if(turn==0):
                print(f'\n{monster_wave[0].name} monster\'s turn, it attacks you for {monster_wave[0].dmg(player)} damage')
                print(f'You have {player.defend(monster_wave[0].attack)} health remaining')
                turn=1
                if(player.health==0):
                    print(f'\nGAME OVER\n\nYou earned {player.shards} unobtainium shards\nReturning to Menu...\n')
                    stats[0]+=player.shards
                    stats[6]+=1
                    openStart(stats)

            else:
                print("\nYour turn!\nWhich skill would you like to use?")
                print("Skills: ")
                for m in range(len(stats[5]) ):
                    print(f'{stats[5][m]}')
                print("Which skill? (0 to exit combat and forgo shards) ", end ='')
                skill_select = input().lower()
                while not skill_select not in {0, stats[5][0], stats[5][1], stats[5][2]}:
                    print("Invalid input! Please enter a skill from the menu selection: ", end='')
                    skill_select = input().lower()

                match skill_select:
                    case "0":
                        print("")
                        openStart(stats)
                    case "ram":
                        monster_wave[0].defend(player.ram(monster_wave[0]))
                        player.defend(player.dmg(player))
                        print(f'You deal {player.ram(monster_wave[0])-monster_wave[0].defense} damage to {monster_wave[0].name} and you did {player.dmg(player)} damage to yourself')
                        print(f'The monster has {monster_wave[0].health} health left and you have {player.health} health left')
                    case "blast":
                        monster_wave[0].defend(player.blast(monster_wave[0]))
                        print(f'You deal {player.blast(monster_wave[0])-monster_wave[0].defense} damage to {monster_wave[0].name}')
                        print(f'The monster has {monster_wave[0].health} health left and you have {player.health} health left')
                    case "rocket":
                        dmg=player.rocket(monster_wave[0])

                        monster_wave[0].defend(dmg)
                        print(f'You deal {dmg - monster_wave[0].defense} damage to {monster_wave[0].name}')
                        print(f'The monster has {monster_wave[0].health} health left and you have {player.health} health left')
                    case "teleport":
                        check=random.randint(1,100)
                        if(check<=player.speed):
                            print(f'You teleported past {monster_wave[0].name} monster')
                            monster_wave.pop(0)
                        else:
                            print(f'Teleportation failed!')
                        print(f'{len(monster_wave)} monsters remain')
                    case "repair":
                        hp=player.repair(stats)
                        if(hp==-1):
                            print(f'Repaired in time!\n You are back to full health!')
                            print(f'You have {player.health} health left')
                        elif(hp==-2):
                            print(f'Repair failed!')
                        else:
                            print(f'Healed 5 hp, you have {player.health} health left')
                    case "siphon":
                        player.siphon()
                    case "explode":
                        monster_wave[0].defend(player.explode(monster_wave[0]))
                        player.defend(player.explode(player))
                        print(f'{monster_wave[0].name} monster was defeated you earned {monster_wave[0].shards} unobtainium shards')
                        player.shards += monster_wave[0].shards
                        monster_wave.pop(0)
                        print(f'{len(monster_wave)} monsters remain')
                        if (player.health == 0):
                            print(f'\nGAME OVER\n\nYou earned {player.shards} unobtainium shards\nReturning to Menu...\n')
                            stats[0] += player.shards
                            stats[6] += 1
                            openStart(stats)

                turn=0
                if(len(monster_wave)!=0 and monster_wave[0].health<=0):
                    print(f'{monster_wave[0].name} monster was defeated you earned {monster_wave[0].shards} unobtainium shards')
                    player.shards+=monster_wave[0].shards
                    monster_wave.pop(0)
                    print(f'{len(monster_wave)} monsters remain')
                if(len(monster_wave)==0):
                    print(f'\nWave Deafeated!\n')
        i+=1

def openShop(stats):
    print("Welcome to the HyperGator sssshop")
    print(f'\nSo you have:\n{stats[0]} Shards\n{stats[1]} Health\n{stats[2]} Attack\n{stats[3]} Defense\n{stats[4]} Speed')
    print("Skills: ", end = '')
    for i in range (len(stats[5])-1):
        print(f'{stats[5][i]}, ', end ='')
    print(f'{stats[5][-1]}')
    print(f'Number of Runs: {stats[6]}\n')

    print("What would you like to buy?")
    print("\nShop Menu")
    print("---------")
    print("1. Stats")
    print("2. Skills")
    print("3. Exit")
    print("\nEnter Menu Selection: ", end='')
    shop_option = input()
    while not shop_option.isnumeric() or shop_option not in {"1", "2", "3"}:
        print("Invalid input! Please enter an integer from the menu selection: ", end='')
        shop_option=input()
    print("")
    shop_option= int(shop_option)
    if shop_option==3:
        print("\nGoodbye! Please come to my sssshop again\n")
    while(shop_option !=3):
        match shop_option:
            case 1:
                print("\nStat Menu")
                print("---------")
                print("1. Health Point")
                print("2. Attack Point")
                print("3. Defense Point")
                print("4. Speed Point")
                print("5. Exit")
                print("\nEnter Menu Selection: ", end ='')
                stat_option = input()
                while not stat_option.isnumeric() or stat_option not in {"1", "2", "3", "4", "5"}:
                    print("Invalid input! Please enter an integer from the menu selection: ", end='')
                    stat_option = input()
                print("")
                stat_option = int(stat_option)
                stat_track=0
                match stat_option:
                    case 1:
                        print(f'It will cost {(stats[1] - 9) * 100} shards')
                        print(f'Are you sure you want to buy a Health Point?\nYes or No?', end = '')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or ((stats[1] - 9) * 100) > stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if ((stats[1] - 9) * 100) > stats[0]:
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        stat_track=1

                    case 2:
                        print(f'It will cost {(stats[2] - 9) * 100} shards')
                        print(f'Are you sure you want to buy a Attack Point?\nYes or No?', end = '')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or ((stats[2] - 9) * 100) > stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if ((stats[2] - 9) * 100) > stats[0]:
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        stat_track=2
                    case 3:
                        print(f'It will cost {(stats[3] - 9) * 100} shards')
                        print(f'Are you sure you want to buy a Defense Point?\nYes or No?', end = '')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or ((stats[3] - 9) * 100) > stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if ((stats[3] - 9) * 100) > stats[0]:
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        stat_track=3
                    case 4:
                        print(f'It will cost {(stats[4] - 9) * 100} shards')
                        print(f'Are you sure you want to buy a Health Point?\nYes or No?', end = '')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or ((stats[4]-9)*100)>stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if ((stats[4]-9)*100)>stats[0]:
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        stat_track=4
                    case 5:
                        print("")
                        openShop(stats)

                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                    stats[0]-=(stats[stat_track]-9)*100
                    stats[stat_track]+=1
                openShop(stats)

            case 2:
                print("Skill Menu")
                print("----------")
                print("1. Ram")
                print("2. Blast")
                print("3. Rocket")
                print("4. Teleport")
                print("5. Repair")
                print("6. Siphon")
                print("7. Explode")
                print("8. Exit")
                print("Enter Menu Selection: ", end = '')
                skill_option = input()
                while not skill_option.isnumeric() or skill_option not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
                    print("Invalid input! Please enter an integer from the menu selection: ", end='')
                    skill_option = input()
                print('')
                skill_option = int(skill_option)
                match skill_option:
                    case 1:
                        print("You max out your thrusters and ram the ship into the enemy")
                        print("-You deal your attack points in damage")
                        print("-You take attack points minus defense points in damage")
                        print("\nCost is 100 shards")
                        print("Are you sure you want to buy the skill Ram?\nYes or No?", end = '')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or 100 > stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if (100 > stats[0]):
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                            print("\nWhich slot would you like to put it in?")
                            print("Slots: ")
                            for i in range(len(stats[5])):
                                print(f'{i+1}. {stats[5][i]}')
                            print("Select slot: ", end='')
                            slot_option=input()
                            while not slot_option.isnumeric() or slot_option not in {"1", "2", "3"}:
                                print("Invalid input! Please enter an integer from the menu selection: ", end='')
                                slot_option=input()
                            print('')
                            slot_option=int(slot_option)
                            stats[5][slot_option-1]="Ram"
                            stats[0] -= 100
                        openShop(stats)


                    case 2:
                        print("You charge up your blasters and fire them at the enemy")
                        print("-You deal half your attack points in damage")
                        print("\nCost is 500 shards")
                        print("Are you sure you want to buy the skill Blast?\nYes or No? ", end='')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or 500 > stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if (500 > stats[0]):
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                            print("\nWhich slot would you like to put it in? ")
                            print("Slots: ")
                            for i in range(len(stats[5])):
                                print(f'{i + 1}. {stats[5][i]}')
                            print("Select slot: ", end='')
                            slot_option = input()
                            while not slot_option.isnumeric() or slot_option not in {"1", "2", "3"}:
                                print("Invalid input! Please enter an integer from the menu selection: ", end='')
                                slot_option = input()
                            print('')
                            slot_option = int(slot_option)
                            stats[5][slot_option - 1] = "Blast"
                            stats[0] -= 500
                        openShop(stats)
                    case 3:
                        print("You fire a rocket")
                        print("-50% chance to deal triple your attack points in damage")
                        print("-50% chance to miss")
                        print("\nCost is 600 shards")
                        print("Are you sure you want to buy the skill Rocket?\nYes or No? ", end='')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or 600 > stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if (600 > stats[0]):
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                            print("\nWhich slot would you like to put it in? ")
                            print("Slots: ")
                            for i in range(len(stats[5])):
                                print(f'{i + 1}. {stats[5][i]}')
                            print("Select slot: ", end='')
                            slot_option = input()
                            while not slot_option.isnumeric() or slot_option not in {"1", "2", "3"}:
                                print("Invalid input! Please enter an integer from the menu selection: ", end='')
                                slot_option = input()
                            print('')
                            slot_option = int(slot_option)
                            stats[5][slot_option - 1] = "Rocket"
                            stats[0] -= 600
                        openShop(stats)
                    case 4:
                        print("You teleport past the enemy")
                        print(f'-(50+speed points)% to escape combat')
                        print("-You don't get any shards from combat")
                        print("\nCost is 1100 shards")
                        print("Are you sure you want to buy the skill Teleport?\nYes or No? ", end='')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or 1100 > stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if (1100 > stats[0]):
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                            print("\nWhich slot would you like to put it in? ")
                            print("Slots: ")
                            for i in range(len(stats[5])):
                                print(f'{i + 1}. {stats[5][i]}')
                            print("Select slot: ", end='')
                            print('')
                            slot_option = input()
                            while not slot_option.isnumeric() or slot_option not in {"1", "2", "3"}:
                                print("Invalid input! Please enter an integer from the menu selection: ", end='')
                                slot_option = input()
                            slot_option = int(slot_option)
                            stats[5][slot_option - 1] = "Teleport"
                            stats[0] -= 1100
                        openShop(stats)
                    case 5:
                        print("You repair part of your ship")
                        print("-(50+speed)% chance to heal 5 Health Points")
                        print("\nCost is 1700 shards")
                        print("Are you sure you want to buy the skill Repair?\nYes or No? ", end='')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or 1700 > stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if (1700 > stats[0]):
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                            print("\nWhich slot would you like to put it in? ")
                            print("Slots: ")
                            for i in range(len(stats[5])):
                                print(f'{i + 1}. {stats[5][i]}')
                            print("Select slot: ", end='')
                            slot_option = input()
                            while not slot_option.isnumeric() or slot_option not in {"1", "2", "3"}:
                                print("Invalid input! Please enter an integer from the menu selection: ", end='')
                                slot_option = input()
                            print('')
                            slot_option = int(slot_option)
                            stats[5][slot_option - 1] = "Repair"
                            stats[0] -= 1700
                        openShop(stats)
                    case 6:
                        print("You siphon health to shield and speed")
                        print("-You lose 5 health")
                        print("-You gain 2 shield")
                        print("-You gain 2 speed")
                        print("\nCost is 2800 shards")
                        print("Are you sure you want to buy the skill Siphon?\nYes or No? ", end='')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or 2800 > stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if (2800 > stats[0]):
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                            print(""
                                  "\nWhich slot would you like to put it in? ")
                            print("Slots: ")
                            for i in range(len(stats[5])):
                                print(f'{i + 1}. {stats[5][i]}')
                            print("Select slot: ", end='')
                            slot_option = input()
                            while not slot_option.isnumeric() or slot_option not in {"1", "2", "3"}:
                                print("Invalid input! Please enter an integer from the menu selection: ", end='')
                                slot_option = input()
                            print('')
                            slot_option = int(slot_option)
                            stats[5][slot_option - 1] = "Siphon"
                            stats[0] -= 2800
                        openShop(stats)
                    case 7:
                        print("You blow up the exterior of your ship")
                        print("-You deal 100 damage to the current enemy")
                        print("-The deal 100 damage to yourself")
                        print("\nCost is 4500 shards")
                        print("Are you sure you want to buy the skill Explode?\nYes or No? ", end='')
                        confirm = input()
                        while confirm not in {"Yes", "No", "Y", "N"} or 4500 > stats[0]:
                            if confirm not in {"Yes", "No", "Y", "N"}:
                                print("Invalid input! Please enter Yes, No, Y, or N: ", end='')
                                confirm = input()
                            if (4500 > stats[0]):
                                if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                                    print("\nNOT ENOUGH SHARDS")
                                confirm = "No"
                                print("")
                                break
                        if confirm.__eq__("Yes") or confirm.__eq__("Y"):
                            print("\nWhich slot would you like to put it in? ")
                            print("Slots: ")
                            for i in range(len(stats[5])):
                                print(f'{i + 1}. {stats[5][i]}')
                            print("Select slot: ", end='')
                            slot_option = input()
                            while not slot_option.isnumeric() or slot_option not in {"1", "2", "3"}:
                                print("Invalid input! Please enter an integer from the menu selection: ", end='')
                                slot_option = input()
                            print('')
                            slot_option = int(slot_option)
                            stats[5][slot_option - 1] = "Explode"
                            stats[0] -= 4500
                        openShop(stats)
                    case 8:
                        print("")
                        openShop(stats)
                        continue

            case 3:
                openStart(stats)
                continue

class Creatures():
    def __init__(self):
        self.health=0
        self.attack=0
        self.defense=0
        self.speed=0

    def explode(self, target):
        return 100
    def siphon(self):
        self.health-=5
        self.defense+=2
        self.speed+=2

    def repair(self, stats):
        check = random.randint(1,100)
        if(check<=self.speed):
            if(self.health+5>stats[1].health):
                self.health=stats[1].health
                return -1;
            else:
                self.health+=5
                return self.health
        return -2

    def rocket(self, target):
        check=random.randint(1,2)
        if(check==1):
            dmg=3*self.attack - target.defense
        else:
            dmg=0
        if(dmg>0):
            return dmg
        return 0

    def blast(self, target):
        dmg=self.attack//2 - target.defense
        if(dmg>0):
            return dmg
        return 0

    def defend(self, attack):
        if(attack-self.defense>0):
            self.health -= attack-self.defense
        if(self.health<0):
            self.health=0
        return self.health

    def dmg(self, target):
        dmg=self.attack - target.defense
        if(dmg> 0):
            return dmg
        return 0

    def ram(self, target):
        if(self.attack<=target.defense):
            return 0
        return self.attack


class Adult(Creatures):
    def __init__(self, wave):
        self.health = 2 * wave
        self.attack = 2 * wave
        self.defense = 2 * wave
        self.speed = 2 * wave
        self.shards = 10 * wave
        self.name="Adult"

class Baby(Creatures):
    def __init__(self, wave):
        self.health = 2 + wave
        self.attack = 2 + wave
        self.defense = 2 + wave
        self.speed = 2 + wave
        self.shards = 10 + wave
        self.name="Baby"

class Boss(Creatures):
    def __init__(self, wave):
        self.health = math.pow(2, wave)
        self.attack = math.pow(2, wave)
        self.defense = math.pow(2, wave)
        self.speed = math.pow(2, wave)
        self.shards = 100*wave
        self.name="Boss"

class Player(Creatures):
    def __init__(self, stats):
        self.health = stats[1]
        self.attack = stats[2]
        self.defense = stats[3]
        self.speed = stats[4]
        self.skills = stats[5]
        self.shards = 0
if __name__ == "__main__":
    startGame()
