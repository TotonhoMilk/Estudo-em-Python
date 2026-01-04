# Calculadora de milhas para quilômetros, e vice-versa
# 4/1/2026

CONST = 1.6093


def converte_km_m(km):
    return km / CONST


def converte_m_km(m):
    return m * CONST


if __name__ == "__main__":
    while True:
        print("Escolha sua opção")
        print("1) Quilômetros para milhas")
        print("2) Milhas para quilômetros")
        print("0) Sair")
        opcao = int(input("--> "))
        if opcao == 0:
            break
        if opcao == 1:
            valor = float(input("Digite quilômetros: "))
            resultado = converte_km_m(valor)
            print(f"Resultado: {resultado:.3f}m")
        elif opcao == 2:
            valor = float(input("Digite milhas: "))
            resultado = converte_m_km(valor)
            print(f"Resultado: {resultado:.3f}km")
        else:
            print("Valor equivocado!")
        print("\n\n\n")
