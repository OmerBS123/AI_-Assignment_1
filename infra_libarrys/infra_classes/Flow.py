import time


class Flow:
    def __init__(self, env, agents_list, package_appear_dict, package_disappear_dict, gui_handler):
        self.env = env
        self.agents_list = agents_list
        self.package_appear_dict = package_appear_dict
        self.package_disappear_dict = package_disappear_dict
        self.timer = 0
        self.gui_handler = gui_handler
        self.running = True

    def run_flow(self):
        time.sleep(1)
        print("Flow thread started")
        while self.running:
            self.timer += 1
            self.gui_handler.update_timer(self.timer)
            self.update_packages_state_if_needed()
            for curr_agent in self.agents_list:
                curr_agent.run_agent_step(self.timer)
            time.sleep(1)
            # self.gui_handler.update_ui(self.timer)
        # self.gui_handler.close_ui()

    def update_packages_state_if_needed(self):
        if self.timer in self.package_appear_dict:
            for curr_new_package in self.package_appear_dict[self.timer]:
                self.env.graph[curr_new_package.pos_x][curr_new_package.pos_y].add_package(curr_new_package, env=self.env)

        if self.timer in self.package_disappear_dict:
            for curr_package in self.package_disappear_dict[self.timer]:
                curr_package.remove_self_from_env(env=self.env)

    def finish_run(self):
        self.gui_handler.close_ui()
