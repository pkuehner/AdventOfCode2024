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
    B = 3
    L = 4

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
    while True:
        dist, (x,y,direction, path) = heapq.heappop(queue)
        if (x,y) == (end_x, end_y):
            return distances[end_x][end_y]
        visited[x][y] = True

        for num_turns in [0, 1, 3]:
            dir_new = direction
            cost = 1
            for i in range(num_turns):
                dir_new = turn(dir_new)
            cost += 1000 * (num_turns % 2)
            x_new, y_new = step(x, y, dir_new)
            print(dir_new, cost)
            if arr[x_new][y_new] == FieldValues.Free:
                if not visited[x_new][y_new]:
                    if distances[x_new][y_new] >= distances[x][y] + cost:
                        distances[x_new][y_new]
                        distances[x_new][y_new] = distances[x][y] + cost
                        heapq.heappush(queue, (distances[x_new][y_new], (x_new, y_new, dir_new)))
            

    
            
    

            
                            


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
            distances[x][y] = 1000000000    
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
    distances[start_x][start_y] = 0
    heapq.heappush(queue, (distances[start_x][start_y], (start_x, start_y, Directions.R, [])))
    print(djikstra(arr, distances, queue, visited, end_x, end_y))

