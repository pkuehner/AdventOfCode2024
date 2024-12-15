from enum import Enum
from typing import Tuple

robot_x = -1
robot_y = -1

class FieldValues(int, Enum):
    Free = 0
    Wall = 1
    Box = 2

class Directions(int, Enum):
    T = 0
    R = 1
    B = 3
    L = 4

def step(x: int, y: int, direction: Directions) -> Tuple[int, int]:
    if direction == Directions.T:
        return (x - 1, y)
    if direction == Directions.R:
        return (x, y + 1)
    if direction == Directions.B:
        return (x + 1, y)
    if direction == Directions.L:
        return (x, y - 1)


def move(arr, command: Directions):
    global robot_x, robot_y
    print(robot_x, robot_y, command)
    x_new, y_new = step(robot_x, robot_y, command)
    if x_new >= 0 and x_new < len(arr) and y_new >= 0 and y < len(arr[x_new]):
        if arr[x_new][y_new] == FieldValues.Wall: 
            return
        if arr[x_new][y_new] == FieldValues.Free: 
            robot_x = x_new
            robot_y = y_new
            return
        if arr[x_new][y_new] == FieldValues.Box:
            field_to_close = None
            field_to_open = (x_new, y_new)
            while True:
                print(x_new, y_new)
                x_new, y_new = step(x_new, y_new, command)
                if not(x_new >= 0 and x_new < len(arr) and y_new >= 0 and y < len(arr[x_new])):
                    break
                if arr[x_new][y_new] == FieldValues.Wall:
                    break
                if arr[x_new][y_new] == FieldValues.Free:
                    field_to_close = (x_new, y_new)
                    break
            if field_to_close is not None:
                to_close_x, to_close_y = field_to_close
                robot_x, robot_y = field_to_open
                arr[robot_x][robot_y] = FieldValues.Free
                arr[to_close_x][to_close_y] = FieldValues.Box
    
            
    

            
                            


with open("input") as file:
    text = file.readlines()
    arr = []
    commands = []
    first_part = True

    for line in text:
        lineArr = []
        if line == "\n":
            first_part = False
        if first_part:
            for value in list(line):
                field_value = FieldValues.Free
                if value == "#":
                    field_value = FieldValues.Wall
                elif value == "O":
                    field_value = FieldValues.Box
                elif value == "@":
                    field_value = "@"
                if value != "\n":
                    lineArr.append(field_value)
            arr.append(lineArr)
        else:
            for value in list(line):
                command = Directions.T
                if value == "<":
                    command = Directions.L
                elif value == ">":
                    command = Directions.R
                elif value == "v":
                    command = Directions.B
                if value != "\n":
                    commands.append(command)    

    
    result = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == "@":
                arr[x][y] = FieldValues.Free
                robot_x = x
                robot_y = y



    for command in commands:
        move(arr, command)

    result = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == FieldValues.Box:
                result += 100*x+y
    print(result)
