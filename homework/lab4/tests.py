from letters_lib import (
    is_letter,
    count_letters,
    shift_letters,
    first_non_letter,
    letters_only
)


# Перевірка is_letter
assert is_letter("a") == True
assert is_letter("Z") == True
assert is_letter("7") == False
assert is_letter("") == False


# Перевірка count_letters
assert count_letters("Hello123!") == 5
assert count_letters("") == 0
assert count_letters("123!@#") == 0


# Перевірка shift_letters
assert shift_letters("abc", 1) == "bcd"
assert shift_letters("xyz", 1) == "yza"
assert shift_letters("ABC XYZ!", 1) == "BCD YZA!"
assert shift_letters("", 5) == ""


# Перевірка first_non_letter
assert first_non_letter("Hello!") == 5
assert first_non_letter("123abc") == 0
assert first_non_letter("Hello") == -1
assert first_non_letter("") == -1


# Перевірка letters_only
assert letters_only("Hello123 World!") == "HelloWorld"
assert letters_only("") == ""
assert letters_only("123!@#") == ""


print("Усі перевірки пройдено!")
