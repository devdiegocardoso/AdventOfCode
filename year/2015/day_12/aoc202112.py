import pathlib
import sys
from typing import List
from copy import copy
class Graph():
    def __init__(self):
        super().__init__()
        self.small_caves= set()
        self.adj = {}
        self.n_paths = 0

    def add_link(self,v1,v2,directed=False):
        if (ord(v1[0]) > 96 and ord(v1[0]) < 123):
            self.small_caves.add(v1)
        if (ord(v2[0]) > 96 and ord(v2[0]) < 123):
            self.small_caves.add(v2)
        if v1 in self.adj.keys():
            self.adj[v1].append(v2)
        else:
            self.adj[v1] = [v2]
        if not directed:
            if v2 in self.adj.keys():
                self.adj[v2].append(v1)
            else:
                self.adj[v2] = [v1]

    
    def find_paths(self,start,end,can_repeat=False):
        visited = []
        path = []
        found_paths = set()
        if 'start' in self.small_caves:
            self.small_caves.remove('start')
        if 'end' in self.small_caves:
            self.small_caves.remove('end')
        if can_repeat:
            for small_cave in sorted(list(self.small_caves)):
                self.dfs_path(start,end,visited,path,found_paths,small_cave)
        else:
            self.dfs_path(start,end,visited,path,found_paths)
   
    def dfs(self,current,visited):
        print(current)
        for node in self.adj[current]:
            if node not in visited:
                visited.append(node)
                self.dfs(node,visited)

    def dfs_path(self,current,destination,visited,path,found,repeat_cave=None):
        if (ord(current[0]) > 96 and ord(current[0]) < 123):
            if current == repeat_cave:
                repeat_cave = None
            else:
                visited.append(current)
        path.append(current)
        if current == destination:
            found.add(tuple(path[:]))
            self.n_paths = len(found)
        else:
            for node in self.adj[current]:
                if node not in visited:
                    self.dfs_path(node,destination,visited,path,found,repeat_cave)
        last_node = path.pop()
        if last_node in visited:
            visited.remove(last_node)

def parse_list(puzzle_input):
    list_tmp = [line for line in puzzle_input.split('\n')]
    list_tmp = [(item.split('-')) for item in list_tmp]
    return list_tmp

def part_one(graph):
    graph.find_paths('start','end')
    return graph.n_paths

def part_two(graph):
    graph.find_paths('start','end',True)
    return graph.n_paths
    #return len(paths)

def solve(puzzle_input):
    numbers = parse_list(puzzle_input)
    graph = Graph()
    for item in numbers:
        graph.add_link(item[0],item[1])
    solution_1 = part_one(graph)
    solution_2 = part_two(graph)

    return solution_1,solution_2

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}')
        local_input = pathlib.Path(path).read_text(encoding='utf-8').strip()

        solutions = solve(local_input)
        print('\n'.join(map(str,solutions)))
        