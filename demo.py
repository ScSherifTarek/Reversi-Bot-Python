from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State
from MovesGenerator import MovesGenerator
from MinimaxAlgorithm import minimax
state = State(
    [
        [BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL,BLACKCELL, WHITECELL, BLACKCELL],
        [EMPTYCELL, WHITECELL, BLACKCELL, WHITECELL,BLACKCELL, WHITECELL, BLACKCELL],
        [BLACKCELL, WHITECELL, WHITECELL, WHITECELL,WHITECELL, EMPTYCELL, BLACKCELL],
        [BLACKCELL, EMPTYCELL, WHITECELL, EMPTYCELL,WHITECELL, WHITECELL, EMPTYCELL],
        [BLACKCELL, WHITECELL, WHITECELL, WHITECELL,WHITECELL, WHITECELL, BLACKCELL],
        [EMPTYCELL, WHITECELL, EMPTYCELL, WHITECELL,BLACKCELL, WHITECELL, BLACKCELL],
        [BLACKCELL, WHITECELL, EMPTYCELL, BLACKCELL,BLACKCELL, WHITECELL, BLACKCELL],
    ], WHITECELL)

print(f"Input: ")
print("x: " + str(state.x) + " , Y: " + str(state.y))
for row in state.board:
    print(row)
print("\n")

movesGenerator = MovesGenerator()
s=minimax(state);

print(f"Next State: ")
print("x: " + str(s[0].x) + " , Y: " + str(s[0].y))
for row in s[0].board:
    print(row)
print("\n")
s=minimax(s[0]);
print(f"Next State: ")
print("x: " + str(s[0].x) + " , Y: " + str(s[0].y))
for row in s[0].board:
    print(row)
print("\n")