def is_letter(ch):
    """Повертає True, якщо ch є латинською літерою."""
    if len(ch) != 1:
        return False
    return ("a" <= ch <= "z") or ("A" <= ch <= "Z")


def count_letters(s):
    """Повертає кількість латинських літер у рядку s."""
    count = 0

    for ch in s:
        if is_letter(ch):
            count = count + 1

    return count


def shift_letters(s, k):
    """Повертає рядок із латинськими літерами, зсунутими на k позицій по колу."""
    result = ""

    for ch in s:
        if "a" <= ch <= "z":
            new_code = ord(ch) + k
            new_code = (new_code - ord("a")) % 26 + ord("a")
            result = result + chr(new_code)
        elif "A" <= ch <= "Z":
            new_code = ord(ch) + k
            new_code = (new_code - ord("A")) % 26 + ord("A")
            result = result + chr(new_code)
        else:
            result = result + ch

    return result


def first_non_letter(s):
    """Повертає індекс першого символу, який не є латинською літерою, або -1."""
    for i in range(len(s)):
        if not is_letter(s[i]):
            return i

    return -1


def letters_only(s):
    """Повертає новий рядок, що містить лише латинські літери з s."""
    result = ""

    for ch in s:
        if is_letter(ch):
            result = result + ch

    return result
