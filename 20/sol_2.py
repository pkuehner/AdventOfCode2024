from enum import Enum
from functools import lru_cache
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
    while True:
        data = heapq.heappop(queue)
        dist, (x,y, path) = data
        path.append((x,y))
        if (x,y) == (end_x, end_y):
            return distances, path

        visited[x][y] = True
        
        for dir_new in Directions:
            path_new = path.copy()
            cost = 1
            x_new, y_new = step(x, y, dir_new)

            if x_new >= 0 and x_new < len(arr) and y_new >= 0 and y_new < len(arr[x_new]):
                if arr[x_new][y_new] == FieldValues.Free:
                    if distances[x_new][y_new] >= dist + cost:
                        distances[x_new][y_new]
                        distances[x_new][y_new] = dist + cost
                        heapq.heappush(queue, (distances[x_new][y_new], (x_new, y_new, path_new)))
            

    
global count           

def cheat(x, y, start_dist, arr, distances,seen,num_cheats_max, num_cheats_current, cache, path, cheats_found, start_x, start_y):
    #print(x,y, path, start_x, start_y)
    if not (x >= 0 and x < len(arr) and y >= 0 and y < len(arr[x])):
        return
    
    if (x,y) != (start_x, start_y) and distances[x][y] != 1000000:
        #print(x,y, start_x, start_y, start_dist, distances[x][y])
        if distances[x][y] + len(path) < start_dist:
            if start_dist-(distances[x][y] + len(path))>= 100:
                cheats_found.add((x,y, start_x,start_y))
                

    if (x,y, num_cheats_current) in seen or (x, y) in path:
        return
    
    path.add((x,y))
    seen.add((x, y, num_cheats_current))

    if (x, y, num_cheats_current) in cache:
        return 0
    if num_cheats_current == 0:
        return 0
    for direction in Directions:
        x_1, y_1 = step(x, y, direction)
        path_new = path.copy()
        cheat(x_1, y_1, start_dist, arr,  distances, seen, num_cheats_max, num_cheats_current-1, cache, path_new, cheats_found, start_x, start_y)
    return count
                            


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
            distances[x][y] = 1000000  
            visited[x][y] = False
            if arr[x][y] == "S":
                arr[x][y] = FieldValues.Free
                start_x = x
                start_y = y
            if arr[x][y] == "E":
                arr[x][y] = FieldValues.Free
                end_x = x
                end_y = y
    distances[start_x][start_y] = 0
    queue = []

    heapq.heappush(queue, (distances[start_x][start_y], (start_x, start_y, [])))
    dists, path = djikstra(arr, distances, queue, visited, end_x, end_y)
    count = 0
    cheats_found = set()
    for x,y in path:
        #print(x,y)
        seen = set()
        cache = {}
        cheat(x, y, distances[x][y], arr, dists, seen, 20, 20, {}, set(), cheats_found, x, y)
        #print(cheats_found)
    print(len(cheats_found))
