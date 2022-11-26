import math
from app.primal_matrix import primal_matrix


class dual_matrix(primal_matrix):
    arr = []
    linha_pivot = None
    coluna_pivot = None

    variaveis = None
    restricoes = None
    linha_objetivo = None
    coluna_resultado = None

    def __init__(self, variaveis, restricoes) -> None:
        super().__init__(variaveis, restricoes)
        pass

    def get_linha_pivot(self) -> int:
        menor_valor = math.inf
        self.linha_pivot = None
        for linha in range(self.restricoes):
            elemento = self.arr[linha, self.coluna_resultado]
            if (elemento < menor_valor and elemento < 0):
                self.linha_pivot = linha
                menor_valor = elemento
        return self.linha_pivot

    def get_coluna_pivot(self) -> tuple[bool, int, int, int]:
        self.coluna_pivot = None
        if (self.get_linha_pivot() != None):
            menor_valor = math.inf
            for coluna in range(self.restricoes):
                if (self.arr[self.linha_pivot, coluna] < 0):
                    elemento = self.divide_rounded(self.arr[self.linha_objetivo, coluna],
                                                   abs(self.arr[self.linha_pivot, coluna]))
                    if (elemento < menor_valor):
                        self.coluna_pivot = coluna
                        menor_valor = elemento
        return self.coluna_pivot

    def get_elemento_pivot(self) -> tuple[bool, int, int, int]:
        if (self.get_linha_pivot() != None and self.get_coluna_pivot() != None):
            return True, self.linha_pivot, self.coluna_pivot, self.arr[self.linha_pivot, self.coluna_pivot]
        return False, 0, 0, 0

    def update_linha(self, linha):
        coeficiente = self.divide_rounded(self.arr[linha, self.coluna_pivot], abs(
            self.arr[self.linha_pivot, self.coluna_pivot]))
        for coluna in range(len(self.arr[linha])):
            self.arr[linha, coluna] += (
                self.arr[self.linha_pivot, coluna] * coeficiente)
        return

    def update_linha_pivot(self) -> list:
        for coluna in range(len(self.arr[self.linha_pivot])):
            self.arr[self.linha_pivot, coluna] = self.divide_rounded(self.arr[self.linha_pivot, coluna],
                                                                     self.arr[self.linha_pivot, coluna])
        return self.arr[self.linha_pivot]

    def executa_dual(self):
        while (self.get_coluna_pivot() != None):
            for linha in range(self.restricoes+1):
                if (linha != self.linha_pivot):
                    self.update_linha(linha)
            self.update_linha_pivot()
        return
