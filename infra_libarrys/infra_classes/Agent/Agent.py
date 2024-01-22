import copy


class Agent:
    def __init__(self, curr_node, env):
        self.env = env
        self.curr_node = curr_node
        self.packages = {}
        self.time_left_to_cross_edge = 0
        self.curr_crossing_edge = None
        self.agent_type = None
        self.agent_color = None
        self.score = 0

    def __copy__(self):
        new_agent = Agent(self.curr_node, self.env)
        new_agent.packages = {copy.copy(package) for package in self.packages}
        new_agent.time_left_to_cross_edge = self.time_left_to_cross_edge
        new_agent.curr_crossing_edge = None
        new_agent.agent_type = self.agent_type
        new_agent.agent_color = self.agent_color
        new_agent.score = self.score
        return new_agent

    def remove_package(self, package):
        self.packages.remove(package)

    def run_agent_step(self):
        pass

    def step_over_edge(self, edge):
        self.curr_crossing_edge = edge
        self.time_left_to_cross_edge = edge.weight
        self.finish_crossing_with_curr_edge()

    def finish_crossing_with_curr_edge(self):
        if self.time_left_to_cross_edge > 0:
            self.time_left_to_cross_edge -= 1
            if self.time_left_to_cross_edge == 0:
                self.curr_node = self.curr_crossing_edge.get_neighbor_node(self.curr_node)
                if self.curr_crossing_edge.is_fragile:
                    self.curr_crossing_edge.remove_self_from_env(env=self.env)
                self.curr_crossing_edge = None
            return False
        return True
