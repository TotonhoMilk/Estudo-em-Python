# Imprime o código fonte na tela
# 13/1/2026

print("======CÓDIGO FONTE======\n")
with open(__file__, "r") as f:
    codigo = f.read()
    print(codigo)
print("\n======CÓDIGO FONTE======")
