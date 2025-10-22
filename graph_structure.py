import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


class graph_structure:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[node].append(neighbor)
        self.graph[neighbor].append(node)

    def show_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node} --> {neighbors}")

    def plot_graph(self, highlight_nodes=None, title="Graph Structure"):
        G = nx.Graph(self.graph)
        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(6, 4))

        # ไฮไลท์โหนด
        node_colors = []
        for n in G.nodes():
            if highlight_nodes and n in highlight_nodes:
                node_colors.append("lightcoral")
            else:
                node_colors.append("skyblue")

        nx.draw(
            G, pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1200,
            font_size=12,
            font_weight='bold',
            edge_color='gray'
        )
        plt.title(title)
        plt.show()

    def bfs(self, start):
        """Breadth-First Search"""
        visited = set()
        queue = deque([start])
        traversal_order = []

        if start not in self.graph:
            print(f"Node {start} not in graph.")
            return

        visited.add(start)

        while queue:
            current_node = queue.popleft()
            traversal_order.append(current_node)

            if current_node in self.graph:
                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        print(f"BFS Traversal starting from {start}: {traversal_order}")
        
        self.plot_graph(highlight_nodes=traversal_order, title=f"BFS from {start}")

    def dfs(self, start):
        """Depth-First Search"""
        visited = set()
        traversal_order = []

        if start not in self.graph:
            print(f"Node {start} not in graph.")
            return

        def dfs_recursive(node):
            visited.add(node)
            traversal_order.append(node)

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)

        dfs_recursive(start)

        print(f"DFS Traversal starting from {start}: {traversal_order}")
        
        self.plot_graph(highlight_nodes=traversal_order, title=f"DFS from {start}")


if __name__ == "__main__":
    g = graph_structure()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')

    print("Grapwh Structure:")
    g.show_graph()

    g.bfs('A')

    g.dfs('A')
