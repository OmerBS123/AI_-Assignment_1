class Node:
    def __init__(self, x, y, package=None, agent=None):
        self.x = x
        self.y = y
        self.package = package
        self.edges = set()
        self.agent = agent

    def add_edge(self, edge):
        self.edges.add(edge)

    def remove_edge(self, edge):
        self.edges.remove(edge)

    def add_package(self, package):
        self.package = package

    def remove_package(self):
        self.package = None

    def __str__(self):
        return f'Node({self.x}, {self.y}, has package:{self.package})'
