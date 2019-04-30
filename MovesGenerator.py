from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State


class MovesGenerator:
    def getNextStates(self, state):
        states = []
        r = -1
        for row in state.board:
            r += 1
            c = -1
            for cell in row:
                c += 1
                stateTemp = self.movesRight(state, r, c)
                if(stateTemp != None):
                    states.append(stateTemp)
        return states

    def movesRight(self, state: State, row, column):
        if(state.board[row][column] != EMPTYCELL):
            return None

        oppColor = state.whoDidThis
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        state.board[row][column] = myColor
        column += 1

        while(state.board[row][column] == oppColor):
            state.board[row][column] = myColor
            column += 1

        if(state.board[row][column] == myColor):

            return state

        return None


state = State([[EMPTYCELL, WHITECELL, WHITECELL, BLACKCELL]], WHITECELL)
print(state.board)
movesGenerator = MovesGenerator()
print(movesGenerator.getNextStates(state)[0].board)
