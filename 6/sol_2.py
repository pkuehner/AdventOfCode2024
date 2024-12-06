from enum import Enum
from typing import Tuple


class Directions(int, Enum):
    T = 0
    R = 1
    B = 3
    L = 4


class FieldValues(str, Enum):
    FREE = "."
    VISITED = "x"
    BLOCKED = "#"


def step(x: int, y: int, direction: Directions) -> Tuple[int, int]:
    if direction == Directions.T:
        return (x - 1, y)
    if direction == Directions.R:
        return (x, y + 1)
    if direction == Directions.B:
        return (x + 1, y)
    if direction == Directions.L:
        return (x, y - 1)


def turn(direction: Directions) -> Directions:
    if direction == Directions.T:
        return Directions.R
    if direction == Directions.R:
        return Directions.B
    if direction == Directions.B:
        return Directions.L
    if direction == Directions.L:
        return Directions.T


def search(xOld: int, yOld: int, arr_cp, visited_cp, direction: Directions):
    while True:
        visited_cp[xOld][yOld] = direction
        arr_cp[xOld][yOld] = FieldValues.VISITED
        for i in range(4):
            xN, yN = step(xOld, yOld, direction)

            if xN < 0 or xN >= len(arr_cp):
                #print("Finishing 2")
                return 0
            if yN < 0 or yN >= len(arr_cp[xOld]):
                #print("Finishing 2")
                return 0

            if arr_cp[xN][yN] == FieldValues.BLOCKED:
                direction = turn(direction)
            elif arr_cp[xN][yN] == FieldValues.VISITED and visited_cp[xN][yN] == direction:
                return 1
            else:
                xOld = xN
                yOld = yN
                break


with open("input") as file:
    text = file.readlines()
    arr = [list(line) for line in text]
    visited = [line.copy() for line in arr.copy()]
    result = 0
    startX = 0
    startY = 0
    startDirection = Directions.T
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            visited[x][y] = -1 #Initial
            startingValue = arr[x][y]
            if startingValue == ".":
                arr[x][y] = FieldValues.FREE
            elif startingValue == "#":
                arr[x][y] = FieldValues.BLOCKED
            elif startingValue != "\n":
                startX = x
                startY = y
                arr[x][y] = FieldValues.FREE
                if startingValue == "^":
                    startDirection = Directions.T
                elif startingValue == ">":
                    startDirection = Directions.R
                elif startingValue == "<":
                    startDirection = Directions.L
    
    result = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            arr_cp = [line.copy() for line in arr.copy()]
            visited_cp = [line.copy() for line in visited.copy()]
            if arr_cp[x][y] == FieldValues.FREE:
                arr_cp[x][y] = FieldValues.BLOCKED
                result+= search(startX, startY, arr_cp, visited_cp, startDirection)
    print(result)

