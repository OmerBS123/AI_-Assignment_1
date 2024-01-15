from Assigment_1.infra_libarrys.consts_and_enums.gui_consts import GuiColorConsts
from Assigment_1.infra_libarrys.infra_classes.Agent.Agent import Agent
from Assigment_1.infra_libarrys.consts_and_enums.agents_consts import AgentConsts
from Assigment_1.infra_libarrys.consts_and_enums.agents_consts import AgentName


class InterferingAgent(Agent):
    def __init__(self, curr_node, env):
        super().__init__(curr_node, env)
        self.agent_type = AgentName.INTERFERING
        self.tag = AgentConsts.INTERFERING_AGENT_FLAG
        self.agent_color = GuiColorConsts.RED

    def run_agent_step(self):
        pass #TODO: looks for the closet fragile edge