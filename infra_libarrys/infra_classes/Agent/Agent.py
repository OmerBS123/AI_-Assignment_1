class Agent:
    def __init__(self, curr_node, env):
        self.env = env
        self.curr_node = None
        self.put_self_on_node(curr_node)
        self.packages = set()
        self.time_left_to_cross_edge = 0
        self.curr_crossing_edge = None
        self.agent_type = None
        self.agent_color = None
        self.score = 0

    @classmethod
    def copy_with_packages(cls, original_agent, created_packages, new_env):
        x, y = original_agent.curr_node.get_x_y_coordinate()
        new_curr_node = new_env.graph[x][y]
        new_agent = cls(new_curr_node, new_env)
        old_agent_package_coordinate = {(package.pos_x, package.pos_y) for package in original_agent.packages}
        new_agent.packages = {package for package in created_packages if (package.pos_x, package.pos_y) in old_agent_package_coordinate}
        new_agent.time_left_to_cross_edge = original_agent.time_left_to_cross_edge
        new_agent.curr_crossing_edge = None
        new_agent.agent_type = original_agent.agent_type
        new_agent.agent_color = original_agent.agent_color
        new_agent.score = original_agent.score
        return new_agent

    def remove_package(self, package):
        self.packages.remove(package)

    def step_over_edge(self, edge):
        self.curr_crossing_edge = edge
        self.time_left_to_cross_edge = edge.weight
        self.finish_crossing_with_curr_edge()

    def finish_crossing_with_curr_edge(self):
        if self.time_left_to_cross_edge <= 0:
            return True
        self.time_left_to_cross_edge -= 1
        if self.time_left_to_cross_edge > 0:
            return False
        next_node = self.curr_crossing_edge.get_neighbor_node(self.curr_node)
        self.put_self_on_node(next_node)
        if self.curr_crossing_edge.is_fragile:
            self.curr_crossing_edge.remove_self_from_env(env=self.env)
        self.curr_crossing_edge = None
        self.pickup_package_if_exists()
        self.drop_package_if_possible() #TODO: chaeck if destination == pickup
        return True

    def drop_package_if_possible(self):
        if not self.packages:
            return
        package_to_remove = self.curr_node.is_node_destination(self.packages)
        if package_to_remove is None:
            return
        self.remove_package(package_to_remove)
        self.score += 1

    def put_self_on_node(self, new_curr_node):
        new_curr_node.agent = self
        if self.curr_node is not None:
            self.env.switch_agent_nodes(old_node=self.curr_node, new_node=new_curr_node)
        self.curr_node = new_curr_node

    def pickup_package_if_exists(self):
        if self.curr_node.package is None:
            return

        self.packages.add(self.curr_node.package)
        self.curr_node.remove_package(env=self.env)

    def run_agent_step(self):
        pass
