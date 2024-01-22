class Node:
    def __init__(self, x, y, package=None, agent=None):
        self.x = x
        self.y = y
        self.package = package
        self.edges = set()
        self.agent = agent

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def add_edge(self, edge):
        self.edges.add(edge)

    def remove_edge(self, edge):
        self.edges.remove(edge)

    def add_package(self, package):
        self.package = package

    def remove_package(self):
        self.package = None

    def get_edge_from_node(self, other_node):
        for edge in self.edges:
            if other_node in edge.nodes:
                return edge
        return None

    def get_x_y_coordinate(self):
        return self.x, self.y

    def is_node_destination(self, packages):
        node_x, node_y = self.get_x_y_coordinate()
        return packages.pop((node_x, node_y), None)
