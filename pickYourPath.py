import time
import random
#I would like to make a dungeon crawler
#templates for creaters and things
#order is health,damage,defense
playerStats = [100,5,5]
playerName = 'null'
playerGender = 'null'
#now the monster stats, they will be seperated out
monsterName = ['Slime']
monsterHp = [20]
monsterDam = [3]
monsterDef = [1]
monsterId = 'null'
cleanTime = 'null'

def startFunction():
    print('Let the game begin!')
    playerName = str(input('What is your name traveler? '))
    print('|')
    time.sleep(0.25)
    print('Well hello there...',playerName)
    print('Let us figure out your stats good sir or Madam...')
    time.sleep(0.5)
    print('...')
    time.sleep(0.75)
    playerGender = str(input('Are you a man or a woman? '))
    if(playerGender == 'man') | (playerGender == 'Man'):
        playerGender = 'Sir'
    elif(playerGender == 'woman') | (playerGender == 'Woman'):
        playerGender = 'Madam'
    else:
        print('Okayyyy.... I don\'t know what that is soooo... ')
        time.sleep(0.5)
        print('...')
        time.sleep(0.25)
        print('Well let\'s just call you \'IT\'')
        playerGender = '\'IT\''
    print('...')
    time.sleep(0.5)
    if(playerGender == 'Sir') | (playerGender == 'Madam'):
        print('Alrighty, let\'s get on with this then',playerGender)
    else:
        print('Alrighty, let\'s get on with this then',playerName)
    time.sleep(0.5)
    print('Okay let\'s see your stats...')
    time.sleep(0.25)
    rollPlayerStats(playerName,playerGender,playerStats)
    showPlayerStats(playerName,playerGender,playerStats)
    time.sleep(0.25)
    if(playerStats[0] > 100) & (playerStats[0] < 120):
        print('Well that is fairly average...')
    elif(playerStats[0] < 100):
        print('oooof... Better luck next time')
    else:
        print('Meh, could be better')
    time.sleep(0.5)
    happy = input('Well are you happy with what you got? ')
    if(happy == 'yes') | (happy == 'Yes') | (happy == 'perhaps'):
        print('Gooddddd.... Moving on then..')
        time.sleep(1)
    elif(happy == 'no') | (happy == 'No') | (happy == 'not really'):
        print('Tooooo bad, moving on')
        time.sleep(1)
    else:
        print('Okayyyy, moving on then?')
        time.sleep(1)
    print('You are probably getting bored at this point... Let\'s get into the game then!')
    time.sleep(5)
    print('...')
    time.sleep(4)
    print('...')
    time.sleep(3)
    print('...What, are you waiting for me?')
    print('...')
    time.sleep(1)
    print('okay... I guess I can give you something to do...?')
    time.sleep(3.25)
    goClean = input('Ummm... go clean that room over there? ')
    if(goClean == 'ok')|(goClean == 'Ok')|(goClean == 'yes')|(goClean == 'why not')|(goClean == 'alright')|(goClean == 'Yes')|(goClean == 'Alright')|(goClean == 'fine')|(goClean == 'sure'):
        print('Gooooodddd... Have fun?')
        time.sleep(1)
        cleanRoom(playerName,playerGender,playerStats)
    elif(goClean == 'no')|(goClean == 'No')|(goClean == 'Nah'):
        print('...')
        time.sleep(1)
        whatDo(playerName,playerGender,playerStats)
    else:
        print('Just get to it!')
        time.sleep(1)
        cleanRoom(playerName,playerGender,playerStats)

def cleanRoom(playerName,playerGender,playerStats):
    print('Cleaning in progress... (ETA:5)')
    time.sleep(3)
    print('...')
    time.sleep(3)
    print('Cleaning in progress... (ETA:4.00000009)')
    time.sleep(4)
    print('Cleaning in progress... (ETA:4.00000008)')
    time.sleep(4)
    print('Cleaning in progress... (ETA:4.00000007)')
    time.sleep(4)
    print('Cleaning in progress... (ETA:4.00000006)')
    time.sleep(3)
    print('Are you having funnnnn?')
    time.sleep(1)
    print('Cleaning in progress... (ETA:4.00000005)')
    time.sleep(2)
    print('....')
    time.sleep(1)
    print('You... okay?')
    time.sleep(2)
    print('Cleaning in progress... (ETA:4.00000004)')
    time.sleep(1)
    print('OKAYYYY, I think that\'s enough cleaning...')
    time.sleep(0.5)
    print('..that was boring as heck')
    somethingElse = input('Can we please do something else? ')
    if(somethingElse == 'yes'):
        whatDo(playerName,playerGender,playerStats)
    elif(somethingElse == 'no'):
        print('fine... have fun, I won\'t be comeing back until you are done')
        cleanTime = 4.00000004
        waitClean(playerName,playerGender,playerStats,cleanTime)
    else:
        print('We are moving onnnnn')
        whatDo(playerName,playerGender,playerStats)

def waitClean(playerName,playerGender,playerStats,cleanTime):
    cleanTime = cleanTime - 0.00000001
    time.sleep(2)
    if(cleanTime > 0):
        print('Cleaning in progress... (ETA:',cleanTime,')')
        waitClean(playerName,playerGender,playerStats,cleanTime)
    else:
       print('IT\'S FINALLY OVER')
       
def whatDo(playerName,playerGender,playerStats):
    what = input('Alright what do you want to do then? ')
    
def rollPlayerStats(playerName,playerGender,playerStats):
    playerStats[0] = random.randint(85,140)
    playerStats[1] = random.randint(2,8)
    playerStats[2] = random.randint(1,5)
    
def showPlayerStats(playerName,playerGender,playerStats):
    print('|')
    print('Hp:',playerStats[0],' Damage:',playerStats[1],' Defense:',playerStats[2])    
    print('|')
    
    
    
    
    
    
startFunction()
