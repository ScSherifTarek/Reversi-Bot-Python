from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL


class State:
    def __init__(self, board, whoDidThis):
        self.board = board
        self.whoDidThis = whoDidThis
        self.id = self.generateID()

    def generateID(self):
        return 0
