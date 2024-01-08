class Agent:
    def __init__(self, starting_node, grid):
        self.grid = grid
        self.curr_node = starting_node
        self.package = None

    def remove_package(self):
        self.package = None

    def run_agent_step(self):
        pass
