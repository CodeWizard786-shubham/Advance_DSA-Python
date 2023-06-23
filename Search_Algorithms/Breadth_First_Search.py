'''
@Author: Shubham shirke
@Date: 2023-06-22 22:30:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-22 22:30:30
@Title : Implement the breadth-first search (BFS) algorithm to find the shortest path between two nodes in a graph represented as an adjacency matrix.
'''

from collections import deque

class BFS:

    def breadth_first_search(self,graph,start,end):
        """
        Description : 
                This function performs breadth first search.
        Parameters :
                graph : Input graph
                start : start node
                end : end node
        Returns    :
                visited : visited set
        """
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex == end:
                return visited
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)

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

    result = bfs.breadth_first_search(graph, start, end)

    if result:
        print(f"There is a path between {start} and {end} is {result}")
    else:
        print(f"There is no path between {start} and {end}.")


if __name__ == "__main__":
    main()