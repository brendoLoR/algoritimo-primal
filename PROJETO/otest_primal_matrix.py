import pytest
from app.primal_matrix import primal_matrix
import numpy as np


class TestPrimalMatrix:
    array_primal = primal_matrix(2, 2)

    def assert_matrix(self, given, expected):
        assert len(given) is len(expected)

        for linha in range(len(expected)):
            assert len(given[linha]) is len(expected[linha])
            np.testing.assert_almost_equal(given[linha], expected[linha])

    def test_create_primal_array(self):
        array_esperado = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.assert_matrix(self.array_primal.array_primal, array_esperado)

    def test_insert_variable_value(self):
        self.array_primal.set_restricao(0, [1, 2], 3)

        array_esperado = [
            [1, 2, 1, 0, 3],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.assert_matrix(self.array_primal.array_primal, array_esperado)
        self.array_primal.set_restricao(1, [4, 5], 6)

        array_esperado = [
            [1, 2, 1, 0, 3],
            [4, 5, 0, 1, 6],
            [0, 0, 0, 0, 0],
        ]

        self.assert_matrix(self.array_primal.array_primal, array_esperado)

    def test_insert_funcao_objetivo(self):
        self.array_primal.set_fun_objetivo([-7, -8])

        array_esperado = [
            [1, 2, 1, 0, 3],
            [4, 5, 0, 1, 6],
            [-7, -8, 0, 0, 0],
        ]

        self.assert_matrix(self.array_primal.array_primal, array_esperado)

    def test_get_coluna_pivot(self):
        coluna_pivot = self.array_primal.get_coluna_pivot()
        assert coluna_pivot == 1

    def test_get_elemento_pivot(self):
        status, menor_id,  coluna_pivot,  menor_valor = self.array_primal.get_elemento_pivot()
        assert status
        assert menor_id == 1
        assert coluna_pivot == 1
        assert menor_valor == 1.2

    def test_mudando_fun_objetivo(self):
        self.array_primal.set_fun_objetivo([-8, -7])

        array_esperado = [
            [1, 2, 1, 0, 3],
            [4, 5, 0, 1, 6],
            [-8, -7, 0, 0, 0],
        ]

        self.assert_matrix(self.array_primal.array_primal, array_esperado)

    def test_get_elemento_pivot_fun_objetivo_mudada(self):
        status, menor_id,  coluna_pivot,  menor_valor = self.array_primal.get_elemento_pivot()
        assert status
        assert menor_id == 1
        assert coluna_pivot == 0
        assert menor_valor == 1.5

    def test_update_linha_pivot(self):
        self.array_primal.update_linha_pivot()

        array_esperado = [
            [1, 2, 1, 0, 3],
            [1, 3.333, 0, 0.667, 4],
            [-8, -7, 0, 0, 0],
        ]

        self.assert_matrix(self.array_primal.array_primal, array_esperado)

    def test_update_linha0(self):
        linha = 0
        self.array_primal.update_linha(linha)

        array_esperado = [
            [0, -1.333, 1, -0.667, -1],
            [1, 3.333, 0, 0.667, 4],
            [-8, -7, 0, 0, 0],
        ]

        self.assert_matrix(self.array_primal.array_primal, array_esperado)

    def test_update_linha2(self):
        linha = 2
        self.array_primal.update_linha(linha)

        array_esperado = [
            [0, -1.333, 1, -0.667, -1],
            [1, 3.333, 0, 0.667, 4],
            [0, 19.664, 0, 5.336, 32],
        ]

        self.assert_matrix(self.array_primal.array_primal, array_esperado)

   