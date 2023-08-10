from typing import Union

import numpy as np
import scipy.sparse as sp


def convert_qubo_to_dict(qubo: Union[np.ndarray, sp.sparse]) -> dict:
    assert qubo.shape[0] == qubo.shape[1], "arr must be square"
    # TODO: check for symmetry
    qubo_ = {}
    if isinstance(qubo, np.ndarray):
        for i in range(qubo.shape[0]):
            for j in range(qubo.shape[1]):
                qubo_[i, j] = qubo[i, j]
    elif isinstance(qubo, sp.spmatrix):
        qubo = qubo.tocoo()
        row_col = zip(qubo.row, qubo.col)
        data = qubo.data
        for ij, val in zip(row_col, data):
            qubo_[ij] = val
    else:
        raise ValueError("Unknown data type, must pass an ndarray or sparse matrix.")
    return qubo_


def compute_energy(qubo, soln_vec):
    return soln_vec.T @ qubo @ soln_vec


def adjust_offdiag_param(qubo_arr, alpha: float) -> np.ndarray:
    """Perturb off-diagonal elements"""
    param = alpha * np.ones(qubo_arr.shape)
    np.fill_diagonal(param, 0)
    return qubo_arr + param
    