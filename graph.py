import heapq
import time
from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
        self.weights = {}
        
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
        
    def add_edge(self, u, v, weight):
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges[u].append(v)
        self.edges[v].append(u)  # For undirected graph
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight  # For undirected graph
        
    def get_vertices(self):
        return list(self.vertices)
    
    def get_edges(self):
        edges = []
        for u in self.edges:
            for v in self.edges[u]:
                if (u, v) not in edges and (v, u) not in edges:
                    edges.append((u, v, self.weights[(u, v)]))
        return edges
    
    def get_neighbors(self, vertex):
        return self.edges[vertex]
    
    def get_weight(self, u, v):
        return self.weights.get((u, v), float('inf'))
    
    def prim_mst(self):
        """
        Prim's algorithm for Minimum Spanning Tree
        """
        start_time = time.time()
        
        if not self.vertices:
            return [], 0, 0
        
        # Start with an arbitrary vertex
        start_vertex = next(iter(self.vertices))
        
        # Priority queue to store vertices and their key values
        pq = [(0, start_vertex)]
        
        # To keep track of vertices included in MST
        mst_set = set()
        
        # To store MST edges
        mst_edges = []
        
        # To store the total weight of MST
        total_weight = 0
        
        # Dictionary to store key values of vertices
        key = {vertex: float('inf') for vertex in self.vertices}
        key[start_vertex] = 0
        
        # Dictionary to store parent of each vertex in MST
        parent = {vertex: None for vertex in self.vertices}
        
        while pq:
            # Extract vertex with minimum key value
            current_key, u = heapq.heappop(pq)
            
            # If vertex is already in MST, skip
            if u in mst_set:
                continue
            
            # Add vertex to MST
            mst_set.add(u)
            
            # Add edge to MST if parent exists
            if parent[u] is not None:
                mst_edges.append((parent[u], u, self.get_weight(parent[u], u)))
                total_weight += self.get_weight(parent[u], u)
            
            # Update key values of adjacent vertices
            for v in self.get_neighbors(u):
                weight = self.get_weight(u, v)
                if v not in mst_set and weight < key[v]:
                    key[v] = weight
                    parent[v] = u
                    heapq.heappush(pq, (key[v], v))
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        return mst_edges, total_weight, execution_time
    
    def kruskal_mst(self):
        """
        Kruskal's algorithm for Minimum Spanning Tree
        """
        start_time = time.time()
        
        if not self.vertices:
            return [], 0, 0
        
        # Sort all edges in non-decreasing order of their weight
        edges = sorted(self.get_edges(), key=lambda x: x[2])
        
        # Initialize disjoint set for each vertex
        parent = {vertex: vertex for vertex in self.vertices}
        rank = {vertex: 0 for vertex in self.vertices}
        
        def find(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])
            return parent[vertex]
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            
            if root_u == root_v:
                return
            
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
        
        # To store MST edges
        mst_edges = []
        
        # To store the total weight of MST
        total_weight = 0
        
        for u, v, weight in edges:
            if find(u) != find(v):
                mst_edges.append((u, v, weight))
                total_weight += weight
                union(u, v)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        return mst_edges, total_weight, execution_time
    
    def dijkstra_shortest_path(self, start_vertex):
        """
        Dijkstra's algorithm for Shortest Path
        """
        start_time = time.time()
        
        if start_vertex not in self.vertices:
            return {}, {}, 0
        
        # Priority queue to store vertices and their distances
        pq = [(0, start_vertex)]
        
        # Dictionary to store distances from start_vertex to each vertex
        dist = {vertex: float('inf') for vertex in self.vertices}
        dist[start_vertex] = 0
        
        # Dictionary to store parent of each vertex in shortest path
        parent = {vertex: None for vertex in self.vertices}
        
        while pq:
            # Extract vertex with minimum distance
            current_dist, u = heapq.heappop(pq)
            
            # If we've already found a shorter path, skip
            if current_dist > dist[u]:
                continue
            
            # Update distances of adjacent vertices
            for v in self.get_neighbors(u):
                weight = self.get_weight(u, v)
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        return dist, parent, execution_time
