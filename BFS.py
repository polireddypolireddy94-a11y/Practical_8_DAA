graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

def BFS(start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


print("BFS Traversal:")
BFS(0)
