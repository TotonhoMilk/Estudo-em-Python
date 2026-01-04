# Calcula a área do círculo
# 4/1/2026

pi = 3.14159


def area(raio):
    return pi * raio**2


if __name__ == "__main__":
    raio = float(input("Digite o raio do círculo --> "))
    resultado = area(raio)
    print(f"Área do cículo de raio {raio:.2f} é {resultado:.2f}ua")
