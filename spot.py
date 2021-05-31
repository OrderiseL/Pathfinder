from algorithms.A_STAR_pathfinding import Node
from settings import *

class Spot(Node):
    """
    Class to represent a spot in the grid.
    It has position(row,col), color(allso state).
    """

    def __init__(self):
        super.__init__()
        self.color = WHITE
