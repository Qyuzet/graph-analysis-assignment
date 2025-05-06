import networkx as nx
import matplotlib.pyplot as plt
from graph_loader import (
    load_cities_graph,
    load_cyclic_graph,
    load_random_graph,
    load_standard_graph
)

def convert_to_networkx(graph):
    """
    Convert our Graph object to a NetworkX graph
    """
    G = nx.Graph()
    
    # Add vertices
    for vertex in graph.get_vertices():
        G.add_node(vertex)
    
    # Add edges
    for u, v, weight in graph.get_edges():
        G.add_edge(u, v, weight=weight)
    
    return G

def visualize_graph(graph, title, mst_edges=None):
    """
    Visualize a graph and its MST
    """
    G = convert_to_networkx(graph)
    
    # Create a layout for the graph
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(10, 8))
    plt.title(title)
    
    # Draw the graph
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_labels(G, pos)
    
    # Draw all edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    
    # Draw edge labels
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Draw MST edges if provided
    if mst_edges:
        mst_edge_list = [(u, v) for u, v, _ in mst_edges]
        nx.draw_networkx_edges(G, pos, edgelist=mst_edge_list, width=3.0, edge_color='red')
    
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
    plt.close()

def main():
    # Load graphs
    cities_graph = load_cities_graph('test_cities.gr')
    cyclic_graph = load_cyclic_graph('test_cyclic.gr')
    random_graph = load_random_graph('test_random.gr')
    standard_graph = load_standard_graph()
    
    # Get MSTs
    cities_mst = cities_graph.prim_mst()[0]
    cyclic_mst = cyclic_graph.prim_mst()[0]
    random_mst = random_graph.prim_mst()[0]
    standard_mst = standard_graph.prim_mst()[0]
    
    # Visualize graphs with MSTs
    visualize_graph(cities_graph, "Cities Graph", cities_mst)
    visualize_graph(cyclic_graph, "Cyclic Graph", cyclic_mst)
    visualize_graph(random_graph, "Random Graph", random_mst)
    visualize_graph(standard_graph, "Standard Graph", standard_mst)
    
    print("Graph visualizations saved as PNG files.")

if __name__ == "__main__":
    main()
