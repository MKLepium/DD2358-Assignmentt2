"""
Test DFT
"""

import pytest
import dft



def test_DFT():
    """
    test DFT
    """
    import math
    xr = [1, 2, 3, 4]
    xi = [0, 0, 0, 0]
    N = len(xr)
    Xr_o = [0] * N
    Xi_o = [0] * N

    dft.dft(xr, xi, Xr_o, Xi_o, N)
    expected_Xr_o = [10, -2, -2, -2]
    expected_Xi_o = [0.0, 2, 0, -2]
    for i in range(N):
        assert math.isclose(Xr_o[i], expected_Xr_o[i], abs_tol=1e-6)
        assert math.isclose(Xi_o[i], expected_Xi_o[i], abs_tol=1e-6)
