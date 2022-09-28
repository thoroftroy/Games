import time
import pygame
import random
import threading
from colorama import init, Fore, Back, Style
init()
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
#GAME FUNCTIONS
#this is the tutorial section
def tutorialWorld(fled,xp,coins,playerhp,playerdam,playerdef,floor):
    color = Fore.LIGHTGREEN_EX
    print(f'{color}Welcome to the tutorial!')
    time.sleep(1)
    print(f'{color}Okay how do we start...')
    print(f'{color}The game is pretty simple, when exploring the dungeon you can come across')
    print(f'{color}all sorts of things, generally it will tell you your options')
    print(f'{color}when you are nearby. For exsample, if you are approched by an enemy')
    print(f'{color}you will be given the option to attack it, defend from it, or flee from it')
    print(f'{color}keep in mind that your choices matter. You can also find loot in chests')
    print(f'{color}or from killing enemies. Feel free to get as strong as you can.')
    print(f'{color}As you progress the monsters will get harder and harder based on what floor')
    print(f'{color}of the dungeon you are on. Make sure you are strong enough before')
    print(f'{color}going down a floor. Each time you make it to the end')
    print(f'{color}of a floor you can battle a boss. Are you getting all of this?')
    time.sleep(1)
    print(f'{color}According to all known laws of aviation, there is no way a bee')
    print(f'{color}should be able to fly. Its wings are too small to get')
    print(f'{color}its fat little body off the ground. The bee, of course, flies anyway')
    print(f'{color}because bees dont care what humans think is impossible. Yellow, black. Yellow, black.')
    print(f'{color}Yellow, black. Yellow, black. Ooh, black and yellow!')
    print(f'{color}Were no strangers to love, You know the rules and so do I')
    print(f'{color}A full commitments what Im thinking of, You wouldnt get this from any other guy')
    print(f'{color}anddd as I was saying you there are multiple endings to this game')
    print(f'{color}When you are given a choice in what you want to do you dont have to follow the options')
    print(f'{color}For exsample, when I ask you what move you want to take when you find a tree')
    print(f'{color}you could answer with yes, no, eat, or anything else you can think of')
    print(f'{color}There are a lot of differant options for what can happen in this game')
    print(f'{color}Just try random things until you find them all!')
    time.sleep(1)
    print(f'{color}...')
    time.sleep(5)
    print(f'{color}I feel like that might be a bit too much all at once..')
    time.sleep(3)
    print(f'{color}Okay here, you can fight this slime, see how you do!')
    time.sleep(1)
    print(f'{color}oh btw you cant see all the stats of your enemy at all times')
    time.sleep(1)
    tut = 'true'
    slimeMon(tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
def tutorialPt2(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    color = Fore.LIGHTGREEN_EX
    print(f'{color}So how was your battle?')
    time.sleep(2)
    print(f'{color}Now I know that was an easy one, slimes generally are...')
    print(f'{color}Honestly I think you can figure everything else out')
    time.sleep(1)
    print(f'{color}So good luck, theres a lot to discover and explore!')
    world(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    
#this is the main game section
def world(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    print('')
    print('')
    color = Fore.LIGHTGREEN_EX
    print(f'{color}Welcome to the Dungeon!!!')
    time.sleep(2)
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print(f'{color}The real adventure starts now!')
    time.sleep(5)
    print(f'{color}So..? are you just gonna sit there? Go out there and explore!')
    color = Fore.MAGENTA
    choose = input("Do you want to explore? ")
    color = Fore.LIGHTGREEN_EX
    if(choose == 'Yes') or (choose == 'yes'):
        explore()
    elif(choose == 'No') or (choose == 'no'):
        color = Fore.GREEN
        time.sleep(2)
        print(f'{color}...')
        time.sleep(2)
        print(f'{color}This... is an exploration game..')
        time.sleep(3)
        print(f'{color}Why are you even here????')
        print(f'{color}Just go exploring its not that bad...')
        time.sleep(5)
        print(f'{color}Yeah you dont get a choice you are going, I dont want you around here anymore.')
        explore()
    else:
        print(f'{color}What are you typing... Fine, I will do it for you')
        explore()

#exploration section
def explore():
    color = Fore.LIGHTGREEN_EX
    print(f'{color}You wander aimlessly...')
    print(5) 
    time.sleep(1)
    print(4) 
    time.sleep(1)
    print(3) 
    time.sleep(1)
    print(2) 
    time.sleep(1)
    print(1) 
    time.sleep(1)
    wand = random.randint(1,10)
    if(wand == 1):
        print('You found a chest!')
        chest()
    elif(wand == 2):
        print('You found a tree!')
        tree()
    elif(wand == 3):
        print('You found an enemy!')
        enemySpotted()
    elif(wand == 4):
        print('You found a shop')
        shop()
    elif(wand == 5):
        print('You found some coins!')
        coinPile()
    elif(wand == 6):
        print('You found a tomb!')
        tomb()
    elif(wand == 7):
        print('You found... Nothing...')
        nothing()
    elif(wand == 8):
        print('You found.. Some sand... I dont like sand..')
        sand()
    elif(wand == 9):
        print('Andddd thats a rock...')
        rock()
    elif(wand == 10):
        print('Mmm yes thats some horse dung.. STOP DONT EAT THAT')
        horseDung()
    else:
        print('You founds a potato!')
        potato()
    
#discoveries/events
#chest (grants random rewards)
def chest():
    print('As you gaze apon the chest glistening in.. you know what &#@! it.. Its a box ._.')
    explore()
#tree (the player can try to punch it, 10% chance to summon an ent, otherwise nothing happens)
def tree():
    print('Yep thats a tree.. Dont hit the poor thing')
    choose = input("What do you do to the tree? ")
    if(choose == 'yes') or (choose == 'Yes'):
        time.sleep(3)
        print('...')
        time.sleep(3)
        print('Yes...? That doesnt even make sense...')
        time.sleep(3)
        print('Are you sure you read that right? You found a tree...')
        print('I was just asking what you could do to the tree...')
        time.sleep(2)
        print('andddd we are moving on')
        explore()
    elif(choose == 'hit') or (choose == 'Hit'):
        time.sleep(1)
        print('I JUST SAID NOT TO DO THAT')
        time.sleep(1)
        print('YOU COULD HAVE A LITTLE RESPECT!!')
        time.sleep(1)
        print('But as you wish... You hit the tree')
        time.sleep(3)
        print('Did you expect something to happen?')
        print('I geuss your hands hurt a little...')
        time.sleep(2)
        print('andddd we are moving on')
        explore()
    elif(choose == 'eat') or (choose == 'Eat'):
        time.sleep(2)
        print('...')
        time.sleep(2)
        print('You are going to eat a tree?????')
        time.sleep(2)
        print('It isnt a head of lettus, that isnt going to go too well...')
        print('But if you say so?')
        time.sleep(1)
        print('You attept to eat the tree. Your teeth hurt.')
        explore()
    elif(choose == 'no') or (choose == 'No'):
        print('okay a wise guy huh')
        time.sleep(1)
        print('You are just going to "no" ey ???')
        print('Go ahead, no right now')
        time.sleep(4)
        print('I am waiting...')
        time.sleep(4)
        print('I am still waiting...')
        time.sleep(4)
        print('I am still still waiting...')
        time.sleep(4)
        print('I am still still still waiting...')
        time.sleep(4)
        print("Have you no'd yet?")
        print('No? Well why not??? MAYBE CAUSE ITS IMPOSSIBLE')
        time.sleep(1)
        explore()
    elif(choose == 'wear') or (choose == 'Wear'):
        print('You are going to wear a tree...')
        time.sleep(1)
        print('How do you even think of these things...')
        time.sleep(1)
        print('Fine you wear the tree. Are you happy now')
        print(' ***Achivement Unlocked: Gain a Tree Hat*** ')
        time.sleep(3)
        print('Just imagine some fireworks and move on')
        explore()
    elif(choose == 'sleep') or (choose == 'Sleep'):
        print('Sleeping next to a tree does sound nice doesnt it')
        time.sleep(1)
        print('How long would you like to rest here good sir?')
        choose = input("How long will you sleep? (50 or 100 seconds) ")
        if(choose > 50):
            print('Thats a long time to sleep... Okay well if you insit...')
            print('Ehh this is close enough')
            time.sleep(25)
            print('Well you are a forth of the way through...')
            time.sleep(25)
            print('How ya feeling bud?')
            time.sleep(25)
            print('Hush little baby dont say a word, papas gonna bite the head off a bird')
            time.sleep(25)
            print('WAKE UP. Andddd we are done here')
            explore()
        elif(choose <= 50):
            print('Okay thats not too long, enjoy a small rest')
            time.sleep(25)
            print('Woahhhhh were half way thereeee. WOAHHHHHH LIVING ON A PRAYER')
            time.sleep(25)
            print('Did you have a nice nap? Lets go')
            explore()
        else:
            print('andd I am not quite sure what you put soooo')
            time.sleep(1)
            explore()
    elif(choose == 'fight') or (choose == 'Fight'):
        print('You want to fight a tree?')
        time.sleep(1)
        print('Okay go for it')
        treemon()
    elif(choose == 'burn') or (choose == 'Burn'):
        print('')
    elif(choose == 'pee') or (choose == 'Pee'):
        print('')
    elif(choose == 'water') or (choose == 'Water'):
        print('')
    elif(choose == 'draw') or (choose == 'Draw'):
        print('')
    elif(choose == 'cut') or (choose == 'Cut'):
        print('')
    elif(choose == 'talk') or (choose == 'Talk'):
        print('')
    elif(choose == 'leave') or (choose == 'Leave'):
        print('')
    elif(choose == 'leaf') or (choose == 'Leaf'):
        print('')
    else:
        print('Okayyyyy... we are moving on.')
        time.sleep(1)
        explore()
#enemy (go into combat with a ranom enemy)
def enemySpotted():
    print('Prepare for war!')
    explore()
#shop (litteraly just a shop)
def shop():
    print('Welcome to a little shop.')
    explore()
#coins (gives the option to take coins or leave, if you take them you are ambushed by mersenaries)
def coinPile():
    print('Just a random coin pile.. Just sitting there...')
    explore()
#tomb (this can be dug up for a chance at rewards or an enemy)
def tomb():
    print('You arent a grave robber are you...')
    explore()
#nothing (nothing really happens)
def nothing():
    print('Wind russles, birds chirp. Why are there no graphics you think to yourself. **Shut up** A voice wispers')
    explore()
#sand (nothing generally happens, give a low chance to find gold or a monster)
def sand():
    print('I dont like sand')
    explore()
#rock (low chance for a trap door that lets the player move down a floor)
def rock():
    print('Yep its a rock.. Move on already')
    explore()
#dung (gives the player an amusing fight with the narrator, they can indeed eat the dung)
def horseDung():
    print('Please dont...')
    choose = input("Eat the dung? ")
    if(choose == 'yes') or (choose == 'Yes'):
        print('WHAT THE HECK WHY!???')
        time.sleep(1)
        print('NO I WONT LET YOU DO THAT')
        print('the horse dung is removed from your hands...')
        choose = input("Do you want to look for horse dung? ")
        if(choose == 'yes') or (choose == 'Yes'):
            time.sleep(4)
            print('you find the horse dung...')
            time.sleep(2)
            print('I... Why the %#&*(%#')
            time.sleep(1)
            print('NO')
            print('NO')
            print('NO')
            print('NO')
            print('NO')
            print('NO NO NO NO NO NO ')
            time.sleep(5)
            print('You werent really going to eat it where you...?')
            choose = input("Where you? ")
            if(choose == 'yes') or (choose == 'Yes'):
                print('...')
                time.sleep(3)
                print('I... you dont deserve to play this game anymore...')
                time.sleep(3)
                print('THIS IS YOUR LAST CHANCE, I KNOW YOU HAVE TO BE JOKING WITH ME')
                time.sleep(1)
                print('DO YOU WANT TO EAT THE HORSE DUNG')
                print('THIS IS LITTERALY HORSE POO')
                choose = input("Do you? ")
                if(choose == 'yes') or (choose == 'Yes'):
                    print('...')
                    time.sleep(4)
                    print('I...')
                    time.sleep(1)
                    print('Fine eat it.. see if I care')
                    time.sleep(1)
                    print('Lets see how much health do you have...')
                    print(playerhp)
                    time.sleep(1)
                    print('Okay eat it then ._.')
                    choose = input("Eat the poop? ")
                    if(choose == 'yes') or (choose == 'Yes'):
                        print('...')
                        time.sleep(4)
                        print('...')
                        time.sleep(3)
                        print('...')
                        time.sleep(2)
                        print('...')
                        time.sleep(1)
                        print('...')
                        time.sleep(1)
                        print('Why.. Why are you... okay...')
                        print('Hp: ',playerhp)
                        playerhp = playerhp - 60
                        print('You choose this...')
                        time.sleep(3)
                        print('you eat the slimy oozing horse poo. You disgusting $(#@')
                        print('Hp: ',playerhp)
                        time.sleep(3)
                        print('Are you done yet, can we move on!?')
                        time.sleep(1)
                        print('No? well too bad, we are anyway.')
                        time.sleep(1)
                        explore()
                    elif(choose == 'no') or (choose == 'No'):
                        print('...')
                        time.sleep(1)
                        print('then why... fine we are leaving')
                        time.sleep(1)
                        explore()
                    else:
                        print('I dont know what you where trying to say but we are moving on...')
                        time.sleep(1)
                        explore()
                elif(choose == 'no') or (choose == 'No'):
                    print('WHY WOULD YOU MESS WITH ME FOR SO LONG')
                    time.sleep(1)
                    print('WHAT THE $&(# IS WRONG WITH YOU')
                    time.sleep(1)
                    print('OKAY WE ARE LEAVING')
                    explore()
                    time.sleep(1)
                else:
                    print('I dont know what you where trying to say but we are moving on...')
                    time.sleep(1)
                    explore()
            elif(choose == 'no') or (choose == 'No'):
                print('Thank gosh we are moving right away from that')
                time.sleep(1)
                explore()
            else:
                print('I dont know what you where trying to say but we are moving on...')
                time.sleep(1)
                explore()
        elif(choose == 'no') or (choose == 'No'):
            print('Thank gosh theres some sense in you left...')
            print('Please lets move on and never speak of this agian...')
            time.sleep(1)
            explore()
        else:
            print('I dont know what you where trying to say but we are moving on...')
            time.sleep(1)
            explore()
    elif(choose == 'no') or (choose == 'No'):
        print('Good, dont scare me like that agian')
        print('Now lets move on')
        time.sleep(1)
        explore()
    else:
        print('I dont know what you where trying to say but we are moving on...')
        time.sleep(1)
        explore()
#potato? (you shouldnt be able to get here)
def potato():
    print('How did you... you werent supposed to get here... go back!')
    explore()
    
#COMBAT SECTIONNNNNN
#this is how you can choose to act in combat
def chooseMove(monsterid,treehp,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    time.sleep(1)
    color = Fore.LIGHTGREEN_EX
    print('You can Attack, Defend, or Flee')
    color = Fore.MAGENTA
    choice = input("Choose Attack, Defend, or Flee: ")
    color = Fore.LIGHTGREEN_EX
    if(choice == 'Attack') or (choice == 'attack'):
        attack(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(choice == 'Defend') or (choice == 'defend'):
        defend(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(choice == 'Flee') or (choice == 'flee'):
        flee(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    else:
        print(f'{color}I am not quite sure what you meant.. Try agian')
        chooseMove(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
        
#The attack system
def attack(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    color = Fore.CYAN
    print(f'{color}You attacked the enemy!')
    attackType = random.randint(1,15)
    if(attackType == 1):
        print(f'{color}You punched it in the inner thigh!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 2):
        print(f'{color}Ooooo a kick to the groin!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 3):
        print(f'{color}You slapped his knee!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 4):
        print(f'{color}You bit his ear!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 5):
        print(f'{color}You forced him to listen to Taylor Swift!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 6):
        print(f'{color}You tried to slam into him but fell over!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
        playerhp = playerhp - 1
    elif(attackType == 7):
        print(f'{color}You poked his eyes out!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 8):
        print(f'{color}Oooof you made him step on a lego!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 9):
        print(f'{color}You knocked his head in!!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 10):
        print(f'{color}You punched his gut!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 11):
        print(f'{color}You elbowed his knee!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 12):
        print(f'{color}You force fed him pinaple pizza!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 13):
        print(f'{color}You cut onions in front of him!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 14):
        print(f'{color}You gave him a cookie... and then took it away!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(attackType == 15):
        print(f'{color}You told him a bad joke!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    else:
        print(f'{color}You bit his eyes!')
        hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
        
#The denfending System
def defend(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    color = Fore.CYAN
    print(f'{color}You defend from the enemy!')
    defendType = random.randint(1,2)
    if(defendType == 1):
        print(f'{color}You tried to dodge out of the way')
        coinFlip = random.randint(1,2)
        if(coinFlip == 1):
            print(f'{color}Your dodge succeded')
            chooseMove(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
        else:
            print(f'{color}You failed your dodge...')
            slimeDealings(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
            chooseMove(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(defendType == 2):
        print(f'{color}You try to block the attack!')
        coinFlip = random.randint(1,2)
        if(coinFlip == 1):
            print(f'{color}Your block succeded')
            chooseMove(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
            chooseMove(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
        else:
            print(f'{color}You failed your block...')
            slimeDealings(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
            chooseMove(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
#The running away portion of our code
def flee(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    color = Fore.CYAN
    print(f'{color}You try to flee from the enemy!')
    coinFlip = random.randint(1,100)
    if(coinFlip <= 10):
        print(f'{color}You managed to escape!')
        fled = 'true'
        slimePool(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
        chooseMove(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    else:
        print(f'{color}Well that did not work..')
        fled = 'false'
        slimeDealings(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
        chooseMove(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
#how the player takes damage
def slimeDealings(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    slimeTruedam = (slimedam-playerdef)
    color = Fore.YELLOW
    if(slimeTruedam <= 0):
        slimeTruedam == 1
        playerhp = playerhp - slimeTruedam
        print(f'{color}Hp: ',playerhp)
    else:
        playerhp = playerhp - slimeTruedam
        print(f'{color}Hp: ',playerhp)
#how the player deals damage
def hit(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    if(monsterid == 0):
        slimehp = slimehp-(playerdam-slimedef)
        color = Fore.RED
        print(f'{color}Slime Hp:',slimehp)
        slimeDealings(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
        time.sleep(2)
        if(slimehp <= 0):
            slimePool(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
        else:
            chooseMove(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)

#enemy stats and pools
def slimeMon(tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    color = Fore.LIGHTRED_EX
    print(f'{color}A slime approches you!')
    slimehp = random.randint(20*floor,30*floor)
    slimedam = random.randint(1*floor,2*floor)
    slimedef = random.randint(1*floor,2*floor)
    monsterid = 0
    color = Fore.RED
    print(f'{color}Slime Hp:',slimehp,)
    time.sleep(1)
    chooseMove(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
def slimePool(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    if(fled != 'true'):
        color = Fore.LIGHTRED_EX
        print(f'{color}You killed the slime!')
        xp = xp + random.randint(10*floor,20*floor)
        coins = coins + random.randint(1*floor,4*floor)
        color = Fore.YELLOW
        print(f'{color}You now have ',xp,' Xp!')
        print(f'{color}You now have ',coins,' coins!')
        time.sleep(3)
        if(tut == 'true'):
            print('Back to the Tutorial we go!')
            tutorialPt2(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(fled == 'true'):
        color = Fore.LIGHTRED_EX
        print(f'{color}You ran away like a coward.')
        color = Fore.YELLOW
        print(f'{color}You now have ',xp,' Xp!')
        print(f'{color}You now have ',coins,' coins!')
        time.sleep(2)
        color = Fore.LIGHTGREEN_EX
        print(f'{color}They havent changed...')
        time.sleep(3)
        if(tut == 'true'):
            color = Fore.LIGHTGREEN_EX
            print(f'{color}Back to the Tutorial we go!')
            tutorialPt2(monsterid,slimehp,slimedam,slimedef,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
def treemon(monsterid,treehp,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor):
    color = Fore.LIGHTRED_EX
    print(f'{color}A Tree approches you!')
    treehp = random.randint(200*floor,3000*floor)
    monsterid = 1
    color = Fore.RED
    print(f'{color}Tree Hp:',treehp,)
    time.sleep(1)
    chooseMove(monsterid,treehp,tut,fled,xp,coins,playerhp,playerdam,playerdef,floor)
#ends the game    
def endGame():
    color = Fore.RED
    print(f'{color}You lose')
    f.stop()
        
#text at the start of the game
def foreground():
    print('')
    print('')
    print('')
    print('')
    print('')
    color = Fore.LIGHTGREEN_EX
    print(f'{color}Hello and welcome to the DUNGEON!!!')
    print(f'{color}Prepare yourself it is time to roll for stats!!!')
    print(f'{color}Anddddd you gettttttt')
    color = Fore.YELLOW
    playerhp = random.randint(75,100)
    playerdam = random.randint(10,20)
    playerdef = random.randint(1,3)
    coins = random.randint(10,30)
    xp = 0
    floor = 1
    time.sleep(2)
    print(f'{color}Health:',playerhp)
    time.sleep(1)
    print(f'{color}Damage:',playerdam)
    time.sleep(1)
    print(f'{color}Defense:',playerdef)
    color = Fore.LIGHTGREEN_EX
    print(f'{color}Hmmm I wonder how wealthy you are...')
    time.sleep(3)
    color = Fore.YELLOW
    print(f'{color}Coins:',coins)
    time.sleep(0.5)
    color = Fore.LIGHTGREEN_EX
    if(coins <= 15):
        print(f'{color}Well I suppose that could be worse...')
    elif(coins >= 16):
        print(f'{color}Thats not that bad actually!')
    else:
        print(f'{color}...mk')
    time.sleep(1)
    print(f'{color}I suppose I should teach you how to play the game..')
    time.sleep(1)
    print(f'{color}Butttt only if you want to. This is a game of choices after all')
    print(f'{color}So do you want to play the tutorial? (Yes to play. No to not play.)')
    time.sleep(3)
    color = Fore.MAGENTA
    tutorial = input(f'{color}What will it be? ')
    color = Fore.LIGHTGREEN_EX
    if(tutorial == 'Yes') or (tutorial == 'yes'):
        print(f'{color}Onward to the tutorial')
        time.sleep(1)
        tutorialWorld(fled,xp,coins,playerhp,playerdam,playerdef,floor)
    elif(tutorial == 'No') or (tutorial == 'no'):
        print(f'{color}Okay fine you dont have to do it I geuss.. I didnt want you to anyway')
        world(fled,xp,coins,playerhp,playerdam,playerdef,floor)
    else:
        print(f'{color}Okay if you cant spell... or maybe you cant read... Yeah you get the tutorial')
        time.sleep(1)
        tutorialWorld(fled,xp,coins,playerhp,playerdam,playerdef,floor)
 
#threading things   
f = threading.Thread(name='foreground', target=foreground)
#some global variables
fled = 'false'
f.start()