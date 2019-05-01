from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State
from MovesGenerator import MovesGenerator
from MinimaxAlgorithm import minimax


state = State(
    [
        [EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL,
            EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL],
        [EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL,
            EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL],
        [EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL,
            EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL],
        [EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL,
            EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL],
        [EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL,
            EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL],
        [EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL,
            EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL],
        [EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL,
            EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL],
        [EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL,
            EMPTYCELL, EMPTYCELL, EMPTYCELL, EMPTYCELL],
    ], WHITECELL)

print(f"Input: ")
print("x: " + str(state.x) + " , Y: " + str(state.y))
for row in state.board:
    print(row)
print("\n")

movesGenerator = MovesGenerator()
s = minimax(state)

print(f"Next State: ")
print("x: " + str(s[0].x) + " , Y: " + str(s[0].y))
for row in s[0].board:
    print(row)
print("\n")
s = minimax(s[0])
print(f"Next State: ")
print("x: " + str(s[0].x) + " , Y: " + str(s[0].y))
for row in s[0].board:
    print(row)
print("\n")
