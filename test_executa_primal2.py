import pytest
from app.primal_matrix import primal_matrix
import numpy as np


class TestExecutaPrimal:
    arr = primal_matrix(2, 3)

    def assert_matrix(self, given, expected):
        assert len(given) is len(expected)

        for linha in range(len(expected)):
            assert len(given[linha]) is len(expected[linha])
            np.testing.assert_almost_equal(given[linha], expected[linha])

    def test_create_new_matrix(self):

        self.arr.set_restricao(0, [6, 4], 30)
        self.arr.set_restricao(1, [1, 0], 1)
        self.arr.set_restricao(2, [0, 1], 2)
        self.arr.set_fun_objetivo([-150, -104])

        array_esperado = [
            [30, 6, 1, 0, 0, 30],
            [1, 1, 0, 1, 0, 1],
            [6, 0, 0, 0, 1, 2],
            [-150, -104, 0, 0, 0, 0],
        ]
        # self.arr.set_restricao(0, [30, 6], 30)
        # self.arr.set_restricao(1, [1, 1], 1)
        # self.arr.set_restricao(2, [6, 0], 2)
        # self.arr.set_fun_objetivo([-150, -104])

        # array_esperado = [
        #     [30, 6, 1, 0, 0, 30],
        #     [1, 1, 0, 1, 0, 1],
        #     [6, 0, 0, 0, 1, 2],
        #     [-150, -104, 0, 0, 0, 0],
        # ]

        # self.assert_matrix(self.arr.arr, array_esperado)

    def test_executa_primal(self):
        self.arr.executa_primal()

        # array_esperado = [
        #     [0, 1, 1.333, 0.667, -0.334, 4],
        #     [1, 0, -0.6665, -0.3335, 0.334, 6],
        #     [0, 0, 2.999, 2.001, 0.668, 92],
        # ]

        # self.assert_matrix(self.arr.arr, array_esperado)

    def test_get_solucoes(self):
        solucoes = self.arr.get_solucoes()
        array_esperado = [
            [1, 6],
            [0, 0, 0],
            [774],
        ]
        self.assert_matrix(solucoes, array_esperado)
