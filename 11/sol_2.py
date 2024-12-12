from enum import Enum
from typing import Tuple


def search(x: int, y: int, arr, cluster, neighbours, visited, cluster_id, dir="NONE", dir2 = "NONE"):
    #print(x,y, cluster_id)
    if not(x >= 0 and x < len(arr) and y >= 0 and y < len(arr)):
        neighbours.append((x, y, dir, dir2))
        return
    
    letter = arr[x][y]
    if letter != cluster_id:
        neighbours.append((x,y, dir, dir2))
        return
    if visited[x][y]:
        return
    visited[x][y] = True

    cluster.append((x,y))
    search(x+1, y, arr, cluster, neighbours, visited, cluster_id, "HOR", "T")
    search(x, y+1, arr, cluster, neighbours, visited, cluster_id, "VER", "L")
    search(x-1, y, arr, cluster, neighbours, visited, cluster_id, "HOR", "B")
    search(x, y-1, arr, cluster, neighbours, visited, cluster_id, "VER", "R")

def search_line(x, y, dir1, dir2, neighbours, seen):
    if (x, y, dir1, dir2) in seen or (x,y,dir1,dir2) not in neighbours:
        return 0
    seen.add((x,y,dir1,dir2))
    if dir1 =="VER":
        search_line(x+1, y, dir1, dir2, neighbours, seen)
        search_line(x-1, y, dir1, dir2, neighbours, seen)
    else:
        search_line(x, y+1, dir1, dir2, neighbours, seen)
        search_line(x, y-1, dir1, dir2, neighbours, seen)
    return 1
    
            
def find_nb_length(neighbours):
    i = 0
    seen = set()
    count = 0
    while i < len(neighbours):
        a,b,c,d = neighbours[i]
        count += search_line(a,b,c,d, neighbours, seen)
        
        i+=1
    return count                           


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
                search(x, y, arr, cluster, neighbours, visited, arr[x][y])
                nb_length = find_nb_length(neighbours)
                print(len(cluster), nb_length, arr[x][y])
            result += len(cluster) * nb_length



    print(result)

 