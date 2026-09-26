# DFS without using any library

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

visited = []

def DFS(vertex):
    visited.append(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            DFS(neighbor)


print("DFS Traversal:")
DFS(0)
