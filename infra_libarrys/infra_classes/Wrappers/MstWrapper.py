class MstWrapper:
    def __init__(self, weight, node, previous_node):
        self.node = node
        self.previous_node = previous_node
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight
