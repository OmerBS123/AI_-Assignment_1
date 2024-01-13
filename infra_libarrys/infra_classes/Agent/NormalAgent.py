from infra_libarrys.infra_classes.Agent.Agent import Agent
from infra_libarrys.consts_and_enums.agents_consts import AgentConsts
from infra_libarrys.infra_classes.SearchAlgorithem.Dijkstra import Dijkstra


class NormalAgent(Agent):
    def __init__(self, curr_node, env):
        super().__init__(curr_node, env)
        self.tag = AgentConsts.NORMAL_AGENT_FLAG

    def run_agent_step(self):
        run_search = self.finish_crossing_with_curr_edge()
        if not run_search:
            return

        search_algo = self.get_search_algo()
        next_node = self.get_next_node_from_search_algo(search_algo)
        edge_to_pass = self.curr_node.get_edge_from_node(next_node)
        self.step_over_edge(edge_to_pass)

    @staticmethod
    def get_next_node_from_search_algo(search_algo):
        path = search_algo.run_search()
        node = path[1]
        return node

    def get_search_algo(self):
        if self.package is not None:
            destination_node = self.env.graph[self.package.dest_pos_x][self.package.dest_pos_y]
            dijkstra_algo = Dijkstra(start_node=self.curr_node, env=self.env, destination_node=destination_node)
        else:
            dijkstra_algo = Dijkstra(start_node=self.curr_node, env=self.env)
        return dijkstra_algo
