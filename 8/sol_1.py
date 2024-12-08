from enum import Enum
from typing import Tuple


def search(x: int, y: int, arr, antidotes, negX: bool = False, negY: bool = False):
    for offSetX in range(0, int(len(arr)/2) + 1):
        for offSetY in range(0, int(len(arr[x])/2) + 1):
            if offSetY == 0 and offSetX == 0:
                continue
            if negX:
                xN = x - 2 * offSetX
                xN2 = x - offSetX
            else:
                xN = x + 2 * offSetX
                xN2 = x + offSetX
            if negY:
                yN = y - 2 * offSetY
                yN2 = y - offSetY
            else:
                yN = y + 2 * offSetY
                yN2 = y + offSetY
            

            if xN < 0 or xN >= len(arr):
                continue
            if yN < 0 or yN >= len(arr[xN]):
                continue
            if xN2 < 0 or xN2 >= len(arr):
                continue
            if yN2 < 0 or yN2 >= len(arr[xN2]):
                continue
            letter = arr[xN][yN]
            if letter != ".":
                if arr[xN2][yN2] == letter:
                    antidotes[x][y] = 1
                    break


with open("input") as file:
    text = file.readlines()
    arr = [list(line) for line in text]
    arr = [line[:-1] if line[-1] =="\n" else line for line in arr ]
    antidotes = [line.copy() for line in arr.copy()]
    result = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            antidotes[x][y] = 0
            search(x, y, arr, antidotes, False, False)
            search(x, y, arr, antidotes, True, False)
            search(x, y, arr, antidotes, False, True)
            search(x, y, arr, antidotes, True, True)

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            result += antidotes[x][y]
    print(result)
