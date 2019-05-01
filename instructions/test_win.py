from graphics import *
from card import *

def main():
    win = GraphWin("My Circle", 200, 200)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    d = Hole(Point(100,50), 10)
    d.setFill("blue")
    d.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()