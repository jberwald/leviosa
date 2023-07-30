import numpy as np

def array2dict(arr: np.ndarray) -> dict:
    assert arr.shape[0] == arr.shape[1], "arr must be square"
    assert np.all(arr == arr.T), "arr must be symmetric"
    d = {}
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            d[i,j] = arr[i,j]
    return d


def compute_energy(qubo, soln_vec):
    return soln_vec.T @ qubo @ soln_vec


def adjust_offdiag_param(qubo_arr, alpha: float) -> np.ndarray:
    """Perturb off-diagonal elements"""
    param = alpha * np.ones(qubo_arr.shape)
    np.fill_diagonal(param, 0)
    return qubo_arr + param
    