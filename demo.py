from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State
from MovesGenerator import MovesGenerator

state  = State(
    [
        [BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL, BLACKCELL, WHITECELL, BLACKCELL],
        [BLACKCELL, WHITECELL, BLACKCELL, WHITECELL, BLACKCELL, WHITECELL, BLACKCELL],
        [BLACKCELL, WHITECELL, WHITECELL, WHITECELL, WHITECELL, EMPTYCELL, BLACKCELL],
        [BLACKCELL, WHITECELL, WHITECELL, EMPTYCELL, WHITECELL, WHITECELL, BLACKCELL],
        [BLACKCELL, WHITECELL, WHITECELL, WHITECELL, WHITECELL, WHITECELL, BLACKCELL],
        [BLACKCELL, WHITECELL, EMPTYCELL, WHITECELL, BLACKCELL, WHITECELL, BLACKCELL],
        [BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL, BLACKCELL, WHITECELL, BLACKCELL],
    ], WHITECELL)

print(f"Input: ")
for row in state.board:
    print(row)
print("\n")

movesGenerator = MovesGenerator()

for s in movesGenerator.getNextStates(state):
    print(f"Next State: ")
    for row in s.board:
        print(row)
    print("\n")