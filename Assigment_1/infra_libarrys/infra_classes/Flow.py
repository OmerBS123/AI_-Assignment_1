class Flow:
    def __init__(self, grid, agents_list, package_appear_dict, package_disappear_dict):
        self.grid = grid
        self.agents_list = agents_list
        self.package_appear_dict = package_appear_dict
        self.package_disappear_dict = package_disappear_dict
        self.timer = 0

    def run_flow(self):
        while True:
            self.update_packages_state_if_needed()
            for curr_agent in self.agents_list:
                curr_agent.run_agent_step()

    def update_packages_state_if_needed(self):
        if self.timer in self.package_appear_dict:
            for curr_new_package in self.package_appear_dict[self.timer]:
                self.grid.grid[curr_new_package.pos_x][curr_new_package.pos_y].add_package(curr_new_package)

        if self.timer in self.package_disappear_dict:
            for curr_package in self.package_disappear_dict[self.timer]:
                curr_package.remove_self_from_grid(self.grid)
