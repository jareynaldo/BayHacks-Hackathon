#Karan, Jose


def main():
    points=0
    attack=10
    defense=10
    health=10
    speed=10
    skills=["Single", "-", "-"]
    print("Welcome to Hyper Gator!\n")
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

    print("Start Menu")
    print("----------")
    print("1. Start Run")
    print("2. Shop")
    print("3. Exit")
    print("\nEnter selection number: ", end ='')
    menu_option=input()
    while not menu_option.isnumeric():
            print("Invalid input, please enter an integer from the menu selection: ", end = '')
            menu_option=input()
    menu_option = int(menu_option)
    if menu_option==3:
        print("\nGoodbye! Please come work for HyperGator again!", end='')
    while(menu_option != 3):
        match menu_option:
            case 1:
                pass
            case 2:
                openShop(points)
            case 3:
                continue

def openShop(shards):
    print("Welcome to the HyperGator sssshop")


if __name__ == "__main__":
    main()
