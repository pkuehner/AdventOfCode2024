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
        if len(queue) == 0:
            print("None")
            return None
        dist, (x, y, path) = heapq.heappop(queue)
        #print(x, y, dist, path)
        if not visited[x][y]:
            path += [(x, y)]
        if (x, y) == (end_x, end_y):
            return distances[end_x][end_y]
        visited[x][y] = True

        for dir_new in Directions:
            cost = 1
            x_new, y_new = step(x, y, dir_new)
            if (
                x_new >= 0
                and x_new < len(arr)
                and y_new >= 0
                and y_new < len(arr[x_new])
            ):

                if arr[x_new][y_new] == FieldValues.Free:
                    if not visited[x_new][y_new]:
                        if distances[x_new][y_new] > dist + cost:
                            distances[x_new][y_new]
                            distances[x_new][y_new] = dist + cost
                            heapq.heappush(
                                queue,
                                (
                                    distances[x_new][y_new],
                                    (x_new, y_new, path.copy()),
                                ),
                            )


with open("input") as file:
    size = 71
    text = file.readlines()
    arr = [[FieldValues.Free for _ in range(size)] for _ in range(size)]
    coords = [
        (int(line.split(",")[0]), int(line.split(",")[1]))
        for line in text
    ]
    for x, y in coords[:1024]:
        arr[y][x] = FieldValues.Wall

    for x, y in coords[1024:]:

        print(x,y,"Done")
        arr[y][x] = FieldValues.Wall
        result = 0
        distances = [line.copy() for line in arr.copy()]
        visited = [line.copy() for line in arr.copy()]

        for x in range(len(arr)):
            for y in range(len(arr[x])):
                distances[x][y] = 1000000000
                visited[x][y] = False
        start_x, start_y = 0, 0
        end_x, end_y = size - 1, size - 1

        queue = []
        distances[start_x][start_y] = 0
        heapq.heappush(queue, (distances[start_x][start_y], (start_x, start_y, [])))
        if djikstra(arr, distances, queue, visited, end_x, end_y) is None:
            print(x,y)
            exit()
