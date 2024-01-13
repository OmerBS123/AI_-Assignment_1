from infra_libarrys.consts_and_enums.EdgeConsts import DEFAULT_WEIGHT


class ReducedEdge:
    def __init__(self, original_object, left_node, right_node, weight=DEFAULT_WEIGHT):
        self.original_object = original_object
        self.weight = weight
        self.nodes = {right_node, left_node}
