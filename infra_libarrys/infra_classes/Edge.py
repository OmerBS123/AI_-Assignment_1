from infra_libarrys.consts_and_enums.EdgeConsts import DEFAULT_WEIGHT


class Edge:
    def __init__(self, nodes=None, is_fragile=False, weight=DEFAULT_WEIGHT):
        # 'regular', 'fragile', 'blocked'
        self.nodes = nodes  # List of connected nodes
        self.is_fragile = is_fragile
        self.weight = weight

    def add_nodes(self, node1, node2):
        self.nodes = {node1, node2}

    def __str__(self):
        return f'Edge(State: {self.state}, Connected Nodes: {self.nodes})'
