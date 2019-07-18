'''
Simple adventure game to illustrate object-oriented programming and
game development concepts.
Requires Python3.
Authors: Chris Branton
Adapted from text-based adventure game by Carol Browning

'''



from world import GameWorld
from ui import UserInterface


class AdventureGame:

    def __init__(self):
        self.ui = UserInterface()
        self.world = GameWorld()
        self.gameOver = False

    # This is the main function for playing the game
    def playGame(self):
        self.ui.printMessage(self.world.getCurrentDescription())
        # each turn, describe current room and ask which way to go next.
        while not self.gameOver:
            move = self.ui.getInput("Which direction now? >>> ")
            self.gameOver = self.world.processMove(move)
            self.ui.printMessage(self.world.getCurrentDescription())
            self.ui.printMessage(self.world.getResult())


if __name__ == '__main__':
    # This code will execute automatically if this is the main module
    AdventureGame().playGame()
