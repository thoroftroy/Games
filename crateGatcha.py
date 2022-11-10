import time
import random
#alrighty we are gonna make a gatha game where you unlock things
#this gatha will be collecting crate bots
#here are the differant bots with their rarities, specials cannot be unlocked through the normal gatcha, basic will be purchased from the store just like special will but basic is super easy to come by and special is expensive. ALl other varients are throuhg the gatcha and get stronger as they go
basic = ['Crate Bot MK1','Electric Crate Bot','Gas Crate Bot','Speedy Crate Bot','Broken Crate Bot','Infested Crate Bot','Tubby Crate Bot','Crate Plane','Crate Boat','Crate','Bot']
common = ['Crate Bot MK2','','','','','','','','','','',]
uncommon = ['Crate Bot MK3','','','','','','','','','','',]
rare = ['Crate Bot MK4','','','','','','','','','','',]
superRare = ['Crate Bot MK5','','','','','','','','','','',]
ultraRare = ['Crate Bot MK6','','','','','','','','','','',]
megaRare = ['Crate Bot MK7','','','','','','','','','','',]
legendary = ['Crate Bot MK8','','','','','','','','','','',]
mythical = ['Crate Bot MK9','','','','','','','','','','',]
special = ['Worm','Worm God','Big Ben','','','','','','','','',]

#globals
unlocked = ['Crate Bot MK1']
def gatcha():
    #here we roll for a random bot
    checkUnlocked()
    botType == random.randint(1,80)
    if(botType == 1):
        append(basic[random.randint(0,len(basic)-1)])
    elif(botType == 2):
        append(common[random.randint(0,len(common)-1)])
    elif(botType == 3):
        append(uncommon[random.randint(0,len(uncommon)-1)])
    elif(botType == 4):
        append(rare[random.randint(0,len(rare)-1)])
    elif(botType == 5):
        append(superRare[random.randint(0,len(superRare)-1)])
    elif(botType == 6):
        append(ultraRare[random.randint(0,len(ultraRare)-1)])
    elif(botType == 7):
        append(megaRare[random.randint(0,len(megaRare)-1)])
    elif(botType == 8):
        append(legendary[random.randint(0,len(legendary)-1)])
    elif(botType == 1):
        append(mythical[random.randint(0,len(mythical)-1)])
    
    
def checkUnlocked():
    #here we check for what bots are unlocked/maxed out. if they are maxed out then we don't want to "unlock" them agian.
    print('I\'l make this later...')
    






