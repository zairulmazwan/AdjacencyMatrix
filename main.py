def find_routes(adj_matrix, start, end, path=[]):
    path = path + [start]  # Add the current node to the path

    # If we reach the end node, return the path
    if start == end:
        return [path]

    # If the start node has no outgoing edges, return an empty list
    if not any(adj_matrix[start]):
        return []

    routes = []

    # Explore all possible paths
    for i in range(len(adj_matrix)):
        # If there's an edge from start to i and i is not already in the path
        if adj_matrix[start][i] != 0 and i not in path:
            new_routes = find_routes(adj_matrix, i, end, path)
            for new_route in new_routes:
                routes.append(new_route)

    return routes


# Example usage:
if __name__ == "__main__":
    # Define an adjacency matrix
    adj_matrix = [
        [0,0,20,0,0,0,0,25],
        [0,0,0,80,0,0,90,0],
        [0,0,0,100,0,0,0,75],
        [0,0,0,0,0,0,0,0],
        [0,50,0,0,0,0,0,0],
        [75,125,100,0,90,0,0,0],
        [0,0,0,45,0,0,0,0],
        [0,0,0,45,0,0,0,0]
    ]

    start_node = 5
    end_node = 3

    all_routes = find_routes(adj_matrix, start_node, end_node)

    print("All routes from node", start_node, "to node", end_node, ":")
    for route in all_routes:
        print(" -> ".join(map(str, route)))
