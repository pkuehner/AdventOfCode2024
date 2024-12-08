from enum import Enum
from typing import Tuple


def search(x: int, y: int, arr, antidotes):
    letter = arr[x][y]
    if letter ==".":
        return

    for xN in range(len(arr)):
        for yN in range(len(arr[x])):
            letter_2 = arr[xN][yN]
            if xN == x and yN == y:
                continue
            if letter_2 != letter:
                continue
            offSetX = xN-x
            offSetY = yN-y
            for i in range(-len(arr), len(arr)):
                xToFill = x+i*offSetX
                if xToFill < 0 or xToFill >= len(arr):
                    continue
                yToFill = y + i*offSetY
                if yToFill < 0 or yToFill >= len(arr[0]):
                    continue

                antidotes[xToFill][yToFill] = 1  
            
                            


with open("input") as file:
    text = file.readlines()
    arr = [list(line) for line in text]
    arr = [line[:-1] if line[-1] =="\n" else line for line in arr ]
    print(arr)
    antidotes = [line.copy() for line in arr.copy()]
    result = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            antidotes[x][y] = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            search(x, y, arr, antidotes)


    for x in range(len(arr)):
        for y in range(len(arr[x])):
            result += antidotes[x][y]
            if antidotes[x][y] == 1:
                #print(x,y)
                pass
    print(result)

