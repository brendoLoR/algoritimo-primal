from app.primal_matrix import primal_matrix
from app.dual_matrix import dual_matrix

# array_primal = primal_matrix(3, 2)


# array_primal.set_restricao(0, [3, 3, 2], 30)
# array_primal.set_restricao(1, [6, 3, 0], 48)
# array_primal.set_fun_objetivo([-10, -8, -1])

# print(array_primal.array_primal)
# print('')
# array_primal.executa_primal()

# print(array_primal.array_primal)
# print('')
# print(array_primal.get_solucoes())

arr = dual_matrix(3, 2)


arr.set_restricao(0, [-2, 4, 1], 2)
arr.set_restricao(1, [4, -2, -3], -1)
arr.set_fun_objetivo([2, 6, 10])

arr.executa_dual()