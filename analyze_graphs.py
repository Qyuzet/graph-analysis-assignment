import time
from graph import Graph
from graph_loader import (
    load_cities_graph,
    load_cyclic_graph,
    load_random_graph,
    load_standard_graph,
    load_large_graph
)

def analyze_graph(graph, graph_name):
    """
    Analyze a graph by running MST and Shortest Path algorithms
    """
    print(f"\n{'=' * 50}")
    print(f"Analyzing {graph_name}")
    print(f"{'=' * 50}")

    # Graph properties
    num_vertices = len(graph.get_vertices())
    num_edges = len(graph.get_edges())

    print(f"Number of vertices: {num_vertices}")
    print(f"Number of edges: {num_edges}")

    # Run Prim's algorithm
    print("\nPrim's MST Algorithm:")
    mst_edges, total_weight, execution_time = graph.prim_mst()
    print(f"MST Edges: {mst_edges}")
    print(f"Total MST Weight: {total_weight}")
    print(f"Execution Time: {execution_time:.6f} seconds")

    # Run Kruskal's algorithm
    print("\nKruskal's MST Algorithm:")
    mst_edges, total_weight, execution_time = graph.kruskal_mst()
    print(f"MST Edges: {mst_edges}")
    print(f"Total MST Weight: {total_weight}")
    print(f"Execution Time: {execution_time:.6f} seconds")

    # Run Dijkstra's algorithm from vertex 0
    print("\nDijkstra's Shortest Path Algorithm (from vertex 0):")
    start_vertex = min(graph.get_vertices())
    dist, parent, execution_time = graph.dijkstra_shortest_path(start_vertex)

    # Print distances to all vertices
    print(f"Distances from vertex {start_vertex}:")
    for vertex in sorted(dist.keys()):
        if dist[vertex] == float('inf'):
            print(f"  Vertex {vertex}: Unreachable")
        else:
            print(f"  Vertex {vertex}: {dist[vertex]}")

    print(f"Execution Time: {execution_time:.6f} seconds")

    return {
        'graph_name': graph_name,
        'num_vertices': num_vertices,
        'num_edges': num_edges,
        'prim_time': graph.prim_mst()[2],
        'kruskal_time': graph.kruskal_mst()[2],
        'dijkstra_time': graph.dijkstra_shortest_path(start_vertex)[2]
    }

def main():
    # Load graphs
    cities_graph = load_cities_graph('test_cities.gr')
    cyclic_graph = load_cyclic_graph('test_cyclic.gr')
    random_graph = load_random_graph('test_random.gr')
    standard_graph = load_standard_graph()
    large_graph = load_large_graph('test_large.gr')

    # Analyze each graph
    results = []
    results.append(analyze_graph(cities_graph, "Cities Graph"))
    results.append(analyze_graph(cyclic_graph, "Cyclic Graph"))
    results.append(analyze_graph(random_graph, "Random Graph"))
    results.append(analyze_graph(standard_graph, "Standard Graph"))
    results.append(analyze_graph(large_graph, "Large Graph"))

    # Comparative analysis
    print("\n\n" + "=" * 50)
    print("COMPARATIVE ANALYSIS")
    print("=" * 50)

    print("\nPerformance Comparison:")
    print(f"{'Graph Name':<15} {'Vertices':<10} {'Edges':<10} {'Prim (s)':<12} {'Kruskal (s)':<12} {'Dijkstra (s)':<12}")
    print("-" * 75)

    for result in results:
        print(f"{result['graph_name']:<15} {result['num_vertices']:<10} {result['num_edges']:<10} "
              f"{result['prim_time']:<12.6f} {result['kruskal_time']:<12.6f} {result['dijkstra_time']:<12.6f}")

    # Analysis of factors affecting performance
    print("\nAnalysis of Factors Affecting Performance:")
    print("1. Number of Vertices:")
    print("   - As the number of vertices increases, the time complexity of all algorithms increases.")
    print("   - Prim's algorithm: O(V^2) without binary heap, O(E log V) with binary heap")
    print("   - Kruskal's algorithm: O(E log E) or O(E log V)")
    print("   - Dijkstra's algorithm: O(V^2) without binary heap, O(E log V) with binary heap")

    print("\n2. Number of Edges:")
    print("   - More edges generally mean more operations for all algorithms.")
    print("   - Kruskal's algorithm is particularly affected as it sorts all edges.")
    print("   - For sparse graphs (E ≈ V), algorithms perform better than for dense graphs (E ≈ V^2).")

    print("\n3. Graph Structure:")
    print("   - Cyclic vs. Acyclic: Cycles require additional checks in MST algorithms.")
    print("   - Connected vs. Disconnected: Disconnected graphs may require special handling.")
    print("   - Weight Distribution: Uniform weights vs. varied weights can affect performance.")

    print("\n4. Implementation Details:")
    print("   - Data structures used (priority queues, disjoint sets)")
    print("   - Optimizations applied")
    print("   - Language and runtime environment")

if __name__ == "__main__":
    main()
