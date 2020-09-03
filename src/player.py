# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.bag = []
        
    def add_item(self, item):
        self.bag.append(item)
    
    def drop_item(self, index):
        if len(self.bag) is 0:
            print("Your bag is empty!")
        else:
            del self.bag[index]
        
    def view_bag(self):
        print("\nIn your bag:")
        if len(self.bag) is not 0:
            for i, e in enumerate(self.bag):
                print(str(i) + "-" + e)
        else:
            print("Your bag is empty!")
    
    def getRoom(self):
        print('***********************************')
        print('You are in: ' + self.room.name)
        print('This room is: ' + self.room.description)