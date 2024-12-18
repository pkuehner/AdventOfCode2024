from enum import Enum
from typing import Tuple

robot_x = -1
robot_y = -1

class FieldValues(str, Enum):
    Free = "."
    Wall = "#"
    BoxL = "["
    BoxR = "]"

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

def findOtherBoxPart(x: int, y: int, value: FieldValues) -> Tuple[int, int]:
    if value == FieldValues.BoxL:
        return (x, y+1)
    elif value == FieldValues.BoxR:
        return (x, y-1)

def move(arr, command: Directions):
    global robot_x, robot_y
    x_new, y_new = step(robot_x, robot_y, command)
    if x_new >= 0 and x_new < len(arr) and y_new >= 0 and y < len(arr[x_new]):
        if arr[x_new][y_new] == FieldValues.Wall: 
            return
        if arr[x_new][y_new] == FieldValues.Free: 
            robot_x = x_new
            robot_y = y_new
            return
        if arr[x_new][y_new] in [FieldValues.BoxL, FieldValues.BoxR]:
            box_parts_to_push = []
            box_parts_to_push.append((x_new, y_new))
            box_parts_to_push.append(findOtherBoxPart(x_new, y_new, arr[x_new][y_new]))
            seen = []
            movable = True
            while len(box_parts_to_push) > 0:
                x_box, y_box = box_parts_to_push.pop(0)
                if (x_box, y_box) in seen:
                    continue
                seen.append((x_box, y_box))

                x_box, y_box = step(x_box, y_box, command)
                if not(x_box >= 0 and x_box < len(arr) and y_box >= 0 and y_box < len(arr[x_box])):
                    movable = False
                    break
                if arr[x_box][y_box] == FieldValues.Wall:
                    movable = False
                    break
                if arr[x_box][y_box] in [FieldValues.BoxL, FieldValues.BoxR]:
                    if (x_box, y_box) not in seen:
                        box_parts_to_push.append((x_box, y_box))
                    x_new_2, y_new_2 = findOtherBoxPart(x_box, y_box, arr[x_box][y_box])
                    if (x_new_2, y_new_2) not in seen:
                        box_parts_to_push.append((x_new_2, y_new_2))
            if movable:
                seen.reverse()
                for x_box, y_box in seen:
                    x_box_new, y_box_new = step(x_box, y_box, command)
                    arr[x_box_new][y_box_new] = arr[x_box][y_box]
                    arr[x_box][y_box] = FieldValues.Free
                robot_x = x_new
                robot_y = y_new


                    

            
    
            
    

            
                            


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
                field_values = [FieldValues.Free]*2
                if value == "#":
                    field_values = [FieldValues.Wall]*2
                elif value == "O":
                    field_values = [FieldValues.BoxL, FieldValues.BoxR]
                elif value == "@":
                    field_values = ["@", FieldValues.Free]
                if value != "\n":
                    lineArr.extend(field_values)
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

    with open(f"./files/start", 'w') as file:
        lines = []
        for x in range(len(arr)):
            line = ""
            for y in range(len(arr[x])):
                line+= arr[x][y]
            line+="\n"
            lines.append(line)
        #print(lines)
        file.writelines(lines)

    for command in commands:
        move(arr, command)

    result = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == FieldValues.BoxL:
                result += 100*x+y
    
    with open(f"./files/end", 'w') as file:
            lines = []
            for x in range(len(arr)):
                line = ""
                for y in range(len(arr[x])):
                    line+= arr[x][y]
                line+="\n"
                lines.append(line)
            #print(lines)
            file.writelines(lines)

    print(result)