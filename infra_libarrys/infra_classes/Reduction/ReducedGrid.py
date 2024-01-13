from infra_libarrys.infra_classes.Reduction.ReducedEdge import ReducedEdge
from infra_libarrys.infra_classes.Reduction.ReducedNode import ReducedNode
from itertools import combinations


class ReducedGrid:
    def __init__(self, original_grid):
        self.width = original_grid.width
        self.height = original_grid.height
        # self.graph = [[Node(x, y) for y in range(height + 1)] for x in range(width + 1)]
        # self.edges_dict = {}

        self.nodes = set()
        self.edges = set()
        self.original_to_reduced_mapping = {}
        self.reduced_to_original_mapping = {}

        for node in original_grid.nodes:
            for edge in node.edges:
                if edge not in self.original_to_reduced_mapping:
                    reduced_node = ReducedNode(edge, package=edge.is_fragile, old_edge=True)
                    self.original_to_reduced_mapping[edge] = reduced_node
                    self.reduced_to_original_mapping[reduced_node] = edge
                    self.nodes.add(reduced_node)

        # Connect ReducedNodes based on original Edges
        for node in original_grid.nodes:
            self.original_to_reduced_mapping[node] = set()
            for left_edge, right_edge in combinations(node.edges, 2):
                left_reduced_node = self.original_to_reduced_mapping[left_edge]
                right_reduced_node = self.original_to_reduced_mapping[right_edge]
                reduced_edge = ReducedEdge(node, left_edge.weight + right_edge.weight)

                left_reduced_node.add_reduced_edge(reduced_edge)
                right_reduced_node.add_reduced_edge(reduced_edge)
                self.original_to_reduced_mapping[node].add(reduced_edge)

    def get_starting_nodes(self, starting_original_node):
        starting_nodes_set = set()
        for reduced_edge in self.original_to_reduced_mapping[starting_original_node]:
            starting_nodes_set |= reduced_edge.nodes
        return starting_nodes_set
