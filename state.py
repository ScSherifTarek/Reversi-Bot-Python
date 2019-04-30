class State:
    def __init__(self, board, whoDidThis):
        self.board = board
        self.whoDidThis = whoDidThis
        self.id = self.generateID()

    def generateID(self):
        return 0


state1 = State([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], 1)
print(state1.board)
