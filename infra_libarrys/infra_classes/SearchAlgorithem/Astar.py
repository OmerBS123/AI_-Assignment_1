import heapq

from infra_libarrys.infra_classes.SearchAlgorithem.SearchAlgorithm import SearchAlgorithm


class Astar(SearchAlgorithm):
    def __init__(self, start_node, original_env, destination_node=None):
        super().__init__(start_node=start_node, env=original_env, destination_node=destination_node)
        self.open_nodes = [self.start_node]
        self.closed_nodes = set()

    def run_search(self):
        while True:
            if not self.open_nodes:
                return None
            curr_node = heapq.heappop(self.open_nodes)
            if curr_node.state.is_goal():
                return curr_node
            same_state_node = self.get_same_state_node(curr_node)
            if same_state_node is not None and curr_node.calculate_f() < same_state_node.calculate_f():
                self.closed_nodes.remove(same_state_node)
                self.closed_nodes.add(curr_node)
                # TODO: expand and add nodes

    def get_same_state_node(self, node):
        state_singleton = {node.state == curr_node.state for curr_node in self.closed_nodes}
        if state_singleton:
            return state_singleton.pop()
        return None
