import numpy as np
import pandas as pd
import math


class primal_matrix:
    array_primal = []
    variaveis = None
    restricoes = None
    linha_objetivo = None
    coluna_resultado = None

    def __init__(self) -> None:
        self.get_qtds()
        self.monut_array_primal()
        self.linha_objetivo = len(self.array_primal) - 1
        self.coluna_resultado = len(self.array_primal[self.linha_objetivo]) - 1
        self.popula_array_primal()
        print(self.array_primal)
        pass

    def get_qtds(self):
        self.variaveis = int(input("Escreva a quantidade de self.variaveis: "))
        self.restricoes = int(
            input("Escreva a quantidade de self.restricoes: "))
        return [self.variaveis, self.restricoes]

    def monut_array_primal(self):
        self.array_primal = np.zeros(
            shape=(self.restricoes+1, self.variaveis + self.restricoes + 1), dtype=int)
        return self.array_primal

    def popula_array_primal(self):

        for linha in range(self.restricoes):
            self.array_primal[linha, self.variaveis + linha] = 1
            for coluna in range(self.variaveis):
                self.array_primal[linha, coluna] = int(
                    input("Insira o valor da restrição " + str(linha)+" e variavel " + str(coluna) + ": "))
            self.array_primal[linha, self.coluna_resultado] = int(
                input("Insira o resultado da restrição " + str(linha) + ": "))

        # recebendo função objetivo
        for coluna in range(self.variaveis):
            self.array_primal[self.linha_objetivo, coluna] = int(
                input("Insira o valor do coeficiente " + str(coluna)+" da função objetivo: "))
        self.array_primal[self.linha_objetivo, self.coluna_resultado] = int(
            input("Insira o resultado da função objetivo " + str(self.linha_objetivo) + ": "))

        return True

    def get_coluna_pivot(self):
        menor_valor = math.inf
        menor_id = False
        for coluna in range(self.variaveis):
            elemento = self.array_primal[self.linha_objetivo, coluna]
            if (elemento < menor_valor and elemento < 0):
                menor_id = coluna
                menor_valor = elemento
        return menor_id

    def get_elemento_pivot(self):
        menor_id = self.restricoes
        coluna_pivot = self.get_coluna_pivot()
        if (not coluna_pivot):
            return False

        menor_valor = math.inf
        for linha in range(self.restricoes):
            menor_tmp = self.array_primal[linha, self.coluna_resultado] / \
                self.array_primal[linha, coluna_pivot]
            if (menor_tmp < menor_valor and menor_valor > 0):
                menor_valor = menor_tmp
                menor_id = linha
        return {"linha_pivot": menor_id, "coluna_pivot": coluna_pivot, "valor_pivot": menor_valor}
