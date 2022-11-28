from app.primal_matrix import primal_matrix
from app.dual_matrix import dual_matrix


def primal():
    variaveis = int(input("QTD variáveis: "))
    restricoes = int(input("QTD restrições: "))
    array_primal = primal_matrix(variaveis, restricoes)

    for i in range(restricoes):
        array = input(
            "entre com valores da primeira restrição, separados por virgula: ")
        sol = input("valor da restrição: ")
        array_primal.set_restricao(i, array.replace(" ", "").split(','), sol)
    funObj = input("entre com valores da F.O, separados por virgula: ")
    array_primal.set_fun_objetivo(funObj.replace(" ", "").split(','))

    # array_primal.set_restricao(0, [3, 3, 2], 30)
    # array_primal.set_restricao(1, [6, 3, 0], 48)
    # array_primal.set_fun_objetivo([-10, -8, -1])
    array_primal.executa_primal()

    arraySol = array_primal.get_solucoes()

    for i in range(len(arraySol[0])):
        print("Valor de x"+str(i+1)+": " + str(arraySol[0][i]))

    print("F.O: "+str(arraySol[2][0]))


def dual():
    variaveis = int(input("QTD variáveis: "))
    restricoes = int(input("QTD restrições: "))
    array_primal = dual_matrix(variaveis, restricoes)

    for i in range(restricoes):
        array = input(
            "entre com valores da primeira restrição, separados por virgula: ")
        sol = input("valor da restrição: ")
        array_primal.set_restricao(i, array.replace(" ", "").split(','), sol)
    funObj = input("entre com valores da F.O, separados por virgula: ")
    array_primal.set_fun_objetivo(funObj.replace(" ", "").split(','))

    # array_primal.set_restricao(0, [3, 3, 2], 30)
    # array_primal.set_restricao(1, [6, 3, 0], 48)
    # array_primal.set_fun_objetivo([-10, -8, -1])
    array_primal.executa_dual()

    arraySol = array_primal.get_solucoes()

    print('----------------------------------------------------------------')
    print('Variáveis:')
    for i in range(len(arraySol[0])):
        print("Valor de x"+str(i+1)+": " + str(arraySol[0][i]))

    print('----------------------------------------------------------------')
    print('Restrições (se houver):')

    for i in range(len(arraySol[1])):
        print("Valor da folga f"+str(i+1)+": " + str(arraySol[1][i]))

    print('----------------------------------------------------------------')
    print('Solução de F.O:')

    print("F.O: "+str(arraySol[2][0]))


print("Método simplex")
print("0 - Primal")
print("1 - Dual")
opc = input()

print("ATENÇÃO - MANIPULE OS VALORES ANTES DE INSERIR NO PROGRAMA")
match opc:
    case '0':
        primal()
    case '1':
        dual()
    case '3':

        # QUESTÃO 6
        # arr = dual_matrix(3, 3)
        # arr.set_restricao(0, [-9, -8, -10], -5)
        # arr.set_restricao(1, [-4, -2, -3], -6)
        # arr.set_restricao(2, [-5, -6, -4], -7.6)
        # arr.set_fun_objetivo([8, 9, 7])

        # # QUESTÃO 5
        # arr = dual_matrix(16, 8)
        # arr.set_restricao(0, [-1, -2.10, -1.10, 0, 0, 0,
        #                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0], -20500)
        # arr.set_restricao(1, [0, 0, 0, 0, -0.90, -0.80, -1,
        #                   0, 0, 0, 0, 0, 0, 0, 0, 0], -25300)
        # arr.set_restricao(2, [0, 0, 0, 0, 0, 0, 0, 0, -
        #                   1.80, -0.70, -1.20, 0, 0, 0, 0, 0], -21000)
        # arr.set_restricao(3, [0, 0, 0, 0, 0, 0, 0, 0, 0,
        #                   0, 0, 0, -1.05, -1.15, -1.50, 0], -20000)
        # arr.set_restricao(4, [-1.00, 0, 0, 0, -0.90, 0, 0,
        #                   0, -1.80, 0, 0, 0, -1.05, 0, 0, 0], -30000)
        # arr.set_restricao(5, [0, -2.10, 0, 0, 0, -0.80,
        #                   0, 0, 0, -0.70, 0, 0, 0, -1.50, 0, 0], -25700.00)
        # arr.set_restricao(6, [0, 0, -1.10, 0, 0, 0, -1, 0,
        #                   0, 0, -1.20, 0, 0, 0, -1.50, 0], -23500)
        # arr.set_restricao(7, [0, 0, 0, 0, 0, 0, 0, 0, 0,
        #                   0, 0, 0, 0, 0, 0, 0], -7850)

        # arr.set_fun_objetivo([1.00, 0.90, 1.80, 1.05, 2.10,	0.80,	0.70,	1.15,
        #                       1.10,	1.00, 1.20, 1.50, 0, 0, 0, 0])

        # QUESTÃO 4
        # arr = primal_matrix(3, 2)
        # arr.set_restricao(0, [10, 5, 15], 450)
        # arr.set_restricao(1, [8, 4, 7], 300)
        # arr.set_fun_objetivo([-100, -50, -90])

        # QUESTÃO 3
        # arr = primal_matrix(2,3)
        # arr.set_restricao(0, [6, 4], 30)
        # arr.set_restricao(1, [1, 0], 1)
        # arr.set_restricao(2, [0, 1], 2)
        # arr.set_fun_objetivo([-150, -104])

        # QUESTÃO 8
        arr = primal_matrix(2, 3)
        arr.set_restricao(0, [1, 1], 8)
        arr.set_restricao(1, [1, 2], 12)
        arr.set_restricao(2, [1, 0], 6)
        arr.set_fun_objetivo([-7, -12])

        # arr.executa_dual()
        arr.executa_primal()
        print(arr.get_solucoes())
