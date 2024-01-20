class State:
    def __init__(self, env, curr_node, time):
        self.env = env
        self.curr_node = curr_node
        self.time = time

    def __eq__(self, other):
        return self.env == other.env and self.curr_node == other.curr_node

    def is_goal(self):
        cond = self.env.package_points or self.env.delivery_points
        return not cond
