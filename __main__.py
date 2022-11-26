from app.primal_matrix import primal_matrix
from app.dual_matrix import dual_matrix

def primal():
    variaveis = int(input("QTD variáveis: "))
    restricoes = int(input("QTD restrições: "))
    array_primal = primal_matrix(variaveis, restricoes)


    for i in range(restricoes):
        array = input("entre com valores da primeira restrição, separados por virgula: ")
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
        array = input("entre com valores da primeira restrição, separados por virgula: ")
        sol = input("valor da restrição: ")
        array_primal.set_restricao(i, array.replace(" ", "").split(','), sol)
    funObj = input("entre com valores da F.O, separados por virgula: ")
    array_primal.set_fun_objetivo(funObj.replace(" ", "").split(','))

    # array_primal.set_restricao(0, [3, 3, 2], 30)
    # array_primal.set_restricao(1, [6, 3, 0], 48)
    # array_primal.set_fun_objetivo([-10, -8, -1])
    array_primal.executa_dual()

    arraySol = array_primal.get_solucoes()


    for i in range(len(arraySol[0])):
        print("Valor de x"+str(i+1)+": " + str(arraySol[0][i]))

    print("F.O: "+str(arraySol[2][0]))

print("Método simplex")
print("0 - Primal")
print("1 - Dual")
opc = input()

match opc:
    case '0':
        primal()
    case '1':
        dual()