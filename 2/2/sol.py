from enum import Enum
import functools
from typing import List

class Directions(Enum):
    ASC = 0
    DESC = 1

def check_line(line: str) -> int:
    elements = list(map(lambda x: int(x), line.split(" ")))
    score = 0
    for i in range(len(elements)):
        # Trying all possibilities of removing one. Could probably be more efficient by removing first and then for each error try removing current and next
        elements_cp = elements[:i] +(elements[i+1:] if i != len(elements)-1 else [])
        score += check_line_elements(elements_cp)
        print(elements, elements_cp)
    return 1 if score > 0 else 0


def check_line_elements(elements: List[int]) -> int:
    even = False
    uneven = False
    for i in range(len(elements)-1):
        diff = elements[i+1] - elements[i]
        if diff < 0:
            uneven = True
        if diff > 0:
            even = True
        if even and uneven:
            return 0
        if abs(diff) == 0 or abs(diff)>3:
            return 0
    return 1


with open("./2/2/input") as file:
    lines = file.readlines()
    report_values = list(map(lambda line: check_line(line), lines))
    print(functools.reduce(lambda a, b: a+b, report_values))
