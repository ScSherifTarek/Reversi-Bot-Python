from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State


class MovesGenerator:
    def getNextStates(self, state):
        states = []
        r = -1

        # we work on the empty cell we move from the empty cells and check if we can go through it
        # to right or to left or up or bottom or either the way is
        for row in state.board:
            r += 1
            c = -1
            for cell in row:
                c += 1

                if(cell != EMPTYCELL):
                    continue

                # to right
                stateTemp = self.movesRight(state, r, c)
                if(stateTemp != None):
                    states.append(stateTemp)

                # to left
                stateTemp = self.movesLeft(state, r, c)
                if(stateTemp != None):
                    states.append(stateTemp)

                # to bottom
                stateTemp = self.movesBottom(state, r, c)
                if(stateTemp != None):
                    states.append(stateTemp)

                # to top
                stateTemp = self.movesTop(state, r, c)
                if(stateTemp != None):
                    states.append(stateTemp)

                # to top left
                stateTemp = self.movesTopLeft(state, r, c)
                if(stateTemp != None):
                    states.append(stateTemp)

                # to top right
                stateTemp = self.movesTopRight(state, r, c)
                if(stateTemp != None):
                    states.append(stateTemp)

                # to bottom left
                stateTemp = self.movesBottomLeft(state, r, c)
                if(stateTemp != None):
                    states.append(stateTemp)

                # to bottom right
                stateTemp = self.movesBottomRight(state, r, c)
                if(stateTemp != None):
                    states.append(stateTemp)

        return states

    def movesRight(self, state: State, row, column):

        oppColor = state.whoDidThis
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        state.board[row][column] = myColor
        column += 1

        while((column < len(state.board[0])) and (state.board[row][column] == oppColor)):
            state.board[row][column] = myColor
            column += 1

        if((column < len(state.board[0])) and (state.board[row][column] == myColor)):
            return state

        return None

    def movesLeft(self, state: State, row, column):
        oppColor = state.whoDidThis
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        state.board[row][column] = myColor
        column -= 1

        while((column >= 0) and (state.board[row][column] == oppColor)):
            state.board[row][column] = myColor
            column -= 1

        if((column >= 0) and (state.board[row][column] == myColor)):
            return state

        return None

    def movesBottom(self, state: State, row, column):

        oppColor = state.whoDidThis
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        state.board[row][column] = myColor
        row += 1

        while((row < len(state.board)) and (state.board[row][column] == oppColor)):
            state.board[row][column] = myColor
            row += 1

        if((row < len(state.board)) and (state.board[row][column] == myColor)):
            return state

        return None

    def movesTop(self, state: State, row, column):

        oppColor = state.whoDidThis
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        state.board[row][column] = myColor
        row -= 1

        while((row >= 0) and (state.board[row][column] == oppColor)):
            state.board[row][column] = myColor
            row -= 1

        if((row >= 0) and (state.board[row][column] == myColor)):
            return state

        return None

    def movesTopLeft(self, state: State, row, column):

        oppColor = state.whoDidThis
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        state.board[row][column] = myColor
        row -= 1
        column -= 1

        while((row >= 0) and (column >= 0) and(state.board[row][column] == oppColor)):
            state.board[row][column] = myColor
            row -= 1
            column -= 1

        if((row >= 0)and (column >= 0) and (state.board[row][column] == myColor)):
            return state

        return None

    def movesTopRight(self, state: State, row, column):

        oppColor = state.whoDidThis
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        state.board[row][column] = myColor
        row -= 1
        column += 1

        while((row >= 0) and (column < len(state.board[0])) and(state.board[row][column] == oppColor)):
            state.board[row][column] = myColor
            row -= 1
            column += 1

        if((row >= 0)and (column < len(state.board[0])) and (state.board[row][column] == myColor)):
            return state

        return None

    def movesBottomLeft(self, state: State, row, column):

        oppColor = state.whoDidThis
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        state.board[row][column] = myColor
        row += 1
        column -= 1

        while((row < len(state.board)) and (column >= 0) and(state.board[row][column] == oppColor)):
            state.board[row][column] = myColor
            row += 1
            column -= 1

        if((row < len(state.board))and (column >= 0) and (state.board[row][column] == myColor)):
            return state

        return None

    def movesBottomRight(self, state: State, row, column):

        oppColor = state.whoDidThis
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        state.board[row][column] = myColor
        row += 1
        column += 1

        while((row < len(state.board)) and (column < len(state.board[0])) and(state.board[row][column] == oppColor)):
            state.board[row][column] = myColor
            row += 1
            column += 1

        if((row < len(state.board))and (column < len(state.board[0])) and (state.board[row][column] == myColor)):
            return state

        return None


state = State([
    [EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL],
    [EMPTYCELL, BLACKCELL, WHITECELL, EMPTYCELL],
    [EMPTYCELL, WHITECELL, BLACKCELL, EMPTYCELL],
    [EMPTYCELL, BLACKCELL, EMPTYCELL, EMPTYCELL]
], BLACKCELL)

print(state.board)
movesGenerator = MovesGenerator()
print(movesGenerator.getNextStates(state)[0].board)
