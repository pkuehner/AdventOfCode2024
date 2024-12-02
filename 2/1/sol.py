import functools


def check_line(line: str) -> int:
    elements = list(map(lambda x: int(x), line.split(" ")))
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


with open("./2/1/input") as file:
    lines = file.readlines()
    report_values = list(map(lambda line: check_line(line), lines))
    print(functools.reduce(lambda a, b: a+b, report_values))

