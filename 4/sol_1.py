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


def search(x: int, y: int, current_letter: str, arr, direction: Directions):
    if x < 0 or x >= len(arr):
        return 0
    if y < 0 or y >= len(arr[x]):
        return 0

    letter = arr[x][y]

    next_letters = {"START": "X", "X": "M", "M": "A", "A": "S"}

    if current_letter == "A":
        if letter == "S":
            return 1
        return 0

    elif letter != next_letters[current_letter]:
        return 0

    else:
        xN, yN = step(x, y, direction)
        return search(xN, yN, next_letters[current_letter], arr, direction)


with open("input") as file:
    text = file.readlines()
    arr = [list(line) for line in text]
    result = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == "X":
                for dir in Directions:
                    result += search(x, y, "START", arr, dir.value)
    print(result)
            
