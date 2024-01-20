class State:
    def __init__(self, env, curr_node):
        self.env = env
        self.curr_node = curr_node

    def __eq__(self, other):
        return self.env == other.env and self.curr_node == other.curr_node
