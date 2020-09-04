from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('lantern', 'it gives off a steady amber glow')]), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('map', 'Map to another treasure chest in a different location')]), 

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('sword', "An old and rusty blade, it's been here a while")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('key', "Old rusty key, it has an inscription on it, but it's worn off")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('skeleton', 'Only dusty bones remain in this room')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("NATALIA", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

running = True
first_run = False
direction = ""
get_actions = ['get', 'take', 'pickup']
drop_actions = ['drop', 'putdown', 'place']
game_exit = ['q', 'quit', 'exit']
game_help = ['?', 'help']
directions = { 'n': 'North', 's': 'South', 'e': 'East', 'w': 'West'}

def perform_move(command):
    if command in game_exit:
        print(f'\nThanks for playing {player.name}!')
        global running
        running = False
    elif command in game_help:
        print("\n Valid commands: ['n' : North, 's' : South, 'e' : East, 'w' : West, 'i' : Inventory, 'q','exit','quit' : Quit, '?','help' : Help]\n")
    elif command == 'i':
        print('Inventory: ')
        print('-----------')
        for index, item in enumerate(player.items):
            print(f'{index + 1}. {item.name}')
    else:
        next_room = player.move_to(command)
        if next_room is None:
            print('\nNo room in that direction')
        elif next_room is room['treasure']:
            item_list = [i.name for i in player.items]
            if 'key' not in item_list:
                print("You're missing the key to get in. Please search for a key and come back!")
            else:
                player.current_room = next_room
        else:
            global direction
            direction = directions[command]
            player.current_room = next_room

def perform_action(command):
    if command[0] in get_actions:
        for item in player.current_room.items:
            if item.name == command[1]:
                item.on_take(player)
            else:
                print(f'{command[1]} cannot be found in this room.')
    elif command[0] in drop_actions:
        for item in player.items:
            if item.name == command[1]:
                item.on_drop(player)

def print_room(direction):
    if direction == "":
        print(f'\n\n{player.current_room.name}\n')
        print(f'{player.current_room.description}\n')
    else:
        print(f'\nYou went {direction} to the {player.current_room.name}\n')
        print(f'{player.current_room.description}\n')

while running:    
    print_room(direction)
    command = input(f'\n Where do you want to go {player.name}?\n Enter (n, s, w, or w; q to quit): ').split(' ')
    if len(command) > 1:
        perform_action(command)
        continue
    else:
        perform_move(command[0])