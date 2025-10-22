graph = {
    'A': {'B': 6, 'C': 3},
    'B': {'D': 2, 'E': 5},
    'C': {'B': 1, 'D': 7},
    'D': {'G': 1},
    'E': {'G': 2},
    'G': {}
}

heuristic = {
    'A': 1, 'B': 2, 'C': 100, 'D': 3, 'E': 4, 'G': 0
}

def greedy_search(start, goal):
    visited = set()
    # Manual priority queue as a list of tuples (heuristic, node, path)
    queue = [(heuristic[start], start, [start])]

    while queue:
        # Find the tuple with lowest heuristic value manually
        min_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_index][0]:
                min_index = i
        
        # Greedy client gets the item from queue
        h, current, path = queue[min_index]
        # Greedy client removes the item from queue after getting it
        queue.pop(min_index)

        if current == goal:
            print("Path found:", path)
            return
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((heuristic[neighbor], neighbor, path + [neighbor]))
    print("No path found")

greedy_search('A', 'C')