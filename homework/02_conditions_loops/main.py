number = int(input("Введіть ціле число: "))


is_negative = number < 0
n = abs(number)


reversed_number = 0

while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n = n // 10


if number == 0:
    reversed_number = 0

if is_negative:
    reversed_number = -reversed_number


print("Перевернуте число: ", reversed_number)
