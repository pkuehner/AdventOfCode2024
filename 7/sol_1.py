from enum import Enum
from functools import reduce
from typing import List

class Operator(int, Enum):
    PLUS = 0
    MUL = 1

        
def solution_bf(parts, current_solution, solution_to_be, operator: Operator)-> int:
    if len(parts) == 0:
        if solution_to_be == current_solution:
            return solution_to_be
        return 0
    
    if current_solution > solution_to_be:
        return 0
    
    next_sol = current_solution * parts[0] if operator == Operator.MUL else current_solution + parts[0]
    sol_a = solution_bf(parts[1:], next_sol, solution_to_be, Operator.MUL)
    if sol_a == solution_to_be:
        return solution_to_be
    sol_b = solution_bf(parts[1:], next_sol, solution_to_be, Operator.PLUS)
    if sol_b == solution_to_be:
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


