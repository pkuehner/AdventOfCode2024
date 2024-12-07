from enum import Enum
from functools import reduce
from typing import List

class Operator(int, Enum):
    PLUS = 0
    MUL = 1
    CONCAT = 2

        
def solution_bf(parts, current_solution, solution_to_be, operator: Operator)-> int:
    if len(parts) == 0:
        if solution_to_be == current_solution:
            return solution_to_be
        return 0
    
    if current_solution > solution_to_be:
        return 0
    
    if operator == Operator.MUL:
        next_sol = current_solution * parts[0]
    elif operator == Operator.PLUS:
        next_sol = current_solution + parts[0]
    elif operator == Operator.CONCAT:
        next_sol = current_solution*10**len(str(parts[0]))+parts[0]

    for operator in Operator: 
        sol = solution_bf(parts[1:], next_sol, solution_to_be, operator)
        if sol == solution_to_be:
            return solution_to_be

    return 0
        
        
    

with open("input") as file:
    text = file.readlines()
    result = 0
    for line in text:
        line_split = line.split(":")
        result_to_be = int(line_split[0])
        parts = [int(x) for x in line_split[1].split(" ")[1:]]
        result += solution_bf(parts, 0, result_to_be, Operator.PLUS)
        print(result)


