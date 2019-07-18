import random
from house import Room, House

# The GameWorld class represents the environment of the game

class GameWorld:
    def __init__ (self):
       #make each room for our house
        kitchen = Room("kitchen","The counter is cluttered.  ",["east","south"])
        porch = Room("porch","There is a flowerpot near the door.  ",["north"])  
        entryway = Room("entryway","There is a rug on the floor.  ",["north","east","south"])
        livingroom = Room("living room","There is a couch by the fireplace.  ",["west","north"])
        diningroom = Room("dining room","There is a table near the window.  ",["west","south"])
        
        #create the roomList and doorList, then create the house.
        self.roomList = [kitchen,porch,entryway,livingroom,diningroom]
        self.doorList = [(porch, "north", entryway),(entryway, "north", kitchen),(entryway, "east", livingroom), (livingroom, "north", diningroom),(diningroom, "west", kitchen)]
        self.myhouse = House(self.roomList, self.doorList)

        # We will start on the porch
        self.location = porch
        self.keylocation = random.choice(self.roomList) #choose the hiding place for the key
        self.keylocation.setIsKeyHere(True) #hide the key
        self.foundKey = False

    # returns the description of the current room
    def getCurrentDescription(self):
        return self.location.describeRoom()

    # returns a string with the current location name
    def getCurrentLocation(self):
        return self.location.getRoomName()

    # returns a string describing the result of the last move
    def getResult(self):
        if self.foundKey:
            return "Hurray! You found my keys in the " +self.location.getRoomName()+"!"
        else:
            return "The keys do not seem to be here.  Let's keep looking."   
    
    # processes the player move and updates the world
    def processMove(self, direction):
        newLocation = self.myhouse.pickRoom(self.location, direction)
        #here is where we would put any actions for leaving the room

        #enter the new room
        self.location = newLocation
        # if the keys are found, end the game
        if self.location == self.keylocation:
            self.foundKey = True # stop the while loop
        return self.foundKey
        
        
