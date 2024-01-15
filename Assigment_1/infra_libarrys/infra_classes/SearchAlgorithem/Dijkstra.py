import heapq

from Assigment_1.infra_libarrys.infra_classes.DistanceNodeWrapper import DistanceNodeWrapper
from Assigment_1.infra_libarrys.infra_classes.SearchAlgorithem.SearchAlgorithm import SearchAlgorithm


class Dijkstra(SearchAlgorithm):
    def __init__(self, start_node, env, destination_node=None):
        super().__init__(start_node, env, destination_node=destination_node)
        self.distances = {node: float('inf') for node in self.env.nodes}
        self.previous = {node: None for node in self.env.nodes}
        self.heap = []
        self.nodes_with_package = [node for node in self.env.nodes if node.package is not None]

    def run_search(self):
        if not self.nodes_with_package and self.destination_node is None:
            return None

        heapq.heappush(self.heap, DistanceNodeWrapper(0, self.start_node))

        self.distances[self.start_node] = 0

        while self.heap:
            node_wrapper = heapq.heappop(self.heap)
            current_distance, current_node = node_wrapper.distance, node_wrapper.node

            for edge in current_node.edges:
                neighbor_node = edge.get_neighbor_node(current_node)
                new_distance = self.distances[current_node] + edge.weight

                if new_distance < self.distances[neighbor_node]:
                    self.distances[neighbor_node] = new_distance
                    self.previous[neighbor_node] = current_node
                    heapq.heappush(self.heap, DistanceNodeWrapper(new_distance, neighbor_node))

        if self.destination_node is None:
            self.destination_node = self.get_min_distance_package_node()

        shortest_path = self.get_shortest_path()

        return shortest_path

    def get_min_distance_package_node(self):
        return min(self.nodes_with_package, key=lambda node: self.distances[node])

    def get_shortest_path(self):
        path = []
        current_node = self.destination_node

        while current_node:
            path.append(current_node)
            current_node = self.previous[current_node]

        return list(reversed(path))
