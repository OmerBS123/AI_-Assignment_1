from infra_libarrys.infra_classes.Node import Node
from infra_libarrys.infra_classes.Edge import Edge


class Env:
    def __init__(self, width, height, blocked_edges=None, fragile_edges=None):
        self.width = width
        self.height = height
        self.graph = [[Node(x, y) for y in range(height + 1)] for x in range(width + 1)]
        self.nodes = {node for row in self.graph for node in row}
        self.edges_dict = {}
        self.blocked_edges = blocked_edges
        self.fragile_edges = fragile_edges
        self.create_all_edges()

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
