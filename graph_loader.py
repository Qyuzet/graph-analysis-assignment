from graph import Graph

def load_large_graph(file_path):
    """
    Load large graph from file
    Format:
    num_vertices num_edges
    e source_vertex destination_vertex weight
    """
    graph = Graph()

    with open(file_path, 'r') as f:
        lines = f.readlines()

        # First line contains number of vertices and edges
        header = lines[0].strip().split()
        num_vertices = int(header[0])

        # Add vertices
        for i in range(num_vertices):
            graph.add_vertex(i)

        # Add edges
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if line.startswith('e '):
                parts = line.split()
                if len(parts) >= 4:
                    source = int(parts[1])
                    dest = int(parts[2])
                    weight = int(parts[3])
                    graph.add_edge(source, dest, weight)

    return graph

def load_cities_graph(file_path):
    """
    Load cities graph from file
    Format:
    a source_vertex destination_vertex weight
    """
    graph = Graph()

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('a '):
                parts = line.split()
                if len(parts) >= 4:
                    source = int(parts[1])
                    dest = int(parts[2])
                    weight = int(parts[3])
                    graph.add_edge(source, dest, weight)

    return graph

def load_cyclic_graph(file_path):
    """
    Load cyclic graph from file
    Format:
    a source_vertex destination_vertex weight
    """
    graph = Graph()

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('a '):
                parts = line.split()
                if len(parts) >= 4:
                    source = int(parts[1])
                    dest = int(parts[2])
                    weight = int(parts[3])
                    graph.add_edge(source, dest, weight)

    return graph

def load_random_graph(file_path):
    """
    Load random graph from file
    Format:
    num_vertices num_edges
    e source_vertex destination_vertex weight
    """
    graph = Graph()

    with open(file_path, 'r') as f:
        lines = f.readlines()

        # First line contains number of vertices and edges
        header = lines[0].strip().split()
        num_vertices = int(header[0])

        # Add vertices
        for i in range(num_vertices):
            graph.add_vertex(i)

        # Add edges
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if line.startswith('e '):
                parts = line.split()
                if len(parts) >= 4:
                    source = int(parts[1])
                    dest = int(parts[2])
                    weight = int(parts[3])
                    graph.add_edge(source, dest, weight)

    return graph

def load_standard_graph():
    """
    Create a standard graph for testing
    """
    graph = Graph()

    # Add vertices
    for i in range(6):
        graph.add_vertex(i)

    # Add edges
    edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 5),
        (1, 3, 2),
        (2, 3, 7),
        (2, 4, 4),
        (3, 4, 6),
        (3, 5, 3),
        (4, 5, 5)
    ]

    for u, v, w in edges:
        graph.add_edge(u, v, w)

    return graph
