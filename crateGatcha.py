import time
import random
#alrighty we are gonna make a gatha game where you unlock things
#this gatha will be collecting crate bots
#here are the differant bots with their rarities, specials cannot be unlocked through the normal gatcha, basic will be purchased from the store just like special will but basic is super easy to come by and special is expensive. ALl other varients are throuhg the gatcha and get stronger as they go
basic = ['Crate Bot MK1','1a','2a','3a','4a','5a','6a','7a','8a','9a']
common = ['Crate Bot MK2','1b','2b','3b','4b','5b','6b','7b','8b','9b']
uncommon = ['Crate Bot MK3','1c','2c','3c','4c','5c','6c','7c','8c','9c']
rare = ['Crate Bot MK4','1d','2d','3d','4d','5d','6d','7d','8d','9d']
superRare = ['Crate Bot MK5','1e','2e','3e','4e','5e','6e','7e','8e','9e']
ultraRare = ['Crate Bot MK6','1f','2f','3f','4f','5f','6f','7f','8f','9f']
megaRare = ['Crate Bot MK7','1g','2g','3g','4g','5g','6g','7g','8g','9g']
legendary = ['Crate Bot MK8','1h','2h','3h','4h','5h','6h','7h','8h','9h']
mythical = ['Crate Bot MK9','1i','2i','3i','4i','5i','6i','7i','8i','9i']
special = ['Worm','Worm God','Big Ben',]
#globals
unlocked = ['Crate Bot MK1']
botType = 'null'
def gatcha():
    #here we roll for a random bot
    botType = random.randint(1,9)
    if(botType == 1):
        unlocked.append(basic[random.randint(0,len(basic)-1)])
    elif(botType == 2):
        unlocked.append(common[random.randint(0,len(common)-1)])
    elif(botType == 3):
        unlocked.append(uncommon[random.randint(0,len(uncommon)-1)])
    elif(botType == 4):
        unlocked.append(rare[random.randint(0,len(rare)-1)])
    elif(botType == 5):
        unlocked.append(superRare[random.randint(0,len(superRare)-1)])
    elif(botType == 6):
        unlocked.append(ultraRare[random.randint(0,len(ultraRare)-1)])
    elif(botType == 7):
        unlocked.append(megaRare[random.randint(0,len(megaRare)-1)])
    elif(botType == 8):
        unlocked.append(legendary[random.randint(0,len(legendary)-1)])
    elif(botType == 9):
        unlocked.append(mythical[random.randint(0,len(mythical)-1)])

def removeDups(unlocked):
    unlocked = list(dict.fromkeys(unlocked))
    unlocked.sort()
    print(unlocked)


count = random.randint(1,5)
while (count < 100):   
    count = count + 1
    gatcha()

removeDups(unlocked)
