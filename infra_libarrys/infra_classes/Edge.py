from infra_libarrys.consts_and_enums.EdgeConsts import DEFAULT_WEIGHT


class Edge:
    def __init__(self, nodes=None, is_fragile=False, weight=DEFAULT_WEIGHT):
        self.nodes = nodes
        self.is_fragile = is_fragile
        self.weight = weight

    def __eq__(self, other):
        return self.nodes == other.nodes

    def add_nodes(self, node1, node2):
        self.nodes = {node1, node2}

    def get_neighbor_node(self, curr_node):
        return (self.nodes - {curr_node}).pop()

    def remove_self_from_env(self, env):
        for node in self.nodes:
            node.remove_edge(edge=self)
        coordinate_tuple = [curr_node.get_x_y_coordinate for curr_node in self.nodes]
        coordinate_tuple = tuple(coordinate_tuple)
        switched_coordinate_tuple = (coordinate_tuple[2], coordinate_tuple[3], coordinate_tuple[0], coordinate_tuple[1])
        env.fragile_edges = env.fragile_edges - {coordinate_tuple, switched_coordinate_tuple}
        env.blocked_edges.add(coordinate_tuple)
