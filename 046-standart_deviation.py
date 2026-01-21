# Desvio padrão da população.
#
# O desvio padrão mede a propagação de uma distribuição de dados.
# Ele mede a distância típica entre cada ponto de dados e a média.
#
# Fórmula
# sigma = sqrt(sum((xi - mi)^2) / N)
#
# Passo 1: Calcule a média dos dados – isso é ‍\[\mu\] na fórmula.
#
# Passo 2 : Subtraia a média de cada ponto de dados.
# Essas diferenças são chamadas de desvios.
# Os pontos de dados abaixo da média terão desvios negativos,
# e os pontos de dados acima da média terão desvios positivos.
#
# Passo 3 : Quadre cada desvio para torná-lo positivo.
#
# Passo 4 : Adicione os desvios quadrados juntos.
#
# Passo 5 : Dividir a soma pelo número de pontos de dados na população.
# O resultado é chamado de variância.
#
# Passo 6 : Pegue a raiz quadrada da variância para obter o desvio padrão.


def stddev(a, N):
    mi = 0
    sum = 0
    for i in range(N):
        mi += a[i]
    mi = mi / N
    print(f"mi: {mi}")
    for i in range(N):
        sum += (a[i] - mi) ** 2
    print(f"sum: {sum}")
    return (sum / N) ** 0.5


if __name__ == "__main__":
    a = [6, 2, 3, 1]
    r = stddev(a, 4)
    print(f"Standart deviation: {r: .2f}")
