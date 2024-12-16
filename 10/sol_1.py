from enum import Enum
from typing import Tuple


class Directions(int, Enum):
    T = 0
    R = 1
    B = 3
    L = 4

def step(x: int, y: int, direction: Directions) -> Tuple[int, int]:
    if direction == Directions.T:
        return (x - 1, y)
    if direction == Directions.R:
        return (x, y + 1)
    if direction == Directions.B:
        return (x + 1, y)
    if direction == Directions.L:
        return (x, y - 1)


def search(xOld: int, yOld: int, arr, visited, seen: set) ->int:
    value_old = arr[xOld][yOld]
    if value_old == 9:
        seen.add((xOld, yOld))
        return 1
    visited[xOld][yOld] = True
    result = 0
    for direction in Directions:
        xNew, yNew = step(xOld, yOld, direction)

        if xNew >=0 and xNew < len(arr):
            if yNew >=0 and yNew < len(arr):
                value_new = arr[xNew][yNew]
                if not visited[xNew][yNew] and value_new == value_old+1:
                    visited_cp = [line.copy() for line in visited.copy()]
                    result += search(xNew, yNew, arr, visited_cp, seen)
    return result


with open("input") as file:
    text = file.readlines()
    arr = [list(line)[:-1] if line[-1] == "\n" else list(line) for line in text]
    visited = [line.copy() for line in arr.copy()]
    result_2 = 0
    result_1 = 0
    startX = 0
    startY = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            visited[x][y] = False #Initial
            arr[x][y] = int(arr[x][y])
    print(arr)
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == 0:
                visited_cp = [line.copy() for line in visited.copy()]
                seen = set()
                result_2+= search(x, y, arr, visited_cp, seen)
                result_1+= len(seen)

    print(result_1, result_2)

