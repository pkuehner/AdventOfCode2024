from functools import lru_cache
from queue import PriorityQueue
from itertools import product


num_pad = [ [7, 8, 9], [4, 5, 6], [1, 2, 3], [None, 0, "A"] ]
move_pad = [ [None, "^" , "A"], ["<", "v", ">"]]

class Robot:
    pad = None
    current = "A"

    def __init__(self, pad):
        self.pad = pad
    
    @lru_cache(maxsize=None)
    def next(self, current, end):
        current_pos = None
        end_pos = None
        
        # Find positions in pad
        for i in range(len(self.pad)):
            for j in range(len(self.pad[i])):
                if self.pad[i][j] == current:
                    current_pos = (i, j)
                if self.pad[i][j] == end:
                    end_pos = (i, j)

        if not current_pos or not end_pos:
            return None

        moves = {"^": (-1, 0),">":(0, 1), "v": (1, 0), "<": (0, -1)}
        queue = [(current_pos, [])]
        possible_paths = []
        max_dist = 100000000
        visited = set()
        while len(queue) > 0:
            current, path = queue.pop(0)
            if current == end_pos:
                if len(path) <= max_dist:
                    max_dist = len(path)
                    possible_paths.append(path)
                else:
                    return possible_paths
            if len(path) > 0:
                last_dir = path[-1]
            else:
                last_dir = "^"

            keys = list(moves.keys())
            keys.remove(last_dir)
            keys.insert(0, last_dir)

            #visited.add(current)
            for key in keys:
                move = moves[key]
                path_cp = path.copy()
                new_i = current[0] + move[0]
                new_j = current[1] + move[1]
                if (0 <= new_i < len(self.pad) and 
                    0 <= new_j < len(self.pad[0]) and 
                    self.pad[new_i][new_j] is not None and 
                    (new_i, new_j) not in visited):
                    path_cp.append(key)
                    queue.append(((new_i, new_j), path_cp))
        return possible_paths

def explode_moves(moves, new_moves):
    new_list = []
    for move in moves:
        for new_move in new_moves:
            move_cp = move.copy()
            move_cp.extend(new_move)
            new_list.append(move_cp)
    return new_list

with open("input") as file:
    result = 0
    num_robot = Robot(num_pad)
    move_robot_1 = Robot(move_pad)
    move_robot_2 = Robot(move_pad)
    
    for line in file.readlines():
        codes = [line[:-1]]
        numerics = line[:-2]


        for door_code in codes:
            possible_codes = [door_code]
            for robot in [num_robot, move_robot_1, move_robot_2]:
                new_possible_codes = []
                for code in possible_codes:
                    code = "".join(code)
                    full_moves = [[]]
                    for x in code:
                        x = int(x) if x.isdigit() else x
                        #if robot.current == x:
                        #    continue
                        moves = robot.next(robot.current, x)
                        for move in moves:
                            move.append("A")
                        robot.current = x
                        full_moves = explode_moves(full_moves, moves)
                    new_possible_codes.extend(full_moves)
                possible_codes = new_possible_codes
            possible_codes = [len(code) for code in possible_codes]
            print(code)
            result += int(numerics) * min(possible_codes)
        print(result)
    