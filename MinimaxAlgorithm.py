from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State
from MovesGenerator import MovesGenerator
from StateEvaluator import is_gameover
from StateEvaluator import evaluate
obj = MovesGenerator()


def minimax(state):
    states = obj.getNextStates(state)
    if(states):
        return max(map(lambda state: [state, min_play(state, state.whoDidThis)], states), key=lambda x: x[1])
    else:
        return (state, -1)


def min_play(state, oppColor=BLACKCELL):

    if is_gameover(state):
        return evaluate(state, oppColor)

    states = obj.getNextStates(state)
    if (states):
        return min(map(lambda state: max_play(state), states))
    else:
        state.reverse_State()
        return max_play(state)


def max_play(state, oppColor=WHITECELL):
    if is_gameover(state):
        # addToOld(state)
        return evaluate(state, oppColor)

    states = obj.getNextStates(state)
    if (states):
        return max(map(lambda state: min_play(state), states))
    else:
        state.reverse_State()
        return min_play(state)
