from room import Room
from player import Player


# Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }
rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "outside", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "foyer", ["torch"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "overlook", ["match"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "narrow",[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "treasure", []),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#
class Main:
    def start(self):
        # Make a new player object that is currently in the 'outside' room.
        playerA = Player('Natalia', rooms['outside'])
        print('Welcome ' + playerA.name + '!')
        playerA.getRoom()
        
        
        move = ''
        
        while move != 'q':
            move = input(">>>>>>Your next move? w(west), s(south), n(north), e(east), i(inventory) or q(quit): ")
            
            if move != 'q':
                if move == 'i':
                    playerA.room.view_items()
                    playerA.view_bag()
                    action = input(">>>>>>Add (a), Drop (d) an item, or Skip(s): ")
                    
                    if action == 'a' or action == 'd':
                        number = input(">>>>>>Item Number: ")
                        try:
                            int(number)
                        except ValueError:
                            print("Not a valid number!")
                        if action == 'a':
                            if int(number) <= (len(playerA.room.items)-1):
                                playerA.add_item(playerA.room.items[int(number)])
                                playerA.room.remove_item(int(number))
                        else:
                            playerA.room.add_item(playerA.bag[int(number)])
                            playerA.drop_item(int(number))
                    
                        playerA.room.view_items()
                        playerA.view_bag()
                        
                else:
                    moveKey = move + '_to'
                    
                    try:
                        print(getattr(playerA.room,moveKey).shortname)
                        rooms[getattr(playerA.room,moveKey).shortname]
                    except AttributeError:
                        print('>>>>>>>There is no way on that direction! Try again!\n')
                        playerA.getRoom()
                    except KeyError:
                        print('>>>>>>>There is no way on that direction! Try again!\n')
                        playerA.getRoom()
                    else:
                        playerA.room = rooms[getattr(playerA.room,moveKey).shortname]
                        playerA.getRoom()
                        
                            
            else:
                print('See you later!')

new_game = Main()
new_game.start()