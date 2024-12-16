from enum import Enum
from typing import Tuple
import heapq

robot_x = -1
robot_y = -1

class FieldValues(int, Enum):
    Free = 0
    Wall = 1
    Box = 2
    

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
    paths_found = []
    while True:
        data = heapq.heappop(queue)
        dist, (x,y,direction, path) = data
        path.append((x,y))
        if dist > end_dist:
            return paths_found
        if (x,y) == (end_x, end_y):
            end_dist = dist
            paths_found.append(path)
            print(path)
        visited[x][y] = True
        
        for num_turns in [0, 1, 3]:
            path_new = path.copy()
            dir_new = direction
            cost = 1
            for i in range(num_turns):
                dir_new = turn(dir_new)
            cost += 1000 * (num_turns % 2)
            x_new, y_new = step(x, y, dir_new)
            #print(dir_new, cost)
            if arr[x_new][y_new] == FieldValues.Free:            
                if distances[x_new][y_new][dir_new] >= dist + cost:
                    distances[x_new][y_new][dir_new]
                    distances[x_new][y_new][dir_new] = dist + cost
                    heapq.heappush(queue, (distances[x_new][y_new][dir_new], (x_new, y_new, dir_new, path_new)))
        

    
            
    

            
                            


with open("input") as file:
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
            distances[x][y] = [10000000 for direction in Directions]   
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
    distances[start_x][start_y][Directions.R] = 0
    heapq.heappush(queue, (distances[start_x][start_y][Directions.R], (start_x, start_y, Directions.R, [])))
    paths = djikstra(arr, distances, queue, visited, end_x, end_y)
    seen = set()
    for i, path in enumerate(paths):
        print(i, path)
        for x, y in path:
            seen.add((x,y))
    
    print(len(seen))

