#imports
import time
import random
from colorama import init, Fore, Back, Style
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.LIGHTGREEN_EX]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]
init(convert=True)
#(universal)
floor = 1
monsterid = 0
#(player)
playerhp = random.randint(75,100)
playerdam = random.randint(5,20)
playerdef = random.randint(0,1)
playerEquipedWeaponMain = 0
playerEquipedWeaponSide = 0
playerEquipedArmorHead = 0
playerEquipedArmorChest = 0
playerEquipedArmorLegs = 0
playerEquipedArmorBoots = 0
ammo = 0
playerInventory = ['Nothing','Copper','Silver','Gold','Platinum','Adimantite','Mithril','Dragon']
playerName = input('What is your name? ')
flee = False
coins = random.randint(20,100)
xp = 0
#monster lists
monsterList = ['slime','bones','mercinary','tree','zombo']
monsterListHp = [random.randint(25*floor,35*floor),random.randint(55*floor,65*floor),random.randint(75*floor,100*floor),random.randint(750*floor,1000*floor),random.randint(50*floor,100*floor)]
monsterListDam = [random.randint(1*floor,5*floor),random.randint(3*floor,10*floor),random.randint(5*floor,10*floor),random.randint(75*floor,100*floor),random.randint(10*floor,20*floor)]
monsterLootCoins = [random.randint(1,5),random.randint(3,10),random.randint(6,30),random.randint(100,500),random.randint(10,50)]
monsterLootXp = [random.randint(10,50),random.randint(30,100),random.randint(60,300),random.randint(1000,5000),random.randint(100,500)]
#tools lists
#each gear has 7 teirs: copper, silver, gold, platinum, adimantite, mithril, and dragon
#armors provide a defense boost and weapons provide an attack boost, tools are used lader on
armorListHead = [0,1,3,5,10,15,25,50]
armorListChest = [0,1,4,6,12,17,30,55]
armorListLegs = [0,1,3,5,10,15,25,50]
armorListBoots = [0,1,3,5,10,15,25,50]
toolListMain = []
weaponListMele = [0,5,10,15,20,30,50,100]
weaponListRanged = [0,8,12,18,25,37,60,140]
gearNames = ['Nothing','Copper','Silver','Gold','Platinum','Adimantite','Mithril','Dragon']
#modifier lists
#good modifers are: Legendary, Godly, Super, Superior, Amazing
#bad modifiers are: horrible, bad, terrable, useless, really bad
goodModifiersAttack = [100,50,25,10,5,1]
badModifiersAttack = [-100,-50,-25,-10,-5,-1]
#list of attacks (for the funnies)
attackSplashText = ['You punched the ',monsterList[monsterid],'!','You kicked the ',monsterList[monsterid],'!','You forced the ',monsterList[monsterid],' to listen to Taylor Swift!', 'You body slammed the ',monsterList[monsterid],'!']
#lists of locations and things
locations = ['Home','Grassland','Caves','Mountains','Tundra','Desert','Castle','Village']
locationsDiscovered = ['Home']
biomeId = 0

#shows the players stats
def playerStats():
    color = Fore.CYAN
    print(f'{color}')
    print(playerName,'Hp:',playerhp)
    print(playerName,'Damage:',playerdam)
    print(playerName,'Defense:',playerdef)
    print('Ammo:',ammo)
    print('Xp:',xp)
    print('Coins:',coins)
    print('Floor:',floor)
    time.sleep(1)
    chooseMove()
#shows the players inventory
def playerGenaricInventory():
    color = Fore.CYAN
    print(f'{color}')
    print('Main Hand:',gearNames[playerEquipedWeaponMain])
    print('Offhand:',gearNames[playerEquipedWeaponSide])
    print('Helmet:',gearNames[playerEquipedArmorHead])
    print('Chestplate:',gearNames[playerEquipedArmorChest])
    print('Leggings:',gearNames[playerEquipedArmorLegs])
    print('Boots:',gearNames[playerEquipedArmorBoots])
    print('Ammo:',ammo)
    print('Inventory:',playerInventory)
    time.sleep(1)
    color = Fore.GREEN
    print(f'{color}')
    choose = input('Do you want to equip differant gear? ')
    if(choose == 'yes') or (choose == 'Yes'):
        print('Lets get Equiping!')
        equip()
    else:
        print('Okay!')
        chooseMove()
#the ability to equip armor
def equip():
    color = Fore.YELLOW
    print(f'{color}')
    print('Here is everything you have!')
    print(playerInventory)
    choose = input('What slot will you equip for? ')
    if(choose == 'head') or (choose == 'Head'):
        choose = input('What will you equip! ')
        print(playerInventory)
        if(choose in playerInventory):
            print('Equiped!')
            playerEquipedArmorHead = playerEquipedArmorHead[choose]
    elif(choose == 'chest') or (choose == 'Chest'):
        choose = input('What will you equip! ')
        print(playerInventory)
    elif(choose == 'Leggings') or (choose == 'leggings'):
        choose = input('What will you equip! ')
        print(playerInventory)
    elif(choose == 'boots') or (choose == 'Boots'):
        choose = input('What will you equip! ')
        print(playerInventory)
    elif(choose == 'Mainhand') or (choose == 'mainhand'):
        choose = input('What will you equip! ')
        print(playerInventory)
    elif(choose == 'offhand') or (choose == 'Offhand'):
        choose = input('What will you equip! ')
        print(playerInventory)
    else:
        color = Fore.RED
        print(f'{color}')
        print('Hmm I didn\'t quite get that. Try: Head,Chest,Mainhand,Offhand,etc')
        equip()
