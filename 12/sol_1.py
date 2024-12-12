from enum import Enum
from typing import Tuple


def search(x: int, y: int, arr, cluster, neighbours, visited, cluster_id):
    #print(x,y, cluster_id)
    if not(x >= 0 and x < len(arr) and y >= 0 and y < len(arr)):
        neighbours.append((x, y))
        return
    
    letter = arr[x][y]
    if letter != cluster_id:
        neighbours.append((x,y))
        return
    if visited[x][y]:
        return
    visited[x][y] = True

    cluster.append((x,y))
    search(x+1, y, arr, cluster, neighbours, visited, cluster_id)
    search(x, y+1, arr, cluster, neighbours, visited, cluster_id)
    search(x-1, y, arr, cluster, neighbours, visited, cluster_id)
    search(x, y-1, arr, cluster, neighbours, visited, cluster_id)

            
                            


with open("input") as file:
    text = file.readlines()
    arr = [list(line) for line in text]
    arr = [line[:-1] if line[-1] =="\n" else line for line in arr ]
    visited = [line.copy() for line in arr.copy()]
    result = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            visited[x][y] = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            cluster = []
            neighbours = []
            if not visited[x][y]:
                #print(neighbours)
                search(x, y, arr, cluster, neighbours, visited, arr[x][y])
                print(len(cluster), len(neighbours), arr[x][y])
            result += len(cluster) * len(neighbours)



    print(result)

