from enum import Enum
import re
from typing import Tuple

import numpy as np

robots = {}


def move_robot(id):
    robot = robots[id]
    robot["x"] +=  robot["v_x"]
    robot["x"] = robot["x"] % size_X

    robot["y"] += robot["v_y"]
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
    for j in range(10000):
        arr = np.zeros((size_X, size_Y))
        double = False
        for robot_key in robots.keys():
            move_robot(robot_key)
            x = robots[robot_key]["x"]
            y = robots[robot_key]["y"]
            if arr[x, y] == 1:
                double = True

            arr[x, y] = 1
        if not double:
            print(j+1)
    
        # with open(f"./files/{j}", 'w') as file:
        #     lines = []
        #     for y in range(size_Y):
        #         line = ""
        #         for x in range(size_X):
        #             if arr[x, y] == 1:
        #                 line+="8"
        #             else:
        #                 line+=" "
        #         line+="\n"
        #         lines.append(line)
        #     #print(lines)
        #     file.writelines(lines)
           