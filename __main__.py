from app.primal_matrix import primal_matrix

array_primal = primal_matrix(2, 2)


def assert_matrix(given, expected):
    assert len(given) is len(expected)

    for linha in range(len(expected)):
        assert len(given[linha]) is len(expected[linha])
        map(lambda x, y: assertAlmostEquals(
            x, y), given[linha], expected[linha])


array_esperado = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

assert_matrix(array_primal.array_primal, array_esperado)

array_primal.set_restricao(0, [1, 2], 3)

array_esperado = [
    [1, 2, 1, 0, 3],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

assert_matrix(array_primal.array_primal, array_esperado)
array_primal.set_restricao(1, [4, 5], 6)

array_esperado = [
    [1, 2, 1, 0, 3],
    [4, 5, 0, 1, 6],
    [0, 0, 0, 0, 0],
]

assert_matrix(array_primal.array_primal, array_esperado)

array_primal.set_fun_objetivo([-8, -7])

assert_matrix(array_primal.array_primal, array_esperado)

coluna_pivot = array_primal.get_coluna_pivot()

array_primal.update_linha_pivot()
array_primal.update_linha(0)
array_primal.update_linha(2)
print(array_primal.array_primal)