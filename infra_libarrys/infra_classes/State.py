class State:
    def __init__(self, env, curr_node, time):
        self.env = env
        self.curr_node = curr_node
        self.time = time
        self.env.update_packages_state_if_needed(self.time)

    def __eq__(self, other):
        return self.env == other.env and self.curr_node == other.curr_node

    def is_goal(self):
        cond1 = self.env.package_points or self.env.delivery_points
        cond2 = self.time > max(self.env.package_appear_dict.keys(), default=float('-inf'))
        return not cond1 and cond2

    def get_edge_from_old_edge(self, old_edge):
        old_node1, old_node2 = old_edge.nodes
        x1, y1 = old_node1.get_x_y_coordinates()
        x2, y2 = old_node2.get_x_y_coordinates()

        state_node1 = self.env.graph[x1][y1]
        state_node2 = self.env.graph[x2][y2]

        return self.env.get_edge_from_nodes(state_node1, state_node2)

    def update_agent(self, old_edge):
        state_edge = self.get_edge_from_old_edge(old_edge)
        next_node = state_edge.get_neighbor_node(self.curr_node)
        agent = self.curr_node.agent
        self.curr_node.agent = None
        self.curr_node = next_node
        next_node.agent = agent
        agent.curr_node = self.curr_node

    def update_state(self, old_edge):
        self.update_agent(old_edge)
        move_edge = self.get_edge_from_old_edge(old_edge)

        if move_edge.is_fragile:
            move_edge.remove_self_from_env()


