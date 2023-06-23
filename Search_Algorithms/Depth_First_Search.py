'''
@Author: Shubham shirke
@Date: 2023-06-22 22:30:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-22 22:30:30
@Title : Implement the breadth-first search (BFS) algorithm to find the shortest path between two nodes in a graph represented as an adjacency matrix.
'''

from collections import deque

class BFS:

    def depth_first_search(self,graph,start,end,visited=None):
        """
        Description : 
                This function performs depth first search.
        Parameters :
                graph : Input graph
                start : start node
                end : end node
                visited : set containing visited nodes
        Returns    :
                visited : visited set
        """
        if visited is None:
            visited = set()

        visited.add(start)

        if start == end:
            return [start]

        for neighbor in graph[start]:
            if neighbor not in visited:
                if self.depth_first_search(graph, neighbor, end, visited):
                    return visited

        return []


def main():
    bfs = BFS()
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }

    start = 'A'
    end = 'F'

    result = bfs.depth_first_search(graph, start, end)

    if result:
        print(f"There is a path between {start} and {end} is {result}")
    else:
        print(f"There is no path between {start} and {end}.")


if __name__ == "__main__":
    main()