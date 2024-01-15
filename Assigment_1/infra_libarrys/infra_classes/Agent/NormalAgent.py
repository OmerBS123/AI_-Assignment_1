from Assigment_1.infra_libarrys.consts_and_enums.gui_consts import GuiColorConsts
from Assigment_1.infra_libarrys.infra_classes.Agent.Agent import Agent
from Assigment_1.infra_libarrys.consts_and_enums.agents_consts import AgentConsts
from Assigment_1.infra_libarrys.infra_classes.SearchAlgorithem.Dijkstra import Dijkstra
from Assigment_1.infra_libarrys.consts_and_enums.agents_consts import AgentName


class NormalAgent(Agent):
    def __init__(self, curr_node, env):
        super().__init__(curr_node, env)
        self.agent_type = AgentName.NORMAL
        self.tag = AgentConsts.NORMAL_AGENT_FLAG
        self.agent_color = GuiColorConsts.GREEN

    def run_agent_step(self):
        run_search = self.finish_crossing_with_curr_edge()
        if not run_search:
            return
        self.drop_package_if_possible()
        search_algo = self.get_search_algo()

        next_node = self.get_next_node_from_search_algo(search_algo)
        if next_node is None:
            return
        elif next_node == self.curr_node:  # if curr node is both dest and pickup
            self.pickup_package_if_exists()
        else:
            edge_to_pass = self.curr_node.get_edge_from_node(next_node)
            self.step_over_edge(edge_to_pass)

    @staticmethod
    def get_next_node_from_search_algo(search_algo):
        path = search_algo.run_search()
        if path is None:
            return None
        elif len(path) == 1:
            node = path[0]
        else:
            node = path[1]
        return node

    def get_search_algo(self):
        if self.package is not None:
            destination_node = self.env.graph[self.package.dest_pos_x][self.package.dest_pos_y]
            dijkstra_algo = Dijkstra(start_node=self.curr_node, env=self.env, destination_node=destination_node)
        else:
            dijkstra_algo = Dijkstra(start_node=self.curr_node, env=self.env)
        return dijkstra_algo

    def finish_crossing_with_curr_edge(self):
        if self.time_left_to_cross_edge > 0:
            self.time_left_to_cross_edge -= 1
            if self.time_left_to_cross_edge == 0:
                self.curr_node = self.curr_crossing_edge.get_neighbor_node(self.curr_node)
                self.curr_crossing_edge = None
                if self.package is None:
                    self.pickup_package_if_exists()
            return False
        return True

    def pickup_package_if_exists(self):
        if self.curr_node.package is not None:
            self.package = self.curr_node.package
            self.curr_node.remove_package()

    def drop_package_if_possible(self):
        if self.package is None:
            return
        if self.curr_node.is_node_destination(self.package):
            self.package = None
            self.score += 1
