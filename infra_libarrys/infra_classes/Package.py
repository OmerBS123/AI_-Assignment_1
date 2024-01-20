class Package:
    def __init__(self, pos_x, pos_y, dest_pos_x, dest_pos_y, time_appearance, time_delivery):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dest_pos_x = dest_pos_x
        self.dest_pos_y = dest_pos_y
        self.time_appearance = time_appearance
        self.time_delivery = time_delivery
        self.agent = None

    def __copy__(self):
        return Package(self.pos_x, self.pos_y, self.dest_pos_x, self.dest_pos_y, self.time_appearance, self.time_delivery)

    def remove_self_from_env(self, env):
        if self.agent:
            self.agent.remove_package()
            self.agent = None
        else:
            env[self.pos_x][self.pos_y].remove_package()

    def add_self_to_env(self, env):
        env.graph[self.pos_x][self.pos_y].add_package(self)

    def get_delivery_x_y(self):
        return self.dest_pos_x, self.dest_pos_y
