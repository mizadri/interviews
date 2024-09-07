from collections import deque

def bfs_iterative(graph, start):
    # Use a queue for BFS
    queue = deque([start])
    visited = set()
    
    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        
        # If the node is not visited, process it
        if node not in visited:
            print(node, end=" ")  # Print the node (optional)
            visited.add(node)
            
            # Enqueue all the unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Iterative BFS:")
bfs_iterative(graph, 'A')
