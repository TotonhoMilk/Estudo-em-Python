# Conta quantas ocorrências de um número em uma matriz
# 23/12/2025

def count_occurencies(numbers:list[int], oc):
    count = 0;
    for num in numbers:
        print(f"número: {num} == oc: {oc}")
        if num == oc:
            count += 1
            print(f"Verdadeiro!\n\tNovo valor de count: {count}")
    return count

if __name__ == '__main__':
    test_array = [1,3,4,5,6,1,3,7,1,9,1]
    num = 1
    occurrencies = count_occurencies(test_array, num)
    print(f"O número {num} apareceu {occurrencies} vezes")
