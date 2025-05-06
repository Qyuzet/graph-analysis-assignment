import random
from graph import Graph

def generate_large_graph(num_vertices, edge_density=0.3):
    """
    Generate a large random graph

    Parameters:
    - num_vertices: Number of vertices in the graph
    - edge_density: Probability of an edge between any two vertices (0.0 to 1.0)

    Returns:
    - A Graph object
    """
    graph = Graph()

    # Add vertices
    for i in range(num_vertices):
        graph.add_vertex(i)

    # Add random edges
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < edge_density:
                weight = random.randint(1, 100)
                graph.add_edge(i, j, weight)

    return graph

def save_graph_to_file(graph, file_path):
    """
    Save a graph to a file in the format:
    num_vertices num_edges
    e source_vertex destination_vertex weight
    """
    vertices = graph.get_vertices()
    edges = graph.get_edges()

    with open(file_path, 'w') as f:
        f.write(f"{len(vertices)} {len(edges)}\n")

        for u, v, weight in edges:
            f.write(f"e {u} {v} {weight}\n")

if __name__ == "__main__":
    print("Starting large graph generation...")

    # Generate a large graph with 200 vertices (reduced for faster execution)
    large_graph = generate_large_graph(200, edge_density=0.05)

    print(f"Graph generated with {len(large_graph.get_vertices())} vertices and {len(large_graph.get_edges())} edges")

    # Save the graph to a file
    save_graph_to_file(large_graph, "test_large.gr")

    print(f"Graph saved to test_large.gr")
