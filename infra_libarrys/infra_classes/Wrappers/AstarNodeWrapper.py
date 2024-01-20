class AstarNodeWrapper:
    def __init__(self, state, parent_node, g, h, prev_action):
        self.state = state
        self.parent_node = parent_node
        self.g = g
        self.h = h
        self.prev_action = prev_action
        self.children = set()

    def calculate_f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.calculate_f() < other.calculate_f()
