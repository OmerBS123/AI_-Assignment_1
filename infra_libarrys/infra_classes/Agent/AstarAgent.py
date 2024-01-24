from infra_libarrys.consts_and_enums.agents_consts import AgentName, AgentConsts
from infra_libarrys.consts_and_enums.gui_consts import GuiColorConsts
from infra_libarrys.infra_classes.Agent.Agent import Agent
from infra_libarrys.infra_classes.SearchAlgorithem.Astar import Astar
from infra_libarrys.infra_classes.State import State
from infra_libarrys.infra_classes.Wrappers.AstarNodeWrapper import AstarNodeWrapper


class AstarAgent(Agent):
    def __init__(self, curr_node, env):
        super().__init__(curr_node, env)
        self.agent_type = AgentName.ASTAR
        self.tag = AgentConsts.ASTAR_AGENT_FLAG
        self.agent_color = GuiColorConsts.SILVER
        self.actions_stack = self.get_actions_stack()

    def get_actions_stack(self):
        search_algo = self.get_search_algo()
        return search_algo.run_search()

    def get_next_step(self):
        if not self.actions_stack:
            return None
        return self.actions_stack.pop()

    def get_search_algo(self):
        start_state = State(env=self.env, curr_node=self.curr_node, time=AgentConsts.AGENT_START_TIME)
        h = AstarNodeWrapper.get_h_for_state(start_state)
        first_a_star_node = AstarNodeWrapper(state=start_state, parent_node=None, g=AgentConsts.G_INITIAL_VALUE, h=h)
        a_star_algo = Astar(start_node=first_a_star_node, original_env=self.env)
        return a_star_algo

    def run_agent_step(self):
        make_next_step = self.finish_crossing_with_curr_edge()
        if not make_next_step:
            return
        self.drop_package_if_possible()
        next_edge = self.get_next_step()
        if next_edge is None:
            return
        self.step_over_edge(next_edge)
