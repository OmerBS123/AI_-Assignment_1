from infra_libarrys.infra_classes.Edge import Edge


class Clique:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2, weight):
        edge = Edge(nodes={node1, node2}, weight=weight)
        self.edges.add(edge)
        node1.edges.add(edge)
        node2.edges.add(edge)