#this is the funtion for choosing what to do in main game play
def chooseMove():
    color = Fore.GREEN
    print(f'{color}')
    print('What do you want to do?')
    choose = input('Ex: Stats, Inventory, Explore, Shop, goto ')
    if(choose == 'stats') or (choose == 'Stats'):
        playerStats()
    elif(choose == 'inventory') or (choose == 'Inventory'):
        playerGenaricInventory()
    elif(choose == 'explore') or (choose == 'Explore'):
        print('Time to explore!')
        explore()
    elif(choose == 'shop') or (choose == 'Shop'):
        shop()
    elif(choose == 'goto') or (choose == 'Goto'):
        goto()
    else:
        print('I didn\' quite get that, try again')
        time.sleep(1)
        chooseMove()
#this is how you can discover things and go places randomly
def explore():
    exploreRand = random.randint(1,2)
    if(exploreRand == 1):
        color = Fore.RED
        print(f'{color}Combat has begun!')
        time.sleep(1)
        chooseMove()
    elif(exploreRand == 2):
        color = Fore.MAGENTA
        print(f'{color}New Location Discovered!')
        newLocation = random.randint(1,7)
        if(locations[newLocation] not in locationsDiscovered):
            locationsDiscovered.append(locations[newLocation])
            print('You have discovered:',locationsDiscovered,'!')
            time.sleep(1)
            chooseMove()
        else:
            color = Fore.GREEN
            print(f'{color}You\'ve already found this place!')
            time.sleep(1)
            chooseMove()
#here is the shop
def shop():
    color = Fore.GREEN
    print(f'{color}Yeah the shop is pretty empty')
    time.sleep(1)
    chooseMove()
#here are the diffearnt biomes
#takes you where you wanna go ['Home','Grassland','Caves','Mountains','Tundra','Desert','Castle','Village']
def goto():
    color = Fore.GREEN
    print(f'{color}')
    choose = input('Wanna know where you can go? ')
    if(choose == 'yes') or (choose == 'Yes'):
        color = Fore.MAGENTA
        global biomeId
        print(f'{color}You are here: ',locations[biomeId])
        print('You can go here: ',locationsDiscovered)
    elif(choose == 'no') or (choose == 'No'):
        print('Okie')
    else:
        print('I don\'t understand...')
        goto()
    color = Fore.GREEN
    print(f'{color}')
    choose = input("Where would you like to go? ")
    if(choose == 'Grasslands') or (choose == 'grasslands'):
        if('Grasslands' in locationsDiscovered):
            biomeId = 1;
            gotoGrasslands()
        else:
            color = Fore.RED
            print(f'{color}Hmm you don\'t know where that is.')
            goto()
    elif(choose == 'Home') or (choose == 'home'):
        if('Home' in locationsDiscovered):
            biomeId = 0;
            gotoHome()
        else:
            color = Fore.RED
            print(f'{color}Hmm you don\'t know where that is.')
            goto()
    elif(choose == 'Castle') or (choose == 'caste'):
        if('Castle' in locationsDiscovered):
            biomeId = 6;
            gotoCastle()
        else:
            color = Fore.RED
            print(f'{color}Hmm you don\'t know where that is.')
            goto()
    elif(choose == 'Village') or (choose == 'village'):
        if('Village' in locationsDiscovered):
            biomeId = 7;
            gotoVillage()
        else:
            color = Fore.RED
            print(f'{color}Hmm you don\'t know where that is.')
            goto()
    elif(choose == 'Caves') or (choose == 'caves'):
        if('Caves' in locationsDiscovered):
            biomeId = 2;
            gotoCaves()
        else:
            color = Fore.RED
            print(f'{color}Hmm you don\'t know where that is.')
            goto()
    elif(choose == 'Mountains') or (choose == 'mountains'):
        if('Mountains' in locationsDiscovered):
            biomeId = 3;
            gotoMountains()
        else:
            color = Fore.RED
            print(f'{color}Hmm you don\'t know where that is.')
            goto()
    elif(choose == 'Tundra') or (choose == 'tundra'):
        if('Tundra' in locationsDiscovered):
            biomeId = 4;
            gotoTundra()
        else:
            color = Fore.RED
            print(f'{color}Hmm you don\'t know where that is.')
            goto()
    elif(choose == 'Desert') or (choose == 'desert'):
        if('Desert' in locationsDiscovered):
            biomeId = 5;
            gotoDesert()
        else:
            color = Fore.RED
            print(f'{color}Hmm you don\'t know where that is.')
            goto()
#every stinking locations
def gotoHome():
    color = Fore.GREEN
    print(f'{color}Welcome to base!')
    time.sleep(1)
    chooseMove()
def gotoGrasslands():
    color = Fore.GREEN
    print(f'{color}Vast open fields stretch before you!')
    time.sleep(1)
    chooseMove()
def gotoMountains():
    color = Fore.GREEN
    print(f'{color}Massive rocky mountains arise!')
    time.sleep(1)
    chooseMove()
def gotoCaves():
    color = Fore.GREEN
    print(f'{color}Dark slimy caves await your path!')
    time.sleep(1)
    chooseMove()
def gotoTundra():
    color = Fore.GREEN
    print(f'{color}Cold dark tundra up ahead!')
    time.sleep(1)
    chooseMove()
def gotoDesert():
    color = Fore.GREEN
    print(f'{color}Dry arid desert is all around you!')
    time.sleep(1)
    chooseMove()
def gotoCastle():
    color = Fore.GREEN
    print(f'{color}Welcome to the kings castle!')
    time.sleep(1)
    chooseMove()
def gotoVillage():
    color = Fore.GREEN
    print(f'{color}You have entered the village!')
    time.sleep(1)
    chooseMove()





def tempStart():
    color = Fore.GREEN
    print(f'{color}Game Start!')
    print('What do you want to do? ')
    chooseMove()

tempStart()