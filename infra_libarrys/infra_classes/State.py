class State:
    def __init__(self, env, curr_node, time, goal_score, agent=None):
        self.env = env
        self.curr_node = curr_node
        self.time = time
        self.agent = agent
        self.env.update_packages_state_if_needed(self.time)
        self.goal_score = goal_score

    def __eq__(self, other):
        return self.curr_node == other.curr_node and self.agent.score == other.agent.score and self.agent.packages == other.agent.packages and self.env == other.env

    def is_goal(self):
        return self.agent.score == self.goal_score

    def get_edge_from_old_edge(self, old_edge):
        old_node1, old_node2 = old_edge.nodes
        x1, y1 = old_node1.get_x_y_coordinate()
        x2, y2 = old_node2.get_x_y_coordinate()

        state_node1 = self.env.graph[x1][y1]
        state_node2 = self.env.graph[x2][y2]

        return self.env.get_edge_from_nodes(state_node1, state_node2)

    def update_agent(self, old_edge):
        state_edge = self.get_edge_from_old_edge(old_edge)
        next_node = state_edge.get_neighbor_node(self.curr_node)
        agent = self.curr_node.agent
        agent.put_self_on_node(next_node)
        self.curr_node = next_node
        self.agent = agent

    def update_state(self, old_edge, time_delta):
        self.update_packages_state_if_needed(time_delta)
        move_edge = self.get_edge_from_old_edge(old_edge)

        if move_edge.is_fragile:
            move_edge.remove_self_from_env(self.env)

        self.update_agent(old_edge)
        self.all_agents_pickup_and_drop_package()

    def update_packages_state_if_needed(self, time_delta):
        for _ in range(time_delta):
            self.time += 1
            self.env.update_packages_state_if_needed(self.time)

    def all_agents_pickup_and_drop_package(self):
        for curr_agent_node in self.env.agent_nodes:
            curr_agent_node.agent.pickup_package_if_exists()
            curr_agent_node.agent.drop_package_if_possible()
