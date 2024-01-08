from infra_libarrys.consts_and_enums.EdgeConsts import DEFAULT_WEIGHT


class Edge:
    def __init__(self, nodes=None, is_fragile=False, weight=DEFAULT_WEIGHT):
        self.nodes = nodes
        self.is_fragile = is_fragile
        self.weight = weight

    def add_nodes(self, node1, node2):
        self.nodes = {node1, node2}

    def get_neighbor_node(self, curr_node):
        return (self.nodes - {curr_node}).pop()
