import heapq

def dijkstra(grid, start, goal, k=3):
    rows, cols = len(grid), len(grid[0])
    all_paths = []

    def find_path(grid, start, goal, blocked_edges):
        queue = [(0, start)]
        distances = {start: 0}
        came_from = {start: None}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == goal:
                path = []
                node = goal
                while node is not None:
                    path.append(node)
                    node = came_from[node]
                path.reverse()
                return path

            x, y = current_node
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

            for neighbor in neighbors:
                nx, ny = neighbor
                if 0 <= nx < rows and 0 <= ny < cols and (current_node, neighbor) not in blocked_edges:
                    new_distance = current_distance + 1
                    if neighbor not in distances or new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        priority = new_distance
                        heapq.heappush(queue, (priority, neighbor))
                        came_from[neighbor] = current_node
        return None

    blocked_edges = set()
    for _ in range(k):
        path = find_path(grid, start, goal, blocked_edges)
        if path:
            all_paths.append(path)
            if len(path) > 1:
                # Block an edge in the found path to force a different route
                blocked_edge = (path[0], path[1])
                blocked_edges.add(blocked_edge)
        else:
            break

    return all_paths
