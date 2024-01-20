import heapq
from copy import copy

from infra_libarrys.infra_classes.Mst import Mst
from infra_libarrys.infra_classes.State import State


class AstarNodeWrapper:
    def __init__(self, state, parent_node, g, h, prev_action):
        self.state = state
        self.parent_node = parent_node
        self.g = g
        self.h = h
        self.prev_action = prev_action
        self.children = set()

    def __lt__(self, other):
        return self.calculate_f() < other.calculate_f()

    def calculate_f(self):
        return self.g + self.h

    def expand(self):
        new_node_list = []
        for curr_edge in self.state.curr_node.edges:
            g = self.g + curr_edge.weight
            parent_node = self
            new_state = self.create_state_from_edge(curr_edge)
            previous_action = curr_edge
            h = self.get_h_for_state(new_state)
            new_node = AstarNodeWrapper(state=new_state, parent_node=parent_node, g=g, prev_action=previous_action, h=h)
            new_node_list.append(new_node)

    def create_state_from_edge(self, edge):
        copy_env = copy(self.state.env)
        new_time = self.state.time + edge.weight
        x, y = self.state.curr_node.get_x_y_coordinate()
        new_curr_node = copy_env.graph[x][y]
        new_state = State(copy_env, curr_node=new_curr_node, time=new_time)
        new_state.update_state(old_edge=edge)
        return new_state

    @staticmethod
    def get_h_for_state(state):
        clique = state.env.create_clique()
        mst = Mst(clique)
        mst.create_mst()
        return mst.get_mst_weight()
