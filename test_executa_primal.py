import pytest
from app.primal_matrix import primal_matrix
import numpy as np


class TestExecutaPrimal:
    arr = primal_matrix(3, 2)

    def assert_matrix(self, given, expected):
        assert len(given) is len(expected)

        for linha in range(len(expected)):
            assert len(given[linha]) is len(expected[linha])
            np.testing.assert_almost_equal(given[linha], expected[linha])

    def test_create_new_matrix(self):

        self.arr.set_restricao(0, [3, 3, 2], 30)
        self.arr.set_restricao(1, [6, 3, 0], 48)
        self.arr.set_fun_objetivo([-10, -8, -1])

        array_esperado = [
            [3,   3,  2, 1, 0, 30],
            [6,   3,  0, 0, 1, 48],
            [-10, -8, -1, 0, 0, 0],
        ]

        self.assert_matrix(self.arr.arr, array_esperado)

    def test_executa_primal(self):
        self.arr.executa_primal()

        array_esperado = [
            [0, 1, 1.333, 0.667, -0.334, 4],
            [1, 0, -0.6665, -0.3335, 0.334, 6],
            [0, 0, 2.999, 2.001, 0.668, 92],
        ]

        self.assert_matrix(self.arr.arr, array_esperado)

    def test_get_solucoes(self):
        solucoes = self.arr.get_solucoes()
        array_esperado = [
            [6, 4, 0],
            [0, 0],
            [92],
        ]
        self.assert_matrix(solucoes, array_esperado)