from infra_libarrys.infra_classes.Agent.Agent import Agent
from infra_libarrys.consts_and_enums.agents_consts import AgentConsts


class InterferingAgent(Agent):
    def __init__(self, starting_node, grid):
        super().__init__(starting_node, grid)
        self.tag = AgentConsts.INTERFERING_AGENT_FLAG

    def run_agent_step(self):
        pass #TODO: looks for the closet fragile edge