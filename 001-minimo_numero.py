# Acha o menor número em uma matriz
# 23/12/2025

def find_min(numbers:list[int]) -> int:
    minimum_value = numbers[0]
    for num in numbers:
        if minimum_value > num:
            minimum_value = num
    return minimum_value

if __name__ == "__main__":
    test_array = [2,6,4,3,4,8,1,4,3,7]
    minimum = find_min(test_array)
    print(f"Menor número = {minimum}")
