from graphics import *
""" Classes and methods to implement an instruction card.

There are some examples and such 

"""

class Hole (Circle):
    """Hole represents a circle that can be open or closed, depending on
        its state variable
    """
    def __init__(self, center_point, radius):
        super().__init__(center_point, radius)

    def state(self, state):
        if state == 1:
            self.setFill("black")
        else:
            self.setFill("Bisque")



class Card(Rectangle):
    def __init__ (self, point1, point2, num_bits = 8):
        """Initialize a card with the number of holes equal to num_bits"""

        super().__init__(Point(point1.getX() + 1, point1.getY() + 1), point2)
        Line(point1,Point(point1.getX(), point2.getX()))
        Line(point1, Point(point1.getY(), point2.getY()))
        self.setFill("Bisque")
        mid_y = (point1.getY() + point2.getY()) / 2
        width = point2.getX() - point1.getX()
        step = width / (num_bits + 1)
        startX = point1.getX()+ step
        self.holes = []
        for i in range(num_bits):
            d = Hole(Point(startX, mid_y), (step - 4)/2)
            #d.setFill("black")
            self.holes.append(d)
            startX += step

    def punch (self, seq):
        for i in range(len(seq)):
            if seq[i] == 1 or seq[i] == '1':
                self.holes[i].setFill("black")

    def draw(self, win):
        """Override parent draw function to draw card with holes"""

        super().draw(win)
        for i in self.holes:
            i.draw(win)

