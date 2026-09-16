def compress_string(text):
    if len(text) == 0:
        return ""

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    result += text[len(text) - 1] + str(count)

    return result


print("Частина А")

text1 = "aaabbc"
print("Вхідні дані:", text1)
print("Результат:", compress_string(text1))

text2 = ""
print("\nВхідні дані:", repr(text2))
print("Результат:", repr(compress_string(text2)))


def above_main_diagonal(matrix):
    result = []

    for i in range(len(matrix)):
        row = []

        for j in range(i + 1, len(matrix[i])):
            row.append(matrix[i][j])

        if len(row) > 0:
            result.append(row)

    return result


print("\nЧастина Б")

matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Матриця 1:")
for row in matrix1:
    print(row)

print("Елементи над головною діагоналлю:")
result1 = above_main_diagonal(matrix1)

for row in result1:
    print(row)


matrix2 = [
    [5, 1, 2, 3],
    [4, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("\nМатриця 2:")
for row in matrix2:
    print(row)

print("Елементи над головною діагоналлю:")
result2 = above_main_diagonal(matrix2)

for row in result2:
    print(row)
