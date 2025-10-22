def greedy_best_first_search(graph, start, goal, heuristic):
    """
    Performs Greedy Best-First Search on the given graph.

    Args:
        graph (dict): The adjacency list of the graph.
        start (str): The starting node.
        goal (str): The goal node.
        heuristic (function): Function mapping a node to its heuristic value h(n).

    Returns:
        list: The path from start to goal, or empty list if no path exists.
    """
    visited = set()
    # Manual priority queue (min-heap) implementation
    heap = []
    # Insert initial node
    heap.append((heuristic(start), [start]))

    def heap_push(heap, item):
        # Simple insert and sort based on the heuristic value, emulating a heap
        heap.append(item)
        heap.sort(key=lambda x: x[0])

    def heap_pop(heap):
        # Pop the smallest element (lowest heuristic) from sorted list
        return heap.pop(0)

    while heap:
        h, path = heap_pop(heap)
        node = path[-1]

        # Debug print: Greedy expansion order
        print(f"Path so far: {path}, expanding node: {node} (h={heuristic(node)})")

        if node == goal:
            print("Found goal (greedy)!")
            return path

        if node in visited:
            continue

        visited.add(node)

        # Only add neighbors with greedy intent: by heuristic
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                print(f"  Greedily adding neighbor: {neighbor}, h({neighbor}) = {heuristic(neighbor)}")
                heap_push(heap, (heuristic(neighbor), path + [neighbor]))

    print("No path found (greedy).")
    return []

# Example usage:
if __name__ == "__main__":
    # Example graph: adjacency list (node: [(neighbor, cost), ...])
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('D', 4), ('E', 2)],
        'C': [('F', 5)],
        'D': [],
        'E': [('F', 1)],
        'F': []
    }

    # Example heuristic function: h(n)
    h_values = {
        'A': 5,
        'B': 3,
        'C': 2,
        'D': 6,
        'E': 1,
        'F': 0  # Goal node has h=0
    }
    heuristic = lambda n: h_values.get(n, float('inf'))

    path = greedy_best_first_search(graph, 'A', 'F', heuristic)
    print("Greedy Best-First Search Path:", path)
