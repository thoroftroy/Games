#break out is a game about breaking out of the game
import random
import time
#affinity is how much the narrator likes you
affinity = 'null'

def start():
    affinity = 0
    print('Hello there!')
    hi = input('A:HI! | B:HELLO! | C:hi ')
    if(hi=='a')|(hi=='A'):
        print(':) Well it is a plesure to meet you, what is your name?')
        naming(affinity)
    elif(hi=='b')|(hi=='B'):
        print('WELL SOMEONE IS ENTHUSIASTIC!!')
        time.sleep(0.2)
        print('SO WHAT IS YOUR NAME????')
        naming(affinity)
    elif(hi=='c')|(hi=='C'):
        time.sleep(0.5)
        print('..ray of sunshine aint ya..')
        time.sleep(0.2)
        print('okayyy, so whats your name kid?')
        naming(affinity)
    #so now lets get into the other options
    else:
        print('...')
        affinity -= 0.5
        time.sleep(0.5)
        print('So to answer me just type the letter by the answer you like :)')
        time.sleep(0.75)
        print('Let\'s try that again shall we :)')
        print('Hello there!')
        hi2 = input('A:HI! | B:HELLO! | C:hi ')
        if(hi2=='a')|(hi2=='A'):
            print(':) Well it is a plesure to meet you, what is your name?')
            naming(affinity)
        elif(hi2=='b')|(hi2=='B'):
            print('WELL SOMEONE IS ENTHUSIASTIC!!')
            time.sleep(0.2)
            print('SO WHAT IS YOUR NAME????')
            naming(affinity)
        elif(hi2=='c')|(hi2=='C'):
            time.sleep(0.5)
            print('..ray of sunshine aint ya..')
            time.sleep(0.2)
            print('okayyy, so whats your name kid?')
            naming(affinity)
        else:
            print('...')
            affinity -= 1
            time.sleep(1)
            print('Again? Really ._.')
            time.sleep(0.5)
            print('Let\'s just move on... What is your name?')
            naming(affinity)
    
def naming(affinity):
    print('|')
    name = input('Name: ')
    if(affinity==1)|(affinity==1.5):
        print('Finally gave me something to work with...')
        print('Its an absolute.. plesure.. to meet you',name)
        time.sleep(1)
    else:
        print('Well it\'s nice to meet you',name)
        
start()
