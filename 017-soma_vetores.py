# Efetua a soma de dois vetores, retornando um vetor soma.
# 28/12/2025


def sum_vector(v1: list[int], v2: list[int]):
    n = len(v1)
    res = [0] * n
    for i in range(n):
        res[i] = v1[i] + v2[i]
    return res


if __name__ == "__main__":
    vec1 = [2, 5, 4]
    vec2 = [3, 2, 1]
    resultado = sum_vector(vec1, vec2)
    print(f"A soma do vetor {vec1} com o vetor {vec2} é ", end="")
    print(resultado)
