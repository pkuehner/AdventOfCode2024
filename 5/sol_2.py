from enum import Enum
from typing import Dict, List, Tuple

def check_line(nums: list[int], after_orders: Dict[int, List[int]]) -> int:
    change = False
    print("BEFORE")
    print(nums)
    print("AFTER")
    i = 0
    while i < len(nums):
        num_i = nums[i]
        last_index = i
        for j in range(i+1, len(nums)):
            num_j = nums[j]
            if num_j in after_orders:
                after = after_orders[num_j]
            else:
                after = {}
            if num_i in after:
                last_index = j
                change = True
        nums[i] = nums[last_index]
        nums[last_index] = num_i
        if i == last_index:
            i+=1
    if not change:
        return 0
    print(nums)
    return nums[int(len(nums)/2)]

with open("input") as file:
    text = file.readlines()
    MODE = "INPUT"
    orders = {}
    value = 0
    for line in text:
        if line == "\n":
            MODE = "EVAL"

        elif MODE == "INPUT":
            x, y = int(line.split("|")[0]), int(line.split("|")[1])
            if x not in orders:
                orders[x] = set()
            orders[x].add(y)
        else:
            nums = [int(x) for x in line.split(",")]
            value += check_line(nums, orders)
    print(value)
                         
        
