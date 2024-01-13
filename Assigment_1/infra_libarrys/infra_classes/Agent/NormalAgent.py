from infra_libarrys.infra_classes.Agent.Agent import Agent
from infra_libarrys.consts_and_enums.agents_consts import AgentConsts


class NormalAgent(Agent):
    def __init__(self, curr_node, env):
        super().__init__(curr_node, env)
        self.tag = AgentConsts.NORMAL_AGENT_FLAG

    def run_agent_step(self):
        if self.package is not None:
            pass

    def run_dijkstra_to_package(self):
        pass

    def run_dijkstra_to_delivery(self):
        pass