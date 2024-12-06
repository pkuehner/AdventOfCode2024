from enum import Enum
from typing import Dict, List, Tuple

def check_line(nums: list[int], before_orders: Dict[int, List[int]]) -> int:
    seen_nums = set()
    for num in nums:
        for seen_num in seen_nums:
            if seen_num in before_orders:
                before = before_orders[seen_num]
            else:
                before = {}
            if num in before:
                print(nums, num)
                return 0
        seen_nums.add(num)
    return nums[int(len(nums)/2)]

with open("input") as file:
    text = file.readlines()
    MODE = "INPUT"
    orders = {}
    value = 0
    for line in text:
        if line == "\n":
            MODE = "EVAL"
            print(orders)

        elif MODE == "INPUT":
            x, y = int(line.split("|")[0]), int(line.split("|")[1])
            if y not in orders:
                orders[y] = set()
            orders[y].add(x)
        else:
            nums = [int(x) for x in line.split(",")]
            value += check_line(nums, orders)
    print(value)
                         
        
