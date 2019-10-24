# https://medium.com/@yasufumy/algorithm-breadth-first-search-408297a075c9


from collections import deque


def bfs(graph, vertex):
    queue = deque([vertex])
    visited = {vertex: True}
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if n not in visited:
                queue.append(n)
                visited[n] = True
    return visited


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['B', 'D']
    }
    result = bfs(graph, 'A')

    for x in result:
        print(x)

