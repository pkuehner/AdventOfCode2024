from enum import Enum
from typing import Tuple
import heapq

robot_x = -1
robot_y = -1

class FieldValues(int, Enum):
    Free = 0
    Wall = 1
    

class Directions(int, Enum):
    T = 0
    R = 1
    B = 2
    L = 3

def turn(direction: Directions) -> Directions:
    if direction == Directions.T:
        return Directions.R
    if direction == Directions.R:
        return Directions.B
    if direction == Directions.B:
        return Directions.L
    if direction == Directions.L:
        return Directions.T


def step(x: int, y: int, direction: Directions) -> Tuple[int, int]:
    if direction == Directions.T:
        return (x - 1, y)
    if direction == Directions.R:
        return (x, y + 1)
    if direction == Directions.B:
        return (x + 1, y)
    if direction == Directions.L:
        return (x, y - 1)


def djikstra(arr, distances, queue, visited, end_x, end_y):
    end_dist = 1000000000
    cheats_found = []
    max_dist = 0
    while True:
        data = heapq.heappop(queue)
        dist, (x,y,cheat_step, path) = data
        if dist != max_dist:
            max_dist = dist
            print(max_dist)
        if (x,y) == (end_x, end_y):
            if cheat_step == 0:
                end_dist = dist
                for cheat_dist in cheats_found:
                    dist_map ={}
                    if cheat_dist < dist:
                        if dist-cheat_dist not in dist_map:
                            dist_map[dist-cheat_dist] = 0
                        dist_map[dist-cheat_dist] += 1
                        return dist_map
            else:
                cheats_found.append(dist)

        visited[x][y] = True
        
        for dir_new in Directions:
            path_new = path.copy()
            cost = 1
            x_new, y_new = step(x, y, dir_new)
            cheat_step_new = cheat_step
            can_pass_wall = True
            
            if cheat_step == 2:
                can_pass_wall = False
            if x_new >= 0 and x_new < len(arr) and y_new >= 0 and y_new < len(arr[x_new]):
                if arr[x_new][y_new] == FieldValues.Free or can_pass_wall:
                    if arr[x_new][y_new] == FieldValues.Wall or cheat_step == 1:
                        cheat_step_new += 1
                    heapq.heappush(queue, (dist+cost, (x_new, y_new, cheat_step_new, path_new)))
            

    
            
    

            
                            


with open("debug") as file:
    text = file.readlines()
    arr = []
    commands = []
    first_part = True

    for line in text:
        lineArr = []
        for value in list(line):
            field_value = FieldValues.Free
            if value == "#":
                field_value = FieldValues.Wall
            elif value == "S":
                field_value = "S"
            elif value == "E":
                field_value = "E"
            elif value == ".":
                field_value = FieldValues.Free
            if value != "\n":
                lineArr.append(field_value)
        arr.append(lineArr)
        

    
    result = 0
    distances = [line.copy() for line in arr.copy()]
    visited = [line.copy() for line in arr.copy()]

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            distances[x][y] = [10000000 for cheat_step in range(3)]   
            visited[x][y] = False
            if arr[x][y] == "S":
                arr[x][y] = FieldValues.Free
                start_x = x
                start_y = y
            if arr[x][y] == "E":
                arr[x][y] = FieldValues.Free
                end_x = x
                end_y = y

    queue = []
    distances[start_x][start_y][0] = 0

    heapq.heappush(queue, (distances[start_x][start_y][0], (start_x, start_y, 0, [])))
    dist = djikstra(arr, distances, queue, visited, end_x, end_y)
    seen = set()
    print(dist)
    
    print(len(seen))

