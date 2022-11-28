import numpy as np
import math
from tabulate import tabulate


class primal_matrix:
    arr = []
    linha_pivot = None
    coluna_pivot = None

    variaveis = None
    restricoes = None
    linha_objetivo = None
    coluna_resultado = None

    def __init__(self, variaveis, restricoes) -> None:
        self.variaveis = variaveis
        self.restricoes = restricoes
        self.monut_arr()
        self.linha_objetivo = len(self.arr) - 1
        self.coluna_resultado = len(self.arr[self.linha_objetivo]) - 1
        self.headers=[]
        for i in range(variaveis) :
            self.headers.append('x%d' % i)
        for i in range(restricoes) :
            self.headers.append('f%d' % i)
        self.headers.append('s')
        pass

    def divide_rounded(self, a, b):
        if (b == 0):
            return 0
        if (a != 0):
            return round(a / b, 3)
        return 0

    def print(self):
        print('--------------------------------------------------')
        print('Matrix')
        print(tabulate(self.arr, self.headers))
        print('--------------------------------------------------')
        print('Coluna Pivot_id')
        print(self.coluna_pivot)
        print('--------------------------------------------------')
        print('Linha Pivot_id')
        print(self.linha_pivot)

    def monut_arr(self) -> list:
        self.arr = np.zeros(
            shape=(self.restricoes+1, self.variaveis + self.restricoes + 1), dtype=float)
        return self.arr

    def set_restricao(self, restricao, valores, resultado):
        self.arr[restricao, self.coluna_resultado] = resultado
        self.arr[restricao, self.variaveis + restricao] = 1
        for coluna in range(self.variaveis):
            self.arr[restricao, coluna] = valores[coluna]
        return

    def set_fun_objetivo(self, valores):
        for coluna in range(self.variaveis):
            self.arr[self.linha_objetivo, coluna] = valores[coluna]
        return

    def get_coluna_pivot(self) -> int | None:
        menor_valor = math.inf
        self.coluna_pivot = None
        for coluna in range(self.variaveis):
            elemento = self.arr[self.linha_objetivo, coluna]
            if (elemento < menor_valor and elemento < 0):
                self.coluna_pivot = coluna
                menor_valor = elemento
        return self.coluna_pivot

    def get_elemento_pivot(self) -> tuple[bool, int, int, int]:
        linha_pivot_id = None
        coluna_pivot_id = self.get_coluna_pivot()

        if (coluna_pivot_id != None):
            menor_valor = math.inf

            for linha in range(self.restricoes):
                menor_tmp = self.divide_rounded(self.arr[linha, self.coluna_resultado],
                                                self.arr[linha, coluna_pivot_id])

                if (menor_tmp < menor_valor and menor_tmp > 0):
                    menor_valor = menor_tmp
                    linha_pivot_id = linha

            return True, linha_pivot_id,  coluna_pivot_id,  self.arr[linha_pivot_id, coluna_pivot_id]
        return False, 0,  0,  0

    def update_linha_pivot(self) -> list:
        status, linha_pivot, coluna_pivot, valor_pivot = self.get_elemento_pivot()
        if (status):
            self.linha_pivot = linha_pivot

            for coluna in range(len(self.arr[linha_pivot])):
                self.arr[linha_pivot, coluna] = self.divide_rounded(self.arr[linha_pivot, coluna],
                                                                    valor_pivot)
            return self.arr[linha_pivot]
        return False

    def update_linha(self, linha):
        coeficiente = self.arr[linha, self.coluna_pivot] * -1
        for coluna in range(len(self.arr[linha])):
            self.arr[linha, coluna] += (
                self.arr[self.linha_pivot, coluna] * coeficiente)
        return

    def executa_primal(self):
        self.print()
        self.update_linha_pivot()
        iteracoes = 0
        while (self.get_coluna_pivot() != None):
            iteracoes += 1
            print('--------------------------------------------------')
            print('Iteração Atual: ')
            print(iteracoes)
            for linha in range(self.restricoes+1):
                print('--------------------------------------------------')
                print('Linha Atual: ')
                print(linha)
                if (linha != self.linha_pivot):
                    self.print()
                    self.update_linha(linha)
            self.update_linha_pivot()
            self.print()
        return

    def get_solucoes(self):
        solucao = []
        variaveis = np.zeros(shape=(self.variaveis), dtype=float)
        for coluna_variavel in range(self.variaveis):
            resultado = 0
            for linha in range(self.restricoes):
                if (self.arr[linha, coluna_variavel] == 1):
                    resultado = self.arr[linha,
                                         self.coluna_resultado]
                if (self.arr[linha, coluna_variavel] != 1 and self.arr[linha, coluna_variavel] != 0):
                    resultado = 0
            variaveis[coluna_variavel] = resultado

        restricoes = np.zeros(shape=(self.restricoes), dtype=float)
        for coluna_restricao in range(self.restricoes):
            coluna = coluna_restricao + self.variaveis
            resultado = 0
            for linha in range(self.restricoes):
                if (self.arr[linha, coluna] == 1):
                    resultado = 1
                if (self.arr[linha, coluna] != 1 and self.arr[linha, coluna] != 0):
                    resultado = 0
            restricoes[coluna_restricao] = resultado

        solucao.append(variaveis)
        solucao.append(restricoes)
        solucao.append(
            [self.arr[self.linha_objetivo, self.coluna_resultado]])

        return solucao
