# If we can go north from the porch to the hall, then we can go south from the hall to the porch.
# We need this function to find the opposite of a direction.
def opposite(direction):
  if direction ==  "north": return "south"
  elif direction == "south": return "north"
  elif direction == "east": return "west"
  elif direction == "west": return "east"



# This class is the pattern for the rooms in an adventure game
class Room:

  def __init__(self,roomName,description,doorList):
    #roomName is a string containing the name of the room
    #description is a string containing a description of the room
    #doorList is a list of strings telling which directions the player may go 
    #isKeyHere is a boolean variable telling whether or not the key is here
    self.roomName = roomName
    self.description = description
    self.doorList = doorList
    # Python requires boolean False to begin upper case
    self.isKeyHere = False
 
  #This method returns a description of the directions the player may go
  def describeDoors(self):
    doorDescription = "There are doors to the "
    for way in self.doorList:
      doorDescription = doorDescription + way + ", "  
    return doorDescription
        
  #This method returns a string describing the room
  def describeRoom(self):
    return "You are in the "+self.roomName+".  "+self.description + self.describeDoors()
    
  # This method sets the value of isKeyHere to the given Boolean value
  def setIsKeyHere(self,value):
    self.isKeyHere = value
    
  # This method returns the name of the room
  def getRoomName(self):
    return self.roomName
    
# this class has an array of rooms and an array of doors.  You can show the introduction to
# the house or choose to go through a door to a new room.
class House:

    def __init__(self,roomList,doorList):
    #roomList is an array of the rooms in the house 
    #doorList is a list of doors between rooms.  A door is of the form (room1, direction, room2)
    #  meaning that if you are in room1 and go through the door in that direction, you enter room2
      self.roomList = roomList
      self.doorList = doorList

    #given a room and a direction, go through the door (if there is one).  Return new room.
    def pickRoom(self,location,direction):
      for door in self.doorList:
        if door[0] == location and door[1] == direction:
          return door[2]
        elif door[2] == location and door[1]==opposite(direction):
          return door[0]
      #if there was no door in that direction, just return the same room.
      return location
