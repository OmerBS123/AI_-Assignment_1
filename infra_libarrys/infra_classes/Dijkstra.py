import heapq

from infra_libarrys.infra_classes.DistanceNodeWrapper import DistanceNodeWrapper


class Dijkstra:
    def __init__(self, start_node, grid):
        self.start_node = start_node
        self.destination_node = None
        self.grid = grid
        self.distances = {node: float('inf') for node in self.grid.nodes}
        self.previous = {node: None for node in self.grid.nodes}
        self.heap = []
        self.nodes_with_package = [node for node in self.grid.nodes if node.package is not None]

    def run_dijkstra(self):
        if not self.nodes_with_package:
            return None

        heapq.heappush(self.heap, DistanceNodeWrapper(0, self.start_node))

        self.distances[self.start_node] = 0

        while self.heap:
            current_distance, current_node = heapq.heappop(self.heap).pair

            # Explore neighbors
            for edge in current_node.edges:
                neighbor_node = edge.get_neighbor_node(current_node)
                new_distance = self.distances[current_node] + edge.weight

                if new_distance < self.distances[neighbor_node]:
                    self.distances[neighbor_node] = new_distance
                    self.previous[neighbor_node] = current_node
                    heapq.heappush(self.heap, DistanceNodeWrapper(new_distance, neighbor_node))

        self.destination_node = self.get_min_dist_package_node()

        shortest_path = self.get_shortest_path()

        return shortest_path

    def get_min_dist_package_node(self):
        return min(self.nodes_with_package, key=lambda node: self.distances[node])

    def get_shortest_path(self):
        path = []
        current_node = self.destination_node

        while current_node:
            path.append(current_node)
            current_node = self.previous[current_node]

        return list(reversed(path))
