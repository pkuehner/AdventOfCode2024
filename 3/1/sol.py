from enum import Enum
import functools

import re 
pattern = r'mul\((\d+),(\d+)\)'
def check_line(line: str) -> int:
    sum = 0
    matches = re.findall(pattern, line) 
    enabled = 1
    for match in matches:
        num_1 = int(match[0])
        num_2 = int(match[1]) 
        sum+=enabled*num_1*num_2
    return sum


with open("./3/1/input") as file:
    lines = file.read()
    print(lines)
    print(check_line(lines))

