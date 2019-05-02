from graphics import *
from card import *

def main():
    win = GraphWin("Card test", 400, 200)

    crd = Card(Point(50,50),Point(250,100), num_bits = 16)
    crd.draw(win)
    crd.punch("01110000")
    crd.punch([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0])
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()