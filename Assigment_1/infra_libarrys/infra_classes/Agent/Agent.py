class Agent:
    def __init__(self, curr_node, env):
        self.env = env
        self.curr_node = curr_node
        self.package = None
        self.time_left_to_cross_edge = 0
        self.curr_crossing_edge = None
        self.agent_type = None

    def remove_package(self):
        self.package = None

    def run_agent_step(self):
        pass

    def step_over_edge(self, edge):
        self.curr_crossing_edge = edge
        self.time_left_to_cross_edge = edge.weight
        self.time_left_to_cross_edge -= 1

    def finish_crossing_with_curr_edge(self):
        if self.time_left_to_cross_edge > 0:
            self.time_left_to_cross_edge -= 1
            if self.time_left_to_cross_edge == 0:
                self.curr_node = self.curr_crossing_edge.get_neighbor_node(self.curr_node)
            return True
        return False
