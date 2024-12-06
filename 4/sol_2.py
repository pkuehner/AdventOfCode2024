from enum import Enum
from typing import Tuple


class Directions(int, Enum):
    T = 0
    TR = 1
    R = 2
    BR = 3
    B = 4
    BL = 5
    L = 6
    TL = 7


def step(x: int, y: int, direction: Directions) -> Tuple[int, int]:
    if direction == Directions.T:
        return (x, y - 1)
    if direction == Directions.TR:
        return (x + 1, y - 1)
    if direction == Directions.R:
        return (x + 1, y)
    if direction == Directions.BR:
        return (x + 1, y + 1)
    if direction == Directions.B:
        return (x, y + 1)
    if direction == Directions.BL:
        return (x - 1, y + 1)
    if direction == Directions.L:
        return (x - 1, y)
    if direction == Directions.TL:
        return (x - 1, y - 1)
    print(direction)


def search(xOld: int, yOld: int, direction: Directions):
    x, y = step(xOld, yOld, direction)

    if x < 0 or x >= len(arr):
        return "NO"
    if y < 0 or y >= len(arr[x]):
        return "NO"

    return arr[x][y]


with open("input") as file:
    text = file.readlines()
    arr = [list(line) for line in text]
    result = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == "A":
                letters = [search(x,y, direction) for direction in [Directions.TL, Directions.BR]]
                if "M" in letters and "S" in letters:
                    letters = [search(x,y, direction) for direction in [Directions.BL, Directions.TR]]
                    if "M" in letters and "S" in letters:
                        result += 1
    print(result)                    
                        
