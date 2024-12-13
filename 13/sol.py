from enum import Enum
from typing import Tuple

def checkOnePrice(xOffsetA, yOffsetA, xOffsetB, yOffsetB, xPrize, yPrize):
    min_tokens = None
    num_b = (yPrize*xOffsetA-xPrize*yOffsetA)/(yOffsetB*xOffsetA-xOffsetB*yOffsetA)
    
    print(num_b)
    if num_b != int(num_b):
        return 0
    num_a = (xPrize - num_b*xOffsetB)/xOffsetA#

    print(num_a, num_b)

    num_a1 = num_a
    num_a = (yPrize - num_b*yOffsetB)/yOffsetA
    print(num_a)

    if num_a1 != num_a or num_a != int(num_a):
        return 0
    return 3*num_a+num_b
    
with open("input") as file:
    text = file.readlines()
    i = 0
    cost = 0
    while i < len(text):
        a = text[i].split(" ")
        b = text[i+1].split(" ")
        c = text[i+2].split(" ")


        xOffsetA = int(a[2][2:-1])
        yOffsetA = int(a[3][2:-1])
        xOffsetB = int(b[2][2:-1])
        yOffsetB = int(b[3][2:-1])
        xPrize = int(c[1][2:-1])+10000000000000
        yPrize = c[2][2:]
        if yPrize[-1] == "\n":
            yPrize = yPrize[:-1]
        yPrize = int(yPrize)+10000000000000
        print(xOffsetA, yOffsetA, xOffsetA, xOffsetB, xPrize, yPrize)
        i = i+4
        cost += checkOnePrice(xOffsetA, yOffsetA, xOffsetB, yOffsetB, xPrize, yPrize)
    print(cost)

    