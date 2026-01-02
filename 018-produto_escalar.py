# Calcula o produto escalar entre dois vetores.
# 26/12/2025


def add_vectors(v1, v2) -> int:
    return sum(a * b for a, b in zip(v1, v2))


if __name__ == "__main__":
    vector1 = [2, 5, 4]
    vector2 = [3, 2, 1]
    print(f"Resultado: {add_vectors(vector1, vector2)}")
