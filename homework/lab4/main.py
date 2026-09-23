from letters_lib import (
    is_letter,
    count_letters,
    shift_letters,
    first_non_letter,
    letters_only
)


def main():
    s = input("Введіть рядок: ")
    k = int(input("Введіть кількість позицій для зсуву: "))

    print("Кількість латинських літер:", count_letters(s))
    print("Перший символ, який не є латинською літерою:", first_non_letter(s))
    print("Рядок лише з латинських літер:", letters_only(s))
    print("Рядок після зсуву:", shift_letters(s, k))

    if len(s) == 1:
        print("Єдина літера є латинською:", is_letter(s))


if __name__ == "__main__":
    main()
