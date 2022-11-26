import random
from math import sqrt

DICE25 = [
    "RUGRWO",
    "TITEII",
    "USENSS",
    "ONWUOT",
    "IYPRRR",
    "PSIRFY",
    "HLRHDO",
    "OUOTTO",
    "HDDNTO",
    "AEAEEE",
    "FAIASR",
    "NNENDA",
    "KQXZBJ",
    "FAYISR",
    "ENGNMA",
    "ARASAF",
    "MEAEEE",
    "NSCTCE",
    "TTTEOM",
    "NRLHOD",
    "LETPIC",
    "NOLDHR",
    "GUEEMA",
    "CIEPTS",
    "CIIETL"
]

def rollDice(boardDim):
    if boardDim == 5:
        dice = DICE25
    else:
        raise Exception("Not a valid board dimension")
    random.shuffle(dice)
    shuffled = [random.choice(d) for d in dice]
    i = 0
    layout = []
    for _ in range(boardDim):
        row = []
        for _ in range(boardDim):
            row.append(shuffled[i])
            i += 1
        layout.append(row)
    return layout
