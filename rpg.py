import random
import time
#define the stats of the player and enemies
player = {'name': '', 'health': 100, 'attack': 10, 'defense': 5}
enemies = [{'name': 'Goblin', 'health': 50, 'attack': 5, 'defense': 2},
           {'name': 'Orc', 'health': 75, 'attack': 8, 'defense': 4},
           {'name': 'Dragon', 'health': 150, 'attack': 15, 'defense': 10}]
inventory = []
#print the stats of the player
def print_status():
    print('\nPlayer:', player['name'], '\nHealth:', player['health'], '\nAttack:', player['attack'], '\nDefense:', player['defense'])
#the fight enemy function
def fight(enemy):
    print('You are fighting', enemy['name'])
    #keep looping until something dies
    while player['health'] > 0 and enemy['health'] > 0:
        print_status()
        choice = input('What would you like to do? (attack/defend/run): ').lower()
        if choice == 'attack':
            damage = random.randint(player['attack'] - 2, player['attack'] + 2)
            print('You attack for', damage, 'damage.')
            enemy['health'] -= damage
        elif choice == 'defend':
            player['defense'] += 1
            print('You defend, increasing your defense by 1.')
        elif choice == 'run':
            if random.random() < 0.5:
                print('You successfully ran away.')
                return
            else:
                print('You failed to run away.')
        else:
            print('Invalid choice, try again.')
            continue
        
        if enemy['health'] <= 0:
            print('You defeated', enemy['name'])
            return
        else:
            damage = random.randint(enemy['attack'] - 2, enemy['attack'] + 2) - player['defense']
            if damage < 0:
                damage = 0
            print(enemy['name'], 'attacks for', damage, 'damage.')
            player['health'] -= damage
            
    if player['health'] <= 0:
        print('You died.')
    else:
        print(enemy['name'], 'defeated you.')
#exploring which isn't entirly implemented
def explore():
    directions = ["north", "south", "east", "west"]
    num_directions = len(directions)
    random_direction = random.randint(0, num_directions-1)
    print("You explore to the " + explore())
    return directions[random_direction]
#now lets make a basic inventory function
def add_to_inventory(item):
    inventory.append(item)
def remove_from_inventory(item):
    if item in inventory:
        inventory.remove(item)
    else:
        print("Item not found in inventory.")
def display_inventory():
    print("Inventory:")
    if not inventory:
        print("Empty.")
    else:
        for item in inventory:
            print("- " + item)
# example usage:
#add_to_inventory("Sword")
#add_to_inventory("Potion")
#display_inventory()
#remove_from_inventory("Sword")
#display_inventory()

#the main startup funciton
def main():
    player['name'] = input('What is your name? ')
    print('Welcome, ', player['name'], '.')
    #lets the fight begin
    while True:
        enemy = random.choice(enemies)
        fight(enemy)
        if player['health'] <= 0:
            break
        choice = input('Would you like to keep playing? (y/n): ').lower()
        if choice != 'y':
            break
    print('Thanks for playing!')
#it do be doing something doe  
if __name__ == '__main__':
    main()
