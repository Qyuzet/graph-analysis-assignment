import time
import statistics
from graph import Graph
from graph_loader import (
    load_cities_graph,
    load_cyclic_graph,
    load_random_graph,
    load_standard_graph,
    load_large_graph
)

# Number of iterations for timing measurements
NUM_ITERATIONS_SMALL = 1000  # More iterations for small graphs
NUM_ITERATIONS_MEDIUM = 100  # Medium number of iterations
NUM_ITERATIONS_LARGE = 5     # Fewer iterations for large graphs

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

    # Run multiple iterations for more accurate timing
    prim_times = []
    kruskal_times = []
    dijkstra_times = []
    start_vertex = min(graph.get_vertices())

    # Determine number of iterations based on graph size
    if num_vertices >= 100:
        iterations = NUM_ITERATIONS_LARGE
    elif num_vertices >= 20:
        iterations = NUM_ITERATIONS_MEDIUM
    else:
        iterations = NUM_ITERATIONS_SMALL

    print(f"\nRunning {iterations} iterations for timing measurements...")

    for _ in range(iterations):
        # Measure Prim's algorithm
        mst_edges, total_weight, execution_time = graph.prim_mst()
        prim_times.append(execution_time)

        # Measure Kruskal's algorithm
        mst_edges, total_weight, execution_time = graph.kruskal_mst()
        kruskal_times.append(execution_time)

        # Measure Dijkstra's algorithm
        dist, parent, execution_time = graph.dijkstra_shortest_path(start_vertex)
        dijkstra_times.append(execution_time)

    # Calculate average times in nanoseconds
    avg_prim_time = statistics.mean(prim_times) * 1_000_000_000  # Convert to nanoseconds
    avg_kruskal_time = statistics.mean(kruskal_times) * 1_000_000_000
    avg_dijkstra_time = statistics.mean(dijkstra_times) * 1_000_000_000

    # Run once more to get the actual results
    print("\nPrim's MST Algorithm:")
    mst_edges, total_weight, _ = graph.prim_mst()
    print(f"MST Edges: {mst_edges}")
    print(f"Total MST Weight: {total_weight}")
    print(f"Average Execution Time: {avg_prim_time:.2f} nanoseconds ({avg_prim_time/1000:.2f} microseconds)")

    print("\nKruskal's MST Algorithm:")
    mst_edges, total_weight, _ = graph.kruskal_mst()
    print(f"MST Edges: {mst_edges}")
    print(f"Total MST Weight: {total_weight}")
    print(f"Average Execution Time: {avg_kruskal_time:.2f} nanoseconds ({avg_kruskal_time/1000:.2f} microseconds)")

    print("\nDijkstra's Shortest Path Algorithm (from vertex 0):")
    dist, parent, _ = graph.dijkstra_shortest_path(start_vertex)

    # Print distances to all vertices (limit to first 10 for large graphs)
    print(f"Distances from vertex {start_vertex}:")
    vertices_to_show = sorted(dist.keys())[:10] if len(dist) > 10 else sorted(dist.keys())
    for vertex in vertices_to_show:
        if dist[vertex] == float('inf'):
            print(f"  Vertex {vertex}: Unreachable")
        else:
            print(f"  Vertex {vertex}: {dist[vertex]}")

    if len(dist) > 10:
        print(f"  ... and {len(dist) - 10} more vertices")

    print(f"Average Execution Time: {avg_dijkstra_time:.2f} nanoseconds ({avg_dijkstra_time/1000:.2f} microseconds)")

    return {
        'graph_name': graph_name,
        'num_vertices': num_vertices,
        'num_edges': num_edges,
        'prim_time': avg_prim_time,
        'kruskal_time': avg_kruskal_time,
        'dijkstra_time': avg_dijkstra_time
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

    print("\nPerformance Comparison (times in nanoseconds):")
    print(f"{'Graph Name':<15} {'Vertices':<10} {'Edges':<10} {'Prim (ns)':<15} {'Kruskal (ns)':<15} {'Dijkstra (ns)':<15}")
    print("-" * 85)

    for result in results:
        print(f"{result['graph_name']:<15} {result['num_vertices']:<10} {result['num_edges']:<10} "
              f"{result['prim_time']:<15.2f} {result['kruskal_time']:<15.2f} {result['dijkstra_time']:<15.2f}")

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
