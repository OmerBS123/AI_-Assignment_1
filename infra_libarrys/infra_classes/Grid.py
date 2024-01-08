from infra_libarrys.infra_classes.Node import Node
from infra_libarrys.infra_classes.Edge import Edge


class Grid:
    def __init__(self, width, height, blocked_edges=None, fragile_edges=None):
        self.width = width
        self.height = height
        self.grid = [[Node(x, y) for y in range(height + 1)] for x in range(width + 1)]
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
        edge.add_nodes(self.grid[x1][y1], self.grid[x2][y2])
        self.edges_dict[(x1, y1, x2, y2)] = edge
        self.grid[x1][y1].edges.add(edge)
        self.grid[x2][y2].edges.add(edge)

# @staticmethod
# def block_edge(node1, node2):
#     if node2 in node1.neighbors:
#         node1.neighbors.remove(node2)
#         node2.neighbors.remove(node1)
#
# def add_agent(self, agent, node):
#     agent.current_node = node
#     node.agents.append(agent)
#
# def move_agent(self, agent, destination_node):
#     if destination_node in agent.current_node.neighbors:
#         agent.current_node.agents.remove(agent)
#         destination_node.agents.append(agent)
#         agent.current_node = destination_node
#
# def deliver_package(self, agent):
#     if agent.current_node.delivery_point and agent.current_node.package:
#         delivered_package = agent.current_node.package
#         agent.current_node.package = None
#         return delivered_package
#     return None
