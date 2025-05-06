# MST and Shortest Path Algorithms Analysis

## Introduction

This report analyzes the implementation and performance of Minimum Spanning Tree (MST) and Shortest Path algorithms on various graph datasets. The algorithms implemented are:

1. **Prim's Algorithm** for MST
2. **Kruskal's Algorithm** for MST
3. **Dijkstra's Algorithm** for Shortest Path

## Graph Datasets

The analysis was performed on the following graph datasets:

1. **Cities Graph**: A graph representing major European cities with 10 vertices and 28 edges.
2. **Cyclic Graph**: A simple cyclic graph with 6 vertices and 12 edges.
3. **Random Graph**: A randomly generated graph with 8 vertices and 26 edges.
4. **Standard Graph**: A standard test graph with 6 vertices and 18 edges.
5. **Large Graph**: A randomly generated large graph with 200 vertices and 3972 edges.

## Performance Results

| Graph Name     | Vertices | Edges | Prim (s)  | Kruskal (s) | Dijkstra (s) |
|----------------|----------|-------|-----------|-------------|--------------|
| Cities Graph   | 10       | 28    | 0.000000  | 0.000000    | 0.000000     |
| Cyclic Graph   | 6        | 12    | 0.000000  | 0.000000    | 0.000000     |
| Random Graph   | 8        | 26    | 0.000000  | 0.000000    | 0.000000     |
| Standard Graph | 6        | 18    | 0.000000  | 0.000000    | 0.000000     |
| Large Graph    | 200      | 3972  | 0.002246  | 0.130890    | 0.003507     |

## Analysis of Factors Affecting Performance

### 1. Number of Vertices

The number of vertices in a graph significantly impacts the performance of graph algorithms:

- **Prim's Algorithm**: O(V²) without a binary heap, O(E log V) with a binary heap
- **Kruskal's Algorithm**: O(E log E) or O(E log V)
- **Dijkstra's Algorithm**: O(V²) without a binary heap, O(E log V) with a binary heap

As observed in our results, the algorithms showed negligible execution times for small graphs (< 10 vertices). However, for the large graph with 200 vertices, we can see measurable execution times, particularly for Kruskal's algorithm.

### 2. Number of Edges

The number of edges also plays a crucial role in algorithm performance:

- **Prim's Algorithm**: Performance is more affected by the number of vertices than edges when using a binary heap.
- **Kruskal's Algorithm**: Significantly affected by the number of edges since it sorts all edges by weight.
- **Dijkstra's Algorithm**: Similar to Prim's, it's more affected by vertices than edges when using a binary heap.

In our large graph with 3972 edges, Kruskal's algorithm showed the highest execution time (0.13 seconds) compared to Prim's (0.002 seconds) and Dijkstra's (0.003 seconds). This aligns with theoretical expectations since Kruskal's algorithm needs to sort all edges.

### 3. Graph Structure

The structure of the graph can significantly impact algorithm performance:

- **Cyclic vs. Acyclic**: Cycles require additional checks in MST algorithms, particularly in Kruskal's algorithm where the union-find data structure is used to detect cycles.
- **Connected vs. Disconnected**: Disconnected graphs may require special handling, especially for MST algorithms that assume connectivity.
- **Weight Distribution**: Uniform weights vs. varied weights can affect the performance of priority queue operations.

### 4. Implementation Details

Implementation details can significantly affect performance:

- **Data Structures**: Our implementation uses binary heaps (via Python's heapq) for Prim's and Dijkstra's algorithms, and a disjoint-set data structure for Kruskal's algorithm.
- **Language and Runtime**: Python's interpreted nature may introduce overhead compared to compiled languages.

## Conclusion

Based on our analysis:

1. **For Small Graphs** (< 100 vertices): All three algorithms perform well with negligible differences in execution time.

2. **For Large Graphs** (≥ 100 vertices):
   - **Prim's Algorithm** is efficient for dense graphs.
   - **Kruskal's Algorithm** is more suitable for sparse graphs but shows higher execution times due to the edge sorting step.
   - **Dijkstra's Algorithm** performs well for finding shortest paths from a single source.

3. **Trade-offs**:
   - **Time vs. Space**: Prim's algorithm with a binary heap offers good time complexity but requires more space for the priority queue.
   - **Implementation Complexity**: Kruskal's algorithm requires implementing a union-find data structure, which adds complexity.

4. **Recommendations**:
   - For dense graphs, prefer Prim's algorithm for MST.
   - For sparse graphs, Kruskal's algorithm may be more efficient despite the sorting overhead.
   - For shortest path problems, Dijkstra's algorithm is efficient when using a binary heap.

## Future Work

1. Implement and compare other shortest path algorithms (e.g., Bellman-Ford, Floyd-Warshall).
2. Test on even larger graphs to better observe performance differences.
3. Optimize implementations for better performance.
4. Analyze memory usage alongside execution time.
