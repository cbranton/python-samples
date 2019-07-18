class UserInterface:
    
    # The prompt will be our output to the player. We will initialize it to be the introduction
    # Triple quotes allow our string to span multiple lines.
    intro ="""Welcome to the my house!  Thank you for offering to help me find my keys.\n
        I know I left them somewhere here, and I don't want to be late for class.\n
        As you check each room, you will be told which directions you can go.\n
        You can move north, south, east, or west by typing that direction."""


    def __init__ (self):
          # Show the introduction to the game
          self.printMessage(self.intro)

          
##    def showIntroduction(self):
##        print(self.prompt)
##        print("------------------------------------------------------")
          
    def getInput(self, prompt):
        direction = input(prompt+"\n")
        return direction

    def printMessage(self, msg):
        print(msg)
        print("------------------------------------------------------")
