from typing import Union

import numpy as np
import scipy.sparse as sp

import dimod
from dwave_qbsolv import QBSolv

from utils import (
    convert_qubo_to_dict
)


class QBSolver:

    def __init__(self):

        self.qbsolv = QBSolv()

        self._qubo = None
        self._response = None

    @property
    def qubo(self):
        return self._qubo

    @qubo.setter
    def qubo(self, value):
        self._qubo = value

    def sample_qubo_array(
            self,
            qubo: Union[np.ndarray, sp.spmatrix],
            **params
    ):
        self.qubo = convert_qubo_to_dict(qubo)
        return self.qbsolv.sample_qubo(self.qubo, **params)
