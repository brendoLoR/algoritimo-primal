import numpy as np
import pandas as pd
import math


class primal_matrix:
    array_primal = []
    linha_pivot = None
    coluna_pivot = None

    variaveis = None
    restricoes = None
    linha_objetivo = None
    coluna_resultado = None

    def __init__(self, variaveis, restricoes) -> None:
        self.variaveis = variaveis
        self.restricoes = restricoes
        self.monut_array_primal()
        self.linha_objetivo = len(self.array_primal) - 1
        self.coluna_resultado = len(self.array_primal[self.linha_objetivo]) - 1
        print(self.array_primal)
        pass

    def monut_array_primal(self) -> list:
        self.array_primal = np.zeros(
            shape=(self.restricoes+1, self.variaveis + self.restricoes + 1), dtype=float)
        return self.array_primal

    def set_restricao(self, restricao, valores, resultado):
        self.array_primal[restricao, self.coluna_resultado] = resultado
        self.array_primal[restricao, self.variaveis + restricao] = 1
        for coluna in range(self.variaveis):
            self.array_primal[restricao, coluna] = valores[coluna]
        return

    def set_fun_objetivo(self, valores):
        for coluna in range(self.variaveis):
            self.array_primal[self.linha_objetivo, coluna] = valores[coluna]
        return

    def get_coluna_pivot(self) -> int:
        menor_valor = math.inf
        self.coluna_pivot = None
        for coluna in range(self.variaveis):
            elemento = self.array_primal[self.linha_objetivo, coluna]
            if (elemento < menor_valor and elemento < 0):
                self.coluna_pivot = coluna
                menor_valor = elemento
        return self.coluna_pivot

    def get_elemento_pivot(self):
        linha_pivot_id = None
        coluna_pivot = self.get_coluna_pivot()
        if(coluna_pivot != None):
            menor_valor = math.inf
            for linha in range(self.restricoes):
                menor_tmp = self.array_primal[linha, self.coluna_resultado] / \
                    self.array_primal[linha, coluna_pivot]
                if (menor_tmp < menor_valor and menor_valor > 0):
                    menor_valor = menor_tmp
                    linha_pivot_id = linha
            return linha_pivot_id,  coluna_pivot,  menor_valor
        return False

    def update_linha_pivot(self) -> list:
        linha_pivot, coluna_pivot, valor_pivot = self.get_elemento_pivot()
        self.linha_pivot = linha_pivot
        self.array_primal[linha_pivot,
                          coluna_pivot] = valor_pivot
        for coluna in range(len(self.array_primal[linha_pivot])):
            self.array_primal[linha_pivot,
                              coluna] = self.array_primal[linha_pivot, coluna] / valor_pivot
        return self.array_primal[linha_pivot]

    def update_linha(self, linha):
        coeficiente = self.array_primal[linha, self.coluna_pivot] * -1
        for coluna in range(len(self.array_primal[linha])):
            self.array_primal[linha, coluna] += (
                self.array_primal[self.linha_pivot, coluna] * coeficiente)
        return