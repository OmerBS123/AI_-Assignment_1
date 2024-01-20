from itertools import combinations

from infra_libarrys.infra_classes.Clique import Clique
from infra_libarrys.infra_classes.Node import Node
from infra_libarrys.infra_classes.Edge import Edge
from infra_libarrys.infra_classes.SearchAlgorithem.Dijkstra import Dijkstra


class Env:
    def __init__(self, width, height, blocked_edges=None, fragile_edges=None):
        self.width = width
        self.height = height
        self.graph = [[Node(x, y) for y in range(height + 1)] for x in range(width + 1)]
        self.nodes = {node for row in self.graph for node in row}
        self.edges_dict = {}
        self.blocked_edges = blocked_edges
        self.fragile_edges = fragile_edges
        self.package_points = {node for node in self.nodes if node.package is not None}
        self.agent_nodes = {node for node in self.nodes if node.agent is not None}
        self.delivery_points = self.get_delivery_nodes()
        self.create_all_edges()

    def __copy__(self):
        copy_env = Env(self.width, self.height, self.blocked_edges, self.fragile_edges)
        package_coordinate = {node.get_x_y_coordinate() for node in self.package_points}
        copy_env.package_points = [copy_env.graph[x][y] for x, y in package_coordinate]

    def __eq__(self, other):
        cond1 = self.package_points == other.package_points
        cond2 = self.delivery_points == other.delivrey_points
        cond3 = self.fragile_edges == other.fragile_edges
        return cond1 and cond2 and cond3

    def get_delivery_nodes(self):
        set_pos_x_y = {node.package.get_delivery_x_y() for node in self.package_points}
        return {self.graph[x][y] for x, y in set_pos_x_y}

    def create_all_edges(self):
        for x in range(self.width + 1):
            for y in range(self.height + 1):
                self.create_edges_for_node(x, y)

    def create_edges_for_node(self, x, y):
        self.create_horizontal_edges(x, y)
        self.create_vertical_edges(x, y)

    def create_horizontal_edges(self, x, y):
        self.connect_nodes(x, y, x - 1, y)
        self.connect_nodes(x, y, x + 1, y)

    def create_vertical_edges(self, x, y):
        self.connect_nodes(x, y, x, y + 1)
        self.connect_nodes(x, y, x, y - 1)

    def connect_nodes(self, x1, y1, x2, y2):
        # Check if the edge already exists
        if x2 < 0 or x2 > self.width or y2 < 0 or y2 > self.height:
            return

        if (x1, y1, x2, y2) in self.edges_dict or (x2, y2, x1, y1) in self.edges_dict:
            return

        if (x1, y1, x2, y2) in self.blocked_edges or (x2, y2, x1, y1) in self.blocked_edges:
            return

        edge = Edge(is_fragile=((x1, y1, x2, y2) in self.fragile_edges or (x2, y2, x1, y1) in self.fragile_edges))
        edge.add_nodes(self.graph[x1][y1], self.graph[x2][y2])
        self.edges_dict[(x1, y1, x2, y2)] = edge
        self.graph[x1][y1].add_edge(edge)
        self.graph[x2][y2].add_edge(edge)

    def get_edge_from_nodes(self, node_1, node_2):
        x1, y1 = node_1.get_x_y_coordinate()
        x2, y2 = node_2.get_x_y_coordinate()
        return next(self.edges_dict[edge] for edge in self.edges_dict if (x1, y1, x2, y2) == edge or (x2, y2, x1, y1) == edge)

    def create_clique(self):
        clique = Clique()

        # Create a copy of the nodes and edges from the original graph
        node_set = self.package_points | self.delivery_points | self.agent_nodes

        distance_dict = {}

        # Add nodes to the clique
        for node in node_set:
            clique.add_node(node)

        # Add edges based on the shortest paths
        for node1, node2 in combinations(node_set, 2):
            if node1 in self.agent_nodes and node2 in self.agent_nodes:
                continue

            if node1 not in distance_dict:
                dijkstra_algo = Dijkstra(start_node=node1, env=self, destination_node=node2)
                _, distances = dijkstra_algo.run_search()
                distance_dict[node1] = distances

            distances = distance_dict[node1]
            clique.add_edge(node1, node2, distances[node1])

        return clique
