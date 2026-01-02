# Converte número binário em decimal.
# 29/12/2025


def binaryDecimal(str):
    print(f"Binário: {str}")
    bin = str[::-1]
    n = len(bin)
    resultado = 0
    for num in range(n):
        if bin[num] == "0":
            print(f"i:{num} - binario: {bin[num]} | 2^{num} | continue")
            continue
        resultado += pow(2, num)
        print(f"i:{num} - binario: {bin[num]} | 2^{num} | resultado: {resultado}")


if __name__ == "__main__":
    binaryDecimal("10011011")
