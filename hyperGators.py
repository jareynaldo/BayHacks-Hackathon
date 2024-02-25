#Karan A. Faldu, Jose
#Contains Guardian Monsters Artwork by Georg Eckert / limbusdev

def main():
    numRuns=0
    points=100000
    health = 10
    attack=10
    defense=10
    speed=10
    skills=["Ram", "-", "-"]

    stats = [points, health, defense, attack, speed, skills]

    print("Welcome to HyperGator!\n")
    print("We hired you to bring back unobtainium from the end of the Black Hole.")
    print("The universsssal council doesn't like ussss trying to obtain that material.")
    print("Ya know... on account of it being unobtainium and all.")
    print("Anywayssss, that's why we hired you.... What was your name again? \n")
    print("Enter player name: ", end ='')
    player_name=input()
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
    print("3. Exit")
    print("\nEnter Menu Selection: ", end='')
    menu_option = input()
    while not menu_option.isnumeric() or menu_option not in {"1", "2", "3"}:
        print("Invalid input! Please enter an integer from the menu selection: ", end='')
        menu_option = input()
    menu_option = int(menu_option)
    if menu_option == 3:
        print("\nGoodbye! Please come work for HyperGator again!", end='')
    while (menu_option != 3):
        match menu_option:
            case 1:
                startRun(stats)
            case 2:
                openShop(stats)
            case 3:
                continue

def startRun(stats):
    pass

def openShop(stats):
    print("Welcome to the HyperGator sssshop")
    print(f'\nSo you have:\n{stats[0]} Shards\n{stats[1]} Health\n{stats[2]} Attack\n{stats[3]} Defense\n{stats[4]} Speed')
    print("Skills: ", end = '')
    for i in range (len(stats[5])-1):
        print(f'{stats[5][i]}, ', end ='')
    print(f'{stats[5][-1]}\n')

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
                print("5. Update")
                print("6. Siphon")
                print("7. Explode")
                print("8. Exit")
                print("Enter Menu Selection: ", end = '')
                print('')
                skill_option = input()
                while not skill_option.isnumeric() or skill_option not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
                    print("Invalid input! Please enter an integer from the menu selection: ", end='')
                    skill_option = input()
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
                        print("You update part of your ship")
                        print("-Gain 5 Health Points")
                        print("\nCost is 1700 shards")
                        print("Are you sure you want to buy the skill Update?\nYes or No? ", end='')
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
                            stats[5][slot_option - 1] = "Update"
                            stats[0] -= 1700
                        openShop(stats)
                    case 6:
                        print("You siphon health for shield")
                        print("-You lose 5 health")
                        print("-You gain 5 shield")
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
                        print("-The run ends")
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




if __name__ == "__main__":
    main()
