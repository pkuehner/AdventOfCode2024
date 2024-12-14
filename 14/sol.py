from enum import Enum
import re
from typing import Tuple

import numpy as np

robots = {}


def move_robot(id):
    robot = robots[id]
    print(robot)
    robot["x"] += 100 * robot["v_x"]
    robot["x"] = robot["x"] % size_X

    robot["y"] += 100 * robot["v_y"]
    robot["y"] = robot["y"] % size_Y


with open("input") as file:
    text = file.readlines()
    size_X = 101
    size_Y = 103
    mid_x = int(size_X / 2)
    mid_y = int(size_Y / 2)
    i = 0
    results = {}

    for line in text:
        numbers = re.findall(r'-?\d+\.?\d*', line)
        result = list(map(int, numbers))
        x, y, v_x, v_y = result
        robots[i] = {"x": x, "y": y, "v_x": v_x, "v_y": v_y}
        i += 1

    for robot_key in robots.keys():
        move_robot(robot_key)
        x = robots[robot_key]["x"]
        y = robots[robot_key]["y"]

        HOR = "N"
        if x < mid_x:
            HOR = "L"
        elif x > mid_x:
            HOR = "R"

        VER = "N"
        if y < mid_y:
            VER = "T"
        elif y > mid_y:
            VER = "B"
        if HOR +VER not in results:
            results[HOR + VER] = 0
        results[HOR + VER] += 1
    print(results)
    print(results["LT"] * results["LB"] * results["RT"] * results["RB"])