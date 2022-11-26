import pytest
from app.dual_matrix import dual_matrix
import numpy as np


class TestExecutadual:
    arr = dual_matrix(3, 2)

    def assert_matrix(self, given, expected):
        assert len(given) is len(expected)

        for linha in range(len(expected)):
            assert len(given[linha]) is len(expected[linha])
            np.testing.assert_almost_equal(given[linha], expected[linha])

    def test_create_new_matrix(self):

        self.arr.set_restricao(0, [-2, 4, 1], 2)
        self.arr.set_restricao(1, [4, -2, -3], -1)
        self.arr.set_fun_objetivo([2, 6, 10])

        array_esperado = [
            [-2, 4, 1, 1, 0, 2],
            [4, -2, -3, 0, 1, -1],
            [2, 6, 10, 0, 0, 0],
        ]

        self.assert_matrix(self.arr.arr, array_esperado)

    def test_get_linha_pivot(self):
        assert self.arr.get_linha_pivot() == 1

    def test_get_coluna_pivot(self):
        assert self.arr.get_coluna_pivot() == 1

    def test_get_elemento_pivot(self):
        status, linha_pivot, coluna_pivot, valor_pivot = self.arr.get_elemento_pivot()
        assert status
        assert linha_pivot == 1
        assert coluna_pivot == 1
        assert valor_pivot == -2

    def test_update_linha(self):
        self.arr.update_linha(0)

        array_esperado = [
            [6, 0, -5, 1, 2, 0],
            [4, -2, -3, 0, 1, -1],
            [2, 6, 10, 0, 0, 0],
        ]

        self.assert_matrix(self.arr.arr, array_esperado)

    def test_executa_dual(self):
        self.arr.executa_dual()

        array_esperado = [
            [6, 0, -5, 1, 2, 0],
            [-2, 1, 3/2, 0, -1/2, 1/2],
            [14, 0, 1, 0, 3, -3],
        ]

        self.assert_matrix(self.arr.arr, array_esperado)

    # def test_get_solucoes(self):
    #     solucoes = self.arr.get_solucoes()
    #     array_esperado = [
    #         [0, 1/2, 0],
    #         [1, 0],
    #         [-3],
    #     ]
    #     self.assert_matrix(solucoes, array_esperado)
