from typing import Union, List
from enum import Enum

import numpy as np
import scipy.sparse as sp
import networkx as nx


class Partition(Enum):
    greedy_communities = "greedy_communities"
    louvain_communities = "louvain_communities"



class NaiveGraphDecomposer:
    """
    Use a simple and efficient tool from NetworkX to partition a Qubo.
    """
    def __init__(self, qubo: Union[np.ndarray, sp.spmatrix, dict]):

        self._qubo = qubo
        self._graph_qubo = None

    @property
    def qubo(self):
        return self._qubo

    @property
    def graph_qubo(self):
        return self._graph_qubo

    @graph_qubo.setter
    def graph_qubo(self, val):
        self._graph_qubo = val

    def qubu_to_graph(self) -> nx.Graph:
        if isinstance(self.qubo, np.ndarray):
            return nx.from_numpy_array(self.qubo)
        elif isinstance(self.qubo, sp.spmatrix):
            return nx.from_scipy_sparse_array(self.qubo)
        elif isinstance(self.qubo, dict):
            raise NotImplementedError("dict conversion not implemented yet")
        else:
            raise ValueError(f"type {type(self.qubo)} not allowed")

    def partition_qubo(self, partition_algo="greedy_community") -> List:

        self.graph_qubo = self.qubu_to_graph()

        # TODO: should we check for connectedness?

        if partition_algo == Partition.greedy_communities:
            parts = nx.community.greedy_modularity_communities(graph_qubo)
        elif partition_algo == Partition.louvain_communities:
            parts = nx.community.louvain_communities(graph_qubo)
        else:
            raise ValueError("unknown partition algorithm")

        return parts

    def get_cut_edges(self, parts):
        """
        Determine which edges were cut.
        """
        pass