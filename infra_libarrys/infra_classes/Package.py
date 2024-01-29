class Package:
    def __init__(self, pos_x, pos_y, dest_pos_x, dest_pos_y, time_appearance, time_delivery):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dest_pos_x = dest_pos_x
        self.dest_pos_y = dest_pos_y
        self.time_appearance = time_appearance
        self.time_delivery = time_delivery
        self.agent = None

    def __eq__(self, other):
        cond1 = self.pos_x == other.pos_x and self.pos_y == other.pos_y
        cond2 = self.dest_pos_x == other.dest_pos_x and self.dest_pos_y == other.dest_pos_y
        cond3 = self.time_delivery == other.time_delivery and self.time_appearance == other.time_appearance

        return cond1 and cond2 and cond3

    def __copy__(self):
        return Package(self.pos_x, self.pos_y, self.dest_pos_x, self.dest_pos_y, self.time_appearance, self.time_delivery)

    def __hash__(self):
        return hash((self.pos_x, self.pos_y, self.dest_pos_x, self.dest_pos_y, self.time_appearance, self.time_delivery))

    def remove_self_from_env(self, env):
        if self.agent:
            self.agent.remove_package(self)
            self.agent = None
        else:
            env[self.pos_x][self.pos_y].remove_package(env=env)

    def add_self_to_env(self, env):
        env.graph[self.pos_x][self.pos_y].add_package(self, env=env)

    def get_delivery_x_y(self):
        return self.dest_pos_x, self.dest_pos_y

    def get_pos_x_y(self):
        return self.pos_x, self.pos_y
