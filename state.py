from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL


class State:
    def __init__(self, board, whoDidThis):
        self.board = []
        for row in board:
            self.board.append(list(row))
        self.whoDidThis = whoDidThis
        self.x = -1
        self.y = -1

    def currentState(self):
        return self

    def generateID(self):
        tempId=""
        for row in board:
            for col in board:
                if (board[row][col] ==0):
                    tempId+='0'
                if (board[row][col] ==1):
                    tempId+='1'
                if (board[row][col] ==2):
                    tempId+='2'
        self.id=tempId
        return (self.id,self.whoDidThis)

    def is_gameover(self):
        for row in board:
            for col in board:
                if (board[row][col]==0):
                    return true
        return false

    def evaluate(self):
        white_Counter=0
        black_Counter=0
        for row in board:
            for col in board:
                if (board[row][col]==1):
                    black_Counter+=1
                if (board[row][col] == 2):
                    white_Counter+=1
        return white_Counter-black_Counter