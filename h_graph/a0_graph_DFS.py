"""
graph = (vertex,edge), vertex -> node, edge -> link
edge with weight
"""

# recursive method adjacent matrix


from collections import deque


def dfs_recursive_matrix(matrix, start, visited=None):
    n = len(matrix)
    if visited is None:
        visited = [False] * n
    visited[start] = True
    print(start)

    for i in range(n):
        if matrix[start][i] and not visited[i]:
            dfs_recursive_matrix(matrix, i, visited)
    return visited


# stack method adjacent matrix


def dfs_iterative_matrix(matrix, start, visited=None):
    n = len(matrix)
    visited = [False] * n
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node)
        for i in range(n-1, -1, -1):
            if not visited[i] and matrix[node][i]:
                stack.append(i)

# stack method adjacent linked list


def dfs_iterative_graph(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
        # reversed() vs .reverse(): do not modify the original vs affect original list
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)


# recursive method adjacent linked list

def dfs_recursive_graph(graph, start, visited):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for neighbor in reversed(graph.get(start, [])):
        if neighbor not in visited:
            dfs_recursive_graph(graph, neighbor, visited)


# Queue method adjacent linked list


def bfs_iterative_graph(graph, start):
    deq = deque([start])
    visited = set()
    while deq:
        node = deq.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                deq.append(neighbor)
    return visited

# Queue method adjacent linked list


def bfs_iterative_matrix(matrix, start, visited=None):
    n = len(matrix)
    visited = [False] * n
    deq = deque([start])
    while deq:
        node = deq.popleft()
        if node not in visited:
            visited[node] = True
            print(node)
        for i in range(n):
            if matrix[node][i] and not visited[i]:
                deq.append(i)
    return visited


if __name__ == "__main__":

    matrix = [
        [0, 1, 1, 0],  # Node 0
        [1, 0, 0, 1],  # Node 1
        [1, 0, 0, 1],  # Node 2
        [0, 1, 1, 0]   # Node 3
    ]

    graph = {
        'a': ['b', 'c'],
        'b': ['a', 'c', 'h'],
        'c': ['a', 'b', 'd'],
        'd': ['c', 'f'],
        'e': ['b', 'g'],
        'f': ['d'],
        'g': ['e'],
        'h': ['b']
    }

    print("Recursive DFS using an adjacency matrix:")
    dfs_recursive_matrix(matrix, 0)

    print("\niterative(stack) DFS using an adjacency matrix:")
    dfs_iterative_matrix(matrix, 0)

    print("\nIterative DFS traversal on graph starting from 'a':")
    dfs_iterative_graph(graph, 'a')

    print("\nIterative bFS traversal on graph starting from 'a':")
    bfs_iterative_graph(graph, 'a')

    print("\niterative(Queue) BFS using an adjacency matrix:")
    bfs_iterative_matrix(matrix, 0)
