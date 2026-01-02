# Gera número aleatório em 0 e 6. Simulador de jogo de dados.
# 25/12/2025

import random

if __name__ == "__main__":
    jogo = True
    while jogo:
        opcao = int(input("Deseja rodar o dado?\n1 - Sim | 2 - Não --> "))
        if opcao == 1:
            print(f"Dado: {random.randint(0, 6)}")
        elif opcao == 2:
            jogo = False
        else:
            print("Opção inválida")
