#imports
import time
import pygame
import random
import threading
from colorama import init, Fore, Back, Style
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.LIGHTGREEN_EX]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]
#    0 = Black       8 = Gray
#    1 = Blue        9 = Light Blue
#    2 = Green       A = Light Green
#    3 = Aqua        B = Light Aqua
#    4 = Red         C = Light Red
#    5 = Purple      D = Light Purple
#    6 = Yellow      E = Light Yellow
#    7 = White       F = Bright White
init(convert=True)
#global variables
#(universal)
floor = 1
monsterid = 0
#(player)
playerhp = random.randint(75,100)
playerdam = random.randint(50,100)
flee = False
coins = random.randint(20,100)
xp = 0
#(monster)
slime = 'Slime'
slimehp = random.randint(25*floor,35*floor)
slimedam = random.randint(1*floor,5*floor)
bones = 'Bones'
boneshp = random.randint(55*floor,65*floor)
bonesdam = random.randint(3*floor,10*floor)
mercinary = 'Mercinary'
mercinaryhp = random.randint(75*floor,100*floor)
mercinarydam = random.randint(5*floor,10*floor)
tree = 'Tree'
treehp = random.randint(750*floor,1000*floor)
treedam = random.randint(75*floor,100*floor)
zombo = 'Zombo'
zombohp = random.randint(50*floor,100*floor)
zombodam = random.randint(10*floor,20*floor)
#monster lists
monsterListHp = [slimehp,boneshp,mercinaryhp,treehp,zombohp]
monsterListDam = [slimedam,bonesdam,mercinarydam,treedam,zombodam]
monsterList = [slime,bones,mercinary,tree,zombo]
monsterLootCoins = [random.randint(1,5),random.randint(3,10),random.randint(6,30),random.randint(100,500),random.randint(10,50)]
monsterLootXp = [random.randint(10,50),random.randint(30,100),random.randint(60,300),random.randint(1000,5000),random.randint(100,500)]

#show the player stats
def showStats(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp):
    color = Fore.LIGHTGREEN_EX
    print(f'{color}You have: '+str(playerhp)+' hp.')
    print(f'{color}You have: '+str(playerdam)+' damage.')
    print(f'{color}You have: '+str(coinstemp)+' coins.')
    print(f'{color}You have: '+str(xptemp)+' xp.')
    print(f'{color}You are on: '+str(floortemp)+' floor.')
    attackSequence(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)
def showStatsExp(xptemp,coinstemp,floortemp):
    color = Fore.LIGHTGREEN_EX
    print(f'{color}You have: '+str(playerhp)+' hp.')
    print(f'{color}You have: '+str(playerdam)+' damage.')
    print(f'{color}You have: '+str(coinstemp)+' coins.')
    print(f'{color}You have: '+str(xptemp)+' xp.')
    print(f'{color}You are on: '+str(floortemp)+' floor.')
    explore(xptemp,coinstemp,floortemp)

#this is how the player chooses their move in a battle
def attackSequence(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp):
    print('You can attack, dodge, flee, or show stats')
    choose = input('Choose your move: ')
    if(choose == 'Attack') or (choose == 'attack'):
        print('Attacking')
        attack(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)
    elif(choose == 'Dodge') or (choose == 'dodge'):
        print('Dodging')
        defend(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)
    elif(choose == 'Flee') or (choose == 'flee'):
        print('Running Away')
        escape(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)
    elif(choose == 'Stats') or (choose == 'stats'):
        showStats(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp);
    else:
        print('I didn\'t quite get that, could you try again?')
        time.sleep(1)
        attackSequence(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)

#fight monsterList = [slime,bones,mercinary,tree,zombo]
def battle(monsterid,xptemp,coinstemp,floortemp):
    print('Battle has begun')
    print('A '+monsterList[monsterid]+' is attacking you!')
    monsterhp = monsterListHp[monsterid]
    monsterdam = monsterListDam[monsterid]
    playerTemphp = playerhp
    playerTempdam = playerdam
    color = Fore.RED
    print(f'{color}Monster Hp: '+str(monsterhp))
    print(f'{color}Monster Damage: '+str(monsterdam))
    attackSequence(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)
def battleEnd(monsterid,xptemp,coinstemp,floortemp):
    print('You defeated the '+monsterList[monsterid]+'!!!')
    xptemp =+ monsterLootXp[monsterid]
    coinstemp =+ monsterLootCoins[monsterid]
    time.sleep(1)
    print('You now have '+str(xptemp)+' xp and '+str(coinstemp)+' coins!!!')
    time.sleep(1)
    explore(xptemp,coinstemp,floortemp)
    
#these are the move sequences
#attack funcion, lets you attack
def attack(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp):
    time.sleep(1)
    print('You attack the monster!')
    monsterhp -= playerTempdam
    if(monsterhp <= 0):
        print('Oooo he dead')
        battleEnd(monsterid,xptemp,coinstemp,floortemp)
    color = Fore.RED
    print(f'{color}Monster Hp: '+str(monsterhp))
    monsterAttacks(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)
    attackSequence(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)
#defend function, lets you dodge an attack
def defend(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp):
    time.sleep(1)
    chance = random.randint(1,5)
    if(chance == 1) or (chance == 2):
        print('You managed to dodge!')
        time.sleep(1)
        attackSequence(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)
    else:
        print('Your dodge failed!')
        monsterAttacks(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)
#you can try and run
def escape(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp):
    time.sleep(1)
    chance = random.randint(1,100)
    if(chance == 1):
        print('You managed to escape!')
        attackSequence(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)
    else:
        print('You failed to run away!')
        monsterAttacks(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)

#how the player takes damage
def monsterAttacks(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp):
    print('You are being attacked!')  
    playerTemphp -= monsterdam
    color = Fore.LIGHTGREEN_EX
    print(f'{color}Player Hp: '+str(playerTemphp))
    if(playerTemphp <= 0):
        print('You dead boi')
        dead(xptemp,coinstemp,floortemp)
    else:
        attackSequence(monsterhp,monsterdam,playerTemphp,playerTempdam,monsterid,xptemp,coinstemp,floortemp)

#this is the death sequence
def dead(xptemp,coinstemp,floortemp):
    print('So you died ey?')
    time.sleep(1)
    print('Here\'s what ya got:')
    color = Fore.LIGHTGREEN_EX
    print(f'{color}XP: '+str(xptemp))
    print(f'{color}Coins: '+str(coinstemp))
    print(f'{color}Level: '+str(floortemp))
    bye = input('This isn\' gonna be perminent')
    
#randomized exploring function
def explore(xptemp,coinstemp,floortemp):
    find = random.randint(1,1)
    if(find == 1):
        monsterid = random.randint(0,4)
        battle(monsterid,xptemp,coinstemp,floortemp)
    else:
        time.sleep(1)
        print('Hmm Didn\'t find anything.')
        showStatsExp(xptemp,coinstemp,floortemp)
        explore(xptemp,coinstemp,floortemp)
#starts the game
def start():
    print('')
    print('')
    print('')
    coinstemp = coins
    xptemp = xp
    floortemp = floor
    explore(xptemp,coinstemp,floortemp)

start()