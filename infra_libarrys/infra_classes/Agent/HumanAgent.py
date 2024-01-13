from infra_libarrys.infra_classes.Agent.Agent import Agent
from infra_libarrys.consts_and_enums.agents_consts import AgentConsts


class HumanAgent(Agent):
    def __init__(self, curr_node, env):
        super().__init__(curr_node, env)
        self.tag = AgentConsts.HUMAN_AGENT_FLAG

    def run_agent_step(self):
        pass
